name = input("What is your name? ")

f = open("answers.txt", "w")
f.write(name)