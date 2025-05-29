Word = input("Input a word: ")
Letter = input("Input a letter: ")

num = 0

Word_list = []
Position = []

for char in Word.lower():
    Word_list.append(char)
    if char == Letter.lower():
        num = num + 1

for index, i in enumerate(Word_list, start = 1):
    if i == Letter:
        Position.append(index)

Dict = {
    Letter : Position
}

print("Number of repititions: ", num)
print(Dict)