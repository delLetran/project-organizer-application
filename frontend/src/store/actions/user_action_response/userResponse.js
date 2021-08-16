import { 
  GETOWNERDATA_SUCCESS,
  GETOWNERDATA_FAIL,
  GETUSER_SUCCESS,
  GETUSER_FAIL
} from "../actionTypes"


export const getOwnerDataSuccess = (owner_data) => {
  return {
    type: GETOWNERDATA_SUCCESS,
    payload: {
      owner: owner_data
    }
  }
}
export const getOwnerDataFail = (owner_data) => {
  return {
    type: GETOWNERDATA_FAIL,
    payload: {
      error: owner_data
    }
  }
}

export const getUserDataSuccess = (user_data) => {
  return {
    type: GETUSER_SUCCESS,
    payload: {
      user: user_data
    }
  }
}
export const getUserDataFail = (user_data) => {
  return {
    type: GETUSER_FAIL,
    payload: {
      error: user_data
    }
  }
}
