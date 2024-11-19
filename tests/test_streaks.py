from datetime import datetime, timedelta

from streak_counter.streaks import calculate_streaks


def test_calculate_streaks():
    today = datetime.now()
    commit_dates = [
        today - timedelta(days=i) for i in [0, 1, 2, 4, 7, 8, 9]
    ]

    streaks = calculate_streaks(commit_dates)

    assert streaks["daily_streak"] == 3
    assert streaks["weekly_streak"] >= 2
    assert streaks["longest_streak"] == 3
