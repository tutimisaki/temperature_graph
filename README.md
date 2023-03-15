# temperature_graph
当日の東京の気温グラフを表示するWebページです

気温データは以下のサイトのWebAPIから取得しています

[Open-Meteo Free Weather API](https://open-meteo.com/)

## Dependency(使用言語、ライブラリ等)
・言語
  Python 3.7.10

・Webフレームワーク
  Flask 2.2.3

・WSGIアプリケーションサーバー
  gunicorn 20.1.0

・グラフ描画ライブラリ
  matplotlib 3.5.3

・HTTP通信ライブラリ
  requests 2.28.2

・matplotlib日本語化モジュール
  japanize-matplotlib 1.1.3

・統合クラウドサービス
  Render.com

## Usage(利用方法)
以下のURLからWebページにアクセスすることができます

Webページにアクセスすることで、当日の東京の気温グラフを確認することができます

[今日の東京の気温グラフ](https://temperature-graph.onrender.com/)

## References(参考情報)
・気温データの取得API利用
[Open-Meteo Free Weather API](https://open-meteo.com/)

・matplotlibで描画したグラフをbase64形式に変換する方法
[参考サイト](https://qiita.com/kujirahand/items/896ea20b28ee2ed96311)

・Flaskで作成したWebページからCSSを読み込む方法
[参考サイト](https://engineeringpython.com/%E3%80%90matplotlibpython%E3%80%91matplotlib%E3%82%92web%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AB%E8%A1%A8%E7%A4%BA/)

・利用した統合クラウドサービス
[Render.com](https://render.com/)

## remarks(備考)
Render.comについてはフリープランを利用しています。
フリープランではWebサイトへのアクセスが15分間無い場合スリープ状態になり、新しいアクセスがあった際にスピンアップを行うため、
アクセスしたとき最大30秒程時間がかかる場合があります。

またフリープランではWebサービスが1か月あたり750時間利用可能という制限があります。
1か月のWebサービスの稼働時間が750時間を超過した場合、Webページにアクセスできなくなります。

[参考情報 Free Instance Types Render.com](https://render.com/docs/free)
