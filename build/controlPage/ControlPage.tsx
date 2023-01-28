import React from 'react'
import LoggerButton from './LoggerButton'
import GrippperButton from "./GripperButton"
import ResetButton from './ResetButton';
import SavePositionButton from './SavePositionButton';
//import ApproachPositionActionButton from '../ApproachPositionActionButton';

/**
 * The ControlPage is used to record an experiment
 * or to control Robots in the current scene
 */
class ControlPage extends React.Component {

    constructor(props) {
        super(props);
      }

    render() { 
        return ( 
            <div>
                <h1>
                    <ResetButton/>
                    <SavePositionButton/>
                    <GrippperButton/>
                    <LoggerButton state={false}/>
                </h1>
            </div>
         );
    }
}
 
export default ControlPage;