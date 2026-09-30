
def choose_mood():
    print("\nHow would you describe your mood?")

    moods = [
        "Happy",
        "Sad",
        "Energetic",
        "Angry",
        "Romantic",
        "Calm",
        "Nostalgic",
        "Motivated",
        "Chill",
        "Heartbroken"
    ]

    for i, mood in enumerate(moods, start=1):
        print(f"{i}. {mood}")

    while True:
        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= len(moods):
            return moods[int(choice) - 1].lower()

        print("Invalid choice. Please enter a number from 1 to 10.")


def choose_description():
    print("\nWould you like to describe your mood in more detail?")
    print("1. Yes")
    print("2. No")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("\nDescribe how you're feeling: ").strip()

            if description:
                return description

            print("Please enter a description.")

        elif choice == "2":
            return None

        else:
            print("Invalid choice. Please enter 1 or 2.")


def choose_language():
    print("\nChoose your preferred language:")

    languages = [
        "English",
        "Hindi",
        "Punjabi"
    ]

    for i, language in enumerate(languages, start=1):
        print(f"{i}. {language}")

    while True:
        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= len(languages):
            return languages[int(choice) - 1]

        print("Invalid choice. Please try again.")


def choose_genre():
    print("\nChoose your preferred genre:")

    genres = [
        "Any",
        "Pop",
        "Hip-Hop",
        "Rap",
        "Rock",
        "Alternative",
        "R&B",
        "Bollywood",
        "Punjabi",
        "Folk"
    ]

    for i, genre in enumerate(genres, start=1):
        print(f"{i}. {genre}")

    while True:
        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= len(genres):
            selected = genres[int(choice) - 1]

            if selected == "Any":
                return None

            return selected

        print("Invalid choice. Please try again.")

