import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    #Here os is used to clear the console making it a bit tidy.

word_genres = {
    "Animals": ["ardvark", "baboon", "camel", "monkey", "dog", "elephant", "giraffe", "octopus", "cat"],
    "Birds": ["sparrow", "eagle", "hawk", "penguin", "ostrich", "peacock"],
    "Movies": ["titanic", "avatar", "inception", "jaws", "matrix", "gladiator"],
    "Vehicles": ["car", "bus", "truck", "motorcycle", "bicycle", "train"],
    "Fruits": ["apple", "banana", "orange", "strawberry", "pineapple", "watermelon"],
    "Random": ["rainbow","sunshine","balloon","popcorn","diamond"]
}

print("Welcome to Hangman Game!")
print("Please select a genre:")
for i, genre in enumerate(word_genres.keys()):
    print(f"{i + 1}. {genre}")

genre_choice = int(input("Enter the number corresponding to your choice: ")) - 1
genre = list(word_genres.keys())[genre_choice]
chosen_word = random.choice(word_genres[genre])   #A word is randomly chosen from the dataset after receiving an input about the genre.


hints = {
    "Animals": {
        "ardvark": "It has a long snout and feeds on ants and termites.",
        "baboon": "Known for its distinctive dog-like snout and large, sharp canines.",
        "camel": "Adapted to desert life, it stores fat in its hump(s) for sustenance.",
        "monkey": "Highly intelligent and agile, known for its playful behavior.",
        "dog": "Commonly referred to as 'man's best friend,' known for its loyalty and companionship.",
        "elephant": "Known for its size, gray skin, and presence in African and Asian habitats",
        "giraffe": "Known for its ability to reach high leaves on trees and its distinctive appearance",
        "octopus": "Known for its intelligence, camouflage abilities, and presence in oceans",
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
    },
    "Random": {
        "rainbow": "Appears after rain and is comprised of various colors like red, orange, yellow, green, blue, indigo, and violet",
        "sunshine": "brings light and heat to the earth during the day",
        "balloon": "Often used for decoration or in celebrations, can be seen floating in the air",
        "popcorn": "Made by heating corn kernels until they burst open and expand",
        "diamond": "Often used in jewelry and prized for its rarity and beauty"
    }
}

secondhint= {
    "Animals": {
        "ardvark": "Often found in sub-saharan Africa, it's nocturnal and has poor eyesight.",
        "baboon": "Living in troops, this primate has a complex social structure.",
        "camel": "Known for its ability to withstand extreme temperatures and long periods without water.",
        "monkey": "Some species have prehensile tails, which they use like an extra hand.",
        "dog": "Comes in various breeds, each with its own unique characteristics and abilities.",
        "elephant": "Known for its ability to reach high leaves on trees and its distinctive appearance",
        "giraffe": "Tallest terrestrial animal with a long neck and spotted coat",
        "octopus": "Eight-armed marine creature with a soft body and suction cups",
        "cat": "Domesticated for thousands of years, it has a strong sense of territory and can be affectionate with its owners and definitely not cute.",
    },
    "Birds": {
        "sparrow":  "It's a small passerine bird with brown and gray plumage.",
        "eagle": "It has strong talons and keen eyesight, making it an apex predator in the avian world.",
        "hawk": "It belongs to the family Accipitridae and is known for its hooked beak and sharp talons.",
        "penguin": "Found primarily in the Southern Hemisphere, they have a distinctive waddling gait on land.",
        "ostrich": "It's native to Africa and is capable of running at high speeds, making it the fastest land bird.",
        "peacock": " It belongs to the pheasant family and is known for its vibrant plumage and distinctive iridescent colors."
    },
    "Movies": {
        "titanic": "It's a romantic drama directed by James Cameron, featuring Leonardo DiCaprio and Kate Winslet.",
        "avatar": "It's directed by James Cameron and is known for its groundbreaking use of 3D technology.",
        "inception": "Directed by Christopher Nolan, it stars Leonardo DiCaprio as a skilled thief who steals secrets from within the subconscious.",
        "jaws": "Directed by Steven Spielberg, it's based on the novel by Peter Benchley and is often credited with popularizing the summer blockbuster.",
        "matrix": "It stars Keanu Reeves as Neo, a computer hacker who discovers the truth about the world he lives in.",
        "gladiator": "Directed by Ridley Scott, it stars Russell Crowe in the lead role and won multiple Academy Awards, including Best Picture."
    },
    "Vehicles": {
        "car": "It's powered by an internal combustion engine or electric motor and provides individual mobility.",
        "bus": "It typically has a longer body than a car and may run on diesel, electric, or other fuels.",
        "truck": "It has a larger cargo area compared to a car and often has a separate cabin for the driver.",
        "motorcycle": "It's powered by an engine and is known for its maneuverability and agility on the road.",
        "bicycle": "Two-wheeled vehicle propelled by pedaling",
        "train": "It typically consists of multiple connected cars or carriages and is powered by locomotives or electric engines."
    },
    "Fruits": {
        "apple": "This fruit is commonly associated with the story of Adam and Eve in the Bible.",
        "banana": "It grows in bunches on trees and is a rich source of potassium.",
        "orange": "It's often consumed fresh or juiced and is a good source of vitamin C.",
        "strawberry": " It's the only fruit with seeds on the outside and is a member of the rose family.",
        "pineapple": "It's native to South America and is a symbol of hospitality in many cultures.",
        "watermelon": "It's often enjoyed in slices or cubed and is a staple at picnics and BBQs"
    },
    "Random": {
        "rainbow": "Colorful arc in the sky formed by the refraction and dispersion of light",
        "sunshine": "Radiant light and warmth emitted by the sun",
        "balloon": "Inflatable object filled with gas, typically helium or air",
        "popcorn": "Popped corn kernels, typically eaten as a snack",
        "diamond": "Precious gemstone composed of carbon, known for its brilliance and hardness"
    }
}



print("Guess the characters \nYou have a total of 6 chances to guess the word")
display = []

if chosen_word in hints[genre]:
    print("Hint:", hints[genre][chosen_word])

for letter in chosen_word:
    display.append('_')

#Pre Defined rules
print(display)
remaining_turns = 6
end_of_game = False
hints_revealed = False

#Main loop of the game
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
        if remaining_turns == 4:  
            if chosen_word in hints[genre]:
                print("Hint:", hints[genre][chosen_word])     #Here Second Hint is provided.
        elif remaining_turns == 2: 
            index_to_reveal = random.choice([i for i, letter in enumerate(display) if letter == '_'])
            display[index_to_reveal] = chosen_word[index_to_reveal]
            #Here is the hints where random letters are displayed. 
            if "_" not in display:
                hints_revealed = True
            print("Hint: Revealing one more letter...")
        elif remaining_turns == 1:  
            index_to_reveal = random.choice([i for i, letter in enumerate(display) if letter == '_'])
            display[index_to_reveal] = chosen_word[index_to_reveal]
            if "_" not in display:
                hints_revealed = True
            print("Last chance! Revealing one more letter...")
            #This are the end game conditions to decide the result.
        print(f"The letter '{guess}' is not in the word. \nRemaining turns: {remaining_turns}")
    print(display)
    if "_" not in display and hints_revealed:
        print("You lose! All characters were revealed during hints.")
    elif "_" not in display:
        end_of_game = True
        print("You win! The word was:", chosen_word)
if remaining_turns == 0:
    print("You lose! The word was:", chosen_word)