import React from 'react';
import { TopBarActionCreate } from '../../../TopBar';
import { Link } from 'react-router-dom';


/**
 * The ActionKindPage is the page where the user chooses the kind of a new action
 */
export default function ActionKindPage (props) {

    return ( 
        <div className='choose-flexbox'>
            <TopBarActionCreate title="Choose action kind"/>
            
            <Link 
              to = {"/ChooseRobot"}
              state = {{action: "open_gripper", link:"/ActionListPage"}}>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                <i className='material-icons'>unfold_more</i>gripper open
                </button>
            </Link>
            <Link to = {"/ChooseRobot"}
                  state = {{ action: "close_gripper", link:"/ActionListPage"}}>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                <i className='material-icons'>unfold_less</i>gripper close
                </button>
            </Link>
            <Link to = {"/ChooseRobot"}
                  state = {{ action: "move", link:"/ChooseVariablePage"}}>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                <i className='material-icons'>gamepad</i>steering
                </button>
            </Link>
            <Link to = {"/ChooseRobot"}
                  state = {{ action: "wait", link:"/SetTimePage"}}>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                <i className='material-icons'>pause</i>wait
                </button>
            </Link>
            <Link to = {"/ChooseRobot"} 
                  state = {{ action: "custom", link:"/SetCustomPage"}}>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                <i className='material-icons'>tune</i>Custom
                </button>
            </Link>
            <Link to = {"/AddList"}>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                <i className='material-icons'>list</i>actionlist
                </button>
            </Link>
        </div>
     );
}

