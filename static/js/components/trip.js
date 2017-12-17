import React, {Component} from 'react';

export default class Trip extends Component{
    render(){
        return(
         <div key={this.props.trip.title}>{this.props.trip.title}</div>
        )
    }

}