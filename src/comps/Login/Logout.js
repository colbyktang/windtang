import React from 'react';
import {Link} from 'react-router-dom';
import { useHistory } from 'react-router'

export default function Logout() {
    const history = useHistory();

    const handleLogOut = () => {
        localStorage.removeItem('token');
        console.log("Token removed!");
        history.go(0);
        
    }

    const doesTokenExist = () => {
        return localStorage.getItem('token') != null;
    }

    if (!doesTokenExist) {
        return null;
    }
    
    return (
        <div className="logout">
            <Link to="/">
                <button onClick={handleLogOut}>Log Out</button>
            </Link>
        </div>
    )
}