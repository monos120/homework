#Isla Shah
#19/03/19
#Quiz? This one is expanded over a bunch of tasks.

questions = [
            "Who is the president of the United States?\n",
            "What is a group of lions called?\n",
            "Which famous Czech author fell to his death from a fifth floor window while feeding pigeons?\n",
            "In which year was Niccolo Machiavelli born?\n",
            "Which company is Jeff Bezos the CEO of?\n"
            "What is the capital city of Estonia?\n"
            ]

answers = [
            "Donald Trump",
            "A pride",
            "Bohumil Hrabal",
            1469,
            "Amazon"
            "Tallinn"
]

u_answer = ""

score = 0

while u_answer != answers[0]:
    u_answer = input(questions[0])

    if u_answer == answers[0]:
        print("Correct!")
        score = score + 1
    elif u_answer != answers[0]:
        print("Try again.")
    else:
        print("program broke")

while u_answer != answers[1]:
    u_answer = input(questions[1])

    if u_answer == answers[1]:
        print("Correct!")
        score = score + 1
    elif u_answer != answers[1]:
        print("Try again.")
    else:
        print("program broke")

while u_answer != answers[2]:
    u_answer = input(questions[2])

    if u_answer == answers[2]:
        print("Correct!")
        score = score + 1
    elif u_answer != answers[2]:
        print("Try again.")
    else:
        print("program broke")


while u_answer != answers[3]:
    u_answer = int(input(questions[3]))

    if u_answer == answers[3]:
        print("Correct!")
        score = score + 1
        print(score)
    elif u_answer != answers[3]:
        print("Try again.")
    else:
        print("program broke")

while u_answer != answers[4]:
    u_answer = input(questions[4    if u_answer == answers[3]:
        print("Correct!")
        score = score + 1
        print(score)
    elif u_answer != answers[3]:
        print("Try again.")
    else:
        print("program broke")])

    if u_answer == answers[4]:
        print("Correct!")
        score = score + 1
    elif u_answer != answers[4]:
        print("Try again.")
    else:
        print("program broke")

while u_answer != answers[5]:
    u_answer = input(questions[5])

    if u_answer == answers[5]:
        print("Correct!")
        score = score + 1
    elif u_answer != answers[5]:
        print("Try again.")
    else:
        print("program broke")
