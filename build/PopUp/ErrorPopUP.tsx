import React from "react";
import PopUp from "./PopUp";
import './../theme.css'
import './../irei_styles.css'
import './Popup.css'

export function ErrorPopUp(props) {
//active deactivate


    return (
        <PopUp trigger={props.active}>
            <form >
                <div>
                    <label id="message">
                        {props.message}
                    </label>
                </div>
                
            </form>
            <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
                onClick={props.deactivate} 
            >
                <i className="material-icons">check</i>
            </button>
        </PopUp>
    )
}