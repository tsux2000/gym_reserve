import pandas as pd

# エンコード うまくいかなければ'shift_jis'を試してみる。
ENCODING = 'utf-8'

# 予約日時
DATETIME = pd.read_csv('./datetime.csv', encoding=ENCODING)

# ユーザー
USER = pd.read_csv('./user.csv', encoding=ENCODING)

# 予約システムURL
URL = "https://g-kyoto.pref.kyoto.lg.jp/reserve_j/core_i/init.asp?SBT=1"

# 予約種目
PURPOSE = 'バスケットボール'

# 予約施設
FACILITY = '東山地域体育館'

# 待機時間（秒）
WAIT_TIME = 1.5
