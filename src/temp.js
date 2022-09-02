const axios = require('axios')

window.onload = function () {
    document.getElementById("button").onclick = function () {
        var file = document.getElementById("file").files[0];
        var Value = 0;
    try{
        var data =await axios.post('http://127.0.0.1/5000/predictimage', {"image":file})
        var elem = document.getElementById("result");
        var text = document.createTextNode(data);
        elem.appendChild(text);
    }catch(err){
        console.log(err);
        }
    };
};