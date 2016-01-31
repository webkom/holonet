import { compose, createStore, applyMiddleware, combineReducers } from 'redux';
import thunkMiddleware from 'redux-thunk';
import createLogger from 'redux-logger';
import { createHistory } from 'history';
import { reduxReactRouter, routerStateReducer } from 'redux-router';
import routes from './routes';
import * as reducers from './reducers';

function promiseMiddleware() {
  return next => action => {
    if (!action.promise) {
      return next(action);
    }

    const { type, meta, payload, promise } = action;

    next({
      type: `${type}_BEGIN`,
      payload,
      meta
    });

    return promise.then(
      result => next({
        type: `${type}_SUCCESS`,
        payload: result,
        meta: {
          ...meta,
          receivedAt: Date.now()
        }
      }),
      error => next({
        type: `${type}_FAILURE`,
        payload: error,
        error: true
      })
    );
  };
}

const loggerMiddleware = createLogger({
  level: 'info',
  collapsed: true
});

let middelwareList = [
  thunkMiddleware,
  promiseMiddleware
];

if ((process.env.NODE_ENV || 'development') === 'development') {
  middelwareList = [
    thunkMiddleware,
    promiseMiddleware,
    loggerMiddleware
  ];
}

const middlewares = applyMiddleware(...middelwareList);

const finalCreateStore = compose(
  middlewares,
  reduxReactRouter({
    routes,
    createHistory
  })
)(createStore);

const reducer = combineReducers({
  router: routerStateReducer,
  ...reducers
});

export default function configureStore(initialState) {
  const store = finalCreateStore(reducer, initialState);

  if (module.hot) {
    module.hot.accept('./reducers', () => {
      const nextReducer = require('./reducers');
      store.replaceReducer(nextReducer);
    });
  }

  return store;
}
