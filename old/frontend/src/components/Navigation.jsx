import React from 'react';
import { Link } from 'react-router-dom';

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/penalties">Input Penalties</Link></li>
        <li><Link to="/timing">Input Timing</Link></li>
        <li><Link to="/results">View Results</Link></li>
        <li><Link to="/generate-pdf">Generate PDF</Link></li>
      </ul>
    </nav>
  );
};

export default Navigation;
