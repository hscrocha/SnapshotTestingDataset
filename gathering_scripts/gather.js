const shell = require('shelljs');
const fs = require('fs');

let lstRepos = null;
let position = 0;
console.log('Hello.');

function readRepoFile(){
    console.log('Reading Repo Files...');
    let content = fs.readFileSync('listrepos.txt');
    lstRepos = content.toString().split("\n");
    //console.log(`How many repos: ${lstRepos.length}`);
}

function readPositionFile(){
    let content = fs.readFileSync('pos.txt');
    position = parseInt( content.toString() );
}

function callShell(repo){
    shell.exec(`./ghtarscript.sh ${repo}`);
}

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function main(){
    console.log("Init.");
    readRepoFile();
    readPositionFile();
    for(let max=12; position<max; position++){
        console.log(`*** Repo ${position} : ${lstRepos[position]}`);
        callShell(lstRepos[position].replace(/(\r\n|\n|\r)/gm, ""));
        await sleep(1000);
    }
    console.log(`End. ${position}`);
}

main();