import React, { useState } from 'react'
import { useEffect } from 'react'
import { useHistory } from 'react-router-dom'
import { Link } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { authSignUp } from '../../store/actions'

import Button from '@material-ui/core/Button'
import Avatar from '@material-ui/core/Avatar'
import Badge from '@material-ui/core/Badge'
import { Box } from '@material-ui/core'
import { FormControl } from '@material-ui/core'
import { InputLabel } from '@material-ui/core'
import { InputAdornment } from '@material-ui/core'
import { IconButton } from '@material-ui/core'
import { FilledInput } from '@material-ui/core'
import { FormHelperText } from '@material-ui/core'
import { Card } from '@material-ui/core'
import { CardActions } from '@material-ui/core'
import { CardHeader } from '@material-ui/core'
import { Typography } from '@material-ui/core'
import { CardContent } from '@material-ui/core'
import { Divider } from '@material-ui/core'


import AccountCircle from '@material-ui/icons/AccountCircle'
import { LockOpen } from '@material-ui/icons'
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
  const form = {
    'variant': 'outlined'
  }
  const signup = useSelector(state => state.auth.signup)
  const [userData, setUserData] = useState(initial_state)
  const [onSubmit, setOnSubmit] = useState(false)
  const [showPassword, setShowPassword] = useState({'password1':false, 'password2':false})
  
  useEffect(()=>{
    signup.error && setOnSubmit(false) 
  }, [signup])
   
  useEffect(()=>{
    signup.msg === 'SignUp Success' && history.push('/activate-account') 
  }, [signup.msg, history])
 
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

  const handleShowPassword = (arg) => {
    showPassword[arg] ?
    setShowPassword({...showPassword, [arg]: false})
    : setShowPassword({...showPassword, [arg]: true})
  }

  return (
    <div>
      <Box
        component="form"
        type='submit'
        sx={{
          '& .MuiTextField-root': { mx: 'auto', m: 1, width: '30ch' }, mt: '1rem' 
        }}
        autoComplete="off"
        onSubmit={e=>e.preventDefault()}
      >
        <Card 
          sx={{ p: '4rem', pt:'1rem', maxWidth: 450, mx: 'auto',}}
          elevation={6}
        >
        <CardContent>
          <Avatar sx={{ mx:'auto', bgcolor: '#a04dee' }} shape="circle" >
            <LockOpen/>
          </Avatar>
          <Typography variant='h5'>
            Sign Up
          </Typography>
        </CardContent>
          <FormControl sx={{ m: 1, width: '50ch' }} variant={form.variant}>
            <InputLabel 
              htmlFor="signup-email" 
              required 
              color='secondary'
              variant={form.variant}
            >
              Email
            </InputLabel>
            <FilledInput
              required 
              variant={form.variant}
              id="signup-email"
              type='email'
              name='email'
              value={userData.email}
              onChange={(event) => handleOnChange(event) }
            />
            <FormHelperText error >
              {signup.error_msg.email && signup.error_msg.email[0]}
            </FormHelperText>
          </FormControl>
          <br />
          <FormControl sx={{ m: 1, width: '50ch' }} variant={form.variant}>
            <InputLabel 
              htmlFor="signup-username" 
              required 
              color='secondary'
              variant={form.variant}
            >
              Username
            </InputLabel>
            <FilledInput
              required 
              id="signup-username"
              type='text'
              name='username'
              value={userData.username}
              onChange={(event) => handleOnChange(event) }
            />
            <FormHelperText error >
              {signup.error_msg.username && signup.error_msg.username[0]}
            </FormHelperText>
          </FormControl>
          <br />
          <FormControl sx={{ m: 1, width: '24ch' }} variant={form.variant}>
            <InputLabel 
              htmlFor="signup-first_name" 
              color='secondary'
              variant={form.variant}
            >
              First Name
            </InputLabel>
            <FilledInput
              id="signup-first_name"
              type='text'
              name='first_name'
              value={userData.first_name}
              onChange={(event) => handleOnChange(event) }
            />
            <FormHelperText error >
              {signup.error_msg.first_name && signup.error_msg.first_name[0]}
            </FormHelperText>
          </FormControl>
          <FormControl sx={{ m: 1, width: '24ch' }} variant={form.variant}>
            <InputLabel 
              htmlFor="signup-last_name" 
              color='secondary'
              variant={form.variant}
            >
              Last Name
            </InputLabel>
            <FilledInput
              required 
              id="signup-last_name"
              type='text'
              name='last_name'
              value={userData.last_name}
              onChange={(event) => handleOnChange(event) }
            />
            <FormHelperText error >
              {signup.error_msg.last_name && signup.error_msg.last_name[0]}
            </FormHelperText>
          </FormControl>
          <br />
          <FormControl sx={{ m: 1, width: '24ch' }} variant={form.variant}>
            <InputLabel 
              htmlFor="signup-password1" 
              required  
              color='secondary'
              variant={form.variant}
            >
              Password
            </InputLabel>
            <FilledInput
              required 
              id="signup-password1"
              type={showPassword['password1'] ? 'text' : 'password'}
              name='password1'
              value={userData.password1}
              onChange={(event) => handleOnChange(event) }
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={()=>handleShowPassword('password1')}
                    edge='end'
                  >
                    {showPassword['password1'] ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
            <FormHelperText error >
              {signup.error_msg.password1 && signup.error_msg.password1[0]}
            </FormHelperText>
          </FormControl>
          <FormControl sx={{ m: 1, width: '24ch' }} variant={form.variant}>
            <InputLabel 
              htmlFor='signup-password2'
              required
              color='secondary'
              variant={form.variant}
            >
              Confirm Password
            </InputLabel>
            <FilledInput
              id='signup-password2'
              type={showPassword['password2'] ? 'text' : 'password'}
              name='password2'
              value={userData.password2}
              onChange={(event) => handleOnChange(event) }
              onKeyPress={handleKeypress}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={()=>handleShowPassword('password2')}
                    edge='end'
                  >
                    {showPassword['password2']  ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
            <FormHelperText error >
              {signup.error_msg.password2 && signup.error_msg.password2[0]}
            </FormHelperText>
          </FormControl>
          <br />
          <br />
          {/* <CardActions> */}
            <Button 
              sx={{ mx: 'auto', mb: 1, width:'55ch', borderRadius: 5,}}
              type="secondary" 
              disabled = {onSubmit ? true : false }
              variant='contained'
              onClick={(event)=>handleSubmit(event)}
            >
              {onSubmit ? 'SIGNING UP' : 'SIGN UP' }
            </Button>
            <br/>
            <Link to='/signin'>
              <Typography variant='small' color='primary'>
                Already have an account? SignIn
              </Typography>
            </Link>
          {/* </CardActions> */}
          
        </Card>
      </Box>
    </div>
  ) 
}
