// import updateObject from '../uitility'

const initialState = {
  project_list:null
}

export const projectReducer = (state=initialState, action) => {
  switch (action.type) {
    case 'GETPROJECTLIST_SUCCESS':
      return {...state, 
        project_list: action.payload.project_list
      }
    case 'GETPROJECTLIST_FAIL':
      return {...state, 
        error: action.payload.error
      }
    case 'GETPROJECTDETAILS_SUCCESS':
      return ({...state,
        project_list: state.project_list.map(
          (project, project_index) => (project.id === action.payload.project_id) ? {
            project: action.payload.project
          } : project
        )
      }) 
    case 'GETPROJECTDETAILS_FAIL':
      return {...state,
        error: action.payload.error
      }

    case 'ADDCOLLABORATOR_SUCCESS':
      return {...state,
        project_list: state.project_list.map(
          (project, project_index) => (project.id === action.payload.project_id) ? {
            ...project, 
            collaborators: [...project.collaborators, action.payload.collaborator]
          } : project
        )
      }
    case 'ADDCOLLABORATOR_FAIL':
      return {...state,
        error: action.payload.error
      }
    case 'REMOVECOLLABORATOR_SUCCESS':
      return {...state,
        project_list: state.project_list.map(
          (project, project_index) => (project.id === action.payload.project_id) ? {
            ...project, 
            collaborators: project.collaborators.filter(collaborator => 
              collaborator.name.username !== action.payload.username)
            // ),
          } : project
        )
      }
    case 'REMOVECOLLABORATOR_FAIL':
      return {...state,
        error: action.payload.error
      }
    case 'UPDATECOLLABORATORPOSITION_SUCCESS':
      return {...state,
        project_list: state.project_list.map(
          (project, project_index) => (project.id === action.payload.project_id) ? {
            ...project, 
            collaborators: project.collaborators.map(
              (collaborator, index) => (collaborator.id === action.payload.collaborator_id) ? 
              { ...collaborator, 
                position: action.payload.position
              } : collaborator
            ),
          } : project
        )
      }
    case 'UPDATECOLLABORATORPOSITION_FAIL':
      return {...state,
        error: action.payload.error
      }
    default:
      return state
  }
}



// const reducer = (state, action) => {
//   swicth(action.type){
//    case PREPEND_PROJECT: 
//     return { // returning a copy of orignal state 
//      ...state, //spreading the original state
//      projects: [action.payload, ...state.projects] // new projects array
//     }

//  case APPEND_PROJECT: 
//    return { // returning a copy of orignal state 
//     ...state, //copying the original state
//     projects: [...state.projects, action.payload] //new projects array 
//    }
//    default: return state;
//   }


// const reducer = (state, action) => {
//   swicth(action.type){
//    case DELETE_PROJECT: 
//     return {  // returning a copy of orignal state
//      ...state, //copying the original state
//      projects: state.projects.filter(project => project.id !== action.payload) 
//                                 // returns a new filtered projects array
//    }
//   }
//  }


// case COMPLETE_PROJECT: {
//   const index = state.projects.findIndex(project => project.id !==                                                                        action.payload); //finding index of the item
//   const newArray = [...state.projects]; //making a new array
//   newArray[index].completed = true//changing value in the new array
//   return { 
//    ...state, //copying the orignal state
//    projects: newArray, //reassingning projects to new array
//   }
//  }


// case INSERT_PROJECT: {
//   const newArray = [...state.projects]; //Copying state array
//   newArray.splice(2, 0, action.payload);
//   //using splice to insert at an index
//  return {
//   ...state,
//   projects: newArray //reassigning projects array to new array
//   }
//  }

// let index=1;// probably action.payload.id
// case 'SOME_ACTION':
//    return { 
//        ...state, 
//        contents: [
//           ...state.contents.slice(0,index),
//           {title: "some other title", text: "some other text"},
//          ...state.contents.slice(index+1)
//          ]
//     }