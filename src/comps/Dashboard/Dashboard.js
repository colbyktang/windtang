import React from 'react';
import Login from '../Login/Login';
import Logout from '../Login/Logout';
import useToken from '../App/useToken';
import {Link} from 'react-router-dom';
import UploadForm from '../UploadForm'

export default function Dashboard() {
    const { token, setToken } = useToken();

    const getFirstName = () => {
        const tokenString = localStorage.getItem('token');
        const userToken = JSON.parse (tokenString);
        return userToken?.first_name;
    }

    const getLastName = () => {
        const tokenString = localStorage.getItem('token');
        const userToken = JSON.parse (tokenString);
        return userToken?.last_name;
    }

    if (!token) {
        return (
            <div className="dashboard">
                <Login setToken={setToken} />
            </div>
        )
    }

    return (
        <div className="dashboard">
            <Logout/>
            <h2>Dashboard</h2>
            <p>Hello there, {getFirstName()} {getLastName()}!</p>
            <Link to="/">Home</Link>
            <br/>
            <Link to="/preferences">Preferences</Link>
            <UploadForm />
        </div>
    );
}