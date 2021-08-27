import { useState } from 'react'
// import { useContext } from 'react';
// import { useSelector } from 'react-redux';
import { useHistory, useRouteMatch } from 'react-router'
import POAppBar from '../../appbar'
import PODrawer from '../drawer'
import POMain  from '../main'
// import Overview from './overview'

import { List, Typography } from '@material-ui/core'
import { ListItem } from '@material-ui/core'
import { ListItemText } from '@material-ui/core'
import { ListItemIcon } from '@material-ui/core'
import { ListItemSecondaryAction } from '@material-ui/core'
import { Box } from '@material-ui/system'
import { IconButton } from '@material-ui/core'

import { Assignment } from '@material-ui/icons'
import { Visibility } from '@material-ui/icons'
import { VisibilityOff } from '@material-ui/icons'

import CssBaseline from '@material-ui/core/CssBaseline'



const ProjectList = ({projects}) => {
  let { path } = useRouteMatch()
  const history = useHistory()
  const [selected, setSelected] = useState(null)
  const [openView, setOpenView] = useState([true])
  // const [openView, setOpenView] = useState([{id:1, value:true}, {id:2, value:true}])
  // const [openView, setOpenView] = useState([(0, true)])

  const handleProjectClick = (project, index) =>  {
    history.push(`${path}/${project.slug}`)
    setSelected(index)
    // history.push(`/device/detail`, { from: 'device detail page' } )
    // I can then access what the previous page was using history.location.state.from
  }


  const handleOpenView = (index) => {
    let arr = [...openView]
    arr[index] = false
    arr.map((val, i)=> i===index ? arr[i]=true : arr[i]=false)
    setOpenView(arr)
  }

  return ( 
    <Box sx={{ display: 'flex'}}>
      <CssBaseline />
      <POAppBar />
      <PODrawer> 
      <Typography variant='h5' align='center' sx={{mx:'1rem', marginTop:'1rem'}}>
        Projects
      </Typography>
      <List> 
        { projects &&
          projects.map((project, index )=>(
            <ListItem 
              button 
              key={project.id} 
              selected={index===selected}
              onClick={()=>handleProjectClick(project, index)}>
              <ListItemIcon>
                <Assignment fontSize="medium" />
              </ListItemIcon>
              <ListItemText primary={project.name}/>
              <ListItemSecondaryAction >
                <IconButton 
                color='secondary' 
                onClick={()=>{handleOpenView(index)}}
                >
                { openView[index]?
                  <Visibility fontSize="medium" />
                  : <VisibilityOff fontSize="medium" />
                }
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))
        }
      </List>  
      </PODrawer>
      <POMain>
      { projects ? projects.map((project, index)=>(
        <div key={index}>
          { openView[index] ? 
            <div>
            <Typography variant='h4' align='left' >
              OverView 
            </Typography>

            <Typography variant='h6' align='left' margin='1rem'>
              { project.name }
            </Typography>

            <Typography variant='p' align='left' marginLeft='2rem'>
              { project.description }
            </Typography>
            </div> : null
          } 
          </div>
        )) : <div>Loading</div>
      }
      </POMain>
    </Box>
  )
}

export default ProjectList