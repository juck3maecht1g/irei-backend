import React from "react";
import ReactDom from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ControlPage from "./controlPage/ControlPage";

export default function App (){
    return (
      <div>
        <BrowserRouter>
        <Routes >
          <Route index element={<ControlPage />} />
        </Routes>
      </BrowserRouter>
      </div>
      
    )
}


ReactDom.render(
    <App /> , document.getElementById("root"));