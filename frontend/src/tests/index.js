import { useEffect } from "react"
import { useDispatch } from 'react-redux'
import { useSelector } from 'react-redux'
import { getUser } from "../store/actions";
// import { useDispatch, useSelector } from 'react-redux'

export const TestComponent = () => {
  const dispatch = useDispatch()
  const auth_user = useSelector(state=>state.user.auth_user.data)
  const email = useSelector(state=>state.auth.auth_user_email)
  console.log(email, auth_user)
    
  useEffect(() => {
    dispatch(getUser('delletran')) 
  }, [])

  return (
    <div>{auth_user.username}</div>
  )
}