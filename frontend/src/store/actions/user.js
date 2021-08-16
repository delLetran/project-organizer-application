import { 
  handleGetOwnerData,
  handleGetUserData 
} from "./user_action_handler"


export const getAuthUser = () => {
  return dispatch => {
    handleGetOwnerData(dispatch)
  }
}

export const getUser = (username) => {
  return dispatch => {
    handleGetUserData(username, dispatch)
  }
}
