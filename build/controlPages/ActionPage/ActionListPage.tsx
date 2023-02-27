import React from 'react';
import {useState} from 'react';
import { TopBarChooseList } from '../../TopBar';
import ActionlistButton from './ActionlistButton';
import { Link, useNavigate } from 'react-router-dom';
import '../../irei_styles.css'
import { GetActionListContent, DeleteAction, SetMappingPos } from './ActionFetch';

/**
 * The ActionListPage is used to edit a list of actions by adding new action and deleting others
 */
export default function ActionListPage () {
    var navigate = useNavigate()
    const [errorMessage, setErrorMessage] = useState("sorry robots couldnt be changed")
    const [error, setError] = useState(false)
    const errorState = () => {
        setError(current => !current)
    }
    const sentPos = (index) => {
        SetMappingPos(index, errorState, setErrorMessage).then(res => {
            if (res) {
                navigate("/MappingRobotsPage")
            }
        })
    }
    
    const [actionlist, setActionlist] = useState(test); //test
    GetActionListContent(setActionlist)
    console.log(actionlist)
    const deleteAction = (position) => {
        DeleteAction(errorState, position, setErrorMessage).then(res => {
            if(res) {
                window.location.reload();
            }
        });
    }
    
    return ( 
        
        <div>
        <div className="test">
            <TopBarChooseList title="Actionlist" />
                <Link to={"/MappingRobotsPage"}
                    state = {{index: [-1]}}>
                    <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick={() => {sentPos([-1])}}>
                        edit mapping
                    </button>
                </Link>
            {
                actionlist.map((currElement, index) => {
                    var listIndex = [index];
                    return <div className="action-list-grid">
                        <ActionlistButton key={index} element={currElement} listPlace={listIndex}/>
                        <button onClick={() =>deleteAction(index)} className="icon-button  mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                            <i className="material-icons">delete</i>
                        </button>
                    </div>
                })
            }
        
            <Link to = {"/ActionKindPage"}>
                <button className="icon-button  mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                <i className="material-icons">playlist_add</i>
                </button>
            </Link>
        
            
        </div>
            <div>
                <Link to = {"/ControlPage"}>
                    <button className="irei-back-button icon-button  mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
                    <i className="material-icons">arrow_back</i>
                    </button>
                </Link>
            </div>
        </div>

     );
}


var position = new Map()
    position.set("name", "bett")
     position.set("coordinates", new Map([["?????", 234634]]))
var robot = new Map ()
    robot.set("name", "bot1")
     robot.set("ip", 1)
var closeGripper = new Map()
    closeGripper.set("key", "close_gripper")
     closeGripper.set("robots", [robot])
var openGripper = new Map()
    openGripper.set("key", "open_gripper")
     openGripper.set("robots", [robot])   
var custom = new Map()
    custom.set("key", "custom"); custom.set("robots", [robot])
    custom.set("action", "tischtennis")
var wait = new Map()
    wait.set("key", "wait"); wait.set("robots", [robot]); wait.set("time", 1235)
var move = new Map()
    move.set("key", "move"); move.set("robots", [robot]); move.set("position", position)
var sList = new Map()
    sList.set("key", "sequential_list");sList.set("name", "kochen"); sList.set("content", [closeGripper, openGripper])
var pList = new Map()
    pList.set("key", "parallel_list"); pList.set("name", "backen"); pList.set("content", [closeGripper, openGripper, sList])

    var test = [closeGripper]
    test.push(openGripper); test.push(custom); test.push(wait); test.push(move); test.push(sList); test.push(pList)
    