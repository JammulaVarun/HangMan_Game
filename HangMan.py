import random
def hangman():
    list_of_words=['car','bus','cat','human','dog','mouse']
    word=random.choice(list_of_words)
    turns=10
    guess_made=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')

    while len(word)>0:
        main_word=""

        for letter in word:
            if letter in guess_made:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("Excellect... You Won !!!")
            print("ThankYou...Hope you enjoyed")
            print("                ---@Ja.Va---")
            break

        print("Guess the word", main_word)
        guess=input()

        if guess in valid_entry:
            guess_made=guess_made+guess
        else:
            print("Enter a valid character")
            guess=input()

        if guess not in word:
            turns=turns-1

            if turns==9:
                print("9 turns left !!!")
            if turns==8:
                print("8 turns left !!!")
                print("       O         ")
            if turns==7:
                print("7 turns left !!!")
                print("       O         ")
                print("       |         ")
            if turns==6:
                print("6 turns left !!!")
                print("       O         ")
                print("       |         ")
                print("      /          ")
            if turns==5:
                print("5 turns left !!!")
                print("       O         ")
                print("       |         ")
                print("      /          ")
            if turns==4:
                print("4 turns left !!!")
                print("      \O         ")
                print("       |         ")
                print("      / \        ")
            if turns==3:
                print("3 turns left !!!")
                print("      \O/        ")
                print("       |         ")
                print("      / \        ")
            if turns==2:
                print("2 turns left !!!")
                print("      \O/  |     ")
                print("       |         ")
                print("      / \        ")
            if turns==1:
                print("Only 1 turns left !!!")
                print("      \O/_|      ")
                print("       |         ")
                print("      / \        ")
            if turns==0:
                print("DEAD !!!")
                print("       O_|       ")
                print("      /|\        ")
                print("      / \        ")
                print("Game Over !")

name = input("Enter Your Namr --  ")
print("Welcome to Hangman",name,"buddy")
print("--------------------")
print("Try to guess the word in les than 10 attempts... !")


hangman()
