import pyttsx3
import os

pyttsx3.speak("Hello There! This is your personal assistant. I can make your life easier!")
pyttsx3.speak("Please Enter Your Name to make your experience more enjoyable: ")
name = input("You entered : ")
      
while True:
    pyttsx3.speak("Hey!"+ name +"What would you like me to do for you ?")

    command = input("What would you like me to do for you ? ").lower()
    
    if "open chrome" in command or "run chrome" in command or "chrome" in command:
        pyttsx3.speak("Hey!"+ name +"Welcome to Chrome!")
        os.system("chrome")                
                                    
    elif "whatsapp" in command or "open whatsapp" in command or "run whatsapp" in command:
        pyttsx3.speak("Hey!"+ name +"Welcome to Whatsapp!")
        os.system("WhatsApp")
                            
    elif "cmd" in command or "run cmd" in command or "execute cmd" in command:
        pyttsx3.speak("Hey!"+ name +"Welcome to Command Prompt!")
        os.system("cmd")
    
    elif "run music player" in command or "music player" in command:
        pyttsx3.speak("Hey!"+ name +"Welcome to Music Player!")
        os.system("PotPlayer")
        
    elif "run notepad" in command or "execute notepad" in command or "notepad" in command:
        pyttsx3.speak("Hey!"+ name +"Welcome to Notepad!")
        os.system("notepad")
             
    elif "stop" in command or "exit" in command or "bye" in command or "quit" in command:
        pyttsx3.speak("It was a pleasure talking to you! "+ name +" see you later! bye !")
        break
      
    else:
        pyttsx3.speak("Sorry, but the command you are looking for is currently unavailable. We are working behind the scene to make it available for you. Have a Good day!")
        
            
