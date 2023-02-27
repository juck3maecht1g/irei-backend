import React from 'react';
import { useNavigate } from 'react-router-dom';
import { ExecuteActionList, SetButtonIndex } from './ActionPage/ActionFetch';
import './../irei_styles.css'

export default function ActionListButton (props) {
    const navigate = useNavigate();
    //const [actionlist, setActionList] = useState("")

    const execute = ()=> {
        informPosition()
        ExecuteActionList(props.list, props.errorfunction, props.errorMessage)

    }


    const edit = async () => {
        if(await informPosition()) {
            navigate("/ActionListPage")
        }
    }

    const swap = async () => {
        if(await informPosition()) {
            navigate("/ChooseListPage")
        }
    }

    const informPosition = async () => {
        var reload = false
        await SetButtonIndex(props.index, props.errorfunction, props.setErrorMessage).then(res => {
            reload = res
        })
        return reload
    }


    const disabledEdit = <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" disabled>
    <i className="material-icons">edit</i>
    </button>

    const editButton = <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick={edit}>
    <i className="material-icons">edit</i>
    </button>

    return (
        <div className="flexbox">
            <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" 
                onClick={execute}>
                <div>
                   {props.list}
                </div>
            </button>
            {props.list == "name"? disabledEdit:editButton}
            <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick={swap}>
                <i className="material-icons">settings</i> 
            </button>
          
        </div>
    )
}



/*
<button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" 
                    onClick={()=>setChoosing(true)}>
                    edit
            </button>

            <Popup trigger= {choosing}>
                <ChooseListPage execute={setActionList} close={informPosition}/>
            </Popup>
*/