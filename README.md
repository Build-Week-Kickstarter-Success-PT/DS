# DS

# Install
When you install glob, you have to install glob3
```sh
pipenv install glob3
```
ipykernal to run a jupyter notebook in vscode
```sh
pipenv install --dev
```

# To run app
```sh
uvicorn app.main:app --reload
```
Go to: localhost:8000 in browser

# git workflow
git checkout main
git pull
git checkout -b <name of branch>
git branch --set-upstream-to=origin/<name of remote branch> <name of local branch> note: these names can be the same
