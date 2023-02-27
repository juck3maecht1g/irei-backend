import React from 'react';
import {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import { TopBarChooseList } from '../../TopBar';
import { GetActionListNames, SetActionList, CreatetActionList } from './ActionFetch';
import { NamingPopUp } from '../../PopUp/NamingPopUp';
import { ErrorPopUp } from '../../PopUp/ErrorPopUP';
import Popup from '../../PopUp/PopUp';
import './../../theme.css'
import './../../irei_styles.css'

/**
 * The ChooseListPage is used to choose an existing list of action 
 */
export default function ChooseListPage () {
    const navigate = useNavigate();
    const [errorMessage, setErrorMessage] = useState("sorry position could not be saved")
    const [error, setError] = useState(false)
    var [popUpNameActive, deactivatePopup] = useState(false);
    var [name, setName] = useState("");

    const saveName = (p1, pName, p3) => {
        setName(pName)
    }

    const errorState = () => {
        setError(current => !current)
       }

    const [lists, setList] = useState([]);
    GetActionListNames(setList)

    const sentChoiceBack = (name) => {
        SetActionList(errorState, name, setErrorMessage).then(res => {
            if(res) {
                navigate("/ActionListPage")
            }
        }); 
    }

    const buttons = lists.map((number) => {
        return  <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" 
        onClick ={() => sentChoiceBack(number)}>
        {number}
     </button>
    
     
    })

    const newList = ( kind) => {
        console.log(name)
        CreatetActionList(name, kind, errorState, setErrorMessage).then(res => {
            sentChoiceBack(name)
        })
       
    }

    return (
        <div>
            <TopBarChooseList title="Choose Action List"/>
            <div className='choose-flexbox'>
            {buttons}
            </div>
            <button onClick={()=>{deactivatePopup(true)}} className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"> 
                <i className='material-icons'>add</i>
            </button>
            <NamingPopUp active = {popUpNameActive} deactivate={()=>{deactivatePopup(false)}} forErrors={errorState}
                        confirm={saveName} getBaseName={(key)=>{return ""}} errorMessage={setErrorMessage}/>
            <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
            <Popup trigger={(name !== "")}>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick = {()=>{newList("parallel_list")}}>
                    parallel
                </button>
                <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick = {()=>{newList("sequential_list")}}>
                    sequential
                </button>
            </Popup>
        </div>
    )
}