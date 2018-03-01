import os
import tkinter, tkinter.filedialog, tkinter.messagebox
import csv

from input_liv.cui_input import cui_input
from convert_liv.input_file import InputFile
from wav_liv.load_wave import load_wave 
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
    out_dir = os.path.abspath(out_dir)

#切り取る長さを入力するプロンプトを表示
cut_length = cui_input("切り取りたい音声の長さを秒(float型)で指定してください: "
          , converter=float)
        
#ファイルとstart地点を入力するプロンプトを表示
convert_list = []
while True:
    command = input("コマンドを入力してください。\n"
          "v:変換予定リストを見る\n"
          "a:変換予定リストに加える\n"
          "d:変換予定リストから削除する"
          "s:変換を開始する\n"
          "q:中止して終了する\n"
          "v/a/d/s/q > ")[0]   
    
    if command == "v":
        if convert_list == []:
            print("変換予定リストは空です")
        else:
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
        
        wav_fname = os.path.abspath(wav_fname)
        
        #切り取り開始地点を取得するプロンプトを表示
        
        str_start_list = input(
            "{}秒切り取る開始地点を入力してください（,で区切って複数指定可）\n"
            "例：3.5, 22.4, 5> ".format(cut_length)).split(",")
        
        #各要素をfloatに変換, 変換できないものは除く
        start_list = []
        for start in str_start_list:
            try:
                start_list.append(float(start))
            except ValueError:
                pass
        
        #InputFileオブジェクトを生成
        for start in start_list:
            fs, data = load_wave(wav_fname, start, cut_length)
            in_file = InputFile(
                path
                ,fs
                ,data
                ,start
                ,cut_length)
            
            if in_file.check_convertable() == True:
                convert_list.append(in_file)
            else:
                print("{}秒からだと{}秒のデータしか得られなかったのでスキップします"
                      .format(start, in_file.data_len))
                continue
                
            #t-sneで使うラベルを設定するプロンプト
            last_label = ""
            if last_label == "":
                label = cui_input(
                    "{}秒から切り取るデータのラベルを入力してください。".format(start)
                    + "(t-sneで使います。)\n例：怒り,太鼓の音, etc> "
                )
            
                last_label = label
            else:
                label = input(
                "{}秒から切り取るデータのラベルを入力してください。\n".format(start)
                + "何も入力しなかった場合は直前のラベル（{}）".format(last_label)
                + "が使用されます\n> "
                )
                
                if(label == ""):
                    label = last_label

            in_file.set_label(label)
            
    
    elif command == "d":
        if convert_list == []:
            print("変換予定リストは空です")
            continue
        for i in range(len(convert_list)):
            print("{}:".format(i+1), end=" ")
            infile.show()
            
        del_num = cui_input("削除したい番号を選択してください", converter=int)
        convert_list.pop(del_num - 1)
        
    elif command == "s":
        if convert_list == []:
            print("リストは空です")
            continue
        
        for in_file in convert_list:
            #calc fft
            amplitudeSpectrum = in_file.calc_fft()
            
            #write data
            outf = open(in_file.ofilename, "w", newline = "")
            writer = csv.writer(outf)
            
            #write meta data
            writer.writerows([[
                "length = {}".format(in_file.length)
                + "  label = {}".format(in_file.label)]])
            #write fft data
            writer.writerows(amplitudeSpectrum)
            
            outf.close()
            
        elif command == "q":
            break
        
        else:
            print("v, a, d, s, qのどれかを入れてください！")
            

            
            
            
    
    
    
    
    
    
    
    



        

