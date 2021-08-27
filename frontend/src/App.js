
import { useEffect } from 'react'
import { useDispatch } from 'react-redux'
import { useSelector } from 'react-redux';
// import { useHistory } from 'react-router';
import { BrowserRouter as Router, 
  // Switch, 
  // Route, 
  Redirect 
} from "react-router-dom";

import { authCheckState } from './store/actions'
// import { setRedirect } from './store/actions';

// import Profile from './pages/profile';
// import Associate from './pages/associates';
// import { Login } from './components/auth'
// import { SignUp } from './components/auth'
// import Homepage from './pages/homepage'
// import { Project } from './pages/project_organizer';

// import { TestComponent } from './tests'
import Routes from './pages';

const App = () => {
  const dispatch = useDispatch()
  // const history = useHistory
  const redirect = useSelector(state => state.router.redirect)

  useEffect(() => {
    // redirect && history.push(`${redirect}`) 
    redirect && <Redirect to={redirect}/> 
  }, [redirect])
  
  useEffect(() => {
    dispatch(authCheckState()) 
  }, [])

  return (
    <div className="App">
      <Router>
        <Routes/>


        {/* <Switch>
          <Route path='/' exact component={ Homepage } />
          <Route path='/profile' exact component={ Profile } />
          <Route path='/projects' component={ Project } />
          <Route path='/associates' component={ Associate } />  

          <Route path='/signin' component={ Login } />
          <Route path='/signup' component={ SignUp } />

          <Route path='/test/' component={ TestComponent } />
          <Route path='/test/:id'  component={ Profile } />
        </Switch> */}
      </Router>
    </div>
  )
}



export default App 
