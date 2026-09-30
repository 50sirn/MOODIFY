# MOODIFY 🎵

## Overview
MOODIFY is a terminal-based Python music recommendation system that recommends songs according to a user's mood, optional free-text emotional description, preferred language, and genre.

The system uses a self-created music catalogue stored in CSV format. It analyzes the user's description using keyword-based mood detection and supports multiple simultaneous moods. Recommendations are generated using emotional compatibility scoring across seven dimensions: energy, happiness, sadness, anger, romance, calm, and nostalgia.

## Features
- Mood selection from 10 mood categories
- Optional free-text mood description
- Multi-mood detection
- Primary/secondary mood weighting (70% / 30%)
- Emotional compatibility scoring
- Language filtering
- Genre filtering
- Top-5 song recommendations
- Playlist generation as a `.txt` file
- CSV-based music database
- Duplicate removal during dataset generation
- Input validation for menu choices

## Technologies
- Python 3
- CSV
- File handling
- Modular programming
- Functions and dictionaries
- PyCharm
- Git/GitHub

## Project Structure
```text
MOODIFY/
├── data/
│   └── music_data.csv
├── main.py
├── mood_analyzer.py
├── recommendation_engine.py
├── music_database.py
├── music_catalog.py
├── dataset_generator.py
├── user_input.py
├── playlist_manager.py
├── README.md
└── statement.md
```

## How to Run
1. Install Python 3.
2. Clone/download the repository.
3. Open the project folder in PyCharm or a terminal.
4. Run:
```bash
python main.py
```

## How to Test
Run the complete application through `main.py`.

Example:
- Select `Sad`
- Choose `Yes` for a description
- Enter: `I feel really sad but I just wanna chill`
- Select `English`
- Select `Any` genre

Expected behavior:
- The description is detected as `sad, chill`.
- The recommendation engine combines the selected mood with the detected secondary mood.
- Five compatible songs are displayed.
- The user can optionally create a playlist.

Individual modules can also be tested directly:
```bash
python mood_analyzer.py
python recommendation_engine.py
python dataset_generator.py
python music_database.py
python playlist_manager.py
```

## Recommendation Method
MOODIFY represents each song using seven emotional dimensions. A selected mood is also represented using a target emotional profile. Compatibility is calculated from the average difference between the song profile and target profile.

When a description contains additional moods:
- Primary selected mood = 70% influence
- Secondary detected moods = 30% combined influence

The resulting score is used to rank recommendations.

## Project Scope
MOODIFY is designed as an academic Python project demonstrating modular programming, input processing, text-based mood classification, data handling, scoring, filtering, and file generation. It does not currently use external AI models or streaming-service APIs.
