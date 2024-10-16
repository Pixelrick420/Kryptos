#kryptos event source code
import sys
import time
import math

#typeanimation
def typestring(text, delay=0.01): #use this function to add type animation to strings
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

slowtime = 0.05 #give this as delay for wrong answer so that they can't bruteforce 

#guidelines
print("\n")
guidelines = '''GUIDELINES
        1. The teams will have to complete 5 challenges which will be based on Cryptography, Logic gates, Coding and/or DSA.
        2. The challenges require the players to find a code/answer and type it into the console. 
        3. After completing a challenge, please inform the nearest volunteer. This is to ensure that there are no ties.
        4. The time limit for the event is 3 hours. 
        5. This is an entirely offline event, and no access to mobile phone, or internet will be allowed during the game.
        6. Decision of judges will be final and binding.'''  
print(guidelines + "\n\n")

def start(): #call this function after printing guidelines
    typestring("WELCOME TO KRYPTOS") 
    typestring(">> Mission log: Vault 71.") #some story line that gives hint for the first clue
    typestring(">> Entry #12")
    typestring(">> We cannot continue further without access to the core. The bossman said it was built in 19XX by [REDACTED].")
    typestring(">> The vault door looks like it wasn't built to keep people out..... but to keep something in.")
    typestring(">> Opening the door requires a pin.")
    q0()


def q0(): # Math ,Number of trailing zeros in 75P45
    typestring("Number of trailing zeros in ⁷⁵P₄₅")
    while True:

            response = input('Code 0 : ')
            if response == '11':
                typestring(">> A low hum fills the room accompanied by the grinding of metal as colossal gears engage with a slow, deliberate clunk, opening the vault door")
                break
            else:
                typestring(">> Whoa, wrong input... the system's rejecting it. Maybe a different approach might be needed", slowtime)
    q1()

def q1(): #caesar cypher shifted by 11
    typestring(">> Looks like someone's been here before. There are cryptic symbols etched onto the walls.")
    typestring(">> This one seems shifted. Maybe the pin has something to do with it.")
    typestring("ESPZFEAFETDDPGPYEPPY")
    while True:
        response = input('Code 1 : ')
        if response == 'THEOUTPUTISSEVENTEEN':
            typestring(">> One of our agents rests against the wall causing a rock next to the engraving to slide inwards.")
            typestring(">> A series of dim candles light illuminating 8 switches that line the bottom of the opposing stone wall.")
            typestring(">> The switches are slightly misaligned, as though they were shifted or tampered with. ")
            typestring(">> The candles flicker gently, casting eerie shadows that dance across a familiar diagram, one of a logic circuit.")
            break
        else:
            typestring(">> That doesn't make any sense. Maybe I should reconsider my approach. The answer might be important.", slowtime)
    q2()

def q2(): #logic circuit
    typestring(">> If the output is to be seventeen, how must the switches be toggled?")
    print("(code will be an 8 bit binary number)")
    while True:
        response = input('Code 2 : ')
        if response == '10010101':
            typestring(">> The switches slowly move into the rock face letting out electrical sparks.")
            typestring(">> The faint sound of an ancient machine activating fills the room.")
            typestring(">> The sound slowly becomes a thunderous rumble that causes the walls the shake.")
            break
        else:
            typestring(">> Carefully adjusting the switches causes a low spark that dies out slowly. That doesn't seem right, I should rethink this", slowtime)
    q3()

def q3(): # Transposition Cipher
    typestring(">> The rockface containing the switches falls forward with a loud thud revealing [REDACTED]")
    typestring(">> The runes... this is how they kept their messages from falling into enemy hands")
    typestring(">> This is why we are here. Vault 71 was where they kept it.")
    typestring(">> The rumbling is getting louder. We have no time for causion.")
    typestring(">> Agent 034 jumps forward, marginally avoiding a falling rock.")
    typestring(">> We go deeper into the catacombs. There is no turning back.")
    print("\n")
    typestring("Entry #14")
    typestring(">> We had lost all hope of escape...")
    typestring(">> We found an exit. But ofcourse, it requires a pin.")
    typestring(">> Carved into the opposing wall was a message.")
    typestring("tuian in(*h   boec ) mslapst'*ibtita a *hotostt3 *andvifso''seidirtia*t ccnna d* rn oehnn*Wef,m h 1'")

    while True:
        response = input('Code 3 : ')
        if response == "What is the number of distinct, valid combinations of parenthesis that contain 31 '(' and ')'":
            break
        else:
            typestring(">> That doesn't make sense... I should think again. This could be important.", slowtime)
    q4()

def q4(): # DSA question involving Catalan numbers 
    typestring(">> The pin.")
    while True:
        response = input('Code 4 : ')
        if response == '4861946401452': # Catalan number for n=31
            typestring(">> The carvings on the cave walls glow brighter, and the ground trembles as the rockface moves away.")
            typestring(">> A blinding light pours in, revealing the overworld.")
            break
        else:
            typestring(">> Incorrect. I should be careful. We can't risk another cave-in", slowtime)
    end()

def end(): # Final part of the story
    print("\n")
    typestring(">> Entry #19")
    typestring(">> (some ending blah blah)")
    typestring("Congratulations! You've completed KRYPTOS.")
    
start()