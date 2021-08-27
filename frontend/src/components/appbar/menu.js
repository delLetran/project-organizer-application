import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router';
// import { Link } from 'react-router';
import { openMenu, closeMenu } from '../../store/actions';
// import { authLogin } from '../../store/actions';
import { authLogout } from '../../store/actions';

import { IconButton } from '@material-ui/core';
import { Divider } from '@material-ui/core';
import { Badge } from '@material-ui/core';
import { Popover } from '@material-ui/core';
import { List  } from '@material-ui/core';
import { ListItem } from '@material-ui/core';
import { ListItemText } from '@material-ui/core';
import { ListItemIcon } from '@material-ui/core';
import { Box } from '@material-ui/core';
import { ClickAwayListener } from '@material-ui/core';
import { Button } from '@material-ui/core';

import { MoreVert } from '@material-ui/icons';
import { ExpandLess } from '@material-ui/icons';
import { ExpandMore } from '@material-ui/icons';
import { ExitToApp } from '@material-ui/icons';
import { AccountCircle } from '@material-ui/icons';
import { Settings } from '@material-ui/icons';
import { ContactsSharp } from '@material-ui/icons';
import { MessageRounded } from '@material-ui/icons';
import { BuildSharp } from '@material-ui/icons';
import { Assignment } from '@material-ui/icons';



const AppMenu = () => {
  const [anchorEl, setAnchorEl] = useState(null)
  const menuOpen = useSelector(state => state.dashboard.menu.isOpen)
  const is_authenticated = useSelector(state => state.auth.isAuthenticated)
  const dispatch = useDispatch()
  const history = useHistory()
  
  const handleMenu = (e) => {
    setAnchorEl(e.currentTarget)
    menuOpen ? dispatch(closeMenu()) : dispatch(openMenu())
  }

  return( is_authenticated ?
    <Box  
      sx={{ 
        marginLeft: "auto", 
        position: 'relative'
      }}>
      <AccountCircle 
        sx={{
          position: 'relative',
          top:'12px',
          right: '10px'
        }}
        fontSize="large"
      />
      { menuOpen ? 
        <IconButton 
          id="menu-popover"
          onClick={handleMenu}
        >
          <ExpandLess/>  
        </IconButton> 
        :
        <Button 
          id='auth-menu'
          variant='contained'
          color='secondary' 
          onClick={handleMenu} 
          endIcon={ <ExpandMore/> }
        >
          Auth_Username
        </Button>
      }
        {/* <IconButton  
          onClick={handleMenu}
          >
          <Badge badgeContent={31} color="secondary">
            <MoreVert/>  
          </Badge>
        </IconButton>  */}
      <Popover   
        id="app-menu"
        open={menuOpen}
        anchorEl={anchorEl}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'right',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}>
        <MenuItems/>
      </Popover>
    </Box>
    :
    <Box
      sx={{ marginLeft: "auto", 
      position: 'relative'
    }}>
      <Button 
      variant='contained'
       color='secondary' 
       onClick={()=>history.push('/login')} 
      >
        LOGIN
      </Button>
    </Box>
  )
}

const MenuItems = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const menuOpen = useSelector(state => state.dashboard.menu.isOpen)


  const handleClickAway = () => {
    menuOpen && dispatch(closeMenu()) 
  }

  const handleProfile = () => {
    handleClickAway()
    history.push('/profile')
  }

  const handleProjects = () => {
    handleClickAway()
    // <Link to='/projects'/>
    history.push('/projects')
  }

  const handleAssociates = () => {
    handleClickAway()
    history.push('/associates')
  }

  const handleMessages = () => {
    handleClickAway()
    history.push('/messages')
  }

  const handleSettings = () => {
    handleClickAway()
    history.push('/account-setting')
  }

  const handleLogout = () => {
    handleClickAway()
    dispatch(authLogout())
    history.push('/login')
  }

  return (
    <ClickAwayListener onClickAway={handleClickAway}>
      <List>
        <ListItem button key={'Profile'} onClick={handleProfile}>
          <ListItemIcon>
            <Badge badgeContent={3} color="primary">
              <AccountCircle/>  
            </Badge>
          </ListItemIcon>
          <ListItemText primary={'Profile'}/>
        </ListItem>

        <ListItem button key={'Projects'} onClick={handleProjects}>
          <ListItemIcon>
            <Badge badgeContent={2} color="primary">
              <BuildSharp sx={{position: 'relative', top: '2px', right: '8px'}}/>
              <Assignment sx={{position: 'absolute', bottom: '5px', left: '1px'}}/>
            </Badge>
          </ListItemIcon>
          <ListItemText primary={'Projects'}/>
        </ListItem>

        <ListItem button key={'Associates'} onClick={handleAssociates}>
          <ListItemIcon>
              <Badge badgeContent={27} color="primary">
                <ContactsSharp/>
              </Badge>
          </ListItemIcon>
          <ListItemText primary={'Associates'}/>
        </ListItem>

        <ListItem button key={'Messages'} onClick={handleMessages}>
          <ListItemIcon>
            <Badge badgeContent={1} color="primary">
              <MessageRounded/>
            </Badge>
          </ListItemIcon>
          <ListItemText primary={'Messages'}/>
        </ListItem>

        <Divider/>

        <ListItem button key={'Settings'} onClick={handleSettings}>
          <ListItemIcon>
            <Settings/>
          </ListItemIcon>
          <ListItemText primary={'Account Settings'}/>
        </ListItem>

        <Divider/>

        <ListItem button key={'LogOut'} onClick={handleLogout}>
          <ListItemIcon>
            <ExitToApp/>
          </ListItemIcon>
          <ListItemText primary={'LogOut'}/>
        </ListItem>
      </List> 
    </ClickAwayListener>

  )
}

export default AppMenu


// {/* <List>
//   {['Profile', 'Projects', 'Associates', 'Messages' , 'Account Settings'].map((item, index)=>(
//   <ListItem button key={item} onClick={handleMenu}>
//     <ListItemIcon>
//       {index===0&&
//         <Badge badgeContent={3} color="primary">
//           <AccountCircle/>  
//         </Badge>
//       }
//       {index===1&&
//         <Badge badgeContent={2} color="primary">
//           <BuildSharp/>
//         </Badge>
//       }
//       {index===2&&
//         <Badge badgeContent={27} color="primary">
//           <ContactsSharp/>
//         </Badge>
//       }
//       {index===3&&
//         <Badge badgeContent={1} color="primary">
//           <MessageRounded/>
//         </Badge>
//       }
//       {index===4&&<Settings/>}
//     </ListItemIcon>
//       <ListItemText primary={item}/>
//   </ListItem>
//   ))}
//   <Divider/>
//   <ListItem button key={'LogOut'} onClick={()=>dispatch(authLogout())}>
//     <ListItemIcon>
//       <ExitToApp/>
//     </ListItemIcon>
//     <ListItemText primary={'LogOut'}/>
//   </ListItem>
// </List> */}