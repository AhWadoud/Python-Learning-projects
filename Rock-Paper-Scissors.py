import random

def mods():
    global win_cond
    if new_options:
        options = new_options.split(",")
        if choice in options:
            new_list = options[options.index(choice) + 1:] + options[:options.index(choice)]
            win_cond = dict({choice:new_list[len(new_list) // 2 :]})
    else:
        options = ["rock", "paper", "scissors"]  
    return options

def keeping_score():
    global score
    counter = 0
    rating = open("rating.txt", "r+")
    for line in rating:
        if username in line:
            score = int(line.split()[1])
            counter += 1
    if counter < 1:
        print(username + " 0", file=rating)
        score = 0
    rating.close()
    return score    

def results():
    global score
    if choice == option:
        print(f"There is a draw ({option})")
        score += 50
    elif option in win_cond[choice]:
        print(f"Well done. The computer chose {option} and failed")
        score += 100
    else:
        print(f"Sorry, but the computer chose {option}")    

win_cond = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
username = input("Enter your name: ")
print(f"Hello, {username}")
new_options = input()
print("Okay, let's start")
score = keeping_score()
while True:
    choice = input()
    options = mods()
    if choice not in options:
        if choice == "!exit":
            print("Bye!")
            quit()
        elif choice == "!rating":
            print(f"Your rating: {score}")
        else:
            print("Invalid input")
        continue    
    option = random.choice(options)
    results()
