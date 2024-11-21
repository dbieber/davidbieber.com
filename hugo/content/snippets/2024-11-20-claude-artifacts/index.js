import React from 'react';
import { createRoot } from 'react-dom/client';
import JellybeanJar from './JellybeanJar.jsx';

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('jellybean-container');
    if (container) {
        const root = createRoot(container);
        root.render(React.createElement(JellybeanJar));
    }
});
