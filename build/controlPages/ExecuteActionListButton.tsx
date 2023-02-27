import React from 'react'
import './../theme.css'
import './../irei_styles.css'

const fetchAdress = "http://127.0.0.1:5000/api/executeList"
const Massage = "executeList"

function informSavePosition() {
    async function post (){
        const response = await fetch(fetchAdress, {
            'method': 'POST',
            headers : {
            'Content-Type': 'application/json'
            },
            body : JSON.stringify(Massage)
        })
        if(response.ok) {
            //todo
        }
    }
    
    post()
}
/**
 * The ExecuteActionListButton is used to execute a list of
 * actions
 */
function ExecuteActionListButton () {
    return ( 
        <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" 
            onClick={informSavePosition}>
            actionlist
        </button>
     );
}
 
export default ExecuteActionListButton;