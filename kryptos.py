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

#guidelines
'''Guidelines 
        1. This contest is open to lone wolves or teams of upto 3 participants. 
        2. A registration fee of ₹50 per head is required.
        3. This is an event that focuses on the overall technical skillset of a team.
        4. There will be a set of __ challenges which will be based on Cryptography, Logical gates, Coding and DSA.
        5. Unlocking one challenge opens up the hint or key to the other.
        6. It is an entirely offline event, and no access to mobile phone, or internet will be allowed during the game.
        7. Decision of judges will be final and binding.'''  #this should be formatted and shortened to be printed at the begining of the event

def start(): #call this function after printing guidelines
    typestring("WELCOME TO KRYPTOS") 
    typestring(">> Mission log: Vault 71") #some story line that gives hint for the first clue
    typestring(">> We cannot continue further without access to the core. The bossman said it was built by [REDACTED].")
    typestring(">> This vault wasn't built to keep people out, but to keep [REDACTED] in")
    typestring(">> Opening the door requires a pin.")
    q0()


def q0(): # Math ,Number of trailing zeros in 75P45
    print("\n")
    typestring("Number of trailing zeros in ⁷⁵P₄₅")
    while True:

            response = input('Code 0 : ')
            if response == '11':
                typestring(">> A low hum fills the room accompanied by the grinding of metal as colossal gears engage with a slow, deliberate clunk, opening the vault door")
                break
            else:
                typestring(">> Whoa, wrong input... the system's rejecting it.", 0.5)
    q1()

def q1(): #caesar cypher shifted by 11
    print("\n")
    typestring(">> Looks like someone's been here before. There are cryptic symbols etched onto the walls.")
    typestring(">> This one seems shifted. Maybe the pin has something to do with it.")
    typestring("PYEPCESPNLELNZXMD")
    while True:
        response = input('Code 1 : ')
        if response == 'ENTERTHECATACOMBS':
            typestring(">> The next one might not be that easy")
            break
        else:
            typestring(">> That doesn't seem right, I should rethink this", 0.5)
    q2()

def q2():
    while True:
        response = input('Code 2 : ')
        if response == 'dummycode':
            break
        else:
            print('bruh cringe')

start()