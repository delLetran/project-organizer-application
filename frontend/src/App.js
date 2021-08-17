import { useEffect } from 'react'
import { useDispatch } from 'react-redux'
import { authCheckState } from './store/actions'
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import { Login } from './components/auth'
import { SignUp } from './components/auth'
import Homepage from './pages/homepage'
import { Project } from './pages/project_organizer';

import { TestComponent } from './tests'

const App = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(authCheckState()) 
  },[])

  return (
    <div className="App">
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

    </div>
  )
}

export default App 
