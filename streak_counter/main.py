from api import get_commits
from streaks import calculate_streaks


def main():
    repo_name = input("Enter the repository (e.g., octocat/Hello-World): ")
    username = input("Enter the GitHub username: ")

    print("Fetching commits...")
    commit_dates = get_commits(repo_name, username)

    print("Calculating streaks...")
    streaks = calculate_streaks(commit_dates)

    print("\n--- Streak Counter ---")
    print(f"Daily Streak: {streaks['daily_streak']} days")
    print(f"Weekly Streak: {streaks['weekly_streak']} weeks")
    print(f"Longest Streak: {streaks['longest_streak']} days")


if __name__ == "__main__":
    main()
