import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

word_list = ["ardvark", "baboon", "camel", "monkey", "dog", "cat","bicycle","elephant","rainbow","sunshine","balloon","giraffe","octopus","popcorn","rainbow","diamond"]
chosen_word = random.choice(word_list)

hints = {
    "ardvark": "It has a long snout and feeds on ants and termites.",
    "baboon": "Known for its distinctive dog-like snout and large, sharp canines.",
    "camel": "Adapted to desert life, it stores fat in its hump(s) for sustenance.",
    "monkey": "Highly intelligent and agile, known for its playful behavior.",
    "dog": "Commonly referred to as 'man's best friend,' known for its loyalty and companionship.",
    "cat": "Independent and agile, known for its hunting prowess and grooming habits.",
    "bicycle": "Common mode of transportation, often seen on roads",
    "elephant": "Known for its size, gray skin, and presence in African and Asian habitats",
    "rainbow": "Appears after rain and is comprised of various colors like red, orange, yellow, green, blue, indigo, and violet",
    "sunshine": "brings light and heat to the earth during the day",
    "balloon": "Often used for decoration or in celebrations, can be seen floating in the air",
    "giraffe": "Known for its ability to reach high leaves on trees and its distinctive appearance",
    "octopus": "Known for its intelligence, camouflage abilities, and presence in oceans",
    "popcorn": "Made by heating corn kernels until they burst open and expand",
    "rainbow": "Appears after rain and is comprised of various colors like red, orange, yellow, green, blue, indigo, and violet",
    "diamond": "Often used in jewelry and prized for its rarity and beauty"
}

secondhint = {
    "ardvark": "Often found in sub-saharan Africa, it's nocturnal and has poor eyesight.",
    "baboon": "Living in troops, this primate has a complex social structure.",
    "camel": "Known for its ability to withstand extreme temperatures and long periods without water.",
    "monkey": "Some species have prehensile tails, which they use like an extra hand.",
    "dog": "Comes in various breeds, each with its own unique characteristics and abilities.",
    "cat": "Domesticated for thousands of years, it has a strong sense of territory and can be affectionate with its owners and definitely not cute.",
    "bicycle": "Two-wheeled vehicle propelled by pedaling",
    "elephant": "Known for its ability to reach high leaves on trees and its distinctive appearance",
    "rainbow": "Colorful arc in the sky formed by the refraction and dispersion of light",
    "sunshine": "Radiant light and warmth emitted by the sun",
    "balloon": "Inflatable object filled with gas, typically helium or air",
    "giraffe": "Tallest terrestrial animal with a long neck and spotted coat",
    "octopus": "Eight-armed marine creature with a soft body and suction cups",
    "popcorn": "Popped corn kernels, typically eaten as a snack",
    "rainbow": "Colorful arc in the sky formed by the refraction and dispersion of light",
    "diamond": "Precious gemstone composed of carbon, known for its brilliance and hardness"
}

print("Guess the characters \nYou have a total of 6 chances to guess the word")
display = []

if chosen_word in hints:
    print("Hint:", hints[chosen_word])

for letter in chosen_word:
    display.append('_')

print(display)
remaining_turns = 6
end_of_game = False
hints_revealed = False

while not end_of_game and remaining_turns > 0:
    guess = input("Guess the letter ").lower()
    found = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            found = True
            clear()
    if not found:
        clear()
        remaining_turns -= 1
        if remaining_turns == 4:  # Provide additional hint when 4 turns left
            if chosen_word in secondhint:
                print("Second Hint:", secondhint[chosen_word])
        elif remaining_turns == 2:  # Display one letter randomly when 2 turns left
            index_to_reveal = random.choice([i for i, letter in enumerate(display) if letter == '_'])
            display[index_to_reveal] = chosen_word[index_to_reveal]
            # check if all blanks are filled or not
            # if true, then hints_revealed = True
            if "_" not in display:
                hints_revealed = True
            print("Hint: Revealing one more letter...")
        elif remaining_turns == 1:  # Display one more letter randomly when 1 turn left
            index_to_reveal = random.choice([i for i, letter in enumerate(display) if letter == '_'])
            display[index_to_reveal] = chosen_word[index_to_reveal]
            # check if all blanks are filled or not
            # if true, then hints_revealed = True
            if "_" not in display:
                hints_revealed = True
            print("Last chance! Revealing one more letter...")

        print(f"The letter '{guess}' is not in the word. \nRemaining turns: {remaining_turns}")
    print(display)
    if "_" not in display and hints_revealed:
        print("You lose! All characters were revealed during hints.")
    elif "_" not in display:
        end_of_game = True
        print("You win! The word was:", chosen_word)

if remaining_turns == 0:
    print("You lose! The word was:", chosen_word)