import React from 'react'

const fetchAdress = "http://127.0.0.1:5000/executeList"
const savePositionMassage = "executeList"

function informExecuteActionList() {
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
 * The ApproachPositionActionButton is used to add an ApproachPositionAction
 * to a list of actions
 */
class ApproachPositionActionButton extends React.Component {
    constructor(props) {
        super(props);
    }
    state = {  }
    render() { 
        return ( 
            <button></button>
         );
    }
}
 
export default ApproachPositionActionButton;