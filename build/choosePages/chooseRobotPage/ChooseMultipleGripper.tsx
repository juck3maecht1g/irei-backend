import React from 'react'
import {useState} from 'react'
import { GetGripperRobots, GetExpRobots } from '../../backendComunication/FetchRobots';
import { SetChangeGripperRobots } from '../../backendComunication/SetRobots';
import ChooseButton from '../ChooseRobotButton';
import { ErrorPopUp } from '../../PopUp/ErrorPopUP';
import { Link } from 'react-router-dom';
import TopBar from '../../TopBar';
import './../../theme.css'
import './../../irei_styles.css'

export default function ChooseMultipleGripper (props) {
    const [errorMessage, setErrorMessage] = useState("sorry robots couldnt be changed")
    const [error, setError] = useState(false)
    const errorState = () => {
        setError(current => !current)
    }

    const [possibleRobots, setPossibleRobots] = useState (new Map<string, string>()); 
    GetExpRobots(setPossibleRobots);

    const [prechosen, setPreChosen] = useState (new Map<string, string>());
    GetGripperRobots(setPreChosen);

    const arrPossible = Array.from(possibleRobots, function (entry) {
        return { key: entry[1], value: entry[0]};
    });

    var chosen = new Map<string, string>() // the chosen robots 

    const clickedBot = (ip, name) => {
        if (chosen.has(ip))  {
            chosen.delete(ip)
        } else {
            chosen.set(ip,name)
        }
    }

    const buttons = arrPossible.map((number) => {
        var chosen = false;
        console.log(number.key)
        if (prechosen.get(number.key)) {
            console.log(number.key)
            chosen = true;
        }
        return <ChooseButton name={number.key} 
        ip = {number.value} 
        state = {chosen}
        action = {clickedBot}/>
      })

    const confirm = () => {
        SetChangeGripperRobots(errorState, chosen, setErrorMessage);
    }

    return (
        <div>
            <TopBar title="Choose Gripper Robots"></TopBar>
            {buttons}
            <Link to = {"/Controlpage"}>
            <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
             onClick = {confirm}>
                <i className="material-icons">check</i>
             </button>
            </Link>
            <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
        </div>
    )
} 

/* // nur zum testen muss noch gelöscht werden
var test = new Map();
test.set("123.234.346", "clara")
test.set("985.234.346", "andre")
test.set("444.234.466", "tessa")
test.set("333.356.875", "hannah")
test.set("875.356.234", "julie")
test.set("024.444.346", "dominik")

var test2 = new Map();
test2.set("123.234.346", "clara")
test2.set("985.234.346", "andre")
test2.set("444.234.466", "tessa")
test2.set("333.356.875", "hannah")
*/