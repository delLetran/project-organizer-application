import { useEffect } from 'react'
import { useDispatch } from 'react-redux'
// import { useSelector } from 'react-redux'
import { authCheckState } from './store/actions'
// import { getUser } from './store/actions';

// import logo from './logo_delletran.png';
import './App.css'; 
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

// import { createTheme, ThemeProvider } from '@material-ui/core/styles';

import { Login } from './components/auth'
import { SignUp } from './components/auth'
import Homepage from './pages/homepage'
import { Project } from './pages/project_organizer';

import { TestComponent } from './tests'

// const theme = createTheme()

function App() {
  const dispatch = useDispatch()
  // const auth_user = useSelector(state=>state.user.auth_user)
  // const user = useSelector(state=>state.auth.auth_user)
   
  // useEffect(() => {
  //   dispatch(getUser(user)) 
  // }, [])

  useEffect(() => {
    dispatch(authCheckState()) 
  })

  return (
    <div className="App">
      {/* <ThemeProvider theme={theme}> */}
        <header>
        </header>
        <div>
          <Router>
            <Switch>
              <Route path='/' exact component={ Homepage } />
              <Route path='/projects' component={ Project } />
              <Route path='/associates' component={ Login } />

              <Route path='/signin' component={ Login } />
              <Route path='/signup' component={ SignUp } />

              <Route path='/test' component={ TestComponent } />
            </Switch>
          </Router>
        </div>
      {/* </ThemeProvider> */}

    </div>
  );
}

export default App;
