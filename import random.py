import random

#all the characters
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = ALPHABET.lower()
numbers = "1234567890"
symbools = "!@#%&*.,"

testlist = []

#here it reads the 1000 words txt file that is being used in this program
filename = "1000_word.txt"

file = open(filename, "r")

for line in file:
        testlist.append(line)

#removes any enters(\n) in the list
wordlist = []
for sub in testlist:
    wordlist.append(sub.replace("\n", ""))



def complete_random_symbool(sileble_amount):
        all_charts = ALPHABET + alphabet + numbers + symbools
        password = ""
        for i in range(sileble_amount):
                next_char = random.choice(all_charts)
                password += next_char
        return password

def complete_random(sileble_amount):
        all_charts = ALPHABET + alphabet + numbers
        password = ""
        for i in range(sileble_amount):
                next_char = random.choice(all_charts)
                password += next_char
        return password

def complete_random_nocapital(sileble_amount):
        all_charts = alphabet + numbers
        password = ""
        for i in range(sileble_amount):
                next_char = random.choice(all_charts)
                password += next_char
        return password

def chooce_word_digit(word):
        all_charts = numbers
        password = word

        for i in range(4):
                next_char = random.choice(all_charts)
                password += next_char
        return password

def random_word():
        word = random.choice(wordlist)
        return(word)



print("1 = complete random letters, numbers and symbools + choose sileble amount")
print("2 = complete random letters and numbers + choose sileble amount")
print("3 = complete random letters and number no capital no symbool + choose sileble amount")
print("4 = random real word + choosen numbers")
print("5 = choosen real word + 4 random numbers")
print("exit = exit", "\n")

option = input("choose your option(1, 2, 3, 4, 5): ")

if option == "1":
        silebles = int(input("how much sileble(s)?: "))
        outcome = complete_random_symbool(silebles)
        print("your new password is: ", outcome)
elif option == "2":
        silebles = int(input("how much sileble(s)?: "))
        outcome = complete_random(silebles)
        print("your new password is: ", outcome)
elif option == "3":
        silebles = int(input("how much sileble(s)?: "))
        outcome = complete_random_nocapital(silebles)
        print("your new password is: ", outcome)
elif option == "4":
        numbersINT = int(input("put in your numbers: "))
        numbersSTR = str(numbersINT)
        outcome = random_word()
        password = outcome + numbersSTR
        print("here is your new password: ", password)
elif option == "5":
        word = input("choose your word: ")
        outcome = chooce_word_digit(word)
        print("your new password is: ", outcome)
elif option == "debug":
        print(wordlist)
elif option == "exit":
        exit()
else:
        print("invalid option")