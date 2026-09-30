
def analyze_moods(mood_text):
    mood_text = mood_text.lower().strip()

    # ==========================================
    # CRISIS DETECTION
    # ==========================================

    crisis_keywords = [
        "kill myself",
        "end my life",
        "suicide",
        "suicidal",
        "want to die",
        "don't want to live",
        "do not want to live",
        "hurt myself",
        "harm myself",
        "self harm",
        "self-harm"
    ]

    for keyword in crisis_keywords:
        if keyword in mood_text:
            return ["crisis"]

    # ==========================================
    # MOOD KEYWORDS
    # ==========================================

    mood_keywords = {

        "happy": [
            "going pretty well",
            "things are going pretty well",
            "life is going well",
            "life is going pretty well",
            "happy", "joyful", "good", "great", "amazing",
            "fantastic", "awesome", "cheerful", "fun",
            "positive", "excited", "glad", "delighted",
            "wonderful", "good mood", "feeling good",
            "feeling great", "having fun", "great day",
            "amazing day", "life is good", "feeling positive",
            "on top of the world", "going well", "going great",
            "things are going well", "things are going great",
            "feeling better", "in a good place"
        ],

        "sad": [
            "sad", "depressed", "lonely", "upset", "miserable",
            "crying", "cry", "low", "down", "empty",
            "drained", "rough day", "bad day", "terrible",
            "awful", "feeling terrible", "feeling awful",
            "feel like crying", "feeling low", "feeling down",
            "going wrong", "going badly", "things are going wrong",
            "tired of everything", "exhausted", "hopeless",
            "rough time", "hard time", "not doing well",
            "feeling terrible lately"
        ],

        "angry": [
            "angry", "mad", "furious", "rage", "raging",
            "annoyed", "irritated", "frustrated", "pissed",
            "pissed off", "aggressive", "fed up",
            "sick of this", "lost my temper",
            "getting on my nerves", "can't stand this",
            "had enough"
        ],

        "romantic": [
            "romantic", "love", "loving", "in love",
            "crush", "date", "affection", "valentine",
            "intimate", "lovey dovey", "thinking about them",
            "fall in love", "feeling romantic",
            "falling for someone", "falling for her",
            "falling for him", "falling for them",
            "catching feelings", "have feelings",
            "developing feelings", "someone special"
        ],

        "calm": [
            "calm", "peaceful", "relaxed", "quiet",
            "peace", "meditation", "comfortable",
            "stress free", "stress-free", "at peace",
            "feeling peaceful", "want to relax",
            "need to relax", "relaxing", "peace and quiet",
            "clear my head", "clear my mind"
        ],

        "chill": [
            "chill", "chilling", "laid back", "laid-back",
            "vibing", "vibe", "just chilling", "taking it easy",
            "hanging out", "lowkey", "low-key",
            "want to vibe", "just vibing", "relaxing",
            "kick back", "sit back", "take it easy"
        ],

        "nostalgic": [
            "nostalgic", "memories", "remember", "childhood",
            "old days", "old times", "throwback",
            "miss the past", "miss those days",
            "reminds me of", "sentimental",
            "thinking about the past",
            "school days", "back in school",
            "how things used to be", "used to be",
            "back then", "good old days",
            "take me back", "miss how things were"
        ],

        "energetic": [
            "energetic", "hyped", "hype", "pumped",
            "pumped up", "active", "workout", "gym",
            "party", "full of energy", "ready to go",
            "feeling alive", "lets go", "let's go",
            "excited to party", "dancing", "dance",
            "ready to party", "adrenaline", "high energy"
        ],

        "motivated": [
            "motivated", "determined", "focused", "productive",
            "ambitious", "ready to grind", "ready to work",
            "need motivation", "want motivation",
            "want to achieve", "chasing goals", "locked in",
            "grind mode", "work hard", "get things done",
            "exam grind", "study grind", "grinding",
            "goal", "goals", "discipline"
        ],

        "heartbroken": [
            "heartbroken", "heart broken", "breakup",
            "break up", "broke up", "broken heart",
            "can't get over them", "cannot get over them",
            "miss my ex", "lost someone", "relationship ended",
            "got dumped", "she left me", "he left me",
            "they left me", "relationship broke down",
            "thinking about my ex",
            "can't stop thinking about my ex",
            "my ex", "ex girlfriend", "ex boyfriend",
            "still love my ex", "miss my ex"
        ]
    }

    # ==========================================
    # SCORE EACH MOOD
    # ==========================================

    mood_scores = {}

    for mood, keywords in mood_keywords.items():

        score = 0

        for keyword in keywords:

            if keyword in mood_text:

                if len(keyword.split()) > 1:
                    score += 2
                else:
                    score += 1

        if score > 0:
            mood_scores[mood] = score

    if not mood_scores:
        return ["unknown"]

    # ==========================================
    # SORT MOODS BY SCORE
    # ==========================================

    sorted_moods = sorted(
        mood_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [mood for mood, score in sorted_moods]


# ==========================================
# BACKWARD COMPATIBILITY
# ==========================================

def analyze_mood(mood_text):

    moods = analyze_moods(mood_text)

    return moods[0]


# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    print("MOODIFY MOOD ANALYZER")
    print("---------------------")

    test_phrases = [
        "bro today was fucking amazing",
        "everything has been going wrong lately",
        "I don't know man, I just feel empty",
        "I'm pissed at everyone right now",
        "I just want to sit back and vibe",
        "take me back to school days",
        "I'm locked in, exam grind starts now",
        "I'm absolutely pumped for tonight",
        "I think I'm falling for someone",
        "I can't stop thinking about my ex",
        "I just need some peace and quiet",
        "life is actually going pretty well",
        "I'm so fucking tired of everything",
        "I feel like dancing tonight",
        "I miss how things used to be",

        # MULTI-MOOD TESTS
        "I feel really sad but I just wanna chill",
        "I'm angry but I need to stay focused",
        "I'm happy and energetic today",
        "I'm heartbroken but feeling nostalgic",
        "I feel romantic and peaceful tonight"
    ]

    for phrase in test_phrases:

        moods = analyze_moods(phrase)

        print(f"\nInput: {phrase}")
        print(f"Detected moods: {', '.join(moods)}")

