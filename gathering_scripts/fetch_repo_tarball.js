const shell = require('shelljs');
const fs = require('fs');

let lstRepos = null;
let position = 0;
let ghtoken = '';

function readRepoFile(){
    console.log('Reading Repo Files...');
    let content = fs.readFileSync('listrepos.txt');
    lstRepos = content.toString().split("\n");
    //console.log(`How many repos: ${lstRepos.length}`);
}

function readTokenFile(){
    let content = fs.readFileSync('mytoken.txt');
    ghtoken = content.toString().trim();
}

function readPositionFile(){
    let content = fs.readFileSync('pos.txt');
    position = parseInt( content.toString() );
}

function writePositionFile(){
    fs.writeFileSync('pos.txt',position.toString());
}

function callShell(repo){
    shell.exec(`./gather_script.sh ${repo} ${ghtoken}`);
}

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function main(){
    console.log('Starting Fetch_Repo_Tarball.js.');
    readRepoFile();
    readTokenFile();
    readPositionFile();
    for(let max=lstRepos.length; position<max;){
        console.log(`*** Repo ${position} : ${lstRepos[position]}`);
        callShell(lstRepos[position].replace(/(\r\n|\n|\r)/gm, ""));
        position++;
        writePositionFile();
        await sleep(1000);
    }
    console.log(`\n**End. ${position}`);
}

main();
