import os
from .exceptions import KeyNotFound, FileEmpty

class load():
    def __init__(self,filepath):
        self.path = filepath
    
    def read(self,key):
        with open(self.path,"w") as f:
            maxl = f.readlines()
            if len(maxl) == 0:
                raise FileEmpty(f'The Following File with this path "{self.path}" is empty\n Failure_code: E02')
            for i in range(len(maxl)):
                s = i - 1
                if f.readline().split('=')[0] == key:
                    break
            if f.readline().split('=')[0] == key:
                value = f.readline().split('=')[1]
            else:
                raise KeyNotFound(f'The Following key "{key}" was not found within the porperties file\n Failure_code: E01')
        return value
        
    def close(self):
        self.path.destory()