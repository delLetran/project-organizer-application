import React, { useState } from 'react'
import { useEffect } from 'react'
import { useHistory } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { authSignUp } from '../../store/actions'

import Button from '@material-ui/core/Button'
import Avatar from '@material-ui/core/Avatar'
import Badge from '@material-ui/core/Badge'
import TextField from '@material-ui/core/TextField';
import { Box } from '@material-ui/core'
import { FormControl } from '@material-ui/core'
import { InputLabel } from '@material-ui/core'
import { InputAdornment } from '@material-ui/core'
import { IconButton } from '@material-ui/core'
import { FilledInput } from '@material-ui/core'
import { FormHelperText } from '@material-ui/core'
import AccountCircle from '@material-ui/icons/AccountCircle'
import { Visibility } from '@material-ui/icons'
import { VisibilityOff } from '@material-ui/icons'

export const SignUp = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const initial_state= {
    "email": "",
    "username": "",
    "first_name": "",
    "last_name": "",
    "password1": "",
    "password2": ""
  }
  const signup = useSelector(state => state.auth.signup)
  const [userData, setUserData] = useState(initial_state)
  const [onSubmit, setOnSubmit] = useState(false)
  const [showPassword, setShowPassword] = useState(false)
  

  const handleOnChange = (event) => {
    const {name, value} = event.target
    setUserData({...userData, [name]: value})
  }

  const handleSubmit = (event) => {
    dispatch(authSignUp(userData))
    setOnSubmit(true)
  }

  const handleKeypress = event => {
  if (event.keyCode === 13) {
    dispatch(authSignUp(userData))
    }
  }

  const handleShowPassword = () => {
    setShowPassword(!showPassword)
  }
  useEffect(()=>{
    signup.error && setOnSubmit(false) 
  }, [signup])
 
  useEffect(()=>{
    signup.msg === 'SignUp Success' && history.push('/profile') 
  }, [signup.msg, history])
 
  return (
    <div>
      <span className="avatar-item">
        <Badge count={27}>
          <Avatar shape="circle" icon={<AccountCircle />} />
        </Badge>
      </span>
      <br/>
        <Box
          component="form"
          type='submit'
          sx={{
            '& .MuiTextField-root': { m: 1, width: '30ch' },
          }}
          autoComplete="off"
          onSubmit={e=>e.preventDefault()}
        >
          <TextField
            required
            color='primary'
            variant="filled"
            margin="normal"
            size="medium"
            label='Email'
            type='email'
            name='email'
            value={userData.email}
            onChange={(event) => handleOnChange(event) }
            helperText = {signup.error_msg.email && signup.error_msg.email[0]}
            error = {signup.error_msg.email ? true : false}
          />
          <br />
          <TextField
            required
            color='primary'
            variant="filled"
            margin="normal"
            size="medium"
            label='Username'
            name='username'
            value={userData.username}
            onChange={(event) => handleOnChange(event) }
            helperText = {signup.error_msg.username && signup.error_msg.username[0]}
            error = {signup.error_msg.username ? true : false}
          />
          <br />
          <TextField
            variant="filled"
            margin="normal"
            size="medium"
            label='First name'
            name='first_name'
            value={userData.first_name}
            onChange={(event) => handleOnChange(event) }
          />
          <br />
          <TextField
            variant="filled"
            margin="normal"
            size="medium"
            label='Last name'
            name='last_name'
            value={userData.last_name}
            onChange={(event) => handleOnChange(event) }
          />
          <br />
          <FormControl sx={{ m: 1, width: '30ch' }} variant="outlined">
            <InputLabel 
              htmlFor="signup-password1" 
              required  
              color='secondary'
              variant="filled"
            >
              Password
            </InputLabel>
            <FilledInput
              required 
              id="signup-password1"
              margin="dense"
              size="medium"
              type={showPassword ? 'text' : 'password'}
              name='password1'
              value={userData.password1}
              onChange={(event) => handleOnChange(event) }
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleShowPassword}
                    edge='end'
                  >
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
            <FormHelperText >
              {signup.error_msg.password2 && signup.error_msg.password1[0]}
            </FormHelperText>
          </FormControl>
          <br/>
          <TextField
            required 
            color='primary'
            variant="filled"
            margin="normal"
            size="medium"
            label='Confirm Password'
            type='password' 
            name='password2' 
            value={userData.password2}
            onChange={(event) => handleOnChange(event) }
            onKeyPress={handleKeypress}
            helperText = {signup.error_msg.password2 && signup.error_msg.password2[0]}
            // error = {signup.error_msg.password2 ? true : false}
          />
          <br />
          <br />
          { onSubmit ?
            <Button 
              sx={{width:'33ch'}}
              type="secondary" 
              disabled
              variant='contained'
            >
              SIGNING UP
            </Button>
            : 
            <Button 
              sx={{width:'33ch'}}
              type="secondary" 
              variant='contained'
              onClick={(event)=>handleSubmit(event)}
            >
              SIGN UP
            </Button>
          }     
        </Box>
    </div>
  ) 
}
