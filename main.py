import random
words = ["python", "monster", "apple", "coding", "seventeen", "school","computer","window","glass","beans","desert","macbook","pneumonoultramicroscopicsilicovolcanoconiosis","pnemonia"]
word = random.choice(words)
turns = 6
guesses = ""
while turns > 0:
    fails = 0
    for i in word:
        if i in guesses:
            print(i)
        else:
            print("_")
            fails = fails + 1
    if fails == 0:
        print("You Win!")
        break
    print

    guess = input("Guess a letter! ")
    guesses = guesses + guess
    if guess not in word:
        turns = turns - 1
        print("Try again!")
        print("You have " + str(turns) + " Turns left")
if turns == 0:
  print("Oh no! You lost, the word was " + word)
