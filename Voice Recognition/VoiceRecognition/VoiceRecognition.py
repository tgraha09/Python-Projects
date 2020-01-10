import speech_recognition as sr
import os 
import subprocess as sp


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
        except:
            print("Sorry could you repeat that?")
          