import React, { useState } from 'react'
import { Link, } from 'react-router-dom';
import { GetExpRobots } from '../../backendComunication/FetchRobots';
import '../../irei_styles.css'

/**
 * The ChooserobotPage is used to choose the robots
 * the user wants to work with
 */
export default function ChooseRobotsForMappingPage(props){

    var [robots, setRobots] = useState(new Map());

    GetExpRobots(setRobots)
    //GetExpRobots(setRobots)

    const arrRobots = Array.from(robots, function (entry) {
      return { key: entry[0], value: entry[1]};
    });

    const handleClick = (ip) => {
        props.execute( ip)
    }

    const buttons = arrRobots.map((number) => {
      return <div>
        <RobotButton key={number.key}
      data_key= {number.key} 
      name= {number.value} 
      execute = {handleClick}/>
      </div>
    })

    return (
      <div>
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
  <button onClick = {() => props.execute(props.data_key)}
  className="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
    <div>{props.data_key} {props.name}</div>
  </button>
   );
}

/*
const help = new Map();
help.set("123.123.234", "julie")
help.set("673.986.638", "maja")
help.set("894.234.467", "dominik")
help.set("235.474.458", "niclas")
help.set("777.345.658", "jule")
help.set("346.346.476", "andre")*/