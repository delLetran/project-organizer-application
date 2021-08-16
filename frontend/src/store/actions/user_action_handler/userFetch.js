import { 
  getOwnerDataSuccess,
  getOwnerDataFail,
  getUserDataSuccess,
  getUserDataFail 
} from "../user_action_response"

const baseURL = `http://localhost:8000/api/`


const handleGetOwnerData = async (dispatch) => {
  const url = `${baseURL}user/data/`
  const resquestOption = {
    method: 'GET',
    headers: {
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    },
  }
  const response = await fetch(url, resquestOption)
  const owner_data = await response.json()
  response.ok ?
    dispatch(getOwnerDataSuccess(owner_data))
  : dispatch(getOwnerDataFail(owner_data))
}


const handleGetUserData = async (username, dispatch) => {
  const url = `${baseURL}user/${username}/`
  const resquestOption = {
    method: 'GET',
    headers: {
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    },
  }
  const response = await fetch(url, resquestOption)
  const user_data = await response.json()
  response.ok ?
    dispatch(getUserDataSuccess(user_data))
  : dispatch(getUserDataFail(user_data))
}

export {
  handleGetOwnerData,
  handleGetUserData
}