# MinecraftServerEvent_DiscordBOT

これはMinecraftサーバのステータス変化や、プレイヤーの出入りをDiscordで通知するDiscord Botです<br>

## 機能
* Minecraftサーバのステータスを、BOTのステータス欄に表示する<br>
* Minecraftサーバのステータスが変化したとき、チャンネルにメッセージを送信する<br>
* Minecraftサーバでプレイヤーの出入りがあったとき、チャンネルにメッセージを送信する<br>

## 動作デモ
### BOTステータス欄
![Demo1](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejV3NzF6YW02cG1xdjAxOWxrMTdkbHloazRjdjM3OWwzdnUzaGZjNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Fg5UQcLMqNneLgZtWH/giphy.gif)

| 表示 | サーバの状態 |
| --- | --- |
| 🟢 | 稼働中（参加者1人以上） | 
| 🟡 | 稼働中（参加者0人）　| 
| 🔴 | オフライン |

### ステータス変化時チャンネル通知
![Demo2](https://i.imgur.com/b7cMhdW.png)

### プレイヤー出入り時チャンネル通知
![Demo3](https://i.imgur.com/ibJaGns.png)

## セットアップと起動
※予めpython、Discord.pyを導入すること

1. 当リポジトリから`main.py`と`config.ini`をDLし、同じ階層にまとめる
1. `config.ini`にDiscoed botトークンと監視対象のMinecraftサーバアドレス、通知したいチャンネルIDをセットする
1. main.pyを叩く

## サーバへの招待と使い方

1. Discord developer portalでOAuth2 URL Generatorを使用し招待する（スコープは「bot」を指定）
1. Botのステータスが表示され、チャンネルへメッセージが送信されることを確認する