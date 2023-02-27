import React from 'react'
import './../theme.css'
import './../irei_styles.css'
import { post } from '../backendComunication/BasicOpperations'

const fetchAdress = "http://127.0.0.1:5000/api/emergency_stop"
const Massage = "emergency_stop"

export default function EmergencyExit (props) {


    function informEmergencyStop() {
        post(Massage, fetchAdress).then(res => {
            if(res !== "Done") {
                props.errorMessage(res)
                props.errorfunction()
            }
          })
}
    return <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" 
                onClick={informEmergencyStop}>
                
                <i className='material-icons'>front_hand</i>emergency stop
            </button>
}