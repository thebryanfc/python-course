def new_game():
    
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        questions_num += 1
    display_score(correct_guesses, guesses)
#--------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------")
    print("RESULTS")
    print("----------------------------------")
    
    print("Answers: ", end = "")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(f"Your score is: {score} %")
#--------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
#--------------------------------
def play_again():
    reponse = input("Do you want to play again? (yes or no):")
    reponse = reponse.upper()
    if reponse == "YES":
        return True
    else:
        return False

#--------------------------------

questions = {
    "Who created Python?: ": "A",
    "What year was python created?: ": "B",
    "Python is tributed to which comedy group": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk","C.Bill Gates", "D.Mark Zuckerburg"],
            ["A. 1989","B.1991","C. 2000", "D. 2016"],
            ["A. Lonely Island","B.Smosh","C. Monty Python","D. SNL"],
            ["A.True","B.False","C.Sometimes","D. What's Earth?"]]

new_game()
while play_again():
    new_game()

print("Byeee!")