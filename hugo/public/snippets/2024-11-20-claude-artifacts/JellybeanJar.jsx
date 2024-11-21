import React from 'react';
import './styles.css';

const JellybeanJar = () => {
  const jellybeans = Array.from({ length: 15 }, (_, i) => ({
    id: i,
    color: ['bg-pink-400', 'bg-blue-400', 'bg-yellow-400', 'bg-green-400', 'bg-purple-400', 'bg-red-400'][Math.floor(Math.random() * 6)],
    left: 20 + Math.random() * 60,
    top: 40 + Math.random() * 40,
  }));

  return (
    <div className="tailwind-scope">
      <div className="relative w-48 h-64 mx-auto">
        {/* Jar lid */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-24 h-6 bg-gray-300 rounded-t-full z-20" />
        
        {/* Jar body */}
        <div className="absolute top-4 left-1/2 -translate-x-1/2 w-32 h-56 bg-gray-100 rounded-3xl overflow-hidden">
          {/* Glass highlight */}
          <div className="absolute top-0 left-2 w-2 h-full bg-white opacity-30 rounded-full" />
          
          {/* Jellybeans */}
          {jellybeans.map((bean) => (
            <div
              key={bean.id}
              className={`absolute w-4 h-3 ${bean.color} rounded-full transform rotate-45`}
              style={{
                left: `${bean.left}%`,
                top: `${bean.top}%`,
              }}
            />
          ))}
        </div>
        
        {/* Jar base */}
        <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-32 h-2 bg-gray-300 rounded-full" />
      </div>
    </div>
  );
};

export default JellybeanJar;
