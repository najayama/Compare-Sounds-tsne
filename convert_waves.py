import os
import tkinter, tkinter.filedialog, tkinter.messagebox

# フォルダ選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))

out_dir ="" 
while not out_dir:
    tkinter.messagebox.showinfo('出力先を選択','変換後のデータを格納するディレクトリを選択してください\n\
！注意！\n違う長さのデータは比較できないので、ディレクトリ名にデータの長さを入れておくといいかも。')
    out_dir = tkinter.filedialog.askdirectory(initialdir = iDir)

#切り取る長さを入力するプロンプトを表示
cut_time = ""
while cut_time == "":
    try:
        cut_time = float(input("切り取るデータの長さを秒(float型)で指定してください。: "))
    except:
        cut_time = ""
        
#ファイルとstart地点を入力するプロンプトを表示

prompt1 = "切り取るもとのwavファイルを選んでください。"
convert_list = []
while True:
    
    
    
    
    
    



        

