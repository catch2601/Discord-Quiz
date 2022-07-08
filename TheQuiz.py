import time
import os
import colorama
import ctypes
from playsound import playsound

os.system('color')
from colorama import Fore
ctypes.windll.kernel32.SetConsoleTitleW("Press enter to start!")

def soundCorrect():
		playsound('assets\correct.mp3')

def soundIncorrect():
		playsound('assets\incorrect.mp3')


score = 0
print(Fore.BLUE + "  _______ _            _____ _____  _____  _____ ____  _____  _____     ____        _     ")
print(" |__   __| |          |  __ \_   _|/ ____|/ ____/ __ \|  __ \|  __ \   / __ \      (_)    ")
print("    | |  | |__   ___  | |  | || | | (___ | |   | |  | | |__) | |  | | | |  | |_   _ _ ____")
print("    | |  | '_ \ / _ \ | |  | || |  \___ \| |   | |  | |  _  /| |  | | | |  | | | | | |_  /")
print("    | |  | | | |  __/ | |__| || |_ ____) | |___| |__| | | \ \| |__| | | |__| | |_| | |/ /")
print("    |_|  |_| |_|\___| |_____/_____|_____/ \_____\____/|_|  \_\_____/   \___\_\\__,_|_/___|")
print("                                                                                          ")
print("                                                                                          ")
print(Fore.WHITE + "Welcome to the DISCORD quiz!\nAnswer all the questions and try to get the correct score!")
input("Press Enter to continue")
print("                                                                                          ")


# FIRST QUESTION
ctypes.windll.kernel32.SetConsoleTitleW("Your current score is: " + str(score))
print(Fore.CYAN + "QUESTION ONE")
print("What year was discord made in?\nA:2019\nB:2012\nC:2015\nD:2014")
answer = input().lower()
if answer == "c":
    print(Fore.GREEN + "You got it correct! A point has been added to your score.")
    newscore = score + 1
    score = newscore
    soundCorrect()
else:
    print(Fore.RED + "You got this question wrong! The correct answer was C (2015)")
    soundIncorrect()


# SECOND QUESTION
print("                                                                                          ")
print("                                                                                          ")
ctypes.windll.kernel32.SetConsoleTitleW("Your current score is: " + str(score))
print(Fore.BLUE + "QUESTION TWO")
print("Who is Discord's CEO?\nA:Tim Cook\nB:Jason Citron\nC:Elon Musk\nD:Mark Zuckerberg")
answer = input().lower()
if answer == "b":
    print(Fore.GREEN + "You got it correct! A point has been added to your score.")
    newscore = score + 1
    score = newscore
    soundCorrect()
else:
    print(Fore.RED + "You got this question wrong! The correct answer was B (Jason Citron)")
    soundIncorrect()

# THIRD QUESTION
print("                                                                                          ")
print("                                                                                          ")
ctypes.windll.kernel32.SetConsoleTitleW("Your current score is: " + str(score))
print(Fore.CYAN + "QUESTION THREE")
print("How many people actively use Discord?\nA:3.2 Million\nB:140 Million\nC:780 Thousand\nD:223 Million")
answer = input().lower()
if answer == "b":
    print(Fore.GREEN + "You got it correct! A point has been added to your score.")
    newscore = score + 1
    score = newscore
    soundCorrect()
else:
    print(Fore.RED + "You got this question wrong! The correct answer was B (140 Million)")
    soundIncorrect()

# FOURTH QUESTION
print("                                                                                          ")
print("                                                                                          ")
ctypes.windll.kernel32.SetConsoleTitleW("Your current score is: " + str(score))
print(Fore.BLUE + "QUESTION FOUR")
print("How much does one month of DISCORD NITRO cost?\nA:$7.99\nB:$4.99\nC:$12.99\nD:$9.99")
answer = input().lower()
if answer == "d":
    print(Fore.GREEN + "You got it correct! A point has been added to your score.")
    newscore = score + 1
    score = newscore
    soundCorrect()
else:
    print(Fore.RED + "You got this question wrong! The correct answer was D ($9.99)")
    soundIncorrect()

print("                                                                                          ")
print("                                                                                          ")
print(Fore.CYAN + "Thank you for playing the quiz!")
accuracy = 25 * score
print("You got a score of " + str(score) + "! That gives you an accuracy of %" + str(accuracy))
time.sleep(5)

