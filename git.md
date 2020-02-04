### Branching
commit to dev branch
- `git checkout -b new_branch develop` checkout a new branch from dev
- `git branch` check current branch 
- `git push origin new_branch` finalize the commit

can't find remote branch?
- `git branch -r` return all remote branches
- `git fetch` if still can't see, fetch everything from remote

### Delete
- delete remote branch: `git push origin --delete old_branch`
- delete local branch: `git branch -D old_branch`
- delete files: 
  - `git rm filename`
  - `git commit -m "remove file"`

