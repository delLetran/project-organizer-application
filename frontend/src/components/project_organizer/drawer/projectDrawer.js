import { useState } from 'react'
// import { useEffect } from 'react'
// import { useDispatch } from 'react-redux'
// import { useSelector } from 'react-redux'
import Collaborators from './collaborators'
import { AddCollaborator } from './collaborators'
import Activities from './activities'

import { IconButton } from '@material-ui/core'
import { List } from '@material-ui/core'
import { ListItem } from '@material-ui/core'
import { ListItemText } from '@material-ui/core'
import { ListItemIcon } from '@material-ui/core'
import { ListItemSecondaryAction } from '@material-ui/core'

import { ArrowDropDown } from '@material-ui/icons'
import { ArrowDropUp } from '@material-ui/icons'
import { Assignment } from '@material-ui/icons'
import { Bookmark } from '@material-ui/icons'
import { Schedule } from '@material-ui/icons'
import { PersonAdd } from '@material-ui/icons'
import { PeopleAltRounded } from '@material-ui/icons'

const ProjectDrawer = ({project}) => {
  const [subList, setSubList] = useState({1:true})
  const [addCollabOpen, setAddCollabOpen] = useState(false)

  const handleSubList = (index) => {
    subList[index] ?
    setSubList({...subList, [index]: false})
    : setSubList({...subList, [index]: true})
    console.log(subList)
    
  }
  
  const menuList = [
    {'name':'Activities', 'desc':'Activities'},
    {'name':'Collaborators'},
    {'name':'Schedules' },
    {'name':'Bookmarks' },
  ]

  
  return  (
    <List align='left'>
      {menuList.map((item, index)=>(
        <div key={item.name}>
          <ListItem key={item.name} onClick={()=>handleSubList(index)}>
            <ListItemIcon>
              {index===0&&<Assignment fontSize="large" />}
              {index===1&&<PeopleAltRounded fontSize="large" />}
              {index===2&&<Schedule fontSize="large" />}
              {index===3&&<Bookmark fontSize="large" />} 
            </ListItemIcon>
            <ListItemText primary={item.name} secondary={item.desc && item.desc}/>

            <ListItemSecondaryAction>
              {subList[1] & index===1 ? 
                <IconButton color='secondary' onClick={()=>setAddCollabOpen(!addCollabOpen)}>
                  <PersonAdd fontSize="small" />
                </IconButton> : null
              }
              <IconButton color='secondary' onClick={()=>handleSubList(index)}>
                { subList[index] ? 
                  <ArrowDropUp fontSize="small" />
                  :
                  <ArrowDropDown fontSize="small" />
                }
              </IconButton>
            </ListItemSecondaryAction>
          </ListItem>

          { subList[1] & addCollabOpen & index===1 ? <AddCollaborator project_id={project.id} /> : null}
          { subList[0] & index===0 ? <Activities activities={project.activities}/> : null }
          { subList[1] & index===1 ? <Collaborators project={project}/> : null }
          {/* { subList[1] ? <Collaborators collaborators={project.collaborators}/> : null } */}
        </div>
      ))} 
    </List> 
  )
}



export default ProjectDrawer