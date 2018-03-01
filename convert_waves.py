import os
import tkinter, tkinter.filedialog, tkinter.messagebox
from input_liv.cui_input import cui_input
# フォルダ選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))

out_dir ="" 
while not out_dir:
    tkinter.messagebox.showinfo('出力先を選択'
                                ,'変換後のデータを格納するディレクトリを選択してください\n'
                                '！注意！\n違う長さのデータは比較できないので、ディレクトリ名に'
                                'データの長さを入れておくといいかも。')
    out_dir = tkinter.filedialog.askdirectory(initialdir = iDir)

#切り取る長さを入力するプロンプトを表示
cui_input("切り取りたい音声の長さを秒(float型)で指定してください: "
          , converter=float)
        
#ファイルとstart地点を入力するプロンプトを表示
convert_list = []
while True:
    command = input("コマンドを入力してください。\n"
          "v:変換予定リストを見る\n"
          "a:変換予定リストに加える\n"
          "d:変換予定リストから削除する"
          "s:変換を開始する\n"
          "q:中止\n"
          "v/a/d/s/q > ")[0]   
    
    if command == "v":
        if convert_list == []:
            print("変換予定リストは空です")
        for infile in convert_list:
            infile.show()
    
    elif command == "a":
        #wavファイルを選択してもらうwindowを表示
        wav_fname ="" 
        while not wav_fname:
            tkinter.messagebox.showinfo("変換したいファイルを選択"
                                        ,'変換したいファイルを選択してください')
            
            fTyp = [("", "*.wav")]
            wav_fname = tkinter.filedialog.askopenfilename(filetypes = fTyp)
        ######here!!!!
            
        
    
    elif command == "d":
        if convert_list == []:
            print("変換予定リストは空です")
            continue
        for i in range(len(convert_list)):
            print("{}:".format(i+1), end=" ")
            infile.show()
            
        del_num = cui_input("削除したい番号を選択してください", converter=int)
        convert_list.pop(del_num - 1)
    
    
    
    
    
    
    
    



        

