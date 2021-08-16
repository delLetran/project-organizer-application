import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { authLogin, authLogout } from '../../store/actions'
import Button from '@material-ui/core/Button';
import Avatar from '@material-ui/core/Avatar';
import Badge from '@material-ui/core/Badge';
import AccountCircle from '@material-ui/icons/AccountCircle'


export function Logout(){
  const [credentials, setCredentials] = useState({'email': '', 'password': ''})
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const dispatch = useDispatch()
  
  const handleOnChange = (e) => {
    const {name, value} = e.target
    setCredentials({...credentials, [name]: value})
  }
  
  const handleKeypress = e => {
  if (e.keyCode === 13) {
    dispatch(authLogin(credentials))
  }
};

  return (
    <div>
      <span className="avatar-item">
        <Badge count={27}>
          <Avatar shape="circle" icon={<AccountCircle />} />
        </Badge>
      </span>
      <br/>
      { isAuthenticated ? 
        <Button type="Danger" onClick={()=>dispatch(authLogout())}>Logout</Button>
      : 
        <form onSubmit={e=>e.preventDefault()}>
          <label>
            Email:
            <input 
              type='email'
              name='email'
              value={credentials.email}
              onChange={(e) => handleOnChange(e) }
            />
          </label>
          <br />
          <label>
            Password:
            <input 
              type='password' 
              name='password' 
              value={credentials.password}
              onChange={(e) => handleOnChange(e) }
              onKeyPress={handleKeypress}
            />
          </label>
          <Button type="primary" onClick={()=>dispatch(authLogin(credentials))}>Login</Button>
        </form>
      }
    </div>
  ) 
}





// let base64 = require('base-64');

// let url = 'http://eu.httpbin.org/basic-auth/user/passwd';
// let username = 'user';
// let password = 'passwd';
// let headers = new Headers();
// headers.append('Authorization', 'Basic ' + username + ":" + password);

// fetch(url, {method:'GET',
//         headers: headers,
//         //credentials: 'user:passwd'
//        })
// .then(res => res.json())
// .then(data => console.log(data));

// function parseJSON(response) {
// return response.json()
// }



// import React, { useState } from 'react'
// import { useDispatch } from 'react-redux'
// import { authLogin } from '../store/actions'
// import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
// import { useDispatch, useSelector } from 'react-redux'
// import { increment, decrement} from './store/actions'

// export function UserLogin(props){
//   const [credentials, setCredentials] = useState({'email': '', 'password': ''})
//   const dispatch = useDispatch()

//   const handleLogin = (e) => {
//     e.preventDefault();
//     dispatch()
//     const url = `http://localhost:8000/api/token/`
//     const resquestOption = {
//       method: 'POST',
//       headers: {
//         "Content-Type": "application/json",
//         "Accept": "application/json" 
//       }, 
//       body:  JSON.stringify(credentials)
//     }
//     fetch(url, resquestOption)
//     .then( res => {
//       if (!res.ok) 
//         throw new Error('Something went wrong')
//       return res.json()
//     })
//     .then(data =>{
//       localStorage.setItem("access_token", data['access'])
//       localStorage.setItem("refresh_token", data['refresh'])
//       const aToken = localStorage.getItem("access_token")
//       const rToken = localStorage.getItem("refresh_token")
//       console.log(aToken)
//       console.log(rToken)
//     })
//     .catch(error => console.error(error))
//   }

//   const handleOnChange = (e) => {
//     const {name, value} = e.target
//     setCredentials({...credentials, [name]: value})
//   }

//   return (
//     <>
//       <h2>User Login</h2>
//       <form>
//         <label>
//           Email:
//           <input 
//             type='email'
//             name='email'
//             value={credentials.email}
//             onChange={(e) => handleOnChange(e) }
//           />
//         </label>
//         <label>
//           Password:
//           <input 
//             type='password' 
//             name='password' 
//             value={credentials.password}
//             onChange={(e) => handleOnChange(e) }
//           />
//         </label>
//         <button onClick={(e) => handleLogin(e) }>Login</button>
//       </form>
//     </>
//   ) 
// }




// // let base64 = require('base-64');

// // let url = 'http://eu.httpbin.org/basic-auth/user/passwd';
// // let username = 'user';
// // let password = 'passwd';
// // let headers = new Headers();
// // headers.append('Authorization', 'Basic ' + username + ":" + password);

// // fetch(url, {method:'GET',
// //         headers: headers,
// //         //credentials: 'user:passwd'
// //        })
// // .then(res => res.json())
// // .then(data => console.log(data));

// // function parseJSON(response) {
// // return response.json()
// // }
