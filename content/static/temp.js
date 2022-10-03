const axios = require("axios");

/*document.getElementById("button").onclick = function () {
        var file = document.getElementById("file").files[0];
        var Value = 0;
    try{
        var data = axios.post('/predictimage', {"image":file})
        var elem = document.getElementById("result");
        var text = document.createTextNode(data);
        elem.appendChild(text);
    }catch(err){
        console.log(err);
        }
    };*/

const func = async function(){
    document.getElementById("button").onclick = function () {
        var file = document.getElementById("file").files[0];
        var Value = 0;
    try{
        var data = axios.post('/predictimage', {"image":file}).then( err => console.log(err));
        var elem = document.getElementById("result");
        var text = document.createTextNode(data);
        elem.appendChild(text);
    }catch(err){
        console.log(err);
        }
    };
}

