import React from 'react';

const JellybeanJar = () => {
  // Generate random positions for jellybeans
  const jellybeans = Array.from({ length: 15 }, (_, i) => ({
    id: i,
    color: ['#F87171', '#60A5FA', '#FBBF24', '#34D399', '#A78BFA', '#EC4899'][Math.floor(Math.random() * 6)],
    left: 20 + Math.random() * 60,
    top: 40 + Math.random() * 40,
  }));

  const styles = {
    container: {
      position: 'relative',
      width: '192px',
      height: '256px',
      margin: '20px auto',
    },
    lid: {
      position: 'absolute',
      top: 0,
      left: '50%',
      transform: 'translateX(-50%)',
      width: '96px',
      height: '24px',
      backgroundColor: '#D1D5DB',
      borderRadius: '24px 24px 0 0',
      zIndex: 20,
    },
    jarBody: {
      position: 'absolute',
      top: '16px',
      left: '50%',
      transform: 'translateX(-50%)',
      width: '128px',
      height: '224px',
      backgroundColor: '#F3F4F6',
      borderRadius: '24px',
      overflow: 'hidden',
    },
    highlight: {
      position: 'absolute',
      top: 0,
      left: '8px',
      width: '8px',
      height: '100%',
      backgroundColor: 'white',
      opacity: 0.3,
      borderRadius: '9999px',
    },
    base: {
      position: 'absolute',
      bottom: 0,
      left: '50%',
      transform: 'translateX(-50%)',
      width: '128px',
      height: '8px',
      backgroundColor: '#D1D5DB',
      borderRadius: '9999px',
    },
    jellybean: (left, top) => ({
      position: 'absolute',
      width: '16px',
      height: '12px',
      borderRadius: '9999px',
      transform: 'rotate(45deg)',
      left: `${left}%`,
      top: `${top}%`,
    }),
  };

  return (
    <div style={styles.container}>
      <div style={styles.lid} />
      <div style={styles.jarBody}>
        <div style={styles.highlight} />
        {jellybeans.map((bean) => (
          <div
            key={bean.id}
            style={{
              ...styles.jellybean(bean.left, bean.top),
              backgroundColor: bean.color,
            }}
          />
        ))}
      </div>
      <div style={styles.base} />
    </div>
  );
};

export default JellybeanJar;