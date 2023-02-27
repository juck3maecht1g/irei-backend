import React from 'react'
import { Link } from 'react-router-dom';
import './theme.css'
import './irei_styles.css'

function NavigationButton(props) {
    
    return ( 
        <Link to={props.destinationLink} state={{ from: "Burgermenu"}} //erst noch mit links maybe weg
                className="navigation-button mdl-button 
                    mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
            {props.destination}
        </Link>
        );

}

export default NavigationButton;