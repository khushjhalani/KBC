#Create a KBC Game
#Use list data type to store the questions and options
#Display the final amount won by the player

import time
import msvcrt

# Easy Level Questions
easy_questions = [[[]],
    ["What is the capital of France?", ["Paris", "Rome", "London", "Madrid"], "1"],
    ["Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "1"],
    ["Who painted the Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "1"],
    ["What is the chemical symbol for water?", ["H2O", "CO2", "NaCl", "O2"], "1"],
    ["Which country is famous for its kangaroos and koalas?", ["Australia", "Brazil", "Canada", "Japan"], "1"]
]

# Medium Level Questions
medium_questions = [[[]],
    ["What is the tallest mountain in the world?", ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"], "2"],
    ["Who wrote the play 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "George Orwell", "Charles Dickens"], "1"],
    ["What is the largest ocean on Earth?", ["Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Southern Ocean"], "1"],
    ["Which scientist developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "2"],
    ["Which country is known for inventing pizza?", ["Italy", "Greece", "Spain", "United States"], "1"]
]

# Hard Level Questions
hard_questions = [[[]],
    ["Who is the author of the book '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.D. Salinger"], "1"],
    ["What is the capital of Brazil?", ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"], "2"],
    ["Which element has the symbol 'Fe' on the periodic table?", ["Iron", "Silver", "Gold", "Zinc"], "1"],
    ["Who painted the famous artwork 'The Starry Night'?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "1"],
    ["What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Earth", "Neptune"], "1"]
]

#amount
prize = [0,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

winnings = 0

def welcomeMsg():
    # Display the welcome message
    print("\n\nWelcome to Kaun Banega Crorepati!\n")

    # Display the rules
    print('''Rules:\
        \n1. There are 3 levels in this game: Easy, Medium and Hard.\
        \n2. Each level has 5 questions.\
        \n3. You will be given 4 options for each question.\
        \n4. You have to enter the option number to answer the question.\
        \n5. You will be awarded with the prize money mentioned below for each correct answer.\
        \n6. If you give a wrong answer, the game will be over and you will lose all the money you have won after the last checkpoint.\
        \n7. You can quit the game at any time by entering 'quit'.\
        \n8. There are 2 checkpoints in the game at clearing first two difficulty levels.\
        \n9. You will get 60 seconds to answer each question at first level and then no timelimit.\
        \n\n''')

def get_user_input(tl=60):
    start_time = time.time()
    user_input = ""

    while True:
        if time.time() - start_time > tl:
            print("Time limit exceeded.")
            return False
        if msvcrt.kbhit():
            char = msvcrt.getche().decode('utf-8')
            if char == '\r':
                print()
                break
            user_input += char

    return user_input

def l1():
    global winnings
    for i in range(1,6):
        print(f"Question {i} is ")
        print(f"{easy_questions[i][0]}")
        print(f"Your options are:")
        for val in range(4):
            print(f"{val+1} . {easy_questions[i][1][val]}")
            
        print("Enter your choice within 60 seconds: ")
        choice = get_user_input()
        if choice == False:
            print("OOPS! Time Limit exceeded.")
            return 'tle'
        elif choice.lower() == 'quit':
            print("You chose to quit the game...")
            winnings = prize[i-1]
            print(f"Your winning amount is: {winnings}")
            exit()
            
        elif choice == easy_questions[i][2]:
            print("Congratulations! Your answer is Correct.")
            winnings = prize[i]
            print(f"Your current winning amount is {winnings}")
        else:
            print("OOPS! You entered wrong answer.")
            return 'lost'
    return True

def l2():
    global winnings
    for i in range(1,6):
        print(f"Question {i+5} is: ")
        print(f"{medium_questions[i][0]}")
        print(f"Your options are:")
        for val in range(4):
            print(f"{val+1} . {medium_questions[i][1][val]}")
            
        choice = input("Enter your choice: ")
        if choice.lower() == 'quit':
            print("You chose to quit the game...")
            winnings = prize[i+5-1]
            print(f"Your winning amount is: {winnings}")
            exit()
        elif choice == medium_questions[i][2]:
            print("Congratulations! Your answer is Correct.")
            winnings = prize[i+5]
            print(f"Your current winning amount is {winnings}")
        else:
            print("OOPS! You entered wrong answer.")
            return 'lost'
    
    return True            
               
def l3():
    global winnings
    for i in range(1,6):
        print(f"Question {i+10} is: ")
        print(f"{hard_questions[i][0]}")
        print(f"Your options are:")
        for val in range(4):
            print(f"{val+1} . {hard_questions[i][1][val]}")
            
        choice = input("Enter your choice: ")
        if choice.lower() == 'quit':
            print("You chose to quit the game...")
            winnings = prize[i+10-1]
            print(f"Your winning amount is: {winnings}")
            exit()
        elif choice == hard_questions[i][2]:
            print("Congratulations! Your answer is Correct.")
            winnings = prize[i+10]
            print(f"Your current winning amount is {winnings}")
        else:
            print("OOPS! You entered wrong answer.")
            return 'lost'
    return True
            

def playGame():
    print("Let's start the game!\nYou are at level 1 right now\n\n")
    global winnings
    c1 = 10000
    c2 = 320000
    
    
    a = l1()
    if a==True:
        print("Congrats!! You cleared level 1 and your checkpoint 1 is now set.\nTimer is now removed and there is no time limit")
        print("Let's start level 2\n")
    elif a=='tle' or a=='lost':
        print(f"You failed to give correct answer on time and thus have not won any amount.")
        winnings = 0
        exit()
    else:
        #Implement error logging for keeping track of unforeseen circumstances 
        print("Something unexpected occurred...")
        
    
    a = l2()
    if a==True:
        print("Congrats!! You cleared level 2 and your checkpoint 2 is now set.\n")
        print("Let's start level 3\n")
    elif a=='lost':
        print(f"You failed to give correct answer")
        winnings = c1
        print(f"Your winning amount according to your checkpoint is: {winnings}")
        exit()
    else:
        #Implement error logging for keeping track of unforeseen circumstances 
        print("Something unexpected occurred...")
       
       
    a=l3()
    if a==True:
        print('''\n\n\n!!!!!!!!!!!!CONGRATULAIONS!!!!!!!!!!!!!!!\nYou have completed the game and you win 1,00,00,000.\nToh kya kariyega aap itni dhanrashi ka?''')
        exit()
    elif a=='lost':
        winnings = c2
        print(f"Your winning amount according to your checkpoint is: {winnings}")
        exit()
    else:
        #Implement error logging for keeping track of unforeseen circumstances 
        print("Something unexpected occurred...")       
        
        
    
    

if __name__=="__main__":
    welcomeMsg()
    a = input("Press any key to continue or 'q' to quit: ")
    if a == 'q':
        exit()
    playGame()
    exit()