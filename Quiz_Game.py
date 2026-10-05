score = 0

print("===== PYTHON QUIZ =====")

questions = [
    ("What keyword is used to create a variable in Python?", "none"),
    ("Which function displays output?", "print"),
    ("Which function gets user input?", "input"),
    ("What symbol is used for multiplication?", "*"),
    ("What keyword starts a function?", "def"),
    ("Which keyword is used for a loop?", "for"),
    ("Which data type stores text?", "str"),
    ("Which data type stores whole numbers?", "int"),
    ("Which operator checks equality?", "=="),
    ("Which keyword ends a loop early?", "break")
]

for question, answer in questions:

    user = input(question + " ").lower()

    if user == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", answer)

print("\nQuiz Finished")
print("Your score:", score, "/10")