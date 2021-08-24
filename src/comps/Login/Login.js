import React, { useState } from 'react';
import PropTypes from 'prop-types';

async function loginUser (credentials) {
    return fetch('http://localhost:4112/api/cs/login', {
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
        <form onSubmit={handleSubmit}>
            <h1>Please Log In</h1>
            <label className="login">
                <p>Username</p>
                <input type="text" onChange={e => setUserName(e.target.value)}/>
            </label>
            <label className="login">
                <p>Password</p>
                <input type="password" onChange={e => setPassword(e.target.value)}/>
            </label>
            <div>
                <button type="submit">Submit</button>
            </div>
        </form>
    )
}

Login.propTypes = {
    setToken: PropTypes.func.isRequired
}