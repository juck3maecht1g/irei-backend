import React from "react";
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom"
import ControlPage from "./controlPages/ControlPage"

import ChooseDirectoryPage from "./choosePages/chooseDirectoryPage/ChooseDirectoryPage"
import ChooseLaboratoryPage from "./choosePages/chooseLaboratoryPage/ChooseLaboratoryPage"
import ChooseExperimentRobots from "./choosePages/chooseLaboratoryPage/ChooseExperimentRobots";
import ChooseExperimentRegistered from "./choosePages/chooseLaboratoryPage/ChooseExperimentRegistered";

import ActionListPage from "./controlPages/ActionPage/ActionListPage";
import ChooseListPage from "./controlPages/ActionPage/ChooseListPage";
import ChooseMultipleGripper from "./choosePages/chooseRobotPage/ChooseMultipleGripper";
import RobotPositionPage from "./choosePages/chooseRobotPage/RobotPositionPage";

import MappingRobotsPage from "./choosePages/chooseRobotPage/MappingRobots";

import ChooseVariablePage from "./controlPages/ActionPage/actionkind/ChooseVariablePage";
import ChooseRobotPage from "./controlPages/ActionPage/actionkind/ChooseRobotPage";
import SetTimePage from "./controlPages/ActionPage/actionkind/SetTimePage";
import SetCustomPage from "./controlPages/ActionPage/actionkind/SetCustomPage";
import ChooseActionlistAsAction from "./controlPages/ActionPage/actionkind/ChooseActionlistAsAction";

import Settings from "./settings/Settings"
import ActionKindPage from "./controlPages/ActionPage/actionkind/ActionKindPage";
import BackButton from "./BackButton";

export default function App (){

  return (

    <div>
      <BrowserRouter>
        <Routes >
          <Route element = {<BackButton />}>
          <Route path="/ActionKindPage" element={<ActionKindPage/>} /> 
            <Route path="/ChooseListPage" element={<ChooseListPage/>} />
            <Route path="/MappingRobotsPage" element={<MappingRobotsPage/>} />
            <Route path="/ChooseRobot" element={<ChooseRobotPage/>} />
            <Route path="/ChooseVariablePage" element={<ChooseVariablePage/>} />
            <Route path="/SetTimePage" element={<SetTimePage/>} />
            <Route path="/SetCustomPage" element={<SetCustomPage/>} />
            <Route path="/AddList" element={<ChooseActionlistAsAction/>} />

            <Route path="/ChooseLaboratoryPage" element={<ChooseLaboratoryPage/>} />
            <Route path="/ChooseExperimentRobots" element={<ChooseExperimentRobots/>} />
            <Route path="/ChooseExperimentRegister" element={<ChooseExperimentRegistered/>} />
            <Route path="/GripperRobots" element={<ChooseMultipleGripper/>} />
            <Route path="/SavePositionRobot" element={<RobotPositionPage/>} />
          </Route>
          
          <Route index element={<ChooseDirectoryPage/>} />
          <Route path="/ControlPage" element={<ControlPage/>} />

          <Route path="/Settings" element={<Settings/>} />

          <Route path="/ActionListPage" element={<ActionListPage/>} />


        </Routes>
      </BrowserRouter>
    </div>
    
  )

}


const domNode = document.getElementById("root");
const root = createRoot(domNode);
root.render(<App />);