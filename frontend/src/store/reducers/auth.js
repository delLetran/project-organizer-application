// 'AUTH_START'   --> login or signup; post username/email and password
// 'AUTH_SUCCESS' --> get pair token (access & refresh)
// 'AUTH_FAIL'    --> invalid credentials; error login
// 'AUTH_REFRESH' --> access token expired, get new pair token using refresh token
// 'AUTH_LOGOUT'  --> refresh token expired

import updateObject from '../uitility'

export const authInitialState = {
  isAuthenticated: false,
  auth_user_email: null,
  msg: "auth msg",
  error: null,
  signup: {
    msg: null,
    error: false,
    error_msg: {
      email: null,
      username: null,
      password1: null,
      password2: null
    }
  },
}

const authStart = (state=authInitialState, action) => {
  return updateObject(state, {
    isAuthenticated: false,
    msg: "authentication started",
    error: 'unknown'
  })
}

const authSuccess = (state=authInitialState, action) => {
  return updateObject(state, {
    isAuthenticated: true,
    auth_user_email: action.payload.user,
    msg: "User Authenticated!",
    error: null
    // accessToken: action.payload.accessToken,
    // accessExpiration: action.payload.accessExpiration
  })
}

const authFail = (state=authInitialState, action) => {
  return updateObject(state, {
    isAuthenticated: false,
    auth_user_email: null,
    msg: action.error,
    error: action.error
    // accessToken: null,
    // accessExpiration: null,
  })
}

const authRefresh = (state=authInitialState, action) => {
  return updateObject(state, {
    isAuthenticated: true, 
    auth_user_email: action.payload.user_email, 
    msg: action.error,
    error: action.error
    // accessToken: action.payload.accessToken,
    // accessExpiration: action.payload.accessExpiration,
  })
}

const authLogout = (state=authInitialState, action) => {
  return updateObject(state, {
    isAuthenticated: false,
    msg: action.msg,
    error: action.error
    // accessToken: null,
    // accessExpiration: null,
  })
}

const authSignUpSuccess = (state=authInitialState, action) => {
  return {...state, 
    signup: {
      ...state.signup,
      msg: 'SignUp Success',
      error: false,
      error_msg: {
        email: null,
        username: null,
        password1: null,
        password2: null
      }
    }
  }
}
const authSignUpFail = (state=authInitialState, action) => {
  return {...state, 
    signup: {
      ...state.signup,
      msg: null,
      error: true,
      error_msg: action.error
    }
  }
}

export const authReducer = (state=authInitialState, action ) => {
  switch (action.type) {
    case 'AUTH_START': return authStart(state, action)     
    case 'AUTH_SUCCESS': return authSuccess(state, action) 
    case 'AUTH_FAIL': return authFail(state, action) 
    case 'AUTH_REFRESH': return authRefresh(state, action) 
    case 'AUTH_LOGOUT': return authLogout(state, action) 
    case 'AUTH_SIGNUP_SUCCESS': return authSignUpSuccess(state, action) 
    case 'AUTH_SIGNUP_FAIL': return authSignUpFail(state, action) 
    default: return state
  }
}
