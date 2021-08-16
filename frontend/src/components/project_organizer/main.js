import { styled } from '@material-ui/core/styles';
import { useSelector } from 'react-redux';
import { drawerWidth } from './drawer';
import { DrawerHeader } from './drawer';
// import ProjectList from './project_components/projectList';

 const Main = styled('main', { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    flexGrow: 1,
    padding: theme.spacing(3),
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginLeft: `-${drawerWidth}px`,
    ...(open && {
      transition: theme.transitions.create('margin', {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
      marginLeft: 0,
    }),
  }),
);

const POMain = (props) => {
  const dashb = useSelector(state => state.dashboard)
  const drawerOpen = dashb.drawer.isOpen

  return (
    <Main open={drawerOpen}>
      <DrawerHeader/>
        {props.children}
    </Main>
  )
}

export default POMain