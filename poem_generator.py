#imports
import random
import os
import docx
from words import *

#functions
def pick_word(wordlist):
    n = random.randint(0,(len(wordlist)-1)) # random index
    return wordlist[n]

def subject(caps):
    def check_vowel():
        vowel_subject = ["",adjective(),""] if random.randint(0,1) == 1 else ["",""]
        noun = pick_word(common_nouns)
        vowel_subject[-1] = noun
        matched_list = [v in ['a','e','i','o','u'] for v in vowel_subject[1][0]]
        if all(matched_list):
            vowel_subject[0] = "an"
        else:
            vowel_subject[0] = "a"
        # vowel_subject[1] = adjective() if random.randint(0,1) == 1 else vowel_subject.remove("adjective-placeholder")
        return(' '.join(vowel_subject))
    proper_or_common = random.randint(0,3)
    switcher = {
        0: pick_word(proper_nouns),
        1: "the " + pick_word(common_nouns), # definite article
        2: "the " + adjective() + " " + pick_word(common_nouns),
        3: check_vowel(),
    }
    return(switcher[proper_or_common].capitalize() if caps == True else switcher[proper_or_common])

def verb():
    return(pick_word(verbs))

def preposition():
    return(pick_word(prepositions))

def conjunction():
    return(pick_word(conjunctions))

def adjective():
    return(pick_word(adjectives))

def sentence(caps = True):
    clause = ""
    sentence_type = random.randint(0,1)
    switcher = {
        0: ' '.join([subject(caps), verb()]),
        1: ' '.join([subject(caps), verb(), preposition(), subject(False)]),
    }
    clause += switcher[sentence_type]
    extended_sentence = random.randint(0,99)
    if extended_sentence < 25:
        clause += " " + ' '.join([conjunction(), sentence(False)])
        return(clause)
    else:
        return(clause)

def poem_generator(p):
    if not os.path.exists('./generated'): os.mkdir('./generated') 
    save_path = './generated'
    i = 0
    while i < p:
        filename = os.path.join(save_path, "Poem " + str(i+1) + ".docx")
        file = docx.Document()
        x = 0
        while x < n:
            file.add_paragraph(sentence())
            x+=1
        i+=1
        file.save(filename)
    print("Generated " + str(p) + " poem! Please check your /generated folder.\n" if p == 1 else "Generated " + str(p) + " poems! Please check your /generated folder.\n")


#interface
print("\n")
print("Welcome to Ryan's poem generator!")
print("\n")
print("Enter a positive integer to randomly generate that number of poems.")
print("Press CTRL + C at any time to abort.")
print("\n")
print("Reminder: existing poems in the /generated folder are overwritten.\nPlease move them out of /generated if you wish to keep poems generated before.")
print("\n")
response = ''
response2 = ''

while True:

    response = input("How many poems?\n")
    response2 = input("How many lines per poem?\n")

    try:
        p = int(response)
        n = int(response2)
        print("\n")
        if p > 0 and n > 0:
            poem_generator(p)
        else:
            print("Please enter a valid positive integer.\n")
    except ValueError:
        print("Invalid input. Please enter positive integers, or use CTRL + C to abort.\n")