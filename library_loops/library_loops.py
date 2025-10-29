library = {
    "The Hobbit": "Available",
    "Slaughterhouse-Five": "Available",
    "Moby Dick": "Available",
    "The Catcher in the Rye": "Checked Out",
    "Siddhartha": "Checked Out",
    "Meditations": "Checked Out",
    "Things Fall Apart": "Available",
    "To Kill a Mockingbird": "Checked Out",
    "Pride and Prejudice": "Available",
    "Jane Eyre": "Checked Out",
    "The Great Gatsby": "Available",
    "War and Peace": "Checked Out",
    "Crime and Punishment": "Available",
    "Brave New World": "Available",
    "A Tale of Two Cities": "Checked Out",
    "Animal Farm": "Available",
    "Dracula": "Checked Out",
    "Frankenstein": "Available",
    "The Road": "Available",
    "The Alchemist": "Checked Out"
}

# Step 1: Get the User's Input
letter = input("Enter a starting letter: ").upper().strip()

# Validate input (ensure it's a single alphabetic character)
if not letter or not letter.isalpha() or len(letter) != 1:
    print("Please enter a single letter (A-Z).")
else:
    # Step 2: Initialize a counter
    match_count = 0

    # Step 3: Display a header message
    print(f"\nBooks starting with '{letter}' that are Available:")

    # Step 4: Search through the dictionary
    for title, status in library.items():
        if title.upper().startswith(letter) and status == "Available":
            print(title)
            match_count += 1

    # Step 5: Show total matches (and helpful message if zero)
    if match_count == 0:
        print("No available books found starting with that letter.")
    else:
        print(f"\nTotal available books starting with '{letter}': {match_count}")
