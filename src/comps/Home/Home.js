import React from 'react';
import Logout from '../Login/Logout';
import {Link} from 'react-router-dom';
import useToken from '../App/useToken';

import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Image, Container, Row, Col, Card } from 'react-bootstrap';

import card_github from '../../images/github_black_256.png';
import button_github from '../../images/github.png';

import card_portfolio from '../../images/windo.png';
import button_portfolio from '../../images/totoro_white_256.png';

import card_ffxiv from '../../images/ffxiv_pic.png';
import button_ffxiv from '../../images/ffxiv.png';

export default function Home() {
    const { token } = useToken();
    return (
        <Container className="home">
            { 
                token &&                     
                <Row className="justify-content-end">
                    <Logout/>
                </Row>
            }
            {
                !token &&
                <Row className="justify-content-md-end">
                    <Link to="/dashboard"><Button>Login</Button></Link>
                </Row>
            }
            <Row style={{ height: '100px'}}>
                <Col>
                    <h1>Windtang</h1>
                </Col>
            </Row>
            { 
                token &&
                <Row>
                    <Col className="justify-content-center">
                        <Link to="/dashboard"><Button>Dashboard</Button></Link>
                    </Col>
                </Row>
            }

            <Row className="cards-flex">
                <Card style={{ backgroundColor: 'white', width: '18rem' }}>
                    <Card.Img variant="top" src={card_github} roundedCircle/>
                    <Card.Body>
                        <Card.Title>Github</Card.Title>
                        <Card.Text>
                            A portfolio of personal software projects I've developed.
                        </Card.Text>
                        <Button href="https://github.com/colbyktang">Visit <Image src={button_github} rounded/></Button>
                    </Card.Body>
                </Card>
                <Card style={{ backgroundColor: 'white', width: '18rem' }}>
                    <Card.Img variant="top" src={card_portfolio} roundedCircle/>
                    <Card.Body>
                        <Card.Title>Digital Media Gallery</Card.Title>
                        <Card.Text>
                            An HTML webpage designed for my Digital Media course back at St. Edward's University.
                        </Card.Text>
                        <Button href="/html/tang_portfolio.html">View <Image style={{height:'32px'}} src={button_portfolio} rounded/></Button>
                    </Card.Body>
                </Card>
                <Card style={{ backgroundColor: 'white', width: '18rem' }}>
                    <Card.Img variant="top" src={card_ffxiv} roundedCircle/>
                    <Card.Body>
                        <Card.Title>FFXIV Album</Card.Title>
                        <Card.Text>
                            A collection of screenshots from Final Fantasy XIV Online. Taken by Windcat Kirisame.
                        </Card.Text>
                        <Link to="/FFGallery"><Button>View <Image style={{height:'32px'}} src={button_ffxiv} rounded/></Button></Link>
                    </Card.Body>
                </Card>
            </Row>
        </Container>
    )
}