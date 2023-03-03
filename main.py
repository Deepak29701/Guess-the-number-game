import pyttsx3
from bs4 import BeautifulSoup
import requests
import random

engine=pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 2.0)    
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def generate_choice():
    p = random.randint(0,100)
    return p

name = input("Enter your name:")
print(f"\n### Welcome to the Game, {name} ###\n")
speak(f"Welcome to the Game, {name}")

def compare():
    computer_choice = generate_choice()
    n = input("Enter the number of turns:")
    count = 0
    for i in range(1,int(n)+1):
        user_input = int(input("Enter your choice:"))

        if (computer_choice > user_input):
            print("You guessed a lesser number\n")
            speak("You guessed a lesser number")
            count = count+1
            
        elif(computer_choice < user_input):
            print("You guessed a greater number\n")
            speak("You guessed a greater number")
            count = count+1
            
        else:
            print("You guessed it right\n")
            speak("You guessed it right")
            count = count+1
            break

    return count

total_turns_taken = compare()
print(f"You have guessed the right number in {total_turns_taken} turns")
speak(f"You have guessed the right number in {total_right} turns")
