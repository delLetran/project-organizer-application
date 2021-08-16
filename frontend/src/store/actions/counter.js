import { INCREMENT, DECREMENT } from "./actionTypes"

const increment = () => {
  return {
    type: INCREMENT,
    payload: {
      user: 'user_incrementer'
    }
  }
}

const decrement = () => {
  return {
    type: DECREMENT,
    payload: {
      user: 'user_decrementer'
    }
  }
}

export { increment, decrement } 