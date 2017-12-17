import React, {Component} from 'react';
import ReactDOM from 'react-dom';

export default class Hello extends Component{
    constructor(){
        super();
    }
    render(){
        return(
            <div>Hello</div>

        )

    }
}

ReactDOM.render(<Hello/>,document.getElementById('container'))