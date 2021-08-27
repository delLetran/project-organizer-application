import { useEffect } from "react"
import { useState } from "react";
import { useDispatch } from 'react-redux'
import { useSelector } from 'react-redux'
import { useHistory } from "react-router";
import { getUser } from "../store/actions";
import { setRedirect } from "../store/actions";
import { Button } from "@material-ui/core";
import { Switch, Redirect, Route } from "react-router";
import { useParams } from "react-router"

// import { useDispatch, useSelector } from 'react-redux'

export const TestComponent = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const auth_user = useSelector(state=>state.user.auth_user.data)
  const email = useSelector(state=>state.auth.auth_user_email)
  const [count, setCount] = useState(0)
  
  useEffect(() => {
    dispatch(getUser('delletran')) 
  }, [])


  const redirect = useSelector(state => state.router.redirect)
  // console.log('redirect: ', redirect)

  useEffect(() => {
    // history.push(`/test/${redirect}`) 
    console.log('redirect: ', redirect)
  }, [redirect])

  const handleRedirect = () => {
    setCount(() => count + 1)
    dispatch(setRedirect('/projects')) 
  }

  return (
    <div>
    {auth_user.username}
    {count}
      <Button onClick={handleRedirect}>Set redirect</Button>
      
    </div>
  )
}

