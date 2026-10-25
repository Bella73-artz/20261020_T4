
import datetime

CURRENT_YEAR = datetime.datetime.now().year
CURRENT_MONTH = datetime.datetime.now().month
CURRENT_DAY = datetime.datetime.now().day

meses = {
    "january" : 1,
    "february" : 2,
    "march" : 3,
    "april" : 4,
    "may" : 5,
    "june" : 6,
    "july" : 7,
    "august" : 8,
    "september" : 9,
    "october" : 10,
    "novemebr" : 11,
    "december" : 12,
 }

user_name = input("Hi......hello?..HEELLOOOOOO???" \
"." \
"." \
"...IS ANYONE THER- AHHH. oh hi there!" \
"Im - - -, nice to meet ya, whats your name?: ")

spelling_answer = input(f"{user_name}?? Did i spell that right?: ")
if spelling_answer == "yes":
    print("Cool")
else:
    print("Nahh ur lying i got it right. anyway...")

#pedir año

#pedir mes

do_you_wanna_play = input("...Ok, how about we play a game...i bet i can guess your age right now. You wanna play? yes or no: ")
if do_you_wanna_play == "yes":
    print("COOL. ok ok let me think...")
else:
    print("NO? Well i'm gonna play anyway. you ready? " \
    ".....................")



Validmonth = False

while not Validmonth:
    month = input("Ummmmm give me a hint. What month? I ALREADY KNOW im just checking: ")

    try:
        month_number = meses[month.lower()]
        Validmonth = True

    except KeyError:
        print("Thats not a month silly, tell me a real month")


day = int(input("Wait ok i got it. uhhhh.. wait tell me what day of the month: "))

year = int(input("Of course, uhh. whats your year of birth? "))


age = CURRENT_YEAR-year
#this gives you the person's age as if they have already had their birthday this year. If their birthday hasn't happened yet, you need to subtract one
if (CURRENT_MONTH, CURRENT_DAY) < (month_number, day):
    age = age - 1

import random

x = random.randint(1, 100)

is_it_wrong_age = input(f"Ok i got it. is it...... {x}!!")
if is_it_wrong_age == "yes":
    print("HELL YEAH I'M A GENIUS. That number was randomly generated btw.")
else:
    right_answer = input(f"HUH? THERES NO WAY I GOT IT WRONG oh wait. HAHA i'm silly. ok this time i will guess it: are you {age}?")

if right_answer == "no":
    print("YOU'RE JOKING?? Ugh i give up, whatever. bye.")
else:
    print("HELL YEAH I'M A GENIUS. That was magic btw, so don't think about it too much.")
    if (month_number, day) == (CURRENT_MONTH, CURRENT_DAY):
        print (f"WAIT A MINUTE. is it your birthday?? HAPPY BIRTHDAY {user_name.upper()}")
    else: 
        pass
    
    if age > 60:
        print("oh wow ur old. Anyways it's getting late, i should go. See ya!")
    elif age >= 17 and age <= 60:
        print("Wow so your about my age, cool. Anyways it's getting late, i should go. See ya!")
    elif age <17:
        print ("you're pretty small... Anyways it's getting late, i should go. See ya!")
    