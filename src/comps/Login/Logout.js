import React from 'react';
import {Link} from 'react-router-dom';
import { useHistory } from 'react-router'
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';

export default function Logout() {
    const history = useHistory();

    const handleLogOut = () => {
        localStorage.removeItem('token');
        console.log("Token removed!");
        window.location.href = "/";
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
                <Button onClick={handleLogOut}>Log Out</Button>
            </Link>
        </div>
    )
}