import React from "react"
import {useState} from 'react';
import './theme.css'
import './irei_styles.css'
import 'material-icons'
import { Link } from "react-router-dom";
import NavigationButton from './NavigationButton';

function TopBar(props) {

  const [isActive, setIsActive] = useState(false);

  const handleClick = event => {
    // 👇️ toggle isActive state on click
    setIsActive(current => !current);
  };

  return(
    <div className ='bar'>
      <div className="title_wrapper">
        <p className="title">
          {props.title}
        </p> 
      </div>

      <div className='wrapper'>
        
        <button id="menu" className="mdl-button mdl-js-button mdl-button--icon" onClick={handleClick}>
          <i className="material-icons">more_vert</i>
        </button>

        <div id='nav-list-container'className= {isActive ? "mdl-menu__container is-visible" : "mdl-menu__container"}>
          <ul id="nav-list" className="mdl-menu__outline mdl-menu--bottom-right mdl-js-menu mdl-js-ripple-effect"
            htmlFor="menu">

            {/*<li className="mdl-menu__item nav-list-item">
              <Link to='/Control' state={{ from: "Burgermenu"}} //erst noch mit links maybe weg
                  className="">
                        wewrgetrztu
            </Link>
            </li>*/}

            {props.children}
          </ul>
        </div>

      </div>
      
    </div>
    
  )
}

export default TopBar

export function TopBarAll (props) {
    return (
        <TopBar title={props.title}>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Control" destinationLink="/ControlPage"></NavigationButton>
            </li>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Choose Directory" destinationLink="/"></NavigationButton>
            </li>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Choose Laboratory" destinationLink="/ChooseLaboratoryPage"></NavigationButton>
            </li>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Choose Experiment" destinationLink="/ChooseExperimentRegistered"></NavigationButton>
            </li>
            {/*<li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Settings" destinationLink="/Settings"></NavigationButton>
            </li>*/}
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Change Gripper Robots" destinationLink="/GripperRobots"></NavigationButton>
            </li>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Change Position Robot" destinationLink="/SavePositionRobot"></NavigationButton> 
            </li>
        </TopBar>
    )
}

export function TopBarControl (props) {
    return (
        <TopBar title={props.title}>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Choose Directory" destinationLink="/"></NavigationButton>
            </li>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Choose Laboratory" destinationLink="/ChooseLaboratoryPage"></NavigationButton>
            </li>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Choose Experiment" destinationLink="/ChooseExperimentRegistered"></NavigationButton>
            </li>
            {/*<li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Settings" destinationLink="/Settings"></NavigationButton>
            </li>*/}
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Change Gripper Robots" destinationLink="/GripperRobots"></NavigationButton>
            </li>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Change Position Robot" destinationLink="/SavePositionRobot"></NavigationButton> 
            </li>
        </TopBar>
    )
}

export function TopBarChooseList (props) {
    return (
        <TopBar title={props.title}>
            <li className="mdl-menu__item nav-list-item">
              <NavigationButton destination="Control" destinationLink="/ControlPage"></NavigationButton>
            </li>
        </TopBar>
    )
}

export function TopBarActionCreate (props) {
  return (
      <TopBar title={props.title}>
          <li className="mdl-menu__item nav-list-item">
            <NavigationButton destination="Control" destinationLink="/ControlPage"></NavigationButton>
          </li>
          <li className="mdl-menu__item nav-list-item">
            <NavigationButton destination="ActionList" destinationLink="/ActionListPage"></NavigationButton>
          </li>
      </TopBar>
  )
}