#imports
import winsound #for .wav files
#from pygame import mixer #for .mp3
import win32com.client as wincl
import os
#def funcs and vars
speak = wincl.Dispatch("SAPI.SpVoice")
def say():
    iwanttosay = input('Say: ')
    #os.system('clc' if os.name == 'nt' else 'clear')
    return iwanttosay
def menu():
    ans = ""
    options = ['n', 'gay', 'som', 'exit']
    while ans.lower() not in options: 
        print('###########################################')
        print('AAC-0.0.3, (c) Alex Healey, TreasDev 2019')
        print('Source of sound files in readme.txt')
        print('Select mode: ')
        print('- Standard AAC [n]')
        print('- Gay mode [gay]')
        print('- Somerset mode [som]')
        print('- Exit Software [exit]')
        ans = input('Input: ')
        if ans.lower == 'n' or ans.lower() == 'gay':
            os.system('clc' if os.name == 'nt' else 'clear')
            break
    return ans
#run 
ans = menu()
while ans.lower() != 'exit':
    if ans.lower() == 'n':
        n = 0
        while n < 1:
            string = say()
            if string.lower() == 'exit':
                break
            else:
                speak.Speak(string)
    elif ans.lower() == 'gay':
        n = 0   
        while n < 1:
            string = say()
            if string.lower() == 'exit':
                break
            else:
                pass
            if string.lower() == 'no':
                winsound.PlaySound('gay/not-today-satan.wav', winsound.SND_ASYNC)
            elif string.lower() == 'yes':
                winsound.PlaySound('gay/yas.wav', winsound.SND_ASYNC)
            elif string.lower() == 'damn honey':
                winsound.PlaySound('gay/honey.wav', winsound.SND_ASYNC)
            else:
                speak.Speak(string)
    elif ans.lower() == 'som':
        n = 0
        while n < 1:
            string = say()
            if string.lower() == 'exit':
                break
            else:
                pass
            if string.lower() == 'yes':
                winsound.PlaySound('somerset/oo-arr.wav', winsound.SND_ASYNC)
            elif string.lower() == 'good job':
                winsound.PlaySound('somerset/proper-job.wav', winsound.SND_ASYNC)
            elif string.lower() == 'hello':
                winsound.PlaySound('somerset/hello.wav', winsound.SND_ASYNC)
            elif string.lower() == 'good':
                winsound.PlaySound('somerset/gert-lush.wav', winsound.SND_ASYNC)
            elif string.lower() == 'anyway':
                winsound.PlaySound('somerset/in-any-case.wav', winsound.SND_ASYNC)
            elif string.lower() == 'where are you going':
                winsound.PlaySound('somerset/were-be-to.wav', winsound.SND_ASYNC)
            else:
                speak.Speak(string)
    elif ans.lower() == 'exit':
        break
    ans = menu()