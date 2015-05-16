import { Flummox } from 'flummox';
import FluxComponent from 'flummox/component';
import React from 'react';

import App from './components/app';

class Flux extends Flummox {
  constructor() {
    super();
  }
}

const flux = new Flux();

React.render(
  <FluxComponent flux={flux}>
    <App />
  </FluxComponent>,
  document.getElementById('app')
);
