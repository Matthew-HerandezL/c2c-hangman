hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)

word = "Test"
name = input("What is your name?").lower()
wrong_guesses = 0
user_guesses = []
guess = 0
max_wrong_guesses = 5
print ("hello " + name + ", homie do you want to play the hangman game?")
while wrong_guesses <= 5:
    guess = input("What is your guess?").lower()
    user_guesses.append(guess)
    print("U have guessed the following... ",user_guesses)
    if guess in word:
        print("correct")
    else:
        wrong_guesses = wrong_guesses + 1
        print("incorrect")
    draw_hangman(wrong_guesses)

if wrong_guesses == max_wrong_guesses:
    print("Fail my guy")
