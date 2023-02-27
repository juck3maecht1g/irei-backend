import React, { useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { GetExpRobots } from '../../backendComunication/FetchRobots';
import TopBar from '../../TopBar';
import { SetSavePositionRobot } from '../../backendComunication/SetRobots';

/**
 * The ChooserobotPage is used to choose the robots
 * the user wants to work with
 */
export default function RobotPositionPage(props){
  var navigate = useNavigate()
  const [errorMessage, setErrorMessage] = useState("sorry position could not be saved")
  const [error, setError] = useState(false)
  const errorState = () => {
      setError(current => !current)
    }

    const changerobots = (ip) => {
      console.log("hi")
      SetSavePositionRobot(errorState, ip, setErrorMessage).then(res => {
        if(res){
          navigate("/Controlpage")
        }
      })
    }

    var [robots, setRobots] = useState(test); //new Map<string, string>()
    GetExpRobots(setRobots)

    const arrRobots = Array.from(robots, function (entry) {
      return { key: entry[0], value: entry[1]};
    });

    const buttons = arrRobots.map((number) => {
      return <RobotButton key={number.key} data_key={number.key} name= {number.value} execute={changerobots}/>
    })

    return (
      <div className='choose-flexbox'>
        <TopBar title="Choose Robot"/>
        {buttons}
      </div>
    )
}

/**
 * The RobotButton is used to choose 
 * the Robot which is displayed from this Button
 */
function RobotButton (props) {

  return (   // noch zurückschicken wenn Gripper
    
        <button onClick = {()=>props.execute(props.data_key)}
        className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
          <div>{props.name}</div>
          <div>{props.data_key}</div>
        </button>
  
   );
}

var test = new Map();
test.set("123.234.346", "clara")
test.set("985.234.346", "andre")
test.set("444.234.466", "tessa")
test.set("333.356.875", "hannah")
test.set("875.356.234", "julie")
test.set("024.444.346", "dominik")