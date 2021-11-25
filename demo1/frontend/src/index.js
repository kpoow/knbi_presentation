import logo from './logo.png';
import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import './index.css';

function Square(props){
    return(
        <button className="button" onClick={props.onClick}>
            {props.name}
        </button>
    );      

}



class Board extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            buttons: Array(3).fill(null),
            information: ''
        };
    }

    handleClick(name){
        const metroCode = {
            Amsterdam: 'AM',
            Warsaw: 'WA',
            Dallas: 'DA'
        }
        console.log(metroCode[name])
        const buttons = this.state.buttons;
        axios.post("http://127.0.0.1:5001/router",{'url':'https://uatapi.equinix.com/fabric/v4/metros/'+metroCode[name],'method':'get','metro_code':metroCode[name]})
            .then((response) =>{
                console.log('Status set to ', response.data);
                this.setState({
                    buttons: buttons,
                    information: JSON.stringify(response.data,null,"\t")
                });
            });
        }
        

    renderButton(name){
        return(<Square name={name} onClick={() => this.handleClick(name)}/>);
    }

    render(){
        let status = this.state.information;
        return(
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                </header>
                <div>
                    <p>
                        IBX locations - check connected metros 
                    </p>
                </div> 
                <div>
                    {this.renderButton('Amsterdam')}
                    {this.renderButton('Warsaw')}
                    {this.renderButton('Dallas')}    
                </div>   
                <p>{status}</p>
            </div>   
        );
    }
}




ReactDOM.render(
<Board />, document.getElementById('root')
);
