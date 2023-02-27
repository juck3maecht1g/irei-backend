import React from 'react';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getLabs, informLabChoise } from '../../backendComunication/FetchAndSetLab';
import { ErrorPopUp } from '../../PopUp/ErrorPopUP';
import TopBar from '../../TopBar';
import ChooseLaboratoryButton from './ChooseLaboratoryButton';
const fetchAdress = "http://127.0.0.1:5000/api/getLab";

/**
 * The ChooseLaboratoryPage is used to choose 
 * the Laboratory the user wants to work in
 */
export default function ChooseLaboratoryPage() {
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState("sorry something went wrong")
  const [error, setError] = useState(false)
    const [labs, setLabs] = useState(new Map<string, Map<string, string>>()); // key = labname, value = robot list
    var [fetched, setfetched] = useState(false)
    getLabs(setLabs, fetched, setfetched)

    const errorState = () => {
      setError(current => !current)
     }


    const arrLabs = Array.from(labs, function (entry) {
      return { key: entry[0], value: entry[1]};
    });


    const action = (name) => {  
      informLabChoise(errorState,name, setErrorMessage).then(res => {
      if(res) {
          
      }
  }
  )
    }

    const robots = (key) => {
     return Array.from(labs.get(key), function (entry) {
      return { key: entry[0], value: entry[1]}})
    }


       return ( 
      <div >
        <TopBar title="Choose Laboratory"></TopBar>
        <div className='choose-flexbox'>
        {
          arrLabs.map((number) => {
            return <ChooseLaboratoryButton name={number.key} action={action}
            buttons = {robots} />
          })
        }
        </div>
         <ErrorPopUp active={error} deactivate={errorState} message={errorMessage}/>
      </div>
    );
}

/**
 * //shema für labornamen 
    for (let key of labs.keys()) {
      console.log(key) //laborname
    }

    // shema um roboter namen zu kriegen
    for (let key of labs.keys()) {
      if(typeof labs.get(key) != "undefined") {
        for (let koy of labs.get(key).keys()) { // is catched one line above
          console.log(koy); // roboternamen
      }          
      }

    }
 */


   