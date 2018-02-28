import os

class InputFile:
    def __init__(self, input_path, data, framerate):
        self.inpath = input_path
        self.ofilename = os.path.basename(input_path)[:-4] + ".csv"
        self.framerate = framerate
        self.data = data
        
