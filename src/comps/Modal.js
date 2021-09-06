import React from 'react';
import {motion} from 'framer-motion'
import { CloseButton } from 'react-bootstrap';

const Modal = ({selectedImg, setSelectedImg}) => {
    
    const handleClick = (e) => {
        // Checks to see if you're clicking on the picture or the close button
        if (e.target.classList.contains('backdrop') || e.target.classList.contains('sr-only')) {
            setSelectedImg(null);
        }
    }

    return <motion.div className="backdrop" onClick={handleClick}
        initial= {{opacity: 0}}
        animate= {{opacity: 1}}
    >
        <motion.img src ={selectedImg} alt="full pic"
            initial={{y: "-20vh"}}
            animate={{y: 0}}
        />
        <CloseButton onClick={handleClick} />
    </motion.div>
}

export default Modal;