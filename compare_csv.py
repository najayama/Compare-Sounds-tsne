import tkinter, tkinter.filedialog, tkinter.messagebox
import os
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble,
                     discriminant_analysis, random_projection)


from input_liv.cui_input import cui_input

def plot_embedding(X, label_list, title=None):
    #いい感じに正規化
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)

  
    
    #label リストと数字を対応付けて色を付ける
    label_dict = {}
    for i in range(len(label_list)):
        if not(label_list[i] in label_dict.keys()):
            label_dict[label_list[i]] = i
    
    plt.figure()
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(label_list[i]),
                 color=plt.cm.Set1(label_dict[label_list[i]]),
                 fontdict={'weight': 'bold', 'size': 9})  

    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)
    
    plt.show()

# フォルダ選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))


###debug_region and shuld be uncommented
#input_dir ="" 
#while not input_dir:
    #tkinter.messagebox.showinfo(
        #"フォルダを選択"
        #,"比較したいcsvファイルがあるディレクトリを選んでください")
    #input_dir = tkinter.filedialog.askdirectory(initialdir = iDir)
    #input_dir = os.path.abspath(input_dir)
###debug_line
   
####debug_line 
input_dir = "/home/naja/Templates/tsne-testout"
###debug_line


#すべてのファイルのリストを得る
ls = os.listdir(input_dir)
input_files = []
for filename in ls:
    if filename[-4:] == ".csv":
        input_files.append(input_dir + "/" + filename)
              
#サンプル長さのリストを取得して選んでもらう
length_list = []

for filename in input_files:
    f = open(filename)
    try:
        length = float(f.readline().split(" ")[4])
    except IndexError:
        continue
    except ValueError:
        continue
    
    length_list.append([filename, float(length)])
    
#集合に入れて重複を削除
length_set = set()
for file_data in length_list:
    length_set.add(file_data[1])
    
if len(length_set) == 0:
    print("error:no csv file found converted by convert_wave.py")
    sys.exit()

#１以上ならプロンプトを表示して選んでもらって、length_listから削除
elif len(length_set) != 1:
    print(
        "複数の選択肢があるようです。"
        "比較したいのはどの長さのファイルたちですか？")
    
    for i in length_set:
        print("{} seq".format(i))
        
    while True:
        choosed_len = cui_input("長さを入力> ", converter = float)
        if choosed_len in length_set:
            break
    
    input_files = []
    for filedata in length_list:
        if filedata[1] == choosed_len:
            input_files.append(filedata[0])
            
else:
    for filedata in length_list:
        input_files.append(filedata[0])    
        

#各ファイルからデータを取得してXに追加
X = []
label_list = []
for file in input_files:
    in_file = open(file, newline="")
    
    #ヘッダー行からlabelを取得して格納
    reader = csv.reader(in_file)
    header = next(reader)
    label = header[0].split(" ")[8]
    label_list.append(label)
    
    #値をリストに格納
    val_list = []
    for row in reader:
        val_list.append(float(row[0]))
        
    X.append(val_list)
    in_file.close()
    
    
    
#Xはリストのリストだけど、各要素の長さが違うと（違わないはずだが）
#まずいので最小のものに合わせて縮める
min_len = len(X[0])
for i in range(len(X)):
    if min_len > len(X[i]):
        min_len = len(X[i])

for i in range(len(X)):
    X[i] = X[i][0:min_len]

#tsne
X = np.array(X)


        


tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)

X_tsne = tsne.fit_transform(X)
plot_embedding(
    X_tsne
    ,label_list
     ,"t-SNE embedding of the digits" )


        
        
    
    
    
    
    
    


