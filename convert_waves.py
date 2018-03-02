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
    command = input("コマンドを入力してください（hでヘルプ）h/v/a/d/s/q > ")
    if command == "h" or command == "":
        print("h:ヘルプを表示\n"
            "v:変換予定リストを見る\n"
          "a:変換予定リストにファイルを加える\n"
          "d:変換予定リストから削除する\n"
          "s:変換を開始する\n"
          "q:中止して終了する\n")
        
    elif command[0] == "v":
        if convert_list == []:
            print("変換予定リストは空です")
        else:
            for infile in convert_list:
                infile.show_params()
    
    elif command[0] == "a":
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
        
        last_label = ""
        for start in start_list:
            fs, data = load_wave(wav_fname, start, cut_length)
            in_file = InputFile(
                wav_fname
                ,fs
                ,data
                ,start
                ,cut_length)
            
            if in_file.check_convertable() == True:
                convert_list.append(in_file)
            else:
                print("{}秒からだと{}秒のデータしか得られなかったのでスキップします"
                      .format(start, in_file.data_len()))
                continue

                
            #t-sneで使うラベルを設定するプロンプト
            
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
                else:
                    last_label = label

            in_file.set_label(label)
            
    
    elif command[0] == "d":
        if convert_list == []:
            print("変換予定リストは空です")
            continue
        for i in range(len(convert_list)):
            print("{}:".format(i+1), end=" ")
            convert_list[i].show_params()
            
        del_num = cui_input("削除したい番号を選択してください", converter=int)
        try:
            convert_list.pop(del_num - 1)
        except:
            print("指定された番号が異常です。")
        
    elif command[0] == "s":
        if convert_list == []:
            print("リストは空です")
            continue
        
        total_file = len(convert_list)
        current_file = 0
        
        for in_file in convert_list:
            current_file += 1
            #進捗を出力
            print("{}/{}: {} -> {}/{}"
                  .format(total_file
                          , current_file
                          , os.path.basename(in_file.inpath)
                          ,out_dir
                          ,in_file.ofilename))
            #calc fft
            amplitudeSpectrum = in_file.calc_fft()
            
            #write data
            outf = open(out_dir + "/" + in_file.ofilename, "w", newline = "")
            writer = csv.writer(outf)
            
            #write meta data
            writer.writerows([[
                "start = {}".format(in_file.start)
                +"length = {}".format(in_file.length)
                + "  label = {}".format(in_file.label)]])
            #write fft data
            writer.writerows([x] for x in amplitudeSpectrum)
            
            outf.close()
            
    elif command[0] == "q":
            break
        
    else:
            print("h, v, a, d, s, qのどれかを入れてください！")
            

            
            
            
    
    
    
    
    
    
    
    



        

