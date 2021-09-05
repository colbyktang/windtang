import React, { useState } from 'react'
import Title from './comps/Title'
import ImageGrid from './comps/ImageGrid'
import Modal from './comps/Modal'
import { motion } from 'framer-motion'

function App() {
    const [selectedImg, setSelectedImg] = useState(null)

    return (
        <motion.div className="App">
            <Title />
            <ImageGrid setSelectedImg={setSelectedImg} />
            {selectedImg && (
            <Modal selectedImg={selectedImg} setSelectedImg={setSelectedImg} />
            )}
        </motion.div>
    )
}

export default App
