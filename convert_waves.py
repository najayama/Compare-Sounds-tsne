import os
import tkinter, tkinter.filedialog, tkinter.messagebox

# フォルダ選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))

dir ="" 
while not dir:
    tkinter.messagebox.showinfo('出力先を選択','変換後のデータを格納するディレクトリを選択してください\n\
！注意！\n違う長さのデータは比較できないので、ディレクトリ名にデータの長さを入れておくといいかも。')
    dir = tkinter.filedialog.askdirectory(initialdir = iDir)

print("出力先を変えたいならプログラムを起動し直してください。\n")

