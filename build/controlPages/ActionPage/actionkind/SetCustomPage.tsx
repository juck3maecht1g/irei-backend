import React from 'react';
import { useState } from 'react';
import { useLocation, Link, useNavigate } from 'react-router-dom';
import { appendAction } from '../ActionFetch';
import {TopBarActionCreate} from '../../../TopBar';
import './../../../theme.css'
import './../../../irei_styles.css'

export default function SetCustomPage() {
    const navigate = useNavigate();
    const [errorMessage, setErrorMessage] = useState("sorry robots couldnt be changed")
    const [error, setError] = useState(false)
    const errorState = () => {
        setError(current => !current)
    }
    const [name, setName] = useState("")


    
    const location = useLocation();
    const { kind } = location.state;
    const { ip } = location.state;

    const sentToBackend = () => {
        console.log("nameContent", name)
        var actionParameters = new Map<string, string>();
        actionParameters.set("key", kind);
        actionParameters.set("robot", ip);
        actionParameters.set("action",name);
        
        appendAction(errorState, actionParameters, setErrorMessage).then(res => {
            console.log(res)
            if(res) {
                navigate("/ActionListPage");
                window.location.reload();
            }
        }); 
    }

    return (
        <div>
            <TopBarActionCreate title="Custom Name"/>
            <form className= "form-settings">
                <div>
                    <label>please enter the name of the custom action:</label>
                </div>
                <div>
                    <input 
                        type= "text"
                        //required
                        value= {name}
                        onChange = {(e) => setName(e.target.value)}
                    />
                </div>
                <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" type="button"
                    onClick = {
                        sentToBackend}> 
                    <i className='material-icons'>check</i>
                </button>
            </form>
        </div>
    )
}