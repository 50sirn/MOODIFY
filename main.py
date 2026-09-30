
from mood_analyzer import analyze_moods
from recommendation_engine import (
    recommend_songs,
    calculate_mood_score,
    calculate_blended_mood_score
)
from playlist_manager import create_playlist
from user_input import (
    choose_mood,
    choose_description,
    choose_language,
    choose_genre
)


print("===================================")
print("          🎵 MOODIFY 🎵")
print("     Your Personal Music System")
print("===================================")


# ============================================================
# MOOD SELECTION
# ============================================================

user_mood = choose_mood()

print(f"\nSelected mood: {user_mood.capitalize()}")


# ============================================================
# OPTIONAL MOOD DESCRIPTION
# ============================================================


description = choose_description()

description_moods = []

if description:

    description_moods = analyze_moods(description)

    print(
        f"\nDescription moods detected: "
        f"{', '.join(description_moods)}"
    )



# ============================================================
# LANGUAGE AND GENRE
# ============================================================

language = choose_language()

genre = choose_genre()


# ============================================================
# GET RECOMMENDATIONS
# ============================================================


recommendations = recommend_songs(
    user_mood,
    language,
    genre,
    5,
    secondary_moods=description_moods
)



# ============================================================
# DISPLAY RECOMMENDATIONS
# ============================================================

print("\n===================================")
print("       YOUR RECOMMENDATIONS")
print("===================================")


if recommendations:

    for i, song in enumerate(recommendations, start=1):


        if description_moods:

            score = calculate_blended_mood_score(
                song,
                user_mood,
                description_moods
            )

        else:

            score = calculate_mood_score(
                song,
                user_mood
            )


        print(
            f"{i}. {song['title']} - {song['artist']}"
        )

        print(
            f"   {song['language']} | "
            f"{song['genre']} | "
            f"Compatibility: {score}%"
        )


    # ========================================================
    # PLAYLIST OPTION
    # ========================================================

    print("\n-----------------------------------")
    print("Would you like to create a playlist from these songs?")
    print("1. Yes")
    print("2. No")

    while True:

        choice = input("Enter your choice: ")

        if choice == "1":

            create_playlist(
                recommendations,
                user_mood
            )

            break

        elif choice == "2":

            print("\nNo playlist created.")

            break

        else:

            print(
                "Invalid choice. Please enter 1 or 2."
            )


else:

    print("\nSorry, no songs matched your preferences.")
    print("Try selecting a different language or genre.")


# ============================================================
# EXIT
# ============================================================

print("\n===================================")
print("          THANK YOU FOR USING")
print("             MOODIFY 🎵")
print("===================================")

