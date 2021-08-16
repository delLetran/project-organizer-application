import { 
  GETPROJECTLIST_SUCCESS,
  GETPROJECTDETAILS_SUCCESS,
  // ADDPROJECT_SUCCESS,
  // UPDATEPROJECT_SUCCESS,
  // DELETEPROJECT_SUCCESS,
  GETPROJECTLIST_FAIL,
  GETPROJECTDETAILS_FAIL,
  // ADDPROJECT_FAIL,
  // UPDATEPROJECT_FAIL,
  // DELETEPROJECT_FAIL
} from "./actionTypes"

const baseURL = `http://localhost:8000/api/`

export const projectDetailsSuccess = (id, data) => {
  return {
    type: GETPROJECTDETAILS_SUCCESS,
    payload: {
      id: id,
      project: data,
    }
  }
}

export const projectDetailsFail = (id, error) => {
  return {
    type: GETPROJECTDETAILS_FAIL,
    payload: {
      id: id,
      error: error,
    }
  }
}

export const projectListSuccess = (data) => {
  return {
    type: GETPROJECTLIST_SUCCESS,
    payload: {
      project_list: data,
    }
  }
}

export const projectListFail = (error) => {
  return {
    type: GETPROJECTLIST_FAIL,
    payload: {
      project_list: null,
      error: error,
    }
  }
}


export const getProjectList = () => {
  return dispatch => {
    handelGetProjecList(dispatch)
  }
}

export const getProjectDetails = (id) => {
  return dispatch => {
    handelGetProjectDetails(id, dispatch)
  }
}


const handelGetProjecList = ( dispatch) => {
  const url = `${baseURL}project/list/`
  const resquestOption = {
    method: 'GET',
    headers: {
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    }
  }
  fetch(url, resquestOption)
  .then( res => {
    return res.json()
  })
  .then(data =>{
    dispatch(projectListSuccess(data))
  })
  .catch(error => { 
    dispatch(projectListFail(error))
  })
}


const handelGetProjectDetails = (id, dispatch) => {
  const url = `${baseURL}project/${id}/`
  const resquestOption = {
    method: 'GET',
    headers: {
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    }
  }
  fetch(url, resquestOption)
  .then( res => {
    return res.json()
  })
  .then(data =>{
    console.log('data: ', data)
    dispatch(projectDetailsSuccess(id, data))
  })
  .catch(error => { 
    console.log('error: ', error)
    dispatch(projectDetailsFail(id, error))
  })
}













