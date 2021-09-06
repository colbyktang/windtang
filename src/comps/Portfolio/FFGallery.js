import React from 'react';
import App from '../../App';
import {Link} from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Container } from 'react-bootstrap';

export default function FFGallery() {
    return (
        <Container>
            <Link to="/"><Button>Home</Button></Link>
            <App/>
        </Container>
    )
}