import React from 'react';
import { useState } from 'react';
import { Link} from 'react-router-dom';
import TopBar from '../../TopBar';
import Popup from '../../PopUp/PopUp';
import ChooseRobotsForMappingPage from './ChooseRobotsForMapping';
import '../../irei_styles.css'
import { GetMapping, SetMapping} from '../../controlPages/ActionPage/ActionFetch';
import { ErrorPopUp } from '../../PopUp/ErrorPopUP';

export default function MappingRobotsPage () {
    const [errorMessage, setErrorMessage] = useState("sorry robots couldnt be changed")
    const [error, setError] = useState(false)
    const errorState = () => {
        setError(current => !current)
    }

    const [index, setIndex] = useState(-1);

    var [roles, setRoles] = useState([])
    GetMapping(setRoles)

    const setChoice = (ip) => {
        var changed = [...roles]
        changed[index].set("robot", ip);
        setRoles(changed)
        setIndex(-1);
    }

    const sentToBackend = () => {
        /*var changed = []
        for (let i=0; i<roles.length; i++) {
            changed.push(roles[i].get("robot"));
        }
        console.log(changed) // changed to Backend
        console.log(index) // changed to Backend
        */
        SetMapping(roles, errorState, setErrorMessage)
    }

    const buttons = roles.map((element, index) => {
        return <MappingRobotsButton key={index} 
        index = {index} 
        element={element.get("robot")} 
        action={element.get("name")} 
        giveKey={setIndex} />
    })

    return (
        <div>
            <TopBar title= "mapping of robots"/>
            {buttons}
            <Link to={"/ActionListPage"}>
                <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick={sentToBackend}>
                <i className="material-icons">check</i>
                </button>
            </Link>
            <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
            <Popup trigger = {index >= 0}>
                <ChooseRobotsForMappingPage execute={setChoice}/>
                <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
                onClick={()=>setIndex(-1)}> 
                    <i className="material-icons">close</i> 
                </button>
            </Popup>
        </div>
    )
}

function MappingRobotsButton (props) {
    const handleClick = () => {
        console.log(props.index)
        props.giveKey(props.index)
    }

    return (
        <div>
            <div className='mapping-grid'>
                <p className='mapping-index'>
                    {props.index}:
                </p>
                <button className="ip-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick={handleClick}>
                    {props.element}
                </button>
                <p className='mapping-action'>
                    {props.action}
                </p>
            </div>
            
        </div>
    )
}

/*
const help1 = new Map();
help1.set("name", "gripperOpen")
help1.set("robot", "234.846.984")

const help2 = new Map();
help2.set("name", "steering")
help2.set("robot", "435.600.000")

const help3 = new Map();
help3.set("name", "gripperClose")
help3.set("robot", "129.666.876")

const help4 = new Map();
help4.set("name", "wait")
help4.set("robot", "657.674.111") */