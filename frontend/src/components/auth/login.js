import { useState } from 'react'
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { Redirect } from 'react-router'
import { useHistory, useLocation } from 'react-router-dom'
// import { authLogout } from '../../store/actions'
import { authLogin } from '../../store/actions'

import { FormControl } from '@material-ui/core'
import { InputLabel } from '@material-ui/core'
import { InputAdornment } from '@material-ui/core'
import { IconButton } from '@material-ui/core'
import { FilledInput } from '@material-ui/core'
// import { FormHelperText } from '@material-ui/core'

import Button from '@material-ui/core/Button';
import Avatar from '@material-ui/core/Avatar';
import Badge from '@material-ui/core/Badge';
import TextField from '@material-ui/core/TextField';

import AccountCircle from '@material-ui/icons/AccountCircle'
import { Visibility } from '@material-ui/icons'
import { VisibilityOff } from '@material-ui/icons'

export function Login(){
  const [credentials, setCredentials] = useState({'email': '', 'password': ''})
  const is_authenticated = useSelector(state => state.auth.isAuthenticated)
  const dispatch = useDispatch()
  const history = useHistory()
  const location = useLocation()
  let { from } = location.state || { from: { pathname: "/" } };
  const [showPassword, setShowPassword] = useState(false)

  
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

  useEffect(() => {
    is_authenticated && history.push(from)
  }, [is_authenticated])

  const handleShowPassword = (arg) => {
    setShowPassword(!showPassword)
  }


  return (
    <div>
      <span className="avatar-item">
        <Badge count={27}>
          <Avatar shape="circle" icon={<AccountCircle />} />
        </Badge>
      </span>
        {/* {history.push({from})} */}
          {/* <Button type="Danger" onClick={ handleLogout }>Logout</Button> */}
      { is_authenticated ? 
        <div> 
          You're already logged in
        </div> 
        :
        <form onSubmit={e=>e.preventDefault()}>
          <FormControl sx={{ m: 1, width: '30ch' }} variant='outlined'>
            <InputLabel 
              htmlFor="login-email" 
              required  
              color='secondary'
              variant='outlined'
            >
              Email
            </InputLabel>
            <FilledInput
              required 
              id="login-email"
              type='email'
              name='email'
              value={credentials.email}
              onChange={(event) => handleOnChange(event) }
            />
            {/* <FormHelperText error >
              {signup.error_msg.password1 && signup.error_msg.password1[0]}
            </FormHelperText> */}
          </FormControl>  
          <br />
          <FormControl sx={{ m: 1, width: '30ch' }} variant='outlined'>
            <InputLabel 
              htmlFor="login-password" 
              required  
              color='secondary'
              variant='outlined'
            >
              Password
            </InputLabel>
            <FilledInput
              required 
              id="login-password"
              type={showPassword ? 'text' : 'password'}
              name='password'
              value={credentials.password}
              onChange={(event) => handleOnChange(event) }
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={()=>handleShowPassword()}
                    edge='end'
                  >
                    {showPassword? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
            {/* <FormHelperText error >
              {signup.error_msg.password1 && signup.error_msg.password1[0]}
            </FormHelperText> */}
          </FormControl>  
            {/* <TextField 
              required
              label='Password'
              type='password' 
              name='password' 
              value={credentials.password}
              onChange={(e) => handleOnChange(e) }
              onKeyPress={handleKeypress}
            /> */}
          <br />
          <br />
          <Button type="primary" onClick={()=>dispatch(authLogin(credentials))}>Login</Button>
        </form>
      }
    </div>
  ) 
}