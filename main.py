# coding: UTF-8

import discord
import configparser
import datetime
from discord.ext import tasks
import requests

#config.ini読み出し
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
token = config_ini.get('DISCORD', 'token')
channelid = int(config_ini.get('DISCORD', 'channelid'))
address = config_ini.get('MINECRAFT', 'address')
servername = config_ini.get('MINECRAFT', 'servername')

#intents設定
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

#チェック項目
lasttime_onlinestatus = False
lasttime_playerlist = []

def main():

    #起動部
    @bot.event
    async def on_ready():
        dt_now = datetime.datetime.now()
        print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'name:' + bot.user.name)
        print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'ID:' + str(bot.user.id))
        print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'Logged in as\n')
        await bot.change_presence(activity=discord.Game("ステータス取得中…"))
        requestURL = "https://api.mcstatus.io/v2/status/java/" + address
        parameter = {"query":"false", "timeout":"5.0"}
        server_status_inquiry.start(requestURL,parameter)

    @tasks.loop(seconds=10)
    async def server_status_inquiry(requestURL,parameter):

        global lasttime_onlinestatus
        global lasttime_playerlist
        channel = bot.get_channel(channelid)

        r = requests.get(requestURL, params=parameter)
        result = r.json()

        #ステータス表示更新部
        if result["online"] == True:
            if int(result["players"]["online"]) == 0:
                await bot.change_presence(status=discord.Status.idle,activity=discord.Game(str(result["players"]["online"]) + "人が" + servername))
            else:
                await bot.change_presence(status=discord.Status.online,activity=discord.Game(str(result["players"]["online"]) + "人が" + servername))
        else:
            await bot.change_presence(status=discord.Status.dnd,activity=discord.Game("オフライン状態"))

        #ステータス更新通知
        if lasttime_onlinestatus == False and result["online"] == True:
            await channel.send("ステータス更新：オンライン✅")
        elif lasttime_onlinestatus == True and result["online"] == False:
            await channel.send("ステータス更新：オフライン❌")

        lasttime_onlinestatus = result["online"]

        #プレイヤー入退室通知
        playerlist = []
        for i in range(len(result["players"]["list"])):
            playerlist.append(result["players"]["list"][i]["name_raw"])

        if playerlist != lasttime_playerlist:

            #ログアウト
            leaving_playerlist = list(set(lasttime_playerlist) - set(playerlist))
            if leaving_playerlist != []:
                await channel.send("ログアウト："+",".join(leaving_playerlist)+"👋")
                
            #ログイン
            entering_playerlist = list(set(playerlist) - set(lasttime_playerlist))
            if entering_playerlist != []:
                await channel.send("ログイン："+",".join(entering_playerlist)+"🖖")

        lasttime_playerlist = playerlist

    bot.run(token)

if __name__ == "__main__":
    main()