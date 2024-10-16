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
                typestring(">> Whoa, wrong input... the system's rejecting it. Maybe a different approach might be needed", slowtime)
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
    typestring(">> If the output is to be seventeen, how must the switches be toggled?")
    print("(code will be an 8 bit binary number)")
    while True:
        response = input('Code 2 : ')
        if response == '10010101':
            typestring(">> The switches slowly move into the rock face letting out electrical sparks.")
            typestring(">> The faint sound of an ancient machine activating fills the room.")
            break
        else:
            typestring(">> Carefully adjusting the switches causes a low spark that dies out slowly. That doesn't seem right, I should rethink this", slowtime)
    q3()

def q3(): # Transposition Cipher
    typestring(">> A hidden compartment slides open, revealing a metallic panel with tiles that form a scrambled message.")
    typestring(">> After careful observation, the message appears to be:")

    typestring("")

    typestring(">> It looks like the words are jumbled, but they form a question.")
    while True:
        response = input('Code 3 : ')
        if response == '':
            typestring(">> As you solve the puzzle, the tiles stop moving, locking into place.")
            break
        else:
            typestring(">> The tiles shift slightly, mocking the wrong answer. Maybe focus on the structure of the question itself.", slowtime)
    q4()

def q4(): # DSA question involving Catalan numbers (in riddle form)
    typestring(">> You walk down the newly revealed passage, where ancient carvings adorn the walls.")

    while True:
        response = input('Code 4 : ')
        if response == '4861946401452': # Catalan number for n=31
            typestring(">> The carvings glow brighter, and the ground trembles as a section of the wall slides open.")
            typestring(">> A blinding light pours in, revealing the final chamber.")
            break
        else:
            typestring(">> The carvings dim slightly, rejecting the incorrect answer. Symmetry must be maintained.", slowtime)
    end()

def end(): # Final part of the story
    typestring(">> You step into the final chamber. In the center stands a grand mechanism, a fusion of ancient technology and cryptography.")
    typestring(">> The mechanism hums with energy as you approach. As you input the final code, the gears click into place.")
    typestring(">> The vault’s secret is finally revealed: a radiant core of knowledge, untouched for centuries.")
    typestring(">> The mission is complete. You've not only unlocked the vault but uncovered the hidden legacy of Vault 71.")
    typestring(">> The room falls silent, leaving you with a sense of accomplishment and mystery about what lies ahead.")
    typestring(">> Congratulations! You've completed KRYPTOS.")
    
start()

    
start()