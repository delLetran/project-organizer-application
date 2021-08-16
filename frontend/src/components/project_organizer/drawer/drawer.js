// import { useState } from 'react'
// import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
// import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
// import { useParams } from 'react-router'
// import { useHistory } from 'react-router-dom'
import { openDrawer, closeDrawer } from '../../../store/actions'
// import { getProjectCollaborators } from '../../../store/actions'
// import { addProjectCollaborator } from '../../../store/actions'
// import { removeProjectCollaborator } from '../../../store/actions'
import { styled } from '@material-ui/core/styles'
// import { useTheme } from '@material-ui/core/styles'
// import Collaborators from './collaborators'

import { IconButton } from '@material-ui/core'
// import { Button } from '@material-ui/core'
import { Divider } from '@material-ui/core'
import { Drawer } from '@material-ui/core'
import { List } from '@material-ui/core'
import { ListItem } from '@material-ui/core'
import { ListItemText } from '@material-ui/core'
import { ListItemIcon } from '@material-ui/core'
// import { ListItemSecondaryAction } from '@material-ui/core'
// import { Typography } from '@material-ui/core'
// import { InputLabel } from '@material-ui/core'
// import { MenuItem } from '@material-ui/core'
// import { FormControl } from '@material-ui/core'
// import { Select } from '@material-ui/core'


// import { ArrowDropDown } from '@material-ui/icons'
// import { ArrowDropUp } from '@material-ui/icons'
// import { Assignment } from '@material-ui/icons'
// import { AccountBox } from '@material-ui/icons'
// import { Bookmark } from '@material-ui/icons'
// import { Schedule } from '@material-ui/icons'
import { NoteAddSharp } from '@material-ui/icons'
import { Star } from '@material-ui/icons'
// import { Add } from '@material-ui/icons'
// import { PersonAdd } from '@material-ui/icons'
// import { PeopleAltRounded } from '@material-ui/icons'
// import { Delete } from '@material-ui/icons'
import { ChevronLeft } from '@material-ui/icons'

export const drawerWidth = 300;

export const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end',
}));



const PODrawer = ({project, children}) => {
  const dispatch = useDispatch()
  // const theme = useTheme()
  // const projects = useContext(ProjectContext)
  const dashb = useSelector(state => state.dashboard)
  const drawerOpen = dashb.drawer.isOpen


  const handleDrawer = () => {
    drawerOpen ? dispatch(closeDrawer()) : dispatch(openDrawer())
  }
  return (
    <Drawer
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: drawerWidth,
          boxSizing: 'border-box',
        },
      }}
      variant="persistent"
      anchor="left"
      open={drawerOpen}
    >
      <DrawerHeader>
        {/* insert Logo here... */}
        <IconButton onClick={handleDrawer}>
          <ChevronLeft />
        </IconButton>
      </DrawerHeader>
      <Divider/>
      {children}
      
      <Divider/>
      <List>
        {['Notes', 'Important'].map((item, index)=>(
        <ListItem button key={item} >
          <ListItemIcon>
            {index===0&&<NoteAddSharp/>}
            {index===1&&<Star/>}
          </ListItemIcon>
          <ListItemText primary={item}/>
        </ListItem>
        ))}
      </List>
    </Drawer>
  )
}

// export const ProjectDrawer = ({project}) => {
//   const dispatch = useDispatch()
//   const [subList, setSubList] = useState({1:true})
//   const [addCollabOpen, setAddCollabOpen] = useState(false)
//   const collaborators = useSelector(state => state.collaborator.collaborators)

//   const handleSubList = (index) => {
//     subList[index] ?
//     setSubList({...subList, [index]: false})
//     : setSubList({...subList, [index]: true})
//   }

//   useEffect(()=>{
//     dispatch(getProjectCollaborators(project.id))
//   }, [])
  
//   const menuList = [
//     {'name':'Activities', 'desc':'Activities'},
//     {'name':'Collaborators'},
//     {'name':'Schedules' },
//     {'name':'Bookmarks' },
//   ]

  
//   // const handleCollaboratorAdd = (username='test_user3', project_id=1) => {
//   //   console.log(`Add Collaborator-popover`)
//   //   setAddCollaboratorOpen(!addCollaboratorOpen)
//   //   // dispatch(addProjectCollaborator(username, project_id))
//   // }
  
//   return  (
//     <List align='left'>
//       {menuList.map((item, index)=>(
//         <div key={item.name}>
//           <ListItem key={item.name} onClick={()=>handleSubList(index)}>
//             <ListItemIcon>
//               {index===0&&<Assignment fontSize="large" />}
//               {index===1&&<PeopleAltRounded fontSize="large" />}
//               {index===2&&<Schedule fontSize="large" />}
//               {index===3&&<Bookmark fontSize="large" />} 
//             </ListItemIcon>
//             <ListItemText primary={item.name} secondary={item.desc && item.desc}/>

//             <ListItemSecondaryAction>
//               {subList[1] & index===1 ? 
//                 <IconButton color='secondary' onClick={()=>setAddCollabOpen(!addCollabOpen)}>
//                   <PersonAdd fontSize="small" />
//                 </IconButton> : null
//               }
//               <IconButton color='secondary' onClick={()=>handleSubList(index)}>
//                 { subList[index] ? 
//                   <ArrowDropUp fontSize="small" />
//                   :
//                   <ArrowDropDown fontSize="small" />
//                 }
//               </IconButton>
//             </ListItemSecondaryAction>
//           </ListItem>

//           { subList[1] & addCollabOpen & index===1 ? <AddCollaborator project_id={project.id} /> : null}
//           { subList[0] & index===0 ? <Activities activities={project.activities}/> : null }
//           { subList[1] & index===1 ? <Collaborators project={project} collaborators={collaborators} /> : null }
//           {/* { subList[1] ? <Collaborators collaborators={project.collaborators}/> : null } */}
//         </div>
//       ))} 
//     </List> 
//   )
// }


// const AddCollaborator = ({project_id}) => {
//   const dispatch = useDispatch()
//   const [value, setValue] = useState('')

//   const associates = [
//     {id:1, username:'delletran'},
//     {id:2, username:'test_user2'},
//     {id:3, username:'test_user3'},
//   ]

//   const handleCollaboratorAdd = () => {
//     dispatch(addProjectCollaborator(value, project_id))
//   }

//   const handleChange = (event) => {
//     setValue(event.target.value);
//   };

//   return (
//     <div>
//       <FormControl variant='standard' sx={{m: 1, mx: '2rem', width: 150}}>
//         <InputLabel>User</InputLabel>
//         <Select
//           value={value}
//           onChange={handleChange}
//           label="A ssociates"
//         >
//         { associates.map((user)=>(
//           <MenuItem key={user.id} value={user.username}>
//             {user.username}
//           </MenuItem>
//         ))}
//         </Select>
//       </FormControl>
//       <IconButton color='secondary' onClick={handleCollaboratorAdd}>
//         <Add fontSize="medium" />
//       </IconButton>
//     </div>
//   )
// }

// const Activities = (props) => {
//   const handleActivityList = () => {

//   }
//   return (
//     <List sx={{marginLeft:'1rem'}}>
//       { props.activities.map((activity, index)=>(
//         <div key={activity.name}>
//           {/* <Typography variant='p' align='left'>
//             { activity.name.substr(0, 15) }
//           </Typography> */}
//           <ListItem button key={activity.name} onClick={()=>handleActivityList(1)}>
//             <ListItemIcon>
//               <Assignment fontSize="small" />
//             </ListItemIcon>
//             <ListItemText primary={activity.name}/>
//           </ListItem>
//         </div>
//       ))}
//     </List> 
//   )
// }


// const Collaborators = ({project, collaborators}) => {
//   const dispatch = useDispatch()

//   const handleCollaboratorRemove = (username, project_id) => {
//     console.log(`Remove Collaborator ${username} from project_id: ${project_id}`)
//     dispatch(removeProjectCollaborator(username, project_id))
//   }
  
//   return (
//       <div>
//         {collaborators ?
//           <List sx={{marginLeft:'3rem'}}>
//             { collaborators.map((collaborator, index)=>(
//               <ListItem button key={collaborator.name.username} disablePadding>
//                 <ListItemIcon>
//                   <AccountBox fontSize="small" />
//                 </ListItemIcon>
//                 <ListItemText   
//                   primary={collaborator.name.username} 
//                   secondary={(collaborator.status === 'Joined')  ? collaborator.position : collaborator.status}
//                   sx={{fontSize:'2rem'}}
//                   />
//                 {(collaborator.name.username !== project.created_by.username) ?
//                   <ListItemSecondaryAction>
//                     <IconButton 
//                       color='secondary' 
//                       onClick={()=>handleCollaboratorRemove(collaborator.name.username, project.id)}>
//                       <Delete fontSize="small" />
//                     </IconButton>
//                   </ListItemSecondaryAction>
//                   : null
//                 }
//               </ListItem>
//             ))}
//           </List>
//           : null
//         } 
      
//         {/* { collaborators ? collaborators.map((collaborator)=>(
//           collaborator.name ?
//             <MenuItem key={collaborator.id} value={collaborator.name.username}>
//             {collaborator.name.username}
//               <IconButton 
//                 color='secondary' 
//                 onClick={()=>handleCollaboratorRemove(collaborator.name.username, project.id)}>
//                 <Delete fontSize="small" />
//               </IconButton>
//             </MenuItem>
//           : null
//         )) : null} */}
//       </div>
//   )
// }

        

// export function SelectVariants() {
//   const [age, setAge] = useState('');

//   const handleChange = (event) => {
//     setAge(event.target.value);
//   };

//   return (
//     <div>
//       <FormControl variant="standard" sx={{ m: 1, minWidth: 120 }}>
//         <InputLabel id="demo-simple-select-standard-label">Age</InputLabel>
//         <Select
//           labelId="demo-simple-select-standard-label"
//           id="demo-simple-select-standard"
//           value={age}
//           onChange={handleChange}
//           label="Age"
//         >
//           <MenuItem value="">
//             <em>None</em>
//           </MenuItem>
//           <MenuItem value={10}>Ten</MenuItem>
//           <MenuItem value={20}>Twenty</MenuItem>
//           <MenuItem value={30}>Thirty</MenuItem>
//         </Select>
//       </FormControl>
//     </div>
//   );
// }
//   return (
//     <List sx={{marginLeft:'1rem'}}>
//       { props.activities.map((activity, index)=>(
//         <div key={activity.name}>
//           {/* <Typography variant='p' align='left'>
//             { activity.name.substr(0, 15) }
//           </Typography> */}
//           <ListItem button key={activity.name} onClick={()=>handleActivityList(1)}>
//             <ListItemIcon>
//               <Assignment fontSize="small" />
//             </ListItemIcon>
//             <ListItemText primary={activity.name}/>
//           </ListItem>
//         </div>
//       ))}
//     </List> 
//   )
// }

// const [drawer, setDrawer] = useState({0:true})
// const handleSubDrawer = (item) => {
//   drawer[item] ?
//   setDrawer({...drawer, [item]: false})
//   : setDrawer({...drawer, [item]: true})
// }
  
// return  (
//   <List>
//     {activities.map((item, index)=>(
//       <div key={item.name}>
//         <ListItem button key={item.name} onClick={()=>handleSubDrawer(index)}>
//           <ListItemIcon>
//             {index===0&&<Assignment fontSize="large" />}
//             {index===1&&<AccountBox fontSize="large" />}
//             {index===2&&<Schedule fontSize="large" />}
//             {index===3&&<Bookmark fontSize="large" />} 
//           </ListItemIcon>
//           <ListItemText primary={item.name} secondary={item.desc}/>
//           { drawer[index] ?
//             <ArrowDropUp fontSize="small" />
//             :
//             <ArrowDropDown fontSize="small" />
//           }
//         </ListItem>
//         { drawer[index] && <DrawerSubList name={item}/> }
//       </div>
//     ))} 
//   </List> 
// )




export default PODrawer