import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useHistory } from 'react-router-dom'
import { authLogin, authLogout } from '../../store/actions'

import Button from '@material-ui/core/Button';
import Avatar from '@material-ui/core/Avatar';
import Badge from '@material-ui/core/Badge';
import TextField from '@material-ui/core/TextField';

import AccountCircle from '@material-ui/icons/AccountCircle'


export function Login(){
  const [credentials, setCredentials] = useState({'email': '', 'password': ''})
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const dispatch = useDispatch()
  const history = useHistory()
  
  const handleOnChange = (e) => {
    const {name, value} = e.target
    setCredentials({...credentials, [name]: value})
  }
  
  const handleKeypress = e => {
    if (e.keyCode === 13) {
      dispatch(authLogin(credentials))
      // history.push(from)
    }
  }

  const handleLogout = () => {
    dispatch(authLogout())
    history.push('/signin/')
  }

  return (
    <div>
      <span className="avatar-item">
        <Badge count={27}>
          <Avatar shape="circle" icon={<AccountCircle />} />
        </Badge>
      </span>
      <br/>
      { isAuthenticated ? 
          <Button type="Danger" onClick={ handleLogout }>Logout</Button>
      : 
        <form onSubmit={e=>e.preventDefault()}>
            <TextField 
              required
              label='Email'
              variant='outlined'
              type='email'
              name='email'
              value={credentials.email}
              onChange={(e) => handleOnChange(e) }
            />
          <br />
            <TextField 
              required
              label='Password'
              type='password' 
              name='password' 
              value={credentials.password}
              onChange={(e) => handleOnChange(e) }
              onKeyPress={handleKeypress}
            />
          <br />
          <br />
          <Button type="primary" onClick={()=>dispatch(authLogin(credentials))}>Login</Button>
        </form>
      }
    </div>
  ) 
}