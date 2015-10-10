import React from 'react';
import { IndexRoute, Route } from 'react-router';
import AppContainer from './containers/appContainer';
import Frontpage from './containers/frontpage';

const routes = (
  <Route path='/' component={AppContainer}>
    <IndexRoute component={Frontpage} />
  </Route>
);

export default routes;
