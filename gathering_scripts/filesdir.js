const testFolder = '../';
const fs = require('fs');

const dir = fs.readdirSync(testFolder);
const proc = [];
let last = "";
for(let file of dir){
    let i = file.indexOf(".");
    let cur = file.substring(0,i);
    if(cur!==last && cur.length>0){ 
        proc.push(cur);
        last = cur;
    }
}

for(let fname of proc){
    console.log(fname);
}
