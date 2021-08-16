import updateObject from '../uitility'

const initialState = {
  count: 0,
  user: null
}

export const counterReducer = (state=initialState, action) => {
  switch (action.type) {
    case "INCREMENT":
      return updateObject(state, {count: state.count + 1, user: action.payload.user})
    case "DECREMENT":
      return updateObject(state, {count: state.count - 1, user: action.payload.user})
    default:
      return state
  }
}
