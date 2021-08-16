import { useState } from 'react'
// import { useEffect } from 'react'
import { useDispatch } from 'react-redux'
// import { useSelector } from 'react-redux'
// import { getProjectCollaborators } from '../../../store/actions'
// import { addProjectCollaborator } from '../../../store/actions'
import { removeProjectCollaborator } from '../../../store/actions'
import { updateProjectCollaborator } from '../../../store/actions'

import { IconButton } from '@material-ui/core'
import { List } from '@material-ui/core'
import { ListItem } from '@material-ui/core'
import { ListItemText } from '@material-ui/core'
import { ListItemIcon } from '@material-ui/core'
import { ListItemSecondaryAction } from '@material-ui/core'
import { FormControl } from '@material-ui/core'
import { Select } from '@material-ui/core'
import { InputLabel } from '@material-ui/core'
import { MenuItem } from '@material-ui/core'

import { AccountBox } from '@material-ui/icons'
import { Delete } from '@material-ui/icons'
import { Edit } from '@material-ui/icons'
import { Save } from '@material-ui/icons'
import { addProjectCollaborator } from '../../../store/actions'
import { Add } from '@material-ui/icons'




const Collaborators = ({project}) => {
  const collaborators = project.collaborators

  const dispatch = useDispatch()
  const [updateCollabOpen, setUpdateCollabOpen] = useState({0:false})
  const [value, setValue] = useState('')

  const positions = ['Project Admin', 'Project Manager', 'Project Leader', 'Member', 'Spectator' ]

  const handleCollaboratorRemove = (username, project_id) => {
    dispatch(removeProjectCollaborator(username, project_id))
  }
  
  const handleOpenUpdate = (index) => {
    let obj = {...updateCollabOpen}
    obj[index] ? obj[index]=false : obj[index]=true
    let k = Object.keys(obj)
    k.map((id)=> (id!==String(index) ?
    obj[id] = false
    : obj[id] = true))
    setUpdateCollabOpen(obj)
  }
  
  const handleCollaboratorUpdate = (project_id, collaborator_id, position, index) => {
    dispatch(updateProjectCollaborator(project_id, collaborator_id, position))
    handleOpenUpdate(index)
  }

  const handleChange = (event) => {
    setValue(event.target.value);
  }

  return (
      <div>
        {collaborators ?
          <List sx={{marginLeft:'1rem'}}>
            { collaborators.map((collaborator, index)=>(
              <div key={collaborator.name.id}> 
                <ListItem button key={collaborator.name.username} disablePadding>
                  <ListItemIcon>
                    <AccountBox fontSize="small" />
                  </ListItemIcon>
                  <ListItemText   
                    primary={collaborator.name.username} 
                    secondary={(collaborator.status === 'Joined')  ? collaborator.position : collaborator.status}
                    sx={{fontSize:'2rem'}}
                    />
                  <ListItemSecondaryAction>
                    {(collaborator.status ==='Joined' & collaborator.name.username !== project.created_by.username) ?
                      <IconButton 
                        color='secondary' 
                        onClick={()=>handleOpenUpdate(index)}>
                        <Edit fontSize="small" />
                      </IconButton>
                      : null
                    }
                    {(collaborator.name.username !== project.created_by.username) ?
                        <IconButton 
                          color='secondary' 
                          onClick={()=>handleCollaboratorRemove(collaborator.name.username, project.id)}>
                          <Delete fontSize="small" />
                        </IconButton>
                      : null
                    }
                  </ListItemSecondaryAction>
                </ListItem>
                { (updateCollabOpen[index] & collaborator.name.username !== project.created_by.username) ? 
                  <div>
                    <FormControl variant='standard' sx={{ marginLeft: '2rem', width: 180}}>
                      <InputLabel>Position</InputLabel>
                      <Select
                        value={value}
                        onChange={handleChange}
                        label="Position"
                      >
                      { positions.map((position)=>(
                        <MenuItem key={position} value={position}>
                          {position}
                        </MenuItem>
                      ))}
                      </Select>
                    </FormControl>
                    <IconButton 
                      color='secondary' 
                      sx={{ mx:'0.5rem', marginTop:'1rem'}}
                      onClick={()=>handleCollaboratorUpdate(project.id, collaborator.id, value, index)}>
                      <Save fontSize="medium" />
                    </IconButton>
                  </div> 
                  : null
                }
              </div> 
            ))}
          </List>
          : null
        } 
      </div>
  )
}


export const AddCollaborator = ({project_id}) => {
  const dispatch = useDispatch()
  const [value, setValue] = useState('')

  const associates = [
    {id:1, username:'delletran'},
    {id:2, username:'test_user2'},
    {id:3, username:'test_user3'},
    {id:4, username:'test_user4'},
  ]

  const handleCollaboratorAdd = () => {
    dispatch(addProjectCollaborator(value, project_id))
  }

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <div>
      <FormControl variant='standard' sx={{marginLeft: '2rem', width: 180}}>
        <InputLabel>User</InputLabel>
        <Select
          value={value}
          onChange={handleChange}
          label="Associates"
        >
        { associates.map((user)=>(
          <MenuItem key={user.id} value={user.username}>
            {user.username}
          </MenuItem>
        ))}


        </Select>
      </FormControl>
      <IconButton 
        color='secondary' 
        sx={{ mx:'0.5rem', marginTop:'1rem'}}
        onClick={handleCollaboratorAdd}>
        <Add fontSize="medium" />
      </IconButton>
    </div>
  )
}


              //  <div key={collaborator.name.id}> 
              //   {/* {updateCollabOpen ? <UpdateCollaboratorPosition collaborator={collaborator}/> : null} */}

              //  </div> 

// const UpdateCollaboratorPosition = ({collaborator}) => {
//   const dispatch = useDispatch()
//   const [value, setValue] = useState('')

//   const positions = ['Project Admin', 'Project Manager', 'Project Leader', 'Member', 'Spectator' ]

//   const handleCollaboratorUpdate = (collaborator_id, position) => {
//     dispatch(updateProjectCollaborator(collaborator_id, position))
//   }

//   const handleChange = (event) => {
//     setValue(event.target.value);
//   };

//   return (
//     <div>
//       <FormControl variant='standard' sx={{ marginLeft: 'rem', width: 150}}>
//         <InputLabel>Position</InputLabel>
//         <Select
//           value={value}
//           onChange={handleChange}
//           label="Position"
//         >
//         { positions.map((position)=>(
//           <MenuItem key={position} value={position}>
//             {position}
//           </MenuItem>
//         ))}
//         </Select>
//       </FormControl>
//       <IconButton color='secondary' onClick={()=>handleCollaboratorUpdate(collaborator.id, value)}>
//         <Save fontSize="small" />
//       </IconButton>
//     </div>
//   )
// }

export default Collaborators
