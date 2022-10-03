import ReactDOM from 'react-dom';
import React from 'react';
import axios from 'axios';


function App(){

    const [image] = React.useState(null)

    const Getres = async function(){
        const formData = new FormData();
        formData.append('image', )
        try{
            var Value = await axios.post('http://127.0.0.1/5000/predictimage', );
            console.log(Value);
        } catch {
            console.error(error)
        }
    }

    return (
    <div>
        <h1>Insert your image here !</h1>
        <input type="file" id="file" name="file" accept="image/*"></input>
        <button id="button" onClick={Getres}>Upload</button>
    </div>)}


ReactDOM.render(<App />, document.getElementById('app'));