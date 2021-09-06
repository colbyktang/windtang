import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Alert, Button, Form, Container, Row, Col } from 'react-bootstrap';

async function loginUser (credentials) {
    return fetch('http://localhost:4112/api/cs/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })
        .then(data => data.json())
        .catch(err => {
            console.error ("Login failed!", err);
        });
}

export default function Login({setToken}) {
    const [username, setUserName] = useState();
    const [password, setPassword] = useState();
    const [show, setShow] = useState(false);

    const handleSubmit = async e => {
        e.preventDefault();
        console.log("Handle Submit");
        const token = await loginUser({
            username,
            password
        });
        if (!token) {
            setShow(true);
        }
        else {
            setToken(token);
        }
    }

    return (
        <Container className="dashboard">
            <Row>
                <Col style={{ height: '75px' }}>
                    <Link to="/"><Button>Return to Home</Button></Link>
                </Col>
            </Row>
            <Row className="justify-content-md-center">
                { 
                    show &&
                    <Alert variant="danger" onClose={() => setShow(false)} dismissible>
                    <Alert.Heading>Oh snap! You got an error!</Alert.Heading>
                    <p>
                        Something went wrong with the login!
                    </p>
                    </Alert>
                }
                <Col xs={12} sm={4} md={4}>
                <h2>Log In</h2>
                <Form onSubmit={handleSubmit}>
                    <Row>
                        <Col style={{ height: '75px' }}>
                            <Form.Control placeholder="Username" onChange={e => setUserName(e.target.value)}/>
                        </Col>
                    </Row>
                    <Row>
                        <Col style={{ height: '75px' }}>
                            <Form.Control type="password" placeholder="Password" onChange={e => setPassword(e.target.value)}/>
                        </Col>
                    </Row>
                    <Row>
                        <Col style={{ height: '75px' }}>
                            <Button type="submit" variant="primary">Submit</Button>{' '}
                        </Col>
                    </Row>
                </Form>
                </Col>
            </Row>
        </Container>
    )
}

Login.propTypes = {
    setToken: PropTypes.func.isRequired
}