import React from 'react'
import './../../theme.css'
import './../../irei_styles.css'

/**
 * The DirectoryButton is used to navigate into the directory
 * this button displays
 */
export default function DirectoryButton (props) {

    const execute = () => {
        props.action(props.name)
    }

    return ( 
        <div>
            <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
                onClick={execute}>{props.name}
            </button>
        </div>
        
     );
}