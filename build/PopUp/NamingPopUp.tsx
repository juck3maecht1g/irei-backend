import React, { useState } from "react";
import PopUp from "./PopUp";
import './../theme.css'
import './../irei_styles.css'
import './Popup.css'



export function NamingPopUp(props) {
//active, confirm, forErrors, getBaseName
    const [name, setName] = useState("")
    props.getBaseName(setName)
    
    return (
        <PopUp trigger={props.active}>
            <form>
                <div>
                    <label>
                        please enter a name {/*or accept the default name*/}:
                    </label>
                </div>
                <div>
                    <input
                    type="text"
                    required
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    />
                </div>
            </form>
            {(name !== "")? 
            <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" 
                onClick={
                    () => {console.log(props.started)
                        if(props.started !== "undefined") {
                            props.confirm(props.forErrors, name, props.errorMessage, props.started)
                         
                        } else {
                        props.confirm(props.forErrors, name, props.errorMessage)
                        }
                        props.deactivate()
                    }
                }>
                <i className="material-icons">check</i>
            </button>
            
            
            : <></>
        } 
        <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" 
            onClick={
                    () => {
                    props.deactivate()
                }
            }>
                <i className="material-icons">close</i>
        </button>    
        </PopUp>
        )
}