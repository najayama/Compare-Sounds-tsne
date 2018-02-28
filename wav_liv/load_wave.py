import wave
import numpy as np
def load_wave(path, start, length):
    """
    pathの示すwavファイルを開いてstart秒からlength秒読み込む
    返り値：(fs, data) fsがサンプリング周波数、dataはndarrayのデータ
    """
    
    infile = wave.open(path, "r")
    
    #秒をフレームに換算
    fs = infele.getframerate()
    start_frame = start * fs
    r_frame = length * fs 

    #整数データを量子化ビット数に応じて正規化    
    raw_data = wf.readframes(int(r_frame))

    if wf.getsampwidth() == 2:
        x = np.frombuffer(raw_data, dtype="int16") / (32768.0)
    else:
        x = np.frombuffer(raw_data, dtype= "u1") 
        x = [(i - 128) / 128 for i in x]
    
    #もしもステレオなら足して二で割ってモノラルにする
    if wf.getnchannels() == 2:
        left = x[    0::2]
        right = x[1::2]
        x = [(i + j) / 2 for i, j in zip(left, right)]
        
    return fs, x