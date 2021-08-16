import {
  handelUpdateProjectCollaborator,
  handelGetProjectCollaborators,
  handelInviteProjectCollaborator,
  handelRemoveProjectCollaborator,
} from './project_action_handler'



export const updateProjectCollaborator = (project_id, collaborator_id, position) => {
  return dispatch => {
    handelUpdateProjectCollaborator(project_id, collaborator_id, position, dispatch)
  }
}

export const addProjectCollaborator = (project_id, collaborator) => {
  return dispatch => {
    handelInviteProjectCollaborator(project_id, collaborator, dispatch)
  }
}

export const removeProjectCollaborator = (project_id, collaborator) => {
  return dispatch => {
    handelRemoveProjectCollaborator(project_id, collaborator, dispatch)
  }
}

export const getProjectCollaborators = (project_id) => {
  return dispatch => {
    handelGetProjectCollaborators(project_id, dispatch)
  }
}



