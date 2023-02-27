import React from 'react';
import { Link } from 'react-router-dom';
import { informLabChoise } from '../../backendComunication/FetchAndSetLab';
import '../Choose.css';
import './../../theme.css'
import './../../irei_styles.css'

/**
 * The ChooseLaboratoryButton is used to choose 
 * the Laboratory which is displayed from this Button
 */
export default function ChooseLaboratoryButton (props) {

    const clicked = () => {
        props.action(props.name)
    }
  
    const roboter = (props.buttons(props.name))
   //   const [robots, setRobots] = useState(props.buttons(props.name))

    return ( 
        <Link
           to = {"/ChooseExperimentRobots"}
           state = {{from: roboter}}
        >
        <button className="irei-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
         onClick={clicked}>
            {props.name}
        </button>
        </Link>
     );
}