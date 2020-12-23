rsync -av davidbieber.com-main/ davidbieber.com-deploy/ --delete --exclude=.gitignore --exclude=.git

cd davidbieber.com-deploy
git config user.email "david810@gmail.com"
git config user.name "David Bieber"

git add .
git commit -m '[skip travis] Automatic commit by GitHub Actions'
git push origin deploy
