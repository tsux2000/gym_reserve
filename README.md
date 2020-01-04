# 東山体育館・自動抽選予約プログラム

以下、Windowsユーザーが多いのでWindowsだとして説明します。

## 初回のみするべき下準備

このリポジトリをダウンロードして、ホームディレクトリにフォルダ名 `gym_reserve` で展開してください。

Chromeのバージョンを更新・確認し、それに合わせたchromedriverをダウンロード、
PATHをとおしてください。

初回のみ、以下を1行1行コマンドプロンプトから実行してください。

```prompt
cd %userprofile%\gym_reserve
py -m venv venv
call venv\Scripts\activate.bat
pip install selenium pandas
deactivate
```

## 実行方法

以上の設定が完了すれば、それ以降は、
次項で説明するように予約日時とユーザーを設定した後、
以下を実行することで予約できます。

```prompt
cd %userprofile%\gym_reserve
call venv\Scripts\activate.bat
py reserve.py
deactivate
```

## 予約日時の設定方法

`datetime.csv` が予約日時の設定CSVファイルです。
無い場合には作成してください。

> 例）
>
> ```csv
> year,month,day,time_code
> 年,月,日,時間帯コード
> 年,月,日,時間帯コード
> 年,月,日,時間帯コード
> 年,月,日,時間帯コード
> 年,月,日,時間帯コード
> ...
> ```

時間帯コードは以下の通りです。

|コード|時間帯|
|:-:|:-:|
|0|9〜11 時|
|1|11〜13 時|
|2|13〜15 時|
|3|15〜17 時|
|4|17〜19 時|
|5|19〜21 時|

## ユーザーの追加・修正・削除方法

### CSVファイルでの手入力修正

`user.csv` がユーザーの設定CSVファイルです。
無い場合には作成してください。

> 例）
>
> ```csv
> user_id,password,name
> ユーザーID,パスワード,名前
> ユーザーID,パスワード,名前
> ユーザーID,パスワード,名前
> ユーザーID,パスワード,名前
> ...
> ```

※ 名前の部分は正確でなくてもいいです。
