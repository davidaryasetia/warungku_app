import React from 'react';
import './TaglineSection.css';

const TaglineSection = () => {
  return (
    <div className="tagline-card">
      <div className="tagline-content">
        <h3>Goals : </h3>
        <p>Simple Inventory management app convering Fast-API Backend Development, Front-End, HTTPS(Let's enscrypt), Cors Handling, and Integration CI/CD deployment using Docker container, Portainer, Jenkins </p>
        <div className="company-badge">
          <span className="powered-by">Powered by</span>
          <span className="company-name">David Infrastructure Service</span>
        </div>
      </div>
    </div>
  );
};

export default TaglineSection;
