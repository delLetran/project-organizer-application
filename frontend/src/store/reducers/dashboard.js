import updateObject from '../uitility'

const initialState = {
  menu :{
    isOpen: false
  },
  drawer :{
    isOpen: false
  }
}

export const dashboardReducer = (state=initialState, action) => {
  switch (action.type) {
    case "OPENMENU":
      return updateObject(state, {menu:{isOpen: true}})
    case "CLOSEMENU":
      return updateObject(state, {menu:{isOpen: false}})
    case "OPENDRAWER":
      return updateObject(state, {drawer:{isOpen: true}})
    case "CLOSEDRAWER":
      return updateObject(state, {drawer:{isOpen: false}})
    default:
      return state
  }
}
