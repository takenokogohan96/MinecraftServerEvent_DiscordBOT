# MinecraftServerStatus-DiscordBOT

これはMinecraftサーバの状態を確認するサービス[Minecraft Server Status](https://mcstatus.io/)で取得したサーバ状態をDiscord上で簡単に確認するためのDiscord Botです<br>
※本スクリプトは個人利用レベルのものであり、第三者による利用を深く想定していません。予めご了承ください

## 機能
* Minecraftの簡易的な状態を、BOTのステータス欄に表示します<br>
（Minecraft Server Statusの仕様上、1分程度のレイテンシがあります）

## 動作デモ
![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejV3NzF6YW02cG1xdjAxOWxrMTdkbHloazRjdjM3OWwzdnUzaGZjNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Fg5UQcLMqNneLgZtWH/giphy.gif)

| Botステータス | サーバの状態 |
| --- | --- |
| オンライン（🟢） | 稼働中（参加者1人以上） | 
| 取り込み中（🟡） | 稼働中（参加者0人）　| 
| 退席中（🔴） | オフライン |

## セットアップと起動
※python、Discord.pyの導入などは割愛

1. 当リポジトリから`main.py`と`config.ini`をDLし、同じ階層にまとめる
1. `config.ini`にDiscoed botトークンと監視対象のMinecraftサーバ、サーバ名をセットする
1. main.pyを叩く

## サーバへの招待と使い方

1. 機能を利用したいサーバへbotを招待します
    * discord developer portalでOAuth2 URL Generatorを使用し招待します<br>
    このとき、**スコープは「bot」を指定してください**
1. Botのステータスにサーバの状態が表示されます

## 使用している主なライブラリなど

Discord.py<br>
https://discordpy.readthedocs.io/ja/latest/

Minecraft Server Status API<br>
https://mcstatus.io/docs
