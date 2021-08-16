import { useEffect } from 'react'
import { useDispatch } from 'react-redux'
import { authCheckState } from './store/actions'
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import { TestComponent } from './tests';


function App() {
  const dispatch = useDispatch()
   
  useEffect(() => {
    dispatch(authCheckState())
  })

  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact={true} path="/" component={ ()=><TestComponent/> }/>
        </Switch>  
      </Router>
    </div>
  )
}

export default App 
