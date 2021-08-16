import { 
  GETCOLLABORATORLIST_SUCCESS,
  // GETCOLLABORATORDETAILS_SUCCESS,
  ADDCOLLABORATOR_SUCCESS,
  UPDATECOLLABORATORPOSITION_SUCCESS,
  REMOVECOLLABORATOR_SUCCESS,
  GETCOLLABORATORLIST_FAIL,
  // GETCOLLABORATORDETAILS_FAIL,
  ADDCOLLABORATOR_FAIL,
  UPDATECOLLABORATORPOSITION_FAIL,
  REMOVECOLLABORATOR_FAIL,
} from "../actionTypes"


export const updateProjectCollaboratorSuccess = (project_id, collaborator_id, position) => {
  return {
    type: UPDATECOLLABORATORPOSITION_SUCCESS,
    payload: {
      project_id,
      collaborator_id,
      position
    }
  }
}

export const updateProjectCollaboratorFail = (error) => {
  return {
    type: UPDATECOLLABORATORPOSITION_FAIL,
    payload: {
      error: error,
    }
  }
}

export const getProjectCollaboratorSuccess = (project_id, data) => {
  console.log('collaborators: ', data)

  return {
    type: GETCOLLABORATORLIST_SUCCESS,
    payload: {
      project_id,
      collaborators: data,
    }
  }
}

export const getProjectCollaboratorFail = (project_id, error) => {

  return {
    type: GETCOLLABORATORLIST_FAIL,
    payload: {
      project_id,
      error: error,
    }
  }
}

export const inviteProjectCollaboratorSuccess = (user, project_id, data) => {

  return {
    type: ADDCOLLABORATOR_SUCCESS,
    payload: {
      username: user,
      project_id,
      collaborator: data,
    }
  }
}

export const inviteProjectCollaboratorFail = (user, project_id, error) => {

  return {
    type: ADDCOLLABORATOR_FAIL,
    payload: {
      username: user,
      project_id,
      error: error,
    }
  }
}

export const removeProjectCollaboratorSuccess = (user, project_id, data) => {

  return {
    type: REMOVECOLLABORATOR_SUCCESS,
    payload: {
      username: user,
      project_id,
      collaborator: data,
    }
  }
}

export const removeProjectCollaboratorFail = (user, project_id, error=null) => {
  console.log(error)

  return {
    type: REMOVECOLLABORATOR_FAIL,
    payload: {
      username: user,
      project_id,
      error: error,
    }
  }
}

