import React from 'react';
import './TaglineSection.css';

const TaglineSection = () => {
  return (
    <div className="tagline-card">
      <div className="tagline-content">
        <h3>Goals : </h3>
        <p>Explore Inventory management app with modern Fast-API Backend Development environtment, frontend integration, and self-managed infrastructure on local and development environtment covering wrap service with Docker, PostgreSQL, CI/CD automation with Jenkins, Portainer, and Secure HTTPS deployment with ssl-let's enscrypt certifate
        </p>
        <div className="company-badge">
          <span className="powered-by">Powered by</span>
          <span className="company-name">David Infrastructure Service  <span className="external-arrow">↗</span></span>
        </div>
      </div>
    </div>
  );
};

export default TaglineSection;
