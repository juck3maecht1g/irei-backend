import React, { useState } from 'react'
import TopBar from '../../TopBar';
import ChooseButton from '../ChooseRobotButton';
import { useLocation } from "react-router-dom";
import { Link } from 'react-router-dom';
import { SetExpRobots } from '../../backendComunication/SetRobots';
import { ErrorPopUp } from '../../PopUp/ErrorPopUP';
import './../../theme.css'
import './../../irei_styles.css'
/**
 * The ChooserobotPage is used to choose the robots
 * the user wants to work with
 */
export default function ChooseExperimentRobots(){
    const [errorMessage, setErrorMessage] = useState("sorry something went wrong")
    const [error, setError] = useState(false)
    const location = useLocation();
    const { from } = location.state;

    var chosen =  new Map<string, string>() // the chosen robots 
    const errorState = () => {
        setError(current => !current)
       }

    const clickedBot = (ip, name) => {
        if (chosen.has(ip))  {
            chosen.delete(ip)
        } else {
            chosen.set(ip,name)
        }
     
    }

    const confirm = () => {
       SetExpRobots(errorState, chosen, setErrorMessage)
    }

    const buttons = from.map((number) => { 
        return <ChooseButton name={number.value} 
        ip={number.key}
        action = {clickedBot}
        state = {false}/>
    })


    const chooseAll = () => { // toDo funktioniert noch nicht
        for(var i = 0;i<from.length;i++) { 
           if (!chosen.has(from[i].key)) {
            chosen.set(from[i].key,from[i].value)
           }
         }
    }

    return ( 
        <div>
        <TopBar title="Choose Robots"></TopBar>
        {buttons}
        <Link 
            to = {"/ChooseExperimentRegister"}
        >
            <button className="icon-button irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
             onClick={confirm}>
                <i className="material-icons">check</i>
             </button>
        </Link>
        <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
        </div>
    );
}