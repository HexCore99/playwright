# Essential Git Commands

| Command | Description |
| --- | --- |
| `git init` | Create a new Git repository in the current folder. |
| `git clone <repo-url>` | Copy an existing remote repository to your computer. |
| `git status` | Show changed, staged, and untracked files. |
| `git add <file>` | Stage one file for the next commit. |
| `git add .` | Stage all changed and untracked files in the current folder. |
| `git commit -m "message"` | Save staged changes with a commit message. |
| `git log --oneline` | Show commit history in a compact format. |
| `git branch` | List local branches. |
| `git branch <branch-name>` | Create a new branch. |
| `git switch <branch-name>` | Move to another branch. |
| `git switch -c <branch-name>` | Create a new branch and switch to it. |
| `git branch -m <new-name>` | Rename the current branch. |
| `git remote -v` | Show configured remote repository URLs. |
| `git remote add origin <repo-url>` | Connect the local repository to a remote named origin. |
| `git remote set-url origin <repo-url>` | Change the URL for the origin remote. |
| `git push -u origin <branch>` | Push a branch and set its upstream remote branch. |
| `git push` | Upload local commits to the tracked remote branch. |
| `git pull` | Download remote changes and merge them into the current branch. |
| `git fetch` | Download remote changes without merging them. |
| `git merge <branch-name>` | Merge another branch into the current branch. |
| `git diff` | Show unstaged file changes. |
| `git diff --staged` | Show staged changes before committing. |
| `git show <commit>` | Show details and changes from a specific commit. |
| `git switch --detach <commit>` | Go back to view any commit without moving a branch. |
| `git checkout <commit>` | Older command to view any commit in detached HEAD mode. |
| `git reset --soft <commit>` | Move the branch back to a commit while keeping changes staged. |
| `git reset --mixed <commit>` | Move the branch back to a commit while keeping changes unstaged. |
| `git reset --hard <commit>` | Move the branch back to a commit and delete later local changes. |
| `git reset --soft HEAD~1` | Undo the last commit but keep its changes staged. |
| `git reset --mixed HEAD~1` | Undo the last commit but keep its changes unstaged. |
| `git reset --hard HEAD~1` | Delete the last commit and discard its changes. |
| `git revert <commit>` | Create a new commit that undoes a previous commit. |
| `git reflog` | Show recent branch and HEAD movements for recovery. |
| `git reset --hard <reflog-entry>` | Restore the repo to a previous position from reflog. |
| `git restore <file>` | Discard unstaged changes in one file. |
| `git restore --staged <file>` | Unstage a file while keeping its changes. |
| `git rm <file>` | Delete a tracked file and stage the deletion. |
| `git stash` | Temporarily save uncommitted changes. |
| `git stash pop` | Reapply the most recent stashed changes and remove them from the stash. |
| `git tag <tag-name>` | Create a tag for the current commit. |
| `git push origin --delete <branch>` | Delete a branch from the remote repository. |
