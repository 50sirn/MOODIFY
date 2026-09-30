import csv
import os


def load_songs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, "data", "music_data.csv")

    songs = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append(row)

    return songs


def get_song_count():
    songs = load_songs()
    return len(songs)


if __name__ == "__main__":
    songs = load_songs()

    print("MOODIFY MUSIC DATABASE")
    print("----------------------")
    print(f"Songs loaded: {len(songs)}")

    if songs:
        print("\nFirst song:")
        print(f"Title: {songs[0]['title']}")
        print(f"Artist: {songs[0]['artist']}")
        print(f"Language: {songs[0]['language']}")
        print(f"Genre: {songs[0]['genre']}")
        print(f"Mood: {songs[0]['mood']}")