import React, { useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { GetExpRobots } from '../../../backendComunication/FetchRobots';
import { TopBarActionCreate } from '../../../TopBar';
import {appendAction} from '../ActionFetch';
import './../../../theme.css'
import './../../../irei_styles.css'

/**
 * The ChooserobotPage is used to choose the robots
 * the user wants to work with
 */
export default function ChooseRobotPage(props){
  
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState("sorry robots couldnt be changed")
  const [error, setError] = useState(false)
  const errorState = () => {
      setError(current => !current)
  }
 
    const location = useLocation();
    const {action} = location.state;
    const {link} = location.state;
    const sentToBackend = (ip) => {
      if (link === "/ActionListPage") {
        var help = new Map();
        help.set("key", action);
        // dirty
        var ipList = [ip]
        help.set("robot", ipList)
        appendAction(errorState, help, setErrorMessage).then(res => {
          if(res) {  navigate(link, { state: {kind: props.actionKind, ip: [props.data_key]} });
      window.location.reload();}
        });
      }
      else {
        // console.log("STUFF", {state: {kind: props.actionKind, ip: [props.data_key]}}, link)
        // navigate(link,{state: {kind: props.actionKind, ip: [props.data_key]} })
      }
    
    }

    var [robots, setRobots] = useState(test);  //new Map<string, string>()); 
    GetExpRobots(setRobots)

    const arrRobots = Array.from(robots, function (entry) {
      return { key: entry[0], value: entry[1]};
    });

    const buttons = arrRobots.map((number) => {
      return <RobotButton key={number.key}
      data_key= {number.key} 
      name= {number.value}
      actionKind={action}
      linkTo={link}
      action={sentToBackend}/>
    })

    return (
      <div>
        <TopBarActionCreate title="Choose Robot"/>
        <div className='choose-flexbox'>
        {buttons}
        </div>
      </div>
    )
}

/**
 * The RobotButton is used to choose 
 * the Robot which is displayed from this Button
 */
function RobotButton (props) {
  console.log("link", props.linkTo)
  return ( 
    <Link to = {props.linkTo}
    state = {{kind: props.actionKind, ip: [props.data_key]}}>
    <button onClick = {() => props.action(props.data_key)}
        className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
          <div>{props.name}</div>
          <div>{props.data_key}</div>
    </button>
    </Link>
   );
}


var test = new Map();
test.set("123.234.346", "ckara")
test.set("985.234.346", "andre")
test.set("444.234.466", "tessa")
test.set("333.356.346", "hannah")
