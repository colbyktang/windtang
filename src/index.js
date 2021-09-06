import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from './comps/Home/Home';
import Dashboard from './comps/Dashboard/Dashboard';
import Preferences from './comps/Preferences/Preferences';
import FFGallery from './comps/Portfolio/FFGallery';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Form, Container, Row, Col } from 'react-bootstrap';

ReactDOM.render(
    <React.StrictMode>
            <BrowserRouter>
                <Switch>
                    <Container className="App">
                    <Route exact path="/">
                        <Row className="justify-content-center">
                            <Col>
                            <Home />
                            </Col>
                        </Row>
                    </Route>
                    <Route path="/dashboard">
                        <Row className="justify-content-center">
                            <Col>
                            <Dashboard/>
                            </Col>
                        </Row>
                    </Route>
                    <Route path="/preferences">
                        <Row className="justify-content-center">
                            <Col>
                            <Preferences/>
                            </Col>
                        </Row>
                    </Route>
                    <Route path="/FFGallery">
                        <FFGallery/>
                        <App/>
                    </Route>
                    </Container>
                </Switch>
            </BrowserRouter>
    </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA