
import { useSelector, useDispatch } from 'react-redux'
// import { useHistory }from 'react-router-dom'
import { openDrawer, closeDrawer } from '../../store/actions'

import { styled } from '@material-ui/core/styles';
import MuiAppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

import { drawerWidth } from '../project_organizer/drawer';
import { AppMenu } from '.';


// const Main = styled('main', { shouldForwardProp: (prop) => prop !== 'open' })(
//   ({ theme, open }) => ({
//     flexGrow: 1,
//     padding: theme.spacing(3),
//     transition: theme.transitions.create('margin', {
//       easing: theme.transitions.easing.sharp,
//       duration: theme.transitions.duration.leavingScreen,
//     }),
//     marginLeft: `-${drawerWidth}px`,
//     ...(open && {
//       transition: theme.transitions.create('margin', {
//         easing: theme.transitions.easing.easeOut,
//         duration: theme.transitions.duration.enteringScreen,
//       }),
//       marginLeft: 0,
//     }),
//   }),
// );

const AppBar = styled(MuiAppBar, {shouldForwardProp: (prop) => prop !== 'open',})(
  ({ theme, open }) => ({
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    ...(open && {
      width: `calc(100% - ${drawerWidth}px)`,
      marginLeft: `${drawerWidth}px`,
      transition: theme.transitions.create(['margin', 'width'], {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
    }),
  })    
);



const POAppBar = () => {
  // const auth = useSelector(state => state.auth
  const dashb = useSelector(state => state.dashboard)
  const dispatch = useDispatch()
  const drawerOpen = dashb.drawer.isOpen
  
  // const history = useHistory()

  const handleDrawer = () => {
    drawerOpen ? dispatch(closeDrawer()) : dispatch(openDrawer())
  }

  return (
    <AppBar 
      position="fixed"
      open={drawerOpen}>
      <Toolbar>
        <IconButton 
          edge="start" 
          onClick={handleDrawer}
          sx={{ mr: 2, ...(drawerOpen && { display: 'none' }) }}
        >
          <MenuIcon/>
        </IconButton>

        <Typography variant="h6" noWrap align="left">
          Project Management App
        </Typography>
        <AppMenu/>
    </Toolbar>
    </AppBar>
  )
}



export default POAppBar
