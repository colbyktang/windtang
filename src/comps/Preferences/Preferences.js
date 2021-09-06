import React from 'react';
import Login from '../Login/Login';
import Logout from '../Login/Logout';
import {Link} from 'react-router-dom';
import useToken from '../App/useToken';

import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Container, Row, Col } from 'react-bootstrap';

export default function Preferences () {

    const { token, setToken } = useToken();
    
    if (!token) {
        return (
            <Login setToken={setToken} />
        )
    }

    return (
        <Container className="preferences">
            <Row>
                <Logout/>
            </Row>
            <Row>
                <Col>
                    <h1>Windtang</h1>
                </Col>
            </Row>
            <Row>
                <h2>Preferences</h2>
            </Row>
            <Row>
                <h3>Work in Progress!</h3>
            </Row>
            <Row className="align-items-center">
                <Col xs='auto' style={{ height: "100px" }} className="justify-content-md-start">
                    <Row md='auto'><Link to="/"><Button>Home</Button></Link></Row>
                    <Row md='auto'><Link to="/Dashboard"><Button>Dashboard</Button></Link></Row>
                </Col>
                <Col lg={true} style={{ backgroundColor: 'white' }}>
                    
                </Col>
            </Row>
        </Container>
    );
}