import React, { useState } from 'react';
import Title from './comps/Title';
import ImageGrid from './comps/ImageGrid';
import Modal from './comps/Modal';
import { motion } from 'framer-motion';
import {Link} from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap';

function App() {
    const [selectedImg, setSelectedImg] = useState(null)

    return (
        <motion.div className="App">
            <Link to="/"><Button>Home</Button></Link>
            <Title />
            <ImageGrid setSelectedImg={setSelectedImg} />
            {selectedImg && (
            <Modal selectedImg={selectedImg} setSelectedImg={setSelectedImg} />
            )}
        </motion.div>
    )
}

export default App
