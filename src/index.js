import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import UploadForm from './comps/UploadForm'

import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';
import Dashboard from './comps/Dashboard/Dashboard';
import Preferences from './comps/Preferences/Preferences';
import SamplePortfolio from './comps/Portfolio/SamplePortfolio';

ReactDOM.render(
  <React.StrictMode>
    
    <BrowserRouter>
        <Switch>
            <Route exact path="/">
                <h1>Application</h1>
                <Link to="/dashboard"><p>Dashboard</p></Link>
                <Link to="/sampleportfolio"><p>Sample Portfolio</p></Link>
                <App />
            </Route>
            <Route path="/dashboard">
                <Link to="/"><p>Home</p></Link>
                <Dashboard/>
                <Link to="/preferences"><p>Preferences</p></Link>
                <UploadForm />
                <App />
            </Route>
            <Route path="/preferences">
                <Link to="/"><p>Home</p></Link>
                <Preferences/>
                <Link to="/dashboard"><p>Dashboard</p></Link>
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