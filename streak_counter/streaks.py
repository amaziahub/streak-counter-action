from datetime import datetime, timedelta


def calculate_streaks(commit_dates):
    """
    Calculate daily, weekly, and longest commit streaks.

    :param commit_dates: List of commit dates (datetime objects).
    :return: A dictionary with streak stats.
    """
    if not commit_dates:
        return {"daily_streak": 0, "weekly_streak": 0, "longest_streak": 0}

    # Sort commit dates in ascending order
    commit_dates = sorted(commit_dates)

    daily_streak = 1
    weekly_streak = 0
    longest_streak = 1
    current_streak = 1

    for i in range(1, len(commit_dates)):
        delta = (commit_dates[i] - commit_dates[i - 1]).days

        if delta == 1:  # Consecutive day
            current_streak += 1
            daily_streak = max(daily_streak, current_streak)
        elif delta > 1:  # Break in streak
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1

        if delta <= 7:  # Weekly streak
            weekly_streak += 1

    # Finalize longest streak
    longest_streak = max(longest_streak, current_streak)

    return {
        "daily_streak": daily_streak,
        "weekly_streak": weekly_streak,
        "longest_streak": longest_streak,
    }
