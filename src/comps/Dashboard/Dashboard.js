import React from 'react';
import Login from '../Login/Login';
import Logout from '../Login/Logout';
import useToken from '../App/useToken';
import {Link} from 'react-router-dom';
import UploadForm from '../UploadForm'
import App from '../../App';

import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Image, Container, Row, Col } from 'react-bootstrap';

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
            <Login setToken={setToken} />
        )
    }

    return (
        <Container className="dashboard">
            <Row>
                <Logout/>
                <h1>Windtang</h1>
            </Row>
            <Row>
                <h2>Dashboard</h2>
            </Row>
            <Row>
                <h3>Hello there, {getFirstName()} {getLastName()}!</h3>
            </Row>
            <Row className="align-items-center">
                <Col xs='auto' style={{ height: "100px" }} className="justify-content-md-start">
                    <Row md='auto'><Link to="/"><Button>Home</Button></Link></Row>
                    <Row md='auto'><Link to="/preferences"><Button>Preferences</Button></Link></Row>
                </Col>
                <Col lg={true} style={{ backgroundColor: 'white' }}>
                    <UploadForm />
                </Col>
            </Row>
            <App />
        </Container>
        
    );
}