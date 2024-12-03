import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';

const factorial = (n) => n === 0 ? 1 : n * factorial(n - 1);

const taylorSin = (x, n) => {
    let result = 0;
    for (let i = 0; i < n; i++) {
        const term = Math.pow(-1, i) * Math.pow(x, 2 * i + 1) / factorial(2 * i + 1);
        result += term;
    }
    return result;
};

const generateData = (n) => {
    const points = [];
    for (let x = -4; x <= 4; x += 0.1) {
        const xFixed = Number(x.toFixed(2));
        points.push({
            x: xFixed,
            sin: Math.sin(xFixed),
            taylor: taylorSin(xFixed, n)
        });
    }
    return points;
};

const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
        const x = Number(label);
        const sinValue = payload[0].value;
        const taylorValue = payload[1].value;
        const error = Math.abs(sinValue - taylorValue);
        
        return (
            <div className="bg-white p-2 border border-gray-300 rounded shadow">
                <p className="text-sm">x: {Number(x).toFixed(2)}</p>
                <p className="text-sm">sin(x): {sinValue.toFixed(3)}</p>
                <p className="text-sm">Taylor: {taylorValue.toFixed(3)}</p>
                <p className="text-sm">Error: {error.toFixed(3)}</p>
            </div>
        );
    }
    return null;
};

const TaylorPlot = ({ n, accuracyBound }) => {
    return (
        <div style={{ minWidth: '400px', height: '200px' }}>
            <ResponsiveContainer width="100%" height="100%">
                <LineChart data={generateData(n)} margin={{ top: 5, right: 5, bottom: 5, left: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis
                        dataKey="x"
                        type="number"
                        domain={[-4, 4]}
                        tickFormatter={(value) => value.toFixed(1)}
                    />
                    <YAxis
                        domain={[-2, 2]}
                        tickFormatter={(value) => value.toFixed(1)}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Legend />
                    <Line
                        type="monotone"
                        dataKey="sin"
                        stroke="#000000"
                        name="sin(x)"
                        dot={false}
                        isAnimationActive={false}
                    />
                    <Line
                        type="monotone"
                        dataKey="taylor"
                        stroke="#FF0000"
                        name={`Taylor (n=${n})`}
                        dot={false}
                        isAnimationActive={false}
                    />
                    <ReferenceLine x={accuracyBound} stroke="#0000FF" strokeDasharray="3 3" />
                    <ReferenceLine x={-accuracyBound} stroke="#0000FF" strokeDasharray="3 3" />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
};

const BoundPlot = () => {
    const boundData = [
        {n: 1, bound_0_1: 0.86, bound_0_01: 0.40, bound_0_001: 0.19},
        {n: 2, bound_0_1: 1.67, bound_0_01: 1.05, bound_0_001: 0.66},
        {n: 3, bound_0_1: 2.47, bound_0_01: 1.77, bound_0_001: 1.27},
        {n: 4, bound_0_1: 3.25, bound_0_01: 2.51, bound_0_001: 1.94},
        {n: 5, bound_0_1: 4.02, bound_0_01: 3.25, bound_0_001: 2.64},
        {n: 6, bound_0_1: 4.79, bound_0_01: 4.00, bound_0_001: 3.35},
        {n: 7, bound_0_1: 5.55, bound_0_01: 4.76, bound_0_001: 4.07},
        {n: 8, bound_0_1: 6.31, bound_0_01: 5.51, bound_0_001: 4.80},
        {n: 9, bound_0_1: 7.07, bound_0_01: 6.26, bound_0_001: 5.54},
        {n: 10, bound_0_1: 7.83, bound_0_01: 7.01, bound_0_001: 6.27}
    ];

    return (
        <div style={{ minWidth: '600px', height: '400px' }}>
            <ResponsiveContainer width="100%" height="100%">
                <LineChart 
                    data={boundData} 
                    margin={{ top: 20, right: 30, bottom: 50, left: 60 }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis
                        dataKey="n"
                        type="number"
                        domain={[1, 10]}
                        ticks={[1,2,3,4,5,6,7,8,9,10]}
                        label={{ 
                            value: 'Number of Terms (n)', 
                            position: 'insideBottom', 
                            offset: -12,
                            style: { textAnchor: 'middle' }
                        }}
                    />
                    <YAxis
                        label={{ 
                            value: 'Accuracy Bound', 
                            angle: -90, 
                            position: 'insideLeft', 
                            style: { textAnchor: 'middle' }
                        }}
                    />
                    <Tooltip />
                    <Legend 
                        verticalAlign="bottom"
                        wrapperStyle={{
                            bottom: 20,
                            marginLeft: 'auto',
                            marginRight: 'auto',
                            width: '100%',
                            textAlign: 'center'
                        }}
                    />
                    <Line
                        type="monotone"
                        dataKey="bound_0_1"
                        stroke="#FF0000"
                        name="ε = 0.1"
                        isAnimationActive={false}
                    />
                    <Line
                        type="monotone"
                        dataKey="bound_0_01"
                        stroke="#2196F3"
                        name="ε = 0.01"
                        isAnimationActive={false}
                    />
                    <Line
                        type="monotone"
                        dataKey="bound_0_001"
                        stroke="#4CAF50"
                        name="ε = 0.001"
                        isAnimationActive={false}
                    />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
};

const TaylorSeriesPlot = () => {
    const accuracyBounds = [0.40, 1.05, 1.77, 2.51, 3.25];
    return (
        <div style={{ 
            display: 'grid',
            justifyContent: 'center',
            width: '1000px',
            marginLeft: 'calc((760px - 1000px) / 2)',
            maxWidth: '90vw'
        }}>
            <div className="space-y-16"> {/* Increased spacing between sections */}
                <div>
                    <h2 className="text-xl font-semibold mb-4">Taylor Series Approximations of sin(x)</h2>
                    <table className="w-full border-collapse bg-white">
                        <thead>
                            <tr>
                                <th className="border p-2" style={{width: '50px'}}>n</th>
                                <th className="border p-2" style={{width: '450px'}}>Plot</th>
                                <th className="border p-2" style={{width: '200px'}}>Taylor Series</th>
                                <th className="border p-2" style={{width: '150px'}}>Accuracy Bound<br/>(|error| &lt; 0.01)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {[1, 2, 3, 4, 5].map((n, index) => (
                                <tr key={n}>
                                    <td className="border p-2 text-center">{n}</td>
                                    <td className="border p-2">
                                        <TaylorPlot n={n} accuracyBound={accuracyBounds[index]} />
                                    </td>
                                    <td className="border p-2 text-center align-middle">
                                        {n === 1 && "x"}
                                        {n === 2 && "x - x³/3!"}
                                        {n === 3 && "x - x³/3! + x⁵/5!"}
                                        {n === 4 && "x - x³/3! + x⁵/5! - x⁷/7!"}
                                        {n === 5 && "x - x³/3! + x⁵/5! - x⁷/7! + x⁹/9!"}
                                    </td>
                                    <td className="border p-2 text-center">|x| ≤ {accuracyBounds[index]}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>

                <div>
                    <h2 className="text-xl font-semibold mb-4">Accuracy Bound vs Number of Terms (for different error thresholds ε)</h2>
                    <div className="bg-white">
                        <BoundPlot />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default TaylorSeriesPlot;
