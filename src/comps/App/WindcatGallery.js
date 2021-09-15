import React from 'react';
import RUG from 'react-upload-gallery';

import 'react-upload-gallery/dist/style.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'react-bootstrap';

export default function WindcatGallery () {
    
    return (
        <Container>
            <Row style={{height: '100px'}}></Row>
            <RUG
                action="/api/upload" // upload route
                source={response => response.source} // response image source
            />
        </Container>
    )
}