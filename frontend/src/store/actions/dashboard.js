import * as actionTypes from './actionTypes'


export const openMenu = () => {
  return {
    type: actionTypes.OPENMENU,
    menu :{
      isOpen: true
    }
  }
}

export const closeMenu = () => {
  return {
    type: actionTypes.CLOSEMENU,
    menu :{
      isOpen: false
    }
  }
}

export const openDrawer = () => {
  return {
    type: actionTypes.OPENDRAWER,
    drawer :{
      isOpen: true
    }
  }
}

export const closeDrawer = () => {
  return {
    type: actionTypes.CLOSEDRAWER,
    drawer :{
      isOpen: false
    }
  }
}