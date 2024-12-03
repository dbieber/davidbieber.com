import React from 'react';
import { createRoot } from 'react-dom/client';
import TaylorSeriesPlot from './taylor-series.jsx';

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('root');
    if (container) {
        const root = createRoot(container);
        root.render(React.createElement(TaylorSeriesPlot));
    }
});
