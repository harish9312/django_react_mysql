import * as React from 'react';
import * as ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import { LoginForm } from './App';

ReactDOM.render(
  <LoginForm />,
  document.getElementById('root') as HTMLElement
);
registerServiceWorker();

