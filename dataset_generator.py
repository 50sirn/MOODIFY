import csv
import os
from music_catalog import songs


# ============================================================
# BASE EMOTIONAL PROFILES
# ============================================================

MOOD_PROFILES = {

    "Happy": {
        "energy": 8,
        "happiness": 10,
        "sadness": 1,
        "anger": 1,
        "romance": 5,
        "calm": 4,
        "nostalgia": 3
    },

    "Sad": {
        "energy": 3,
        "happiness": 2,
        "sadness": 9,
        "anger": 2,
        "romance": 6,
        "calm": 6,
        "nostalgia": 8
    },

    "Energetic": {
        "energy": 10,
        "happiness": 8,
        "sadness": 1,
        "anger": 4,
        "romance": 3,
        "calm": 1,
        "nostalgia": 3
    },

    "Calm": {
        "energy": 2,
        "happiness": 6,
        "sadness": 2,
        "anger": 1,
        "romance": 3,
        "calm": 10,
        "nostalgia": 5
    },

    "Angry": {
        "energy": 9,
        "happiness": 3,
        "sadness": 3,
        "anger": 10,
        "romance": 1,
        "calm": 1,
        "nostalgia": 2
    },

    "Romantic": {
        "energy": 5,
        "happiness": 7,
        "sadness": 2,
        "anger": 1,
        "romance": 10,
        "calm": 7,
        "nostalgia": 6
    },

    "Nostalgic": {
        "energy": 5,
        "happiness": 5,
        "sadness": 5,
        "anger": 1,
        "romance": 6,
        "calm": 6,
        "nostalgia": 10
    },

    "Motivated": {
        "energy": 9,
        "happiness": 8,
        "sadness": 1,
        "anger": 4,
        "romance": 2,
        "calm": 2,
        "nostalgia": 3
    },

    "Chill": {
        "energy": 4,
        "happiness": 6,
        "sadness": 3,
        "anger": 1,
        "romance": 5,
        "calm": 9,
        "nostalgia": 6
    },

    "Heartbroken": {
        "energy": 4,
        "happiness": 1,
        "sadness": 10,
        "anger": 3,
        "romance": 9,
        "calm": 5,
        "nostalgia": 9
    }
}


# ============================================================
# SONG-SPECIFIC ADJUSTMENTS
# ============================================================

SONG_ADJUSTMENTS = {

    # ---------------- HAPPY ----------------

    "Blinding Lights": {
        "energy": 1,
        "happiness": 0,
        "romance": 0
    },

    "Watermelon Sugar": {
        "energy": 0,
        "happiness": 0,
        "romance": 2
    },

    "Shape of You": {
        "energy": 0,
        "happiness": 0,
        "romance": 2
    },

    "Party in the U.S.A.": {
        "energy": 1,
        "happiness": 0,
        "nostalgia": 2
    },

    "Ilahi": {
        "energy": 0,
        "happiness": 1,
        "nostalgia": 1
    },

    "Jeene Laga Hoon": {
        "romance": 2,
        "happiness": 1
    },

    "Born to Shine": {
        "energy": 1,
        "happiness": 1
    },


    # ---------------- SAD ----------------

    "Easy On Me": {
        "sadness": 1,
        "calm": 1
    },

    "Fix You": {
        "sadness": 1,
        "calm": 2
    },

    "In the End": {
        "anger": 2,
        "energy": 1
    },

    "Boulevard of Broken Dreams": {
        "sadness": 1,
        "nostalgia": 1
    },

    "Agar Tum Saath Ho": {
        "sadness": 1,
        "romance": 1,
        "nostalgia": 1
    },


    # ---------------- ENERGETIC ----------------

    "FE!N": {
        "energy": 0,
        "anger": 2,
        "happiness": -1
    },

    "SICKO MODE": {
        "energy": 0,
        "anger": 1
    },

    "DNA.": {
        "energy": 0,
        "anger": 2
    },

    "Apna Time Aayega": {
        "energy": 1,
        "happiness": 1
    },

    "Malhari": {
        "energy": 1,
        "anger": 1
    },

    "Chak De India": {
        "energy": 1,
        "happiness": 1
    },


    # ---------------- CALM / CHILL ----------------

    "Starboy": {
        "energy": 1,
        "calm": -1
    },

    "goosebumps": {
        "energy": 1,
        "romance": 1
    },

    "Highest in the Room": {
        "energy": 1,
        "calm": -1
    },

    "Passionfruit": {
        "romance": 2,
        "calm": 1
    },

    "Let It Happen": {
        "calm": 1,
        "nostalgia": 1
    },

    "We Rollin": {
        "energy": 1
    },


    # ---------------- ANGRY ----------------

    "Not Like Us": {
        "energy": 1,
        "anger": 1
    },

    "Numb": {
        "anger": 1,
        "sadness": 1
    },

    "Rolling in the Deep": {
        "anger": 1,
        "energy": 1
    },


    # ---------------- ROMANTIC ----------------

    "Die For You": {
        "romance": 1,
        "sadness": 1
    },

    "Adore You": {
        "romance": 1,
        "happiness": 1
    },

    "Perfect": {
        "romance": 1,
        "calm": 1
    },

    "Tum Hi Ho": {
        "romance": 1,
        "sadness": 1
    },

    "Kesariya": {
        "romance": 1,
        "happiness": 1
    },

    "Apna Bana Le": {
        "romance": 1,
        "happiness": 1
    },


    # ---------------- NOSTALGIC ----------------

    "Save Your Tears": {
        "nostalgia": 1,
        "sadness": 1
    },

    "As It Was": {
        "nostalgia": 1,
        "sadness": 1
    },

    "505": {
        "nostalgia": 1,
        "romance": 1
    },

    "Viva La Vida": {
        "nostalgia": 1,
        "happiness": 1
    },

    "The Last Ride": {
        "nostalgia": 1,
        "sadness": 1
    },


    # ---------------- MOTIVATED ----------------

    "HUMBLE.": {
        "energy": 1,
        "anger": 1
    },

    "Lose Yourself": {
        "energy": 1,
        "anger": 1
    },

    "Industry Baby": {
        "energy": 1,
        "happiness": 1
    },

    "Congratulations": {
        "energy": 1,
        "happiness": 1
    },

    "Zinda": {
        "energy": 1,
        "happiness": 1
    },

    "Kar Har Maidaan Fateh": {
        "energy": 1,
        "happiness": 1
    },

    "GOAT": {
        "energy": 1,
        "happiness": 1
    },


    # ---------------- HEARTBROKEN ----------------

    "Someone Like You": {
        "sadness": 1,
        "romance": 1,
        "nostalgia": 1
    },

    "Wrecking Ball": {
        "sadness": 1,
        "anger": 1
    },

    "Circles": {
        "sadness": 1,
        "nostalgia": 1
    },

    "Channa Mereya": {
        "sadness": 1,
        "romance": 1,
        "nostalgia": 1
    },

    "Excuses": {
        "sadness": 1,
        "romance": 1
    },

    "No Love": {
        "sadness": 1,
        "anger": 1
    }
}


# ============================================================
# CREATE DATASET
# ============================================================

def create_dataset():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, "data", "music_data.csv")

    headers = [
        "id",
        "title",
        "artist",
        "language",
        "genre",
        "mood",
        "energy",
        "happiness",
        "sadness",
        "anger",
        "romance",
        "calm",
        "nostalgia"
    ]

    # Remove duplicate songs
    unique_songs = []
    seen_songs = set()

    for song in songs:

        song_key = (
            song[0].lower(),
            song[1].lower()
        )

        if song_key not in seen_songs:

            unique_songs.append(song)
            seen_songs.add(song_key)

    # Create CSV
    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(headers)

        for song_id, song in enumerate(unique_songs, start=1):

            title = song[0]
            artist = song[1]
            language = song[2]
            genre = song[3]
            mood = song[4]

            # Start with base emotional profile
            profile = MOOD_PROFILES[mood].copy()

            # Apply song-specific adjustments
            adjustments = SONG_ADJUSTMENTS.get(title, {})

            for emotion, adjustment in adjustments.items():

                profile[emotion] += adjustment

                # Keep values between 1 and 10
                profile[emotion] = max(
                    1,
                    min(10, profile[emotion])
                )

            row = [
                song_id,
                title,
                artist,
                language,
                genre,
                mood,
                profile["energy"],
                profile["happiness"],
                profile["sadness"],
                profile["anger"],
                profile["romance"],
                profile["calm"],
                profile["nostalgia"]
            ]

            writer.writerow(row)

    print("===================================")
    print("      MOODIFY DATASET CREATED")
    print("===================================")
    print(f"Songs in catalogue: {len(songs)}")
    print(f"Unique songs written: {len(unique_songs)}")
    print(f"Duplicates removed: {len(songs) - len(unique_songs)}")
    print(f"Song-specific profiles: {len(SONG_ADJUSTMENTS)}")
    print(f"File created: {filename}")
    print("===================================")


if __name__ == "__main__":
    create_dataset()