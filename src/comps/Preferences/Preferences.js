import React from 'react';
import Logout from '../Login/Logout';
import {Link} from 'react-router-dom';

export default function Preferences () {
    return (
        <div className="preferences">
            <Logout/>
            <h2>Preferences</h2>
            <Link to="/">Home</Link>
            <br/>
            <Link to="/dashboard">Dashboard</Link>
            <p>Work in progress!</p>
        </div>
    );
}