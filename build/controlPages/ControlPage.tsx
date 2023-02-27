import React, {useState} from 'react';
import LoggerButton, { BaseNameStop , postLoggingStop}  from './LoggerButton';
import GrippperButton from "./GripperButton"
import ResetButton from './ResetButton';
import SavePositionButton, { BaseNamePosition, informSavePosition } from './SavePositionButton';
import EmergencyExit from './EmergencyExit';
import ModeButton from './ModeButton';
import './../theme.css'
import './../irei_styles.css'
import { NamingPopUp } from '../PopUp/NamingPopUp';
import { ErrorPopUp } from '../PopUp/ErrorPopUP';
import ActionListButton from './ActionListButton';
import { post } from '../backendComunication/BasicOpperations';
import { GetALButtonContent, GetALButtonContentLen } from './ActionPage/ActionFetch';
const postAdressDecALB = "http://127.0.0.1:5000/api/decrease_shortcuts"
const postAdressIncALB = "http://127.0.0.1:5000/api/increase_shortcuts"
const postAdressStart = "http://127.0.0.1:5000/api/start_request"


async function StartRequest (errorfunction, setErrorMessage) {
    var message = "start_request"
    await post(message, postAdressStart).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
        }})


}
//import ApproachPositionActionButton from '../ApproachPositionActionButton';

/**
 * The ControlPage is used to record an experiment
 * or to control Robots in the current scene
 */
function ControlPage (props) {
    var running = false
    const [errorMessage, setErrorMessage] = useState("sorry position could not be saved")
    const [started, setIsStarted] = useState(false);
    const [namePosition, setNamePosition] = useState(false)
    const [nameSave, setNameSave] = useState(false)
    const [error, setError] = useState(false)
   
    const [numberALists, setNumberALists] = useState(0)
    const [aList, setAList] = useState([])
    
    GetALButtonContentLen(setNumberALists)
    GetALButtonContent(setAList)    

    const increaseListButtons = () => {
        increaseALB(errorState, setErrorMessage).then(res => {
            if(res) {
                
                window.location.reload();
            }
        });
    }

    const decreaseListButtons = () => {
        decreaseALB(errorState, setErrorMessage).then(res => {
            if(res) {
                
                window.location.reload();
            }
        });

    }
    
 //   console.log("list",aList)

    var actions = new Array(numberALists)
    for (let i = 0; i < numberALists; i++) {
        actions[i] = i;
    }

    const errorState = () => {
       setError(current => !current)
      }
      
    const namePos= () => {
        setNamePosition(current => !current)
    }
    const nameSaved= () => {
        setNameSave(current => !current)
    }
   
    const startedLogging = () => {
      setIsStarted(current => !current)
    }
    if(!running) {
        running = true
        StartRequest(errorState, setErrorMessage)
    }
    StartRequest(errorState, setErrorMessage)

    return ( 
        <div >
            <LoggerButton state={started} action={startedLogging} stoped={nameSaved} errorfunction={errorState} errorMessage={setErrorMessage}/>
            <h1 className="header">
                <div className='flexbox'>
                
                <EmergencyExit errorfunction={errorState} errorMessage={setErrorMessage}/>
                <ResetButton forErrors={errorState} errorMessage={setErrorMessage}/>
                <SavePositionButton action={namePos}/>
                <GrippperButton forErrors={errorState} errorMessage={setErrorMessage}/>
                <ModeButton forErrors={errorState} errorMessage={setErrorMessage}/>
                </div>
                
                {
                    actions.map((index) => {
                        console.log("test",index)
                        return <ActionListButton index = {index} list= {aList[index]}errorfunction={errorState} errorMessage={setErrorMessage}/>
                    })
                }
                <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
                onClick={(increaseListButtons)}>
                    <i className="material-icons">add</i>
                </button> 
                <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
                onClick={decreaseListButtons}>
                    <i className="material-icons">remove</i>
                </button>
            </h1>

            <NamingPopUp active = {namePosition} deactivate={namePos} forErrors={errorState}
            confirm={informSavePosition} getBaseName={BaseNamePosition} errorMessage={setErrorMessage}/>

            <NamingPopUp active = {nameSave} deactivate={nameSaved} forErrors={errorState}
            confirm={postLoggingStop} getBaseName={BaseNameStop} errorMessage={setErrorMessage} started = {startedLogging}/>

            <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
        </div>
     );
}
 
export default ControlPage;





async function increaseALB(errorFunktion, setErrorMessage){
    var message =  new Map()
    message.set("marker", "increase_shortcuts")
    var reload = false
    const result = Object.fromEntries(message)
    await post(result, postAdressIncALB).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorFunktion()
            console.log(1)
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

  }


  async function decreaseALB(errorFunktion, setErrorMessage){
    var message =  new Map()
    message.set("marker", "decrease_shortcuts")
    var reload = false
    const result = Object.fromEntries(message)
    await post(result, postAdressDecALB).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorFunktion()
            console.log(1)
            reload = false
        }
      else {
       reload = true
      }
    })

    return reload

  }