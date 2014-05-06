#   pyWords is a program that counts the number of times a word or words
#   occur in a text file 
#
#   ***Disclaimer I am not the author of the scanner module that is  ***
#   ***distributed with this program it belongs to Dr. John C. Lusth ***
#   ***and is distributed under his original license.                ***
#
#   this program takes command line input in the form:
#   python3 pyWords.py <filename> <keyword> <keyword> ...
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from scanner import *

def main():
    print("pyWords  Copyright (C) 2014 Cameron M. Brock")
    print("This program comes with ABSOLUTELY NO WARRANTY")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions")
    print("Special Thanks to Dr. John C. Lusth for the inspiration and")
    print("some of the code")
    s = Scanner(sys.argv[1])
    tokens = []
    t = s.readtoken()
    while (t != ""):
        tokens.append(t)
        t = s.readtoken()
    clean = []
    for i in range(0,len(tokens),1):
        c = cleanToken(tokens[i])
        clean.append(c)
    small = []
    for i in range(0,len(clean),1):
        c = reduceToken(clean[i])
        small.append(c)
    for i in range(2,len(sys.argv),1):
        c = countOccurrences(sys.argv[i],small)
        print(sys.argv[i],"appears",c,"times")
    return

def cleanToken(token):
    cleanToken = ""
    for i in range(0,len(token),1):
        if (token[i].isalpha()):  #test token[i] to see if it is a letter
            cleanToken = cleanToken + token[i]
    return cleanToken
def reduceToken(token):
    char = ""
    for i in range(0,len(token),1):
        char = char +  toLower(token[i])
    return char

def toLower(ch):
    if (ord(ch) <= ord('Z')): #this is true if ch is uppercase
        return chr(ord(ch) + ord('a') - ord('A'))
    else: #otherwise ch is lowercase, so return it
        return ch
        
def countOccurrences(target,array):
    count = 0
    for i in range(0,len(array),1):
        if (target == array[i]):
            count += 1
    return count

main()
