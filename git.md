### Cleanning 
- `git reset filename` un-add beore commit
- `git checkout filename` undo all changes before adding
- `git reset --hard` undo all local changes and revert to recent commit state
- print list of untracked files `git clean -n`
- delete these untracked files `git clean -f`


### Delete
- delete remote branch: `git push origin --delete old_branch`
- delete local branch: `git branch -D old_branch`
- delete files: 
  - `git rm filename`
  - `git commit -m "remove file"`
- revert after pushing: `git revert 85756v(commit#)`
- revert after adding `git reset `
  
### Branching
commit to dev branch
- `git checkout -b new_branch develop` checkout a new branch from dev
- `git branch` check current branch 
- `git push origin new_branch` finalize the commit

can't find remote branch?
- `git branch -r` return all remote branches
- `git fetch` if still can't see, fetch everything from remote

migrate to a new org
- `git remote set-url origin new_url` to point to new url

### Stashing
- `git stash` temporarily save current uncommit work so that I can checkout a diff branch
- `git stash list` see all the previous stash work
- `git stash pop stash@{0}` go back to one of the previous temporary saved version 
- `git stash drop <stash_id>` delete a particular stash
- `git stash clear` delete all stash

### User
- `git config --global user.email "krystinkrystin@hotmail.com"`
- `git config --global user.name krystinli`
