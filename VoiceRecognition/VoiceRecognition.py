import speech_recognition as sr
import os
import subprocess as sp

def run_Simon():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Testing")
            audio=r.listen(source)
        
            try:
                text=r.recognize_google(audio) 
                print('You said: {}'.format(text))
                if text=="stop":
                    break
                else:
                    if text=="open Youtube Folder":
                        os.startfile('Youtube_launch.bat')
                    
                    elif text=="open Google Chrome":
                    
                        sp.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
                        print("Opening Google Chrome.")
                    elif text=="hey Simon":
                        print("Yes?")
                        audio=r.listen(source)
                        text=r.recognize_google(audio)
                        if text=="search":
                            print("What would you like to search?")
                            audio=r.listen(source)
                            text=r.recognize_google(audio)
                            print('Searching for: {}'.format(text))
                            run_Search(text)
            except:
                print("Sorry could you repeat that?")

def run_Search(query):
    size = 10
    sites = [None] * size
   
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
    i = 0
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        str = j
        sites[i] = str
        print(sites[i]) 
        i = i + 1

#run_Simon()
run_Search("pizza")