import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { createStore, applyMiddleware, compose } from 'redux'
import thunk from 'redux-thunk'
import { Provider } from 'react-redux'
import _reducers from './store/reducers'

const store = createStore(
  _reducers, 
  compose(
    applyMiddleware(thunk),
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
  )
)


ReactDOM.render(
  <React.StrictMode>
    {/* <MuiThemeProvider> */}
      <Provider store={store}>
          <App />
      </Provider>
    {/* </MuiThemeProvider> */}
  </React.StrictMode>,
  document.getElementById('root')
);


// reportWebVitals();