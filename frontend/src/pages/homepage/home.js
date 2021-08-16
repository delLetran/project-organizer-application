// import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
// import { Appbar } from '../containers'
// import POAppBar from '../../components/appbar'

import POAppBar from '../../components/appbar'
import PODrawer from '../../components/project_organizer/drawer'
import POMain from '../../components/project_organizer/main'

import CssBaseline from '@material-ui/core/CssBaseline'
import Box from '@material-ui/core/Box'


const Homepage = () =>{
  
  return (
    <Box sx={{ display: 'flex'}}>
      <CssBaseline />
      <POAppBar />
      <PODrawer />
      <POMain/>
    </Box>
  )
} 

export default Homepage