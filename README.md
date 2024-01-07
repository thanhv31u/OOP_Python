OOP Project


Init a local repository
Define the origin to the remote repository
Add the file to the index
Commit the files
Push the files from the local repository to the remote
It leads to something like that:

```
cd yourLocalFolder
git init
git remote add origin https://github.com/<yourLogin>/<yourRepository>.git
git add .
git commit -m "Initial commit"
git push -u origin master
```
