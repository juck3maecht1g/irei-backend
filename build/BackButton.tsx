import React from 'react';
import { useNavigate } from "react-router-dom";
import { Outlet } from "react-router-dom";


export default function Layout () {
    return (
        <>
          <Outlet />
          <BackButton />
        </>
      );
}

function BackButton () {
    let navigate = useNavigate();
    return (
        <>
          <button className="irei-back-button icon-button mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"  
          onClick={() => navigate(-1)}><i className="material-icons">arrow_back</i></button>
        </>
    );
}