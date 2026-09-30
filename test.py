from music_database import load_songs

songs = load_songs()

for song in songs:
    if song["mood"].lower() == "energetic":
        print(
            song["title"],
            "|",
            song["artist"],
            "|",
            song["language"],
            "|",
            song["genre"]
        )