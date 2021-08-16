
import { 
  handleLogin,
  handleSignUp,
  setAuthRefreshTimeout,
  setAuthAccessTimeout
} from "./auth_action_handler"


import { 
  authLogout
} from "./auth_action_response"
 

//Start Login
export const authLogin = (credentials) => {
  return dispatch => {
    handleLogin(credentials, dispatch)
  }
}

export const authSignUp = (user_data) => {
  return dispatch => {
    handleSignUp(user_data, dispatch)
  }
}

export const authCheckState = () => {
  return dispatch => {
    const refreshToken = localStorage.getItem('refresh_token')
    const refreshExpiration = localStorage.getItem('refresh_expiration')
    
    if (refreshToken === undefined){
      dispatch(authLogout())
    }else {
      if (refreshExpiration <= new Date()){
        dispatch(authLogout())
      }else {
        dispatch(setAuthRefreshTimeout((new Date(refreshExpiration).getTime() - new Date().getTime()) / 1000))
        dispatch(setAuthAccessTimeout())
      }
    }
  }
}

export {
  authLogout
}