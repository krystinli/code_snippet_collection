### Branching
commit to dev branch
- `git checkout -b new_branch develop` checkout a new branch from dev
- `git push origin new_branch` push to the new branch

manage remote branches
- `git fetch` fetch everything from remote
- `git branch -r` return all remote branches
- `git reset --hard` undo all local changes and revert to recent commit state

### Stashing
- `git stash list` see all the previous stash work
- `git stash pop stash@{0}` go back to one of the previous temporary saved version 
- `git stash drop <stash_id>` delete a particular stash
- `git stash clear` delete all stash

### Delete
- delete remote branch: `git push origin --delete old_branch`
- delete local branch: `git branch -D old_branch`
- delete files on git: 
  - `git rm filename`
  - `git rm -r folder`
  - `git commit -m "remove file"`
- revert after pushing: `git revert 85756v(commit#)`
- revert after adding `git reset`

Cleaning 
- `git reset filename` un-add before commit
- `git checkout develop -- path/filename` grab a file from diff branch 
