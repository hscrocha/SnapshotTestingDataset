# SnapShot Testing Collection Node.js and Shell Scripts

## Scripts:
1. gather_script.sh
2. fetch_repo_tarball.js

## Auxiliary Files 
1. listrepos.txt - contain a list of repositories for the Node.js script to feed to the shell script
2. pos.txt - saves the current position on the list of repos (previous file). In case you want to download repositories in intervals, this will save the last position (currently set as 680 for the running example).
3. mytoken.txt - you must change the contents of this file to have your github access token (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
4. packages.json and packages-lock.json - dependencies for Node.js.
5. README.md - its me!




