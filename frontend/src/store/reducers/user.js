// 'AUTH_START'   --> login or signup; post username/email and password
// 'AUTH_SUCCESS' --> get pair token (access & refresh)
// 'AUTH_FAIL'    --> invalid credentials; error login
// 'AUTH_REFRESH' --> access token expired, get new pair token using refresh token
// 'AUTH_LOGOUT'  --> refresh token expired

import { user } from "."


export const userInitialState = {
  auth_user: {
    data: {},
    msg: null,
    error: false,
  },
  user_list: [],
  error: null
}


const getOwnerDataSuccess = (state=userInitialState, action) => {
  return {...state, 
    auth_user: {
      ...state.auth_user,
      data: action.payload.user
    }
  }
}
const getOwnerDataFail = (state=userInitialState, action) => {
  return {...state, 
    auth_user: {
      ...state.auth_user,
      error: action.payload.error
    }
  }
}

const getUserDataSuccess = (state=userInitialState, action) => {
  return {...state, 
    // user_list: [...state.user_list, state.user_list.filter(user=>
    //   user.id===action.payload.user.id)[0] ? action.payload.user :  ]
    // user_list: [...state.user_list, action.payload.user]
    user_list: [
      ...state.user_list.map((user)=>
        user.id !== action.payload.user.id ? 
          user : action.payload.user
      )

    ]
    
  }
}
const getUserDataFail = (state=userInitialState, action) => {
  return {...state, 
    error: 'Failure retrieving user data.'
  }
}

export const userReducer = (state=userInitialState, action ) => {
  switch (action.type) {
    case 'GETOWNERDATA_SUCCESS': return getOwnerDataSuccess(state, action)    
    case 'GETOWNERDATA_FAIL': return getOwnerDataFail(state, action)    
    case 'GETUSER_SUCCESS': return getUserDataSuccess(state, action)    
    case 'GETUSER_FAIL': return getUserDataFail(state, action)    
    default: return state
  }
}
