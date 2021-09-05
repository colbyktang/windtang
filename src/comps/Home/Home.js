import React from 'react';
import Logout from '../Login/Logout';
import {Link} from 'react-router-dom';
import useToken from '../App/useToken';

export default function Home() {
    const { token } = useToken();

    if (!token) {
        return (
            <div className="home">
                <Link to="/dashboard">Login</Link>
                <br/>
                <a href="./html/tang_portfolio.html">Sample Portfolio</a>
            </div>
        )   
    }
    else {
        return (
            <div className="home">
                <Logout/>
                <Link to="/dashboard">Dashboard</Link>
                <br/>
                <a href="./html/tang_portfolio.html">Sample Portfolio</a>
            </div>
        )
    }


}