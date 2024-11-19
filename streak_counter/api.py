from github import Github
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Initialize GitHub API client
github = Github(GITHUB_TOKEN)


def get_commits(repo_name: str, username: str, since_days: int = 30):
    """
    Fetch commits for a user from a repository within the last N days.

    :param repo_name: Repository name (e.g., 'octocat/Hello-World')
    :param username: GitHub username to filter commits by.
    :param since_days: Number of days to look back for commits.
    :return: List of commit dates (datetime objects).
    """
    repo = github.get_repo(repo_name)
    since_date = datetime.now() - timedelta(days=since_days)

    commits = repo.get_commits(since=since_date)
    user_commits = [
        commit.commit.author.date
        for commit in commits
        if commit.author and commit.author.login == username
    ]
    return user_commits
