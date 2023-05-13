import os
from .exceptions import KeyNotFound, FileEmpty

def _fixtext(text):
    return text.replace('\n', '')

class load():
    def __init__(self,filepath):
        if not os.path.exists(filepath):
            raise FileExistsError(f"The following path {filepath} was not found\n E03")
        self.path = filepath
    
    def read(self,key):
        with open(self.path,"r") as f:
            maxl = f.readlines()
            if len(maxl) == 0:
                raise FileEmpty(f'The Following File with this path "{self.path}" is empty\n Failure_code: E02')
            for i in range(len(maxl)):
                s = i - 1
                if maxl[s].split('=')[0] == key:
                    break
            if maxl[s].split('=')[0] == key:
                value = maxl[s].split('=')[1]
            else:
                raise KeyNotFound(f'The Following key "{key}" was not found within the porperties file\n Failure_code: E01')
        return _fixtext(value)
    
    def readall(self):
        output = {}
        with open(self.path,"r") as f:
            maxl = f.readlines()
            if len(maxl) == 0:
                raise FileEmpty(f'The Following File with this path "{self.path}" is empty\n Failure_code: E02')
            for i in range(len(maxl)):
                s = i - 1
                if len(maxl[s].split('=')) == 2:
                    output[maxl[s].split('=')[0]] = _fixtext(maxl[s].split('=')[1])
        
    def close(self):
        self.path.destory()