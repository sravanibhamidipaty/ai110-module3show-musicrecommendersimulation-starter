"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations for profile genre=pop, mood=happy, energy=0.8\n")
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


if __name__ == "__main__":
    main()
