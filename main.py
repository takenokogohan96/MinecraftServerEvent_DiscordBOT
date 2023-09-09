# coding: UTF-8

import discord
import configparser
import datetime
from discord.ext import tasks
import requests

#config.ini読み出し
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
token = config_ini.get('KEY', 'token')

#intents設定
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

def main():

    #起動部
    @bot.event
    async def on_ready():
        dt_now = datetime.datetime.now()
        print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'name:' + bot.user.name)
        print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'ID:' + str(bot.user.id))
        print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'Logged in as\n')
        await bot.change_presence(activity=discord.Game("ステータス取得中…"))
        address = config_ini.get('ADDRESS', 'address')
        address = "https://api.mcstatus.io/v2/status/java/" + address
        parameter = {"query":"false", "timeout":"5.0"}
        server_status_inquiry.start(address,parameter)

    @tasks.loop(seconds=10)
    async def server_status_inquiry(requestURL,parameter):
        r = requests.get(requestURL, params=parameter)
        result = r.json()
        if result["online"] == True:
            if int(result["players"]["online"]) == 0:
                await bot.change_presence(status=discord.Status.idle,activity=discord.Game(str(result["players"]["online"]) + "人がバニラ鯖"))
            else:
                await bot.change_presence(status=discord.Status.online,activity=discord.Game(str(result["players"]["online"]) + "人がバニラ鯖"))
        else:
            await bot.change_presence(status=discord.Status.dnd,activity=discord.Game("オフライン状態"))

    bot.run(token)

if __name__ == "__main__":
    main()