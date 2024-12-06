import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary containing words for different genres
word_genres = {
    "Animals": ["ardvark", "baboon", "camel", "monkey", "dog", "cat"],
    "Birds": ["sparrow", "eagle", "hawk", "penguin", "ostrich", "peacock"],
    "Movies": ["titanic", "avatar", "inception", "jaws", "matrix", "gladiator"],
    "Vehicles": ["car", "bus", "truck", "motorcycle", "bicycle", "train"],
    "Fruits": ["apple", "banana", "orange", "strawberry", "pineapple", "watermelon"]
}

# Prompt the user to select a genre
print("Welcome to Hangman Game!")
print("Please select a genre:")
for i, genre in enumerate(word_genres.keys()):
    print(f"{i + 1}. {genre}")

genre_choice = int(input("Enter the number corresponding to your choice: ")) - 1
genre = list(word_genres.keys())[genre_choice]
chosen_word = random.choice(word_genres[genre])

# Hints dictionary for the chosen genre
hints = {
    "Animals": {
        "ardvark": "It has a long snout and feeds on ants and termites.",
        "baboon": "Known for its distinctive dog-like snout and large, sharp canines.",
        "camel": "Adapted to desert life, it stores fat in its hump(s) for sustenance.",
        "monkey": "Highly intelligent and agile, known for its playful behavior.",
        "dog": "Commonly referred to as 'man's best friend,' known for its loyalty and companionship.",
        "cat": "Independent and agile, known for its hunting prowess and grooming habits."
    },
    "Birds": {
        "sparrow": "Small, common bird known for its brown plumage and chirping sound.",
        "eagle": "Large bird of prey with strong talons and keen eyesight.",
        "hawk": "A type of raptor known for its sharp beak and hunting abilities.",
        "penguin": "Flightless bird found in the Southern Hemisphere, known for its tuxedo-like appearance.",
        "ostrich": "Largest bird in the world, known for its speed and powerful legs.",
        "peacock": "Colorful bird with iridescent plumage, known for its extravagant tail display."
    },
    "Movies": {
        "titanic": "A romantic disaster film directed by James Cameron, based on the sinking of the RMS Titanic.",
        "avatar": "A science fiction film directed by James Cameron, set in the mid-22nd century on the moon Pandora.",
        "inception": "A mind-bending thriller directed by Christopher Nolan, exploring the concept of dreams within dreams.",
        "jaws": "A classic thriller directed by Steven Spielberg, about a giant man-eating great white shark.",
        "matrix": "A science fiction action film directed by the Wachowskis, exploring the concept of a simulated reality.",
        "gladiator": "An epic historical drama directed by Ridley Scott, set in ancient Rome and centered on a betrayed general who seeks revenge."
    },
    "Vehicles": {
        "car": "Common mode of transportation with four wheels, typically powered by an internal combustion engine.",
        "bus": "Large vehicle designed to carry multiple passengers, often used for public transportation.",
        "truck": "Heavy-duty vehicle used for transporting goods, typically larger than a car.",
        "motorcycle": "Two-wheeled vehicle powered by an engine, often used for personal transportation.",
        "bicycle": "Human-powered vehicle with two wheels, propelled by pedaling.",
        "train": "Long, connected series of rail vehicles used for transporting passengers or freight."
    },
    "Fruits": {
        "apple": "Fruit with a crisp texture and sweet taste, typically red or green in color.",
        "banana": "Long, curved fruit with a yellow skin and soft, sweet flesh.",
        "orange": "Round citrus fruit with a bright orange rind and juicy segments.",
        "strawberry": "Small, red fruit with a sweet flavor, commonly used in desserts.",
        "pineapple": "Tropical fruit with a spiky outer skin and sweet, tangy flesh.",
        "watermelon": "Large, juicy fruit with a green rind and red or pink flesh, often enjoyed in the summer."
    }
}

# Print hint for the chosen word
if chosen_word in hints[genre]:
    print("Hint:", hints[genre][chosen_word])

# Initialize display with underscores
display = ['_' for _ in chosen_word]

# Print initial display
print(display)

# Initialize game variables
remaining_turns = 6
end_of_game = False
hints_revealed = False

# Main game loop
while not end_of_game and remaining_turns > 0:
    guess = input("Guess a letter: ").lower()
    found = False
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            found = True
            clear()
    if not found:
        clear()
        remaining_turns -= 1
        if remaining_turns == 4:
            if chosen_word in hints[genre]:
                print("Hint:", hints[genre][chosen_word])
        elif remaining_turns == 2 or remaining_turns == 1:
            if "_" in display and not hints_revealed:
                index_to_reveal = random.choice([i for i, letter in enumerate(display) if letter == '_'])
                display[index_to_reveal] = chosen_word[index_to_reveal]
                hints_revealed = True
                print("Hint: Revealing one more letter...")
        print(f"The letter '{guess}' is not in the word. Remaining turns: {remaining_turns}")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You guessed the word correctly.")
    elif remaining_turns == 0:
        print("Sorry, you've run out of turns. The word was:", chosen_word)
