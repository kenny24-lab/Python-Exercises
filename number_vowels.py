sentence = input("Enter a sentence: ")

count = 0

for letter in sentence:

    if letter.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)