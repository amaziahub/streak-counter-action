# streak-counter-action

# Streak Counter

Track and display commit streaks for contributors and notify them!

## Inputs
- `github-token`: (Required) GitHub token for accessing the API.
- `username`: (Required) GitHub username to track.

## Outputs
- `daily-streak`: Current daily streak.
- `weekly-streak`: Current weekly streak.
- `longest-streak`: Longest streak.

## Example Workflow
```yaml
name: Commit Streak Tracker
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  track-streak:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Track Commit Streak
        uses: your-org/streak-counter-action@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          username: octocat



---

#### **4. Test Your Action**
- Ensure the Action works correctly in a sample workflow.
- Use your GitHub repositories to test the Action in real-world scenarios.

---

#### **5. Tag a Release**
- Create a semantic version tag (e.g., `v1.0.0`) to reference your Action reliably.
  ```bash
  git tag -a v1.0.0 -m "First release"
  git push origin v1.0.0
