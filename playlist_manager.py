
import os


def create_playlist(songs, mood):

    if not songs:
        print("\nNo songs available to create a playlist.")
        return

    filename = f"MOODIFY_{mood.capitalize()}_Playlist.txt"

    base_dir = os.path.dirname(os.path.abspath(__file__))
    playlist_path = os.path.join(base_dir, filename)

    with open(playlist_path, "w", encoding="utf-8") as file:

        file.write("===================================\n")
        file.write("           MOODIFY PLAYLIST\n")
        file.write("===================================\n\n")

        file.write(f"Mood: {mood.capitalize()}\n")
        file.write(f"Number of songs: {len(songs)}\n\n")

        for i, song in enumerate(songs, start=1):

            file.write(
                f"{i}. {song['title']} - {song['artist']}\n"
            )

            file.write(
                f"   Language: {song['language']}\n"
                f"   Genre: {song['genre']}\n\n"
            )

    print("\nPlaylist created successfully!")
    print(f"Saved as: {filename}")


if __name__ == "__main__":

    test_songs = [
        {
            "title": "Blinding Lights",
            "artist": "The Weeknd",
            "language": "English",
            "genre": "Pop"
        }
    ]

    create_playlist(test_songs, "energetic")

