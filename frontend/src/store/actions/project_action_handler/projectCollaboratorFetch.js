
import { 
  updateProjectCollaboratorSuccess,
  updateProjectCollaboratorFail,
  getProjectCollaboratorSuccess,
  getProjectCollaboratorFail,
  inviteProjectCollaboratorSuccess,
  inviteProjectCollaboratorFail,
  removeProjectCollaboratorSuccess,
  removeProjectCollaboratorFail,
} from "../project_action_response"


const baseURL = `http://localhost:8000/api/`


async function handelUpdateProjectCollaborator(project_id, collaborator_id, position, dispatch) {
  const url = `${baseURL}collaborator/${collaborator_id}/update/`
  const data = {"position": position}
  const resquestOption = {
    method: 'PUT',
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    }, 
    body: JSON.stringify(data)
  }

  const response = await fetch(url, resquestOption)
  // const string = await response.text();
  // const json = string === "" ? {} : JSON.parse(string);
  console.log(response)
  response.ok ?
    dispatch(updateProjectCollaboratorSuccess(project_id, collaborator_id, position))
    : dispatch(updateProjectCollaboratorFail(response))
}

const handelGetProjectCollaborators = (project_id, dispatch) => {
  const url = `${baseURL}collaborator/${project_id}/`
  const resquestOption = {
    method: 'GET',
    headers: {
      // "Content-Type": "application/json",
      // "Accept": "application/json",
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    }
  }
  fetch(url, resquestOption)
  .then( res => {
    return res.json()
  })
  .then(data =>{
    dispatch(getProjectCollaboratorSuccess(project_id, data))
  })
  .catch(error => { 
    dispatch(getProjectCollaboratorFail(project_id, error))
  })
}


const handelInviteProjectCollaborator = (user, project_id, dispatch) => {
  const url = `${baseURL}collaborator/${user}/${project_id}/invite/`
  const resquestOption = {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    }
  }
  fetch(url, resquestOption)
  .then( res => {
    return res.json()
  })
  .then(data =>{
    dispatch(inviteProjectCollaboratorSuccess(user, project_id, data))
  })
  .catch(error => { 
    dispatch(inviteProjectCollaboratorFail(user, project_id, error))
  })
}

async function handelRemoveProjectCollaborator( project_id, collaborator, dispatch) {
  const url = `${baseURL}collaborator/${collaborator}/${project_id}/remove/`
  const resquestOption = {
    method: 'PUT',
    headers: {
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    }
  }

  const response = await fetch(url, resquestOption)
  const string = await response.text();
  const json = string === "" ? {} : JSON.parse(string);
  console.log('response: ', response.status)
  console.log('string: ', string)
  console.log('json: ', json)
  response.ok ?
    dispatch(removeProjectCollaboratorSuccess(project_id, collaborator,json))
  : dispatch(removeProjectCollaboratorFail(project_id, collaborator))
}





// const _handelRemoveProjectCollaborator = (user, project_id, dispatch) => {
//   const url = `${baseURL}collaborator/${user}/${project_id}/remove/`
//   const resquestOption = {
//     method: 'PUT',
//     headers: {
//       "Content-Type": "json",
//       "Accept": "application/json",
//       "Authorization": `Bearer ${localStorage.getItem("access_token")}`
//     }, 
//     // body: JSON.stringify({})
//   }
//   fetch(url, resquestOption)
//   .then( res => {
//     return res.json()
//   })
//   .then(data =>{
//     dispatch(removeProjectCollaboratorSuccess(user, project_id, data))
//   })
//   .catch(error => { 
//     dispatch(removeProjectCollaboratorFail(user, project_id, error))
//   })
// }


// async function __handelRemoveProjectCollaborator(user, project_id, dispatch) {
//   const url = `${baseURL}collaborator/${user}/${project_id}/remove/`
//   const resquestOption = {
//     method: 'PUT',
//     headers: {
//       // "Content-Type": "json",
//       // "Accept": "application/json",
//       "Authorization": `Bearer ${localStorage.getItem("access_token")}`
//     }, 
//     // body: JSON.stringify({})
//   }

//   const response = await fetch(url, resquestOption)
//   const string = await response.text();
//   const json = string === "" ? {} : JSON.parse(string);
//   console.log('response: ', response)
//   console.log('string: ', string)
//   console.log('json: ', json)
//   fetch(url, resquestOption)
//   .then( res => {
//     return res.json()
//   })
//   .then(data =>{
//     dispatch(removeProjectCollaboratorSuccess(user, project_id, data))
//   })
//   .catch(error => { 
//     dispatch(removeProjectCollaboratorFail(user, project_id, error))
//   })
// }






export {
  handelUpdateProjectCollaborator,
  handelGetProjectCollaborators,
  handelInviteProjectCollaborator,
  handelRemoveProjectCollaborator,
}