import os, io
from .exceptions import *

class Properties:
    def __init__(self,fp: io.TextIOWrapper):
        """# Properties class
        
        Parser for the Java Properties file format.
        
        ### Functions
        - getdict()
            - Makes the dictionary structure of all the key(s), subkey(s) and values and compresses the key(s), subkey(s) and values into a dictionary
        
        - getkey(*key)
            - Returns the value from the key(s) passed to the function
            - Examples: getkey("username"), getkey("user","password")
        
        - setvalue(*key,value="New value")
            - Changes the value to a new value
            - Examples: setvalue("username",value="Root"), setvalue("user","password",value="My Very not so secure password")
        
        - update()
            - Updates the file to match the newlines added
        
        - update_usingdict()
            - Updates the file from the changes to self.keys
        
        - close()
            - Closes the Properties class including the passed TextIOWrapper
        """
        self.fp = fp
        self.keys = {}
        try:
            self.lines = fp.readlines()
        except:
            self.lines = []
        
        try:
            self.getdict()
        except:
            pass
            
    def _add_to_dict(self, d, keys, value):
        key = keys[0]
        if len(keys) == 1:
            d[key] = value
        else:
            if key not in d:
                d[key] = {}
            self._add_to_dict(d[key], keys[1:], value)

    
    def getdict(self):
        """Makes the dictionary structure of all the key(s), subkey(s) and values and compresses the key(s), subkey(s) and values into a dictionary.
        
        ### Returns
        - dict
            - The dictionary structure that contains all the key(s), subkey(s) and values
            
        ### Raises
        - IncorrectModeError
            - Raises if the properties file format is incorrect
        """
        for i in self.fp.readlines():
            
            unformattedline = i.strip()
            
            #Ignores commits starting with #
            
            if not unformattedline or unformattedline.startswith('#'):
                continue
            
            key, value = unformattedline.split("=")
            
            key = key.strip()
            value = value.strip()
            
            subkeys = key.split('.')
            self._add_to_dict(self.keys, subkeys, value)
            return self.keys
    
    def getkey(self,*keys):
        """Returns the value from the key(s) passed to the function

        ### Args
            *keys (str):
                The key(s) to get the value

        ### Returns:
        - str
            - Value of the key(s) passed
        - None
            - Returns None if the key(s) is not found
        """
        
        fullkeystructure = ""
        s = 0
        for i in keys:
            if s == 0:
                fullkeystructure += i
            else:
                fullkeystructure += "." + i
            s += 1
        
        k = None
        
        for i in self.lines:
            unformattedline = i.strip()
            
            if not unformattedline or unformattedline.startswith('#'):
                continue
            
            key, value = unformattedline.split("=")
            if key == fullkeystructure:
                k = value
                break
        
        return k

    def setvalue(self,*keys,value="Value"):
        """Changes the value to a new value

        ### Args
            *keys (str):
                The key(s) to get pointing to the value
            
            value (str):
                New value to change
        """
        fullkeystructure = ""
        s = 0
        for i in keys:
            if s == 0:
                fullkeystructure += i
            else:
                fullkeystructure += "." + i
            s += 1
        
        d = 0
        for i in self.lines:
            unformattedline = i.strip()
            
            if not unformattedline or unformattedline.startswith('#'):
                continue
            
            key, value = unformattedline.split("=")
            if key == fullkeystructure:
                
                break
            d += 1
    
    def close(self):
        """Closes the Properties class including the TextIOWrapper"""
        self.fp.close()
        self.lines = None
        self.fp = None
        self.keys = None