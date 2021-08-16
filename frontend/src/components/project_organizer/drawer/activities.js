// import { useState } from 'react'
// import { useEffect } from 'react'
// import { useSelector, useDispatch } from 'react-redux'

// import { IconButton } from '@material-ui/core'
import { List } from '@material-ui/core'
import { ListItem } from '@material-ui/core'
import { ListItemText } from '@material-ui/core'
import { ListItemIcon } from '@material-ui/core'
// import { ListItemSecondaryAction } from '@material-ui/core'

import { Assignment } from '@material-ui/icons'

const Activities = (props) => {
  const handleActivityList = () => {

  }
  return (
    <List sx={{marginLeft:'1rem'}}>
      { props.activities.map((activity, index)=>(
        <div key={activity.name}>
          {/* <Typography variant='p' align='left'>
            { activity.name.substr(0, 15) }
          </Typography> */}
          <ListItem button key={activity.name} onClick={()=>handleActivityList(1)}>
            <ListItemIcon>
              <Assignment fontSize="small" />
            </ListItemIcon>
            <ListItemText primary={activity.name}/>
          </ListItem>
        </div>
      ))}
    </List> 
  )
}

export default Activities