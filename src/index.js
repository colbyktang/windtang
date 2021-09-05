import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';
import Home from './comps/Home/Home';
import Dashboard from './comps/Dashboard/Dashboard';
import Preferences from './comps/Preferences/Preferences';
import SamplePortfolio from './comps/Portfolio/SamplePortfolio';

ReactDOM.render(
    <React.StrictMode>
        <BrowserRouter>
            <Switch>
                <Route exact path="/">

                    <Home />
                    <App />
                </Route>
                <Route path="/dashboard">
                    <Dashboard/>
                    <App />
                </Route>
                <Route path="/preferences">
                    <Preferences/>
                </Route>
                <Route path="/sampleportfolio">
                    <SamplePortfolio/>
                </Route>
            </Switch>
        </BrowserRouter>
    </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA