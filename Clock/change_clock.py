
import tkinter
import datetime

# ウィンドウを作成
root = tkinter.Tk()
# ウィンドウをフルスクリーンにします。タイトルバーの部分も表示されなくなります。
root.attributes('-fullscreen', True)

# 文字を表示させるウィジェット
label = tkinter.Label(root)

#ここからは「時かけ」風に改造するための部分-------------------------------------------

# ウィンドウの背景色(background)
root["bg"] = "black"

# font:文字のフォントと大きさ
# bg:文字領域の背景色
# fg:文字の色
label["font"] = ("timeleap", 90)
label["bg"] = "black"
label["fg"] = "white"

# labelを配置するコマンド
# anchorとexpandは、labelをウィンドウの中央に配置するためのオプションです。
label.pack(anchor = "ce", expand = True)

#ここまでが改造するための部分----------------------------------------------------------

# 時計の時間を更新する関数
def change_clock():
    #　表示する時刻を更新する
    label["text"] = datetime.datetime.now().strftime("%H:%M:%S")

    # 遅らせる時間(ms), 実行する関数を入れます。
    # この場合は、0.1秒後にchange_clockを実行してくれるので、0.1秒おきに時刻を更新できます。
    root.after(100, change_clock)

# ループの一回目を実行します
root.after(0, change_clock)

# root.bind(sequence, func)で設定できます。
# この場合は、root(セーバーのウィンドウ)の中で、sequenceのイベントを検出して、funcを実行してくれます。
# "<Motion>"はマウスの動き、<Key>は、キーが押されたことを検出してくれます。
# funcの方は、無名関数を使って、画面を閉じる関数をしてしてあります。
root.bind("<Motion>", func=lambda x: root.destroy())
root.bind("<Key>", func=lambda x: root.destroy())

# rootを実行
root.mainloop()