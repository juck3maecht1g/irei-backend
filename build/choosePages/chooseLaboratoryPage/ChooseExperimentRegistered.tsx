import React from 'react'
import {useState} from 'react'
import { Link, useNavigate } from 'react-router-dom';
import { GetExperiments, SetExperiment } from '../../backendComunication/FetchAndSetDirExp';
import { ErrorPopUp } from '../../PopUp/ErrorPopUP';
import TopBar from '../../TopBar';
import '../Choose.css';
import './../../theme.css'
import './../../irei_styles.css'

/**
 * The ChooseExperimentRegister is used to choose 
 * the experiment class the user wants to execute
 */
export default function ChooseExperimentRegistered() {
    const navigate = useNavigate();
    const [errorMessage, setErrorMessage] = useState("sorry something went wrong")
    const [error, setError] = useState(false)
    const [exp, setExperiment] = useState([]);
    GetExperiments(setExperiment);

    const errorState = () => {
        setError(current => !current)
       }
       const setExp = (name) => {
            SetExperiment(errorState,name, setErrorMessage ).then(res => {
                if(res) {
                    navigate("/Controlpage")
                }
            }
            )
       }


    const buttons = exp.map((number) => {
        return <ChooseRegisterButton name={number} action= {setExp}/>
    })

    return (
        <div>
            <TopBar title="Choose Experiment"></TopBar>
            <div className='choose-flexbox'>
            {buttons}
            </div>
            <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
        </div>
    )
}

/**
 * The ChooseRegisterButton is used to choose 
 * the Esperiment out of the register which is displayed by this Button
 */

function ChooseRegisterButton (props) {
    const setChoise = () => {
        props.action(props.name) 
    }
    return ( 
       
        <button onClick={setChoise} 
        className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
            {props.name}
        </button>
    
     );
}

/*
function SaveChoice () {
    //sent to Backend
}
*/