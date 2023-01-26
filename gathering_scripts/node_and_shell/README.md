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

## You will Need
- A Unix-type shell.
- wget installed (https://www.gnu.org/software/wget/)
- Node.js installed (https://nodejs.org/en/)

## Instructions

Make sure you can run wget from your shell command line. Also please make sure that all scripts have the permission to be executed in your machine, and the folder has writeable permission for the scripts to download and create the tarball files. Moreover, Node.js and NPM (Node Package Manager -- already bundled with Nodejs instalation) also need to be installed.

1. gather_script.sh is a Unix-shell script that uses wget to fetch a repository. It requires two parameters in the following order: the repository fullname as 'user/reponame', and your github access token.
2. fetch_repo_tarball.js is a Nodejs script that reads the listrepos.txt and mytoken.txt and feeds them to the gather_script.sh and sleeping for 1 second between each call. This automates the gathering to multiple repositories since the shell script only fetchs one repo at a time.

## Example

### gather_script.sh

In this example lets get the repository 'NewSpring/Holtzman' (top-1 in snapshot files in our dataset). For this we just need to call the script in our shell command-line (make sure the script is on the current folder):
```
./gather_script.sh NewSpring/Holtzman gh_token
```
This should create a file called 'NewSpring_Holtzman.tar.gz' in your current folder. You need to make sure this script works properly before using the next one.

### fetch_repo_tarball.js

In this example, we use the Node.js script to fetch multiple repositories. The position file 'pos.txt' is pre-set on the 680 position, meaning it will only fetch 6 repos in this example. You can adjust the position and the list of repos for this code to fetch more or different repositories. Firstly, we need to install the dependencies for our Node.js code to run. On the command-line make sure the current folder is set to folder 'node_and_shell', and type:
```
npm install
```

This should have installed the dependencies, and a new folder called "node_modules" was created (that is where npm installed the dependencies). Now we can run the main code in the command-line as:
```
node fetch_repo_tarball.js
```

After it is done, you should have new files each representing a different compacted repository.


