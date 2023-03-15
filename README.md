# temperature_graph
当日の東京の気温グラフを表示するWebページです<br>
気温データは以下のサイトのWebAPIから取得しています<br>
[Open-Meteo Free Weather API](https://open-meteo.com/)

## Dependency(使用言語、ライブラリ等)
・言語<br>
　Python 3.7.10

・Webフレームワーク<br>
　Flask 2.2.3
  
・WSGIアプリケーションサーバー<br>
　gunicorn 20.1.0
  
・グラフ描画ライブラリ<br>
　matplotlib 3.5.3
  
・HTTP通信ライブラリ<br>
　requests 2.28.2
  
・matplotlib日本語化モジュール<br>
　japanize-matplotlib 1.1.3
  
・統合クラウドサービス<br>
　Render.com

## Usage(利用方法)
以下のURLからWebページにアクセスすることができます<br>
Webページにアクセスすることで、当日の東京の気温グラフを確認することができます<br>
[今日の東京の気温グラフ](https://temperature-graph.onrender.com/)

## References(参考情報)
・気温データの取得API利用<br>
[Open-Meteo Free Weather API](https://open-meteo.com/)  

・matplotlibで描画したグラフをbase64形式に変換する方法<br>
[参考サイト](https://engineeringpython.com/%E3%80%90matplotlibpython%E3%80%91matplotlib%E3%82%92web%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AB%E8%A1%A8%E7%A4%BA/)  

・Flaskで作成したWebページからCSSを読み込む方法<br>
[参考サイト](https://qiita.com/kujirahand/items/896ea20b28ee2ed96311)  

・利用した統合クラウドサービス<br>
[Render.com](https://render.com/)

## remarks(備考)
Render.comについてはフリープランを利用しています。<br>
フリープランではWebサイトへのアクセスが15分間無い場合スリープ状態になり、新しいアクセスがあった際にスピンアップを行うため、<br>
アクセスしたとき最大30秒程時間がかかる場合があります。<br>

またフリープランではWebサービスが1か月あたり750時間まで利用可能という制限があります。<br>
1か月のWebサービスの稼働時間が750時間を超過した場合、Webページにアクセスできなくなります。<br>

[【参考情報】 Free Instance Types - Render.com](https://render.com/docs/free)
