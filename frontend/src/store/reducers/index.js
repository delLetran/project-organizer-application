import { combineReducers } from 'redux'

import { authReducer as auth } from './auth'
import { dashboardReducer as dashboard } from './dashboard'
import { projectReducer as project } from './project'
import { userReducer as user } from './user'
// import { collaboratorReducer as collaborator } from './projectCollaborators'
// import { counterReducer as counter } from './counter'

const _reducers = combineReducers({
  auth: auth,
  dashboard,
  project,
  user,
  // collaborator,
  // counter: counter,
})


export default _reducers 

export {
  auth,
  dashboard,
  project,
  user,
  // collaborator,
  // counter,
}