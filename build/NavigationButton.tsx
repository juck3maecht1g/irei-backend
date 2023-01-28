import React from 'react'
import { Link } from 'react-router-dom';

class NavigationButton extends React.Component {
   
    constructor(props) {
        super(props);
    }
    location = null
    state = {  }
    render() { 
        return ( 
            <Link to={this.location}>
            <button></button>
            </Link>
         );
    }
}
 
export default NavigationButton;