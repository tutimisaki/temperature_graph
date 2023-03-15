import os
from flask import Flask, render_template, url_for
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import datetime
import japanize_matplotlib

app = Flask(__name__)

# 「Weather Forecast API」から当日の気温データを取得する
url = "https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&"+\
       "hourly=temperature_2m&forecast_days=1&timezone=Asia%2FTokyo"
res = requests.get(url)

# json形式で取得できる
temperature_json_data = json.loads(res.text)

# グラフの作成
fig = plt.figure()
x = np.arange(24) # 各時間帯
y = temperature_json_data['hourly']['temperature_2m'] # 1時間ごとの気温データ
plt.xticks(np.arange(0, 24, 3)) # 3時間ごとに目盛りを表示する(21時まで表示)
plt.yticks(np.arange(0, 50, 5)) # 5℃ごとに目盛りを表示する(45℃まで表示)
plt.ylim(0, 50) # 気温の高さによってグラフの表示範囲がばらつかないようにグラフの表示上限位置を50℃で固定する

# 各ラベルの設定
plt.title("本日の気温")
plt.xlabel("時間")
plt.ylabel("気温（℃）")

# 棒グラフを作成する
bar_list = plt.bar(x, y)

# 現在時刻を取得し、該当する時刻の帯の色を強調する
# ※render.comのWebサーバ上で確認すると、別リージョンのタイムゾーンで時刻を取得するため
# ※時刻のずれを調整して取得（render.comに東京リージョンが追加されるまでの暫定策）
DATE_DIFF_HOUR = 9
now_date = datetime.datetime.now() + datetime.timedelta(hours=DATE_DIFF_HOUR)
bar_list[now_date.hour].set_color("#ff7f00")

# 遷移先のページでグラフを表示するためグラフの画像をbase64形式に変換する
io = BytesIO()
fig.savefig(io, format="png")
io.seek(0)
base64_img = base64.b64encode(io.read()).decode()

# 遷移先で利用するデータ
result = {"base64_img" : base64_img,
          "now_month" : now_date.month,
          "now_day" : now_date.day,
          "now_hour" : now_date.hour,
          "temperature" : temperature_json_data['hourly']['temperature_2m'][now_date.hour]}

# 気温グラフ画面へのルーティング
@app.route("/")
@app.route("/index")
def show_graph_page():
    return render_template('index.html', result=result)

# css読み込みのためurl_forを書き換え
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

# url_for書き換え用のメソッド
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)