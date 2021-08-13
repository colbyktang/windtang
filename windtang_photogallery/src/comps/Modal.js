import React from 'react';
import {motion} from 'framer-motion'

const Modal = ({selectedImg, setSelectedImg}) => {
    
    const handleClick = (e) => {
        // Checks to see if you're clicking on the picture or the backdrop
        if (e.target.classList.contains('backdrop')) {
            setSelectedImg(null);
        }
    }

    return <motion.div className="backdrop" onClick={handleClick}
        initial= {{opacity: 0}}
        animate= {{opacity: 1}}
    >
        <motion.img src ={selectedImg} alt="full pic"
            initial={{y: "-100vh"}}
            animate={{y: 0}}
        />
    </motion.div>
}

export default Modal;