# Aroleid Simple Strategy Prototyper

A Python package for backtesting trading strategies with OHLCV data.

## Quickstart Guide

(Section under development)

## Documentation

(Section under development)

## Development

### Feature Roadmap

Each feature is listed in the order in which it should be implemented, with the most significant features listed first.
Each feature is assigned a number, such as `#03`, and a short name, such as `price-feed`.
This number and name will be used when creating Git branches (e.g., `feature/03-price-feed`), or writing commit messages, so that the user can easily track what feature each change is related to.

- `#01-Github-workflow-in-README` Add GitHub workflow to README.
- `#02-csv-to-pandas_df` Read external CSV file in databento format into a pandas DataFrame.


### Issue Tracking

Each issue is documented and addressed in the order of importance or urgency.
Like features, issues are assigned a number and a short name, such as `#i05-fix-timestamp-format`, prepended with `i` to indicate that it is an issue and not a feature.
This identifier will be used in Git branches (e.g., `fix/i05-fix-timestamp-format`), commit messages, or pull request titles to make it easy to trace which changes resolve which issues.


### CI/CD Workflow (v0.1.0)

This project follows the [**GitHub Flow**](https://docs.github.com/en/get-started/using-github/github-flow) workflow for facilitating CI/CD:

1. **Create a feature branch** from `master`:
   ```bash
   git checkout master
   git pull origin master
   git checkout -b feature/#<feature-number>-<feature-short-name>
   ```

2. **Make changes and commit** regularly:
   ```bash
   git add .
   git commit -m "Fix #<issue-number>: <commit-message> or Feature #<feature-number>: <commit-message>"
   ```

3. **Push branch**:
   ```bash
   git push origin feature/#xx-feature-description
   ```

4. **Verify code quality and tests**:
   ```bash
   # Run the verification script that checks formatting, linting, and tests
   ./scripts/verify.sh
   ```
   
   Only proceed to the next step if all checks pass.
   
5. **Optional: Create Pull Request** if collaboration or review is needed:
   - Create a PR on GitHub targeting the `master` branch
   - Code review and discussion happens in the PR
   - Merge to master after approval using "Squash and merge" or "Merge pull request"
   - Delete the remote feature branch after merging

6. **Merge to master** (directly or after PR approval):
   ```bash
   git checkout master
   git pull origin master
   git merge feature/#xx-feature-description
   git push origin master
   ```

7. **Update local master and cleanup**:
   ```bash
   git checkout master
   git pull origin master  # If merged via PR
   git branch -d feature/#xx-feature-description
   ```