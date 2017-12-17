import React, {Component} from 'react';
import Trip from "./trip"
import $ from 'jquery';

export default class App extends Component{
    constructor(){
        super();
        this.state = {
            trips:[]
        }
        this.getTrips = this.getTrips.bind(this);
    }
    componentDidMount(){
        this.getTrips();
    }
    render(){
        return(
          <div>
          hello
            { this.state.trips.map((trip,i) =>(
                <div key = {i}>
                    <Trip
                    trip = {this.state.trips[i]}/>
                </div>
            ))}
           </div>
        );
    }
    getTrips(){
        $.ajax( {
            url: "/api/",
            method: "GET",
            contentType: "application/json"
        } ).then((trips) => this.setState({trips:trips})).catch(
            (error) => {
            console.log(error)
        } )
    }
}