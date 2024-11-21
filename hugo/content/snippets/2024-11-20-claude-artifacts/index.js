import React from 'react';
import { createRoot } from 'react-dom/client';
import JellybeanJar from './JellybeanJar.jsx';

console.log('Jellybean script loaded');

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('jellybean-container');
    console.log('Container found:', container);
    if (container) {
        const root = createRoot(container);
        console.log('Created root');
        root.render(React.createElement(JellybeanJar));
        console.log('Rendered JellybeanJar');
    }
});