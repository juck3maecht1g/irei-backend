import React from 'react';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useLocation } from "react-router-dom";
import {TopBarActionCreate} from '../../../TopBar';
import { SetCoordinateType, GetPositions, appendAction, GetCoordinates } from '../ActionFetch';


/**
 * The ChooseVariablePage is used to choose 
 * a variable for a robot to approach
 */
export default function ChooseVariablePage (props) {
    
    const navigate = useNavigate();
    const [errorMessage, setErrorMessage] = useState("sorry robots couldnt be changed")
    const [error, setError] = useState(false)
    const errorState = () => {
        setError(current => !current)
    }

    const location = useLocation();
    const { kind } = location.state;
    const { ip } = location.state;  

    const [arrayPosition, setPositions] = useState([ new Map()])

    GetCoordinates(setPositions).then(res => {
      
    })
   
    var [state, setState] = useState("joint");
    
    const changeType = () => {
        var send = state
        if (state === "cartesian") {
            setState("joint");
            send = "joint"
        } else {
            setState("cartesian");
            send = "cartesian"
        }
        console.log("here")
        SetCoordinateType(send, errorState, setErrorMessage);
        console.log("where")
        GetPositions(setPositions)
        console.log("done")
    }
    
    //const arrayPosition = Array.from( positions, function (entry) {
        //return { key: entry[0], value: entry[1]}})


    const buttons = arrayPosition.map((number) => {
        return  <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
        onClick = {() => {
            var help = new Map();
            help.set("key", kind);
            help.set("robot", ip);
            help.set("position", number.get("name"))
            appendAction(errorState, help, setErrorMessage).then(res => {
                if(res) {
                    navigate("/ActionListPage");
                    window.location.reload();
                }
            });
          
        } }>
          {number.get("name")}
          {"\n"}
          {number.get("coordinates")}
        </button>
    })

    const jointButton = <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick = {changeType}> joint </button>
    const cartButton = <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored" onClick = {changeType}> cartesian </button>

    return (
        <div>
            <TopBarActionCreate title="Choose Position" />
            {state==="joint"? jointButton:cartButton}
            { buttons}
        </div>
    );
}



// function PositionButton (props) {

//     const sent = () => {
//         var help = new Map();
//         help.set("key", props.kind);
//         help.set("robot", props.ip);
//         help.set("position", props.position)
//         appendAction(props.errorState, help, props.setErrorMessage);
//     } 
//     console.log("props", props)
//     return ( 
//     <Link to = {"/ActionListPage"}>
//       <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
//       onClick = {sent}>
//         {props.name}
//         {"\n"}
//         {props.position.get("values")}
//       </button>
//     </Link>
//      );
//   }