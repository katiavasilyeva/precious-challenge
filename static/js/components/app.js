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
          <div className="container">
              <h1 className="text-center"> Adventure Trips   </h1>
                { this.state.trips.map((trip,i) =>(
                    <div key = {i} className=".col-md-4">
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