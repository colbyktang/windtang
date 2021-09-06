import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

async function loginUser (credentials) {
    return fetch('http://localhost:4112/api/cs/login'
    .catch(err => console.log("error!")), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })
        .then(data => data.json())
}

export default function Login({setToken}) {
    const [username, setUserName] = useState();
    const [password, setPassword] = useState();

    const handleSubmit = async e => {
        e.preventDefault();
        console.log("Handle Submit");
        const token = await loginUser({
            username,
            password
        });
        setToken(token);
    }

    return (
        <div className="login">
            <form className="login-wrapper" onSubmit={handleSubmit}>
                <div className="login-box">
                    <Link to="/">Home</Link>
                    <h1>Please Log In</h1>
                    <p>Username</p>
                    <input type="text" onChange={e => setUserName(e.target.value)}/>
                    <p>Password</p>
                    <input type="password" onChange={e => setPassword(e.target.value)}/>
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

Login.propTypes = {
    setToken: PropTypes.func.isRequired
}