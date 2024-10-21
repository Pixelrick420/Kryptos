#kryptos event source code
import sys
import time
import math

#typeanimation
def typestring(text, delay=0.03): #use this function to add type animation to strings
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

slowtime = 0.1 #give this as delay for wrong answer so that they can't bruteforce 

#guidelines
print("\n")
guidelines = '''GUIDELINES
        1. The teams will have to complete 5 challenges which will be based on Cryptography, Logic gates, Coding and/or DSA.
        2. The challenges require the players to find a code/answer and type it into the console. 
        3. After completing a challenge, please inform the nearest volunteer. The winners will be decided based on whoever completes the challenges the fastest.
        4. The time limit for the event is 3 hours. 
        5. No access to mobile phone, or internet will be allowed during the game.
        6. You can ask for hints if you feel stuck, but these will result in negative marks and may affect your final time.
        7. Decision of judges will be final and binding.'''  
print(guidelines + "\n\n")

def start(): #call this function after printing guidelines
    typestring("WELCOME TO KRYPTOS") 
    typestring(">> Mission log: Vault 71.") #some story line that gives hint for the first clue
    typestring(">> Entry #6")
    typestring(">> We cannot continue further without access to the core. The bossman said it was built by [REDACTED].")
    typestring(">> The vault door looks like it wasn't built to keep people out..... but to keep something in.")
    typestring(">> Opening the door requires a pin.")
    q0()


def q0(): # Math: number of trailing zeros in 75P45
    typestring("Number of trailing zeros in ⁷⁵P₄₅")
    while True:

            response = input('Code 0 : ')
            if response == '11':
                typestring(">> A low hum fills the room accompanied by the grinding of metal as colossal gears engage with a slow, deliberate clunk, opening the vault door.")
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
            typestring(">> Output... of what?")
            print("\n")
            typestring(">> Entry #9")
            typestring(">> Bossman told us to take a closer look at section 06. Navigating the fissures and cracks has become arduous.")
            typestring(">> One of our agents leaned against the wall causing a rock next to the engraving to slide inwards.")
            typestring(">> A series of dim candles light, illuminating 8 switches that line the bottom of the opposing stone wall.")
            typestring(">> The switches are slightly misaligned, as though they were shifted or tampered with. ")
            typestring(">> The candles flicker gently, casting eerie shadows that dance across a familiar diagram, one of a logic circuit. [circuit.jpg]")
            typestring(">> I think we may have the answer to that question.")
            break
        else:
            typestring(">> That doesn't make any sense. I should reconsider.", slowtime)
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
    typestring(">> The rockface containing the switches falls forward with a loud thud.")
    typestring(">> Agent 034 jumps forward, marginally avoiding the falling rock.")
    typestring(">> His face, illuminated by a warm golden light emitted by he newly exposed wall behind the fallen rockface.")
    typestring(">> Deep cracks crisscross the stone, yet the ancient writing carved into it remains pristine, untouched by the erosion that has worn down the rest of the wall.")
    typestring(">> The runes[rune.py]... this is how they kept their messages from falling into enemy hands")
    typestring(">> The rumbling is getting louder. We have no time for causion.")
    typestring(">> We go deeper into the catacombs. There is no turning back.")
    print("\n")
    typestring("Entry #14")
    typestring(">> The way to reach the core remained elusive... until we found the gate.")
    typestring(">> We were exploring section 08 when we saw it. a towering, ancient structure made of thick, dark metal, its surface etched with intricate runes and symbols from a forgotten age.")
    typestring(">> The metal is worn and slightly rusted yet impenetrable. The gate requires a pin.")
    typestring(">> Carved into the opposing wall was a message. Maybe it was left by [REDACTED].")
    typestring("tuian in(*h   boec ) mslapst'*ibtita a *hotostt3 *andvifso''seidirtia*t ccnna d* rn oehnn*Wef,m h 1'")

    while True:
        response = input('Code 3 : ')
        if response == "What is the number of distinct, valid combinations of parenthesis that contain 31 '(' and ')'":
            print("""Example : Consider a string with 3 '(' and ')'.There are 5 distinct valid combinations.
                        - ((()))
                        - (())()
                        - ()(())
                        - ()()()
                        - (()()) 
                  """)
            break
        else:
            typestring(">> No... that can't be it. There must be something more.", slowtime)
    q4()

def q4(): # DSA question involving Catalan numbers 
    typestring(">> Ofcourse.. the pin.")
    while True:
        response = input('Code 4 : ')
        if response == '14428278950913093728': # Catalan number for n=31
            break
        else:
            typestring(">> Incorrect. I should be careful. We can't afford any mustakes.", slowtime)
    end()

def end(): # Final part of the story
    print("\n")
    typestring(">> The gate slowly grinds open, revealing a massive chamber filled with intricate carvings and encrypted writing.")
    typestring(">> In the center of the room lies the ancient artifact, glowing. The light flowing in strange, twisting patterns that seem almost alive.")
    typestring(">> This is it... the artifact we've been searching for. The source of all the encrypted messages, the one they swore to protect at all costs.")
    typestring(">> A torn piece of paper lies on the floor next to the artifact. It's the last log entry from the previous team that was sent here.")
    typestring(">> 'We weren't meant to find this'", slowtime)
    typestring(">> They never returned...")
    print("\n")
    time.sleep(3)
    typestring("CONGRATULATIONS! You've completed KRYPTOS.")
    
start()