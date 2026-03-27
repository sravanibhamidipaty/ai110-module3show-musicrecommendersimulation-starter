"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def _print_recommendations_for_profile(profile_name: str, user_prefs: dict, songs: list[dict]) -> None:
    """Print top recommendations for one named user profile."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n=== Profile: {profile_name} ===")
    print(
        "Preferences: "
        f"genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
        f"energy={user_prefs['energy']}, likes_acoustic={user_prefs.get('likes_acoustic')}"
    )
    print("Top 5 recommendations:\n")

    for idx, rec in enumerate(recommendations, start=1):
        # Returned item format: (song_dict, score, explanation)
        song, score, explanation = rec
        reasons_text = explanation.replace("Score recipe:", "").strip()
        reasons = [reason.strip()
                   for reason in reasons_text.split(",") if reason.strip()]

        print(f"{idx}. {song['title']}")
        print(f"   Score   : {score:.2f}")
        print("   Reasons :")
        for reason in reasons:
            print(f"     - {reason}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy",
                "energy": 0.8, "likes_acoustic": False},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill",
                "energy": 0.4, "likes_acoustic": True},
        ),
        (
            "Deep Intense Rock",
            {"genre": "rock", "mood": "intense",
                "energy": 0.9, "likes_acoustic": False},
        ),
        # Edge case suggested for stress testing: conflicting preferences.
        (
            "Edge Case: High Energy + Sad Mood",
            {"genre": "pop", "mood": "sad", "energy": 0.9, "likes_acoustic": False},
        ),
        # Edge case: unknown genre and mood to test fallback behavior.
        (
            "Edge Case: Unknown Genre/Mood",
            {"genre": "kpop", "mood": "melancholic",
                "energy": 0.5, "likes_acoustic": True},
        ),
    ]

    for profile_name, user_prefs in profiles:
        _print_recommendations_for_profile(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
