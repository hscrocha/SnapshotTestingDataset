const fs = require('fs');

let filRepos = fs.readFileSync('listrepos.txt');
let lstRepos = filRepos.toString().split("\n");
lstRepos.sort();

let filestxt = fs.readFileSync('files.txt');
let lstFiles = filestxt.toString().split("\n");


for(let repo of lstRepos){
    let procrepo = repo.replace('/','_').trim();
    //console.log(procrepo);
    if(lstFiles.includes(procrepo)===false){
        console.log(procrepo);
    }
}
