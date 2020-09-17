import time as t
import requests, json, random, pprint, os
clear = lambda: os.system('clear')

############## FUNCTIONS ##################
def CheckAttempt(word, letter_attempt):
    poslist = []
    attempt = False
    pos = 0
    for letter in word:
        if letter.lower() == letter_attempt.lower():
            attempt = True
            poslist.append(pos)
        pos += 1
    return attempt,poslist

def AddLetters(letter_attempt,posvect,guessed_letters_print):
    for pos in posvect:
        guessed_letters_print = guessed_letters_print[0:pos] + letter_attempt + guessed_letters_print[pos+1:]
    return guessed_letters_print

def AddSpaces(guessed_letters_print):
    out = ""
    for i in range(len(guessed_letters_print)):
        out = out + guessed_letters_print[i]+" "
    return out

def PrintHangman(i):
    switcher = {
            1:"  ______ \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n",
            2:"  ______ \n"
            "  |    | \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n",
            3:"  ______ \n"
            "  |    | \n"
            "  |    O  \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n",
            4:"  ______ \n"
            "  |    | \n"
            "  |    O  \n"
            "  |    |  \n"
            "  |      \n"
            "  |      \n"
            "__|__\n",
            5:"  ______ \n"
            "  |    | \n"
            "  |    O  \n"
            "  |    |  \n"
            "  |      \n"
            "  |      \n"
            "__|__\n",
            6:"  ______ \n"
            "  |    | \n"
            "  |    O \n"
            "  |    |\  \n"
            "  |       \n"
            "  |      \n"
            "__|__\n",
            7:"  ______ \n"
            "  |    | \n"
            "  |    O \n"
            "  |   /|\  \n"
            "  |       \n"
            "  |      \n"
            "__|__\n",
            8:"  ______ \n"
            "  |    | \n"
            "  |    O \n"
            "  |   /|\  \n"
            "  |   /  \n"
            "  |      \n"
            "__|__\n",
            9:"  ______ \n"
            "  |    | \n"
            "  |    O \n"
            "  |   /|\  \n"
            "  |   / \ \n"
            "  |      \n"
            "__|__\n"
        }
    hungman = switcher.get(i,"Invalid attempt")
    return print(hungman)

####### MAIN ###############
total_attempts = 9

QuitGame = False
while QuitGame == False:
    clear()
    used_letters = []
    remaining_attempts = total_attempts
    guessed_letters = 0
    # print("You are going to play the Hangman game!")
    print("\nIniciando juego... \n")
    t.sleep(1)

    ###############
    #Get words from Datamuse API
    valid_word = False
    while valid_word == False:
        word_size = random.randint(3,10)
        alphabet = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
        word_ini = alphabet[random.randint(1,25)]
        URL = "http://api.datamuse.com/words?sp="+word_ini+"?"*word_size+"&max=10&v=es"
        r = requests.get(URL)
        words_dict = json.loads(r.text)
        word = words_dict[random.randint(0,9)]["word"]
        if " " not in word:
            valid_word = True
    ###############

    guessed_letters_print = "_"*len(word)
    out = AddSpaces(guessed_letters_print)

    while remaining_attempts > 0 and guessed_letters < len(word) and QuitGame == False:
        # print("The word is: " + out + ". Length: " + str(len(word))+ " letters")
        print("La palabra: " + out + ". tiene: " + str(len(word))+ " letras")
        # print("\n*Remaining attempts: " + str(remaining_attempts))
        print("\n*intentos restantes: " + str(remaining_attempts))
        print("letras usadas: " + str(used_letters))
        # print("Used letters: " + str(used_letters))
        data_valid = False
        while data_valid == False:
            letter_attempt = input("\n>Type a letter: ")
            try:
                int(letter_attempt)
                print("Only letters are valid")
                continue
            except:
                if len(letter_attempt)>1:
                    print("Please, type a single letter")
                elif letter_attempt == "":
                    print("Please, type any letter")
                elif letter_attempt in used_letters or letter_attempt in guessed_letters_print:
                    print("You have used that letter already. Type a different letter.")
                else:
                    data_valid = True

        attempt, pos = CheckAttempt(word,letter_attempt)
        if attempt == False:
            remaining_attempts -= 1
            PrintHangman(total_attempts-remaining_attempts)
            used_letters.append(letter_attempt)
            if(remaining_attempts == 0):
                print("Sorry, that letter is not in the word.")
            else:
                print("Sorry, that letter is not in the word, try again.")
        else:
            print("\nCorrect!")
            guessed_letters = guessed_letters + len(pos)
            guessed_letters_print = AddLetters(letter_attempt,pos,guessed_letters_print)
            out = AddSpaces(guessed_letters_print)
            if(guessed_letters == len(word)):
                print("The word is: " + out)

    if remaining_attempts == 0:
        print("You lose! :(")
        print("The word was: " + word.upper())
    else:
        print("Congrats, You win! :)")

    data_valid = False
    while data_valid == False:
        answer = input("\nDo you want to play again. y = yes, n = no: ")
        if answer == "y":
            data_valid = True
            QuitGame = False
        elif answer == "n":
            data_valid = True
            QuitGame = True
        else:
            continue
