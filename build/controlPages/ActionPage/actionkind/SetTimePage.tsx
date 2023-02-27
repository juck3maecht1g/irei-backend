import React from 'react';
import { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { appendAction } from '../ActionFetch';
import {TopBarActionCreate} from '../../../TopBar';

export default function SetTimePage() {
    const navigate = useNavigate();
    const [errorMessage, setErrorMessage] = useState("sorry robots couldnt be changed")
    const [error, setError] = useState(false)
    const errorState = () => {
        setError(current => !current)
    }
    const [time, setTime] = useState('0')

    const location = useLocation();
    const { kind } = location.state;
    const { ip } = location.state;
console.log("custumLoc", kind)

    const sentToBackend = () => {
        console.log("hi")
        var actionParameters = new Map<string, string>();
        actionParameters.set("key", kind);
        actionParameters.set("robot", ip);
        actionParameters.set("time", time);
        appendAction(errorState, actionParameters, setErrorMessage).then(res => {
            if(res) {
                navigate("/ActionListPage")
                window.location.reload();
            }
        });
    }

    return (
        <div>
            <TopBarActionCreate title="Custom Name"/>
            <form className= "form-settings">
                <div>
                    <label>please set a time in seconds:</label>
                </div>
                <div>
                    <input
                        type= "number"
                        required
                        value= {time}
                        onChange = {(e) => setTime(e.target.value)}
                    />
                </div>
                <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"  type ="button"
                        onClick = {sentToBackend}>
                        <i className='material-icons'>check</i>
                </button>
            </form>
        </div>
    )
}