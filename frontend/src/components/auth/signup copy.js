import React, { useState } from 'react'
import { useEffect } from 'react'
import { useHistory } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { authSignUp } from '../../store/actions'

import Button from '@material-ui/core/Button'
import Avatar from '@material-ui/core/Avatar'
import Badge from '@material-ui/core/Badge'
import { Box } from '@material-ui/core'
import { FormControl } from '@material-ui/core'
import { FormHelperText } from '@material-ui/core'
import { OutlinedInput } from '@material-ui/core'
import { InputLabel } from '@material-ui/core'
import { InputAdornment } from '@material-ui/core'
import { IconButton } from '@material-ui/core'

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
  
  signup.msg === 'SignUp Success' && history.push('/profile') 

  const handleOnChange = (event) => {
    const {name, value} = event.target
    setUserData({...userData, [name]: value})
  }
  const handleSubmit = (event) => {
    dispatch(authSignUp(userData))
    setOnSubmit(true)
  }
  // const handleKeypress = event => {
  // if (event.keyCode === 13) {
  //   dispatch(authSignUp(userData))
  //   }
  // }

  const handleShowPassword = () => {
    setShowPassword(!showPassword)
  }
  const emailInputForm = useFormControl('Email', 'email', 'email', userData.email, handleOnChange, '50ch', 'signup-email', signup.error_msg.email)
  const usernameInputForm = useFormControl('Username', 'text', 'username', userData.username, handleOnChange, '50ch', 'signup-username', signup.error_msg.username)
  const first_nameInputForm = useFormControl('First Name', 'text', 'first_name', userData.first_name, handleOnChange, '24ch', 'signup-first_name', signup.error_msg.first_name, false)
  const last_nameInputForm = useFormControl('Last Name', 'text', 'last_name', userData.last_name, handleOnChange, '24ch', 'signup-last_name', signup.error_msg.last_name, false)
  const password1InputForm = useFormControl('Password', 'password', 'password1', userData.password1, handleOnChange, '24ch', 'signup-password1',  signup.error_msg.password1, true, showPassword, handleShowPassword )
  const password2InputForm = useFormControl('Confirm Password', 'password', 'password2', userData.password2, handleOnChange, '24ch', 'signup-password2', signup.error_msg.password2,)

  useEffect(()=>{
    signup.error && setOnSubmit(false) 
  }, [signup])
 
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
          {emailInputForm}<br/>
          {usernameInputForm}<br/>
          {first_nameInputForm}
          {last_nameInputForm}<br/>
          {password1InputForm}
          {password2InputForm}<br/>
          <br/>
          <Button 
            sx={{width:'55ch'}}
            type="secondary" 
            disabled = {onSubmit ? true : false }
            variant='contained'
            onClick={(event)=>handleSubmit(event)}
          >
            {onSubmit ? 'SIGNING UP' : 'SIGN UP' }
          </Button>
        </Box>
    </div>
  ) 
}


function useFormControl(label, type, name, value, onChange, width, id, helper, required=true, toggle, onClick, variant='outlined') {  
  return (
    <FormControl sx={{ m: 1, width: width }} variant={variant}>
      <InputLabel 
        htmlFor={id}
        required={required}
        color='secondary'
        variant={variant}
      >
        {label}
      </InputLabel>
      <OutlinedInput
        id={id}
        type={onClick ? (toggle ? 'text' : 'password') : type}
        name={name}
        value={value}
        onChange={onChange}
        endAdornment={ onClick &&
          <InputAdornment position="end">
            <IconButton
              aria-label="toggle password visibility"
              onClick={onClick}
              edge='end'
            >
              {toggle ? <VisibilityOff /> : <Visibility />}
            </IconButton>
          </InputAdornment>
        }
      />
      <FormHelperText>{helper && helper[0]}</FormHelperText>
    </FormControl>
  )
}