
from music_database import load_songs


MOOD_PROFILES = {
    "happy": {
        "energy": 8,
        "happiness": 10,
        "sadness": 1,
        "anger": 1,
        "romance": 5,
        "calm": 4,
        "nostalgia": 3
    },
    "sad": {
        "energy": 3,
        "happiness": 2,
        "sadness": 9,
        "anger": 2,
        "romance": 6,
        "calm": 6,
        "nostalgia": 8
    },
    "energetic": {
        "energy": 10,
        "happiness": 8,
        "sadness": 1,
        "anger": 4,
        "romance": 3,
        "calm": 1,
        "nostalgia": 3
    },
    "angry": {
        "energy": 9,
        "happiness": 3,
        "sadness": 3,
        "anger": 10,
        "romance": 1,
        "calm": 1,
        "nostalgia": 2
    },
    "romantic": {
        "energy": 5,
        "happiness": 7,
        "sadness": 2,
        "anger": 1,
        "romance": 10,
        "calm": 7,
        "nostalgia": 6
    },
    "calm": {
        "energy": 2,
        "happiness": 6,
        "sadness": 2,
        "anger": 1,
        "romance": 3,
        "calm": 10,
        "nostalgia": 5
    },
    "nostalgic": {
        "energy": 5,
        "happiness": 5,
        "sadness": 5,
        "anger": 1,
        "romance": 6,
        "calm": 6,
        "nostalgia": 10
    },
    "motivated": {
        "energy": 9,
        "happiness": 8,
        "sadness": 1,
        "anger": 4,
        "romance": 2,
        "calm": 2,
        "nostalgia": 3
    },
    "chill": {
        "energy": 4,
        "happiness": 6,
        "sadness": 3,
        "anger": 1,
        "romance": 5,
        "calm": 9,
        "nostalgia": 6
    },
    "heartbroken": {
        "energy": 4,
        "happiness": 1,
        "sadness": 10,
        "anger": 3,
        "romance": 9,
        "calm": 5,
        "nostalgia": 9
    }
}


EMOTIONS = [
    "energy",
    "happiness",
    "sadness",
    "anger",
    "romance",
    "calm",
    "nostalgia"
]


def calculate_mood_score(song, mood):
    """
    Calculate compatibility between one song and one mood.
    """

    mood = mood.lower()

    if mood not in MOOD_PROFILES:
        return 0

    target_profile = MOOD_PROFILES[mood]

    total_difference = 0

    for emotion in EMOTIONS:

        target_value = target_profile[emotion]
        song_value = int(song[emotion])

        difference = abs(target_value - song_value)

        total_difference += difference

    average_difference = total_difference / len(EMOTIONS)

    score = 100 - (average_difference / 9 * 100)

    return round(score, 2)


def create_blended_profile(primary_mood, secondary_moods=None):
    """
    Create a combined emotional profile.

    Primary mood has 70% influence.
    Secondary moods share the remaining 30%.
    """

    primary_mood = primary_mood.lower()

    if primary_mood not in MOOD_PROFILES:
        return None

    if not secondary_moods:
        return MOOD_PROFILES[primary_mood].copy()

    valid_secondary_moods = []

    for mood in secondary_moods:

        mood = mood.lower()

        if mood in MOOD_PROFILES and mood != primary_mood:
            valid_secondary_moods.append(mood)

    if not valid_secondary_moods:
        return MOOD_PROFILES[primary_mood].copy()

    primary_weight = 0.70
    secondary_weight = 0.30 / len(valid_secondary_moods)

    blended_profile = {}

    for emotion in EMOTIONS:

        primary_value = MOOD_PROFILES[primary_mood][emotion]

        value = primary_value * primary_weight

        for mood in valid_secondary_moods:

            secondary_value = MOOD_PROFILES[mood][emotion]

            value += secondary_value * secondary_weight

        blended_profile[emotion] = value

    return blended_profile


def calculate_blended_mood_score(
    song,
    primary_mood,
    secondary_moods=None
):
    """
    Calculate compatibility using a primary mood
    and optional secondary moods.
    """

    blended_profile = create_blended_profile(
        primary_mood,
        secondary_moods
    )

    if blended_profile is None:
        return 0

    total_difference = 0

    for emotion in EMOTIONS:

        target_value = blended_profile[emotion]
        song_value = int(song[emotion])

        difference = abs(target_value - song_value)

        total_difference += difference

    average_difference = total_difference / len(EMOTIONS)

    score = 100 - (average_difference / 9 * 100)

    return round(score, 2)


def recommend_songs(
    mood,
    language=None,
    genre=None,
    limit=5,
    secondary_moods=None
):
    """
    Recommend songs based on a primary mood
    and optional secondary moods.
    """

    mood = mood.lower()

    if mood not in MOOD_PROFILES:
        return []

    songs = load_songs()
    recommendations = []

    for song in songs:

        if language and song["language"].lower() != language.lower():
            continue

        if genre and song["genre"].lower() != genre.lower():
            continue

        if secondary_moods:

            score = calculate_blended_mood_score(
                song,
                mood,
                secondary_moods
            )

        else:

            score = calculate_mood_score(
                song,
                mood
            )

        recommendations.append(
            (score, song)
        )

    recommendations.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        song
        for score, song in recommendations[:limit]
    ]


if __name__ == "__main__":

    print("MOODIFY RECOMMENDATION ENGINE")
    print("-----------------------------")

    mood = "sad"

    secondary_moods = ["chill"]

    results = recommend_songs(
        mood,
        language="English",
        genre="Hip-Hop",
        limit=5,
        secondary_moods=secondary_moods
    )

    for i, song in enumerate(results, start=1):

        score = calculate_blended_mood_score(
            song,
            mood,
            secondary_moods
        )

        print(
            f"{i}. {song['title']} - {song['artist']} "
            f"| Compatibility: {score}%"
        )
