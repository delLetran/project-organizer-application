
import { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'
import { openDrawer, closeDrawer } from '../../store/actions'

// import POAppBar from '../components/appbar'
import { POAppBar } from '../../components/appbar'
import Main from './main'
import {
  // Button,
  // Typography,
  IconButton,
  Divider,
  Drawer,
  // Menu,
  // MenuList,
  // MenuItem,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
} from '@material-ui/core'

import { 
  MenuOpen,
  // ExpandMore, 
  // ExpandLess,
  ArrowDropDown,
  ArrowDropUp,
  Assignment,
  AccountBox,
  Bookmark,
  Schedule,
  NoteAddSharp,
  Star
} from '@material-ui/icons';

import { createStyles, makeStyles } from '@material-ui/styles'
import { styled } from '@material-ui/core/styles'
// import { createTheme, ThemeProvider } from '@material-ui/core/styles';


// const theme = createTheme()


const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end',
}));



const ProjectOrganizer = () => {
  const dashb = useSelector(state => state.dashboard)
  const dispatch = useDispatch()
  const drawerOpen = dashb.drawer.isOpen
  // const [drawer, setDrawer] = useState({item1:{isOpen: false}})
  const [drawer, setDrawer] = useState({0:true})
  const classes = useStyles()

  const handleDrawer = () => {
    drawerOpen ? dispatch(closeDrawer()) : dispatch(openDrawer())
  }

  const handleSubDrawer = (item) => {
    drawer[item] ?
    setDrawer({...drawer, [item]: false})
    : setDrawer({...drawer, [item]: true})
  }

  const objList = [
    {'name': 'Deliverables', 'desc': 'Documents'}, 
    {'name': 'Members', 'desc': 'Project Members'},
    {'name': 'Schedule', 'desc': 'Tasks / Activities '}, 
    {'name': 'Bookmarks', 'desc': 'marked'}
  ]

  return (
    <div className={classes.root}>
      <POAppBar count={4}/> 
      <Drawer
        anchor='left'
        variant="persistent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
          },
        }}
        open={drawerOpen}>
        <DrawerHeader>
          <IconButton onClick={handleDrawer}>
            <MenuOpen/>
          </IconButton>
        </DrawerHeader>
        <Divider/>
        <List>
          {objList.map((item, index)=>(
            <div key={item.name}>
              <ListItem button key={item.name} onClick={()=>handleSubDrawer(index)}>
                <ListItemIcon>
                  {index===0&&<Assignment fontSize="large" />}
                  {index===1&&<AccountBox fontSize="large" />}
                  {index===2&&<Schedule fontSize="large" />}
                  {index===3&&<Bookmark fontSize="large" />} 
                </ListItemIcon>
                <ListItemText primary={item.name} secondary={item.desc}/>
                { drawer[index] ?
                  <ArrowDropUp fontSize="small" />
                  :
                  <ArrowDropDown fontSize="small" />
                }
              </ListItem>
              {/* { drawer[index] && <DrawerSubList name={item}/> } */}
            </div>
          ))}
        </List>
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
      <Main/>
    </div>
  )
}

// v

export const DrawerSubList = ( props) => {
  const history = useHistory()
  const classes = useStyles()

  return (
    <List className={classes.subItem} >
      {['subItem1','subItem2','subItem3','subItem4'].map((subItem, index)=>(
      <ListItem button key={subItem} onClick={()=>{history.push(`/p/pmapp/${props.name}/${subItem}`)}}>
        <ListItemIcon>
          {index===0&&<Star fontSize="small" />}
          {index===1&&<Star fontSize="small" />}
        </ListItemIcon>
        <ListItemText primary={subItem}/>
      </ListItem>
      ))}
    </List>
  )
}

export const drawerWidth = 250;



const useStyles = makeStyles((theme)=>
  createStyles({
    root: {
      display: 'flex'
    },
    drawerHeader: {
      display: 'flex',
      alignItems: 'center',
      ...theme.mixins.toolbar,
      justifyContent: 'flex-end'
    },
    drawer: {
      width: drawerWidth,
      flexShrink: 0,
    },
    drawerClose: {
      width: drawerWidth,
    },
    content: {
      flexGrow: 1,
      transition: theme.transitions.create('margin', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      marginLeft: 0,
    },
    contentShift: {
      transition: theme.transitions.create('margin', {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
      marginLeft: drawerWidth,
    },
    subItem: {
      paddingLeft: theme.spacing(3),
    }
  })
)

export default ProjectOrganizer 