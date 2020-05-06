"""
*  ____           _                      
* |  _ \ ___   __| |_ __ _   _ _ __ ___  
* | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""
from sys import platform

def getOS():
    if platform == 'linux' or platform == 'linux2':
        return 'linux'
    elif platform == 'darwin':
        return 'osx'
    elif platform == 'win32' or platform == 'win64':
        return 'windows'
    elif platform == 'orbis':
        return 'playstation'
    elif platform == 'nx':
        return 'nintendo'
    elif platform == 'xbox':
        return 'xbox'
