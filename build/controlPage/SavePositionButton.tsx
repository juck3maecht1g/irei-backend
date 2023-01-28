import React from 'react'
const fetchAdress = "http://127.0.0.1:5000/savePosition"
const savePositionMassage = "savePosition"

function informSavePosition() {
    async function post (){
        const response = await fetch(fetchAdress, {
            'method': 'POST',
            headers : {
            'Content-Type': 'application/json'
            },
            body : JSON.stringify(savePositionMassage)
        })
        if(response.ok) {
            //todo
        }
    }
    
    post()
}
/**
 * The SavePositionButton is used to save a Position 
 * for later use
 */
class SavePositionButton extends React.Component {
    constructor(props) {
        super(props);
    }
    state = {  }
    render() { 
        return ( 
            <button onClick={informSavePosition}></button>
         );
    }
}
 
export default SavePositionButton;