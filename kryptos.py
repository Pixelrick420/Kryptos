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
                typestring(">> Whoa, wrong input... the system's rejecting it.", slowtime)
    q1()

def q1(): #caesar cypher shifted by 11
    typestring(">> Looks like someone's been here before. There are cryptic symbols etched onto the walls.")
    typestring(">> This one seems shifted. Maybe the pin has something to do with it.")
    typestring("ESPZFEAFETDDPGPYEPPY")
    while True:
        response = input('Code 1 : ')
        if response == 'THEOUTPUTISSEVENTEEN':
            typestring(">> One of our agents slants against the wall causing a rock next to the engraving to slide inwards.")
            typestring(">> A series of dim candles light illuminating 8 switches that line the bottom of the opposing stone wall.")
            typestring(">> The switches are slightly misaligned, as though they were shifted or tampered with. ")
            typestring(">> The candles flicker gently, casting eerie shadows that dance across a familiar diagram, one of a logic circuit.")
            break
        else:
            typestring(">> That doesn't make any sense. Maybe I should reconsider my approach. The answer might be important.", slowtime)
    q2()

def q2(): #logic circuit
    typestring(">> If the output is seventeen, how should the switches be toggled?")
    while True:
        response = input('Code 2 : ')
        if response == '10010101':
            typestring(">> The switches slowly move into the rock face letting out electrical sparks.")
            typestring(">> A faint sound of some machine activating fills the room.")
            break
        else:
            typestring(">> Carefully adjusting the switches causes a low spark that dies out slowly. That doesn't seem right, I should rethink this", slowtime)

start()