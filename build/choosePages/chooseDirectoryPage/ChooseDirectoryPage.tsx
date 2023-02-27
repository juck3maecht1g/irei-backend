import React from 'react'
import {useState} from 'react'
import { useNavigate } from 'react-router-dom';
import TopBar from '../../TopBar';
import DirectoryButton from './DirectoryButton';
import { GetDirectories, NavigateDown, NavigateUP, Create, DeleteDirectory, BaseNameDir, confirmDirChoise, GetPath, IsTop } from '../../backendComunication/FetchAndSetDirExp';
import { NamingPopUp } from '../../PopUp/NamingPopUp';
import { ErrorPopUp } from '../../PopUp/ErrorPopUP';
import './../../theme.css'
import './../../irei_styles.css'

/**
 * The ChooseDirectoryPage is used to navigate in a Datastructure
 * and choose a directory
 */
export default function ChooseDirectoryPage () {
    const navigate = useNavigate();
    const [directories, setDirectories] = useState(new Map<String,[]>());
    const [errorMessage, setErrorMessage] = useState("sorry something went wrong")
    const [error, setError] = useState(false)
    var [popUpName, setPopUpName] = useState(false);
    var [path, setPath] = useState("");
    GetDirectories(setDirectories);

    const errorState = () => {
        setError(current => !current)
       }

    const createDir = (action, name, setErrorMessage) => {
          Create(action, name, setErrorMessage).then(res => {
            if(res) {
                navigate("/ChooseLaboratoryPage")
            }
        }
        )
    }

    const navUp = () => {
        NavigateUP(errorState,setErrorMessage).then(res => {
            if(res) {
            window.location.reload()
            }
        })
    }

    const navDown = (name) => {
        NavigateDown( errorState, name, setErrorMessage).then(res => {
            if(res) {
            window.location.reload()
            }
        })
    }
    
    const confirmChoise = () => {
        confirmDirChoise(errorState, setErrorMessage).then(res => {
            if(res) {
                navigate("/ControlPage")
            }
        }
        )
    }

    const getPath = () => {
        GetPath(setPath)
    }
    getPath()

    const activatePopup = () => {
        setPopUpName(current => !current)
    }

    const [top, setTop] = useState(false)
    IsTop(setTop)

    const notTop = <div className="flexbox">
        <div>
            <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
            onClick = {()=> setPopUpName(true)}>
                <i className="material-icons">add</i>
            </button>
        </div>
        <div>
            <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
                        onClick = {navUp}>
                            navigate up
            </button>
        </div>
        <div>
            <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onClick={confirmChoise}>
                <i className="material-icons">check</i>
            </button>
        </div>
    </div>

    const isTop = <div className="flexbox">
        <div>
            <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
            onClick = {()=> setPopUpName(true)}>
                <i className="material-icons">add</i>
            </button>
        </div>
        <div>
            <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" disabled>
                            navigate up
            </button>
        </div>
        <div>
            <button className="icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" disabled>
                <i className="material-icons">check</i>
            </button>
        </div>
    </div>

    return ( 
        <div>
            <TopBar title="Choose Directory"></TopBar>
            <div >
                <div className="choose-flexbox">
                    {
                        directories.get("to_navigate")?.map((number) => {
                        return <DirectoryButton name={number} action={navDown}/>
                        })
                    }
                </div>
                <div className="grid directory-grid">
                    <div>
                        <p className="irei-path">
                            cwd: {path}
                        </p>
                    </div>
                </div>
                <div >
                    
                    {top? isTop:notTop}
                    <NamingPopUp active = {popUpName} deactivate={activatePopup} forErrors={errorState}
                        confirm={createDir} getBaseName={BaseNameDir} errorMessage={setErrorMessage}/>
                    <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
                    
                </div>
            </div>
            
        </div>
     );
}
