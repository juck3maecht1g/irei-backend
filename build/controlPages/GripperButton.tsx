import React from 'react'
import { post } from '../backendComunication/BasicOpperations'
import './../theme.css'
import './../irei_styles.css'
const fetchAdress = "http://127.0.0.1:5000/api/execchangegripper"
const Message = "execchangegripper"

function informexecChangeGripper(errorMessage, forErrors) {
    post(Message, fetchAdress).then(
        res=> {
            if(res !== "Done") {
            errorMessage(res)
            forErrors()   
            }
        }
    )
}

/**
 * The GripperButton is used to control the Gripper auf chosen Robots
 */
function GripperButton (props) {
    return ( 
        <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
            onClick={
                ()=> {informexecChangeGripper(props.errorMessage, props.forErrors)}
            }>
            
            <i className='material-icons'>precision_manufacturing</i>gripper
        </button>
     );
}
 
export default GripperButton;