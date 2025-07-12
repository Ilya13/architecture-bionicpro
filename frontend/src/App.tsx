import React from 'react';
import { ReactKeycloakProvider } from '@react-keycloak/web';
import Keycloak, { KeycloakConfig, KeycloakInitOptions, KeycloakPkceMethod } from 'keycloak-js';
import ReportPage from './components/ReportPage';

const keycloakConfig: KeycloakConfig = {
  url: process.env.REACT_APP_KEYCLOAK_URL,
  realm: process.env.REACT_APP_KEYCLOAK_REALM||"",
  clientId: process.env.REACT_APP_KEYCLOAK_CLIENT_ID||"",
};

const keycloak = new Keycloak(keycloakConfig);

const initOptions: KeycloakInitOptions = {
  pkceMethod: process.env.REACT_APP_KEYCLOAK_PKCE_METHOD as KeycloakPkceMethod,
}

const App: React.FC = () => {
  return (
    <ReactKeycloakProvider authClient={keycloak} initOptions={initOptions}>
      <div className="App">
        <ReportPage />
      </div>
    </ReactKeycloakProvider>
  );
};

export default App;