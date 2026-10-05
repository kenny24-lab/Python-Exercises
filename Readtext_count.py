with open("notes.txt", "r") as file:

    text = file.read()

words = text.split()

print("Number of words:", len(words))