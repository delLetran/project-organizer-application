import React, {  } from 'react'
import { Switch, Route } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { authLogout } from '../store/actions'
import { SignUp, SignIn } from './forms'
import { Button } from '@material-ui/core'


export const Auth = () => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const dispatch = useDispatch()
  
  return (
    <div>
      <h2>Auth</h2>
      {
        isAuthenticated ? 
          <Button onClick={dispatch(authLogout())}>Logout</Button>
          : 
          <SignInSignUp />
      }
    </div>
  )
}

const SignInSignUp = () =>
(
  <div> 
    <h2>Sign</h2>
    <Menu />
    <Switch>
      <Route path={'/auth/signin'} component={ SignIn } />
      <Route path={'/auth/signup'} component={ SignUp } />
    </Switch>
  </div> 
)

const Menu = () => (
  <Route render={({ history }) => (
    <>
      <Button type='primary' onClick={() => { history.push('/auth/signin') }}>SignIn</Button>{' or '}
      <Button type='primary' onClick={() => { history.push('/auth/signup') }}>SignUp</Button>
    </>
  )} />
)