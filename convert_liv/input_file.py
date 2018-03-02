import os
import scipy.fftpack
import numpy as np

class InputFile:
    def __init__(self, input_path, framerate, data, start, length):
        self.inpath = input_path
        self.ofilename = os.path.basename(input_path)[:-4] + ".csv"
        self.framerate = framerate
        self.data = data
        self.start = float(start)
        self.length = length
        self.label = ""
        
    def show_params(self):
        """
        show parametars
        """
        print("filename: {}, start={}, label={}".format(
            os.path.basename(self.inpath)
            , self.start, self.label))
        
    def check_convertable(self):
        """
        得られたデータが指定した長さか確認する
        """
        if(int(self.length * self.framerate) == len(self.data)):
            return True
        else:
            return False
        
    def data_len(self):
        return len(self.data) / self.framerate 
    
    def set_label(self, label):
        self.label = label
        
    def calc_fft(self):
        """
        calc fft and return ndarray
        """
        X = scipy.fftpack.fft(self.data)
        amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
        return amplitudeSpectrum
        
        
        
        