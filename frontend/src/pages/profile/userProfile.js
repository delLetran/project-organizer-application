// import { useHistory } from "react-router"
// import { useSelector } from "react-redux"
// import { useState } from "react"
import { useRouteMatch } from "react-router"

import POAppBar from "../../components/appbar"
import PODrawer from "../../components/project_organizer/drawer"
import POMain from "../../components/project_organizer/main"
import AuthProfile from "./authUser"

import { Typography } from "@material-ui/core"
import { Grid } from '@material-ui/core'
import { Box } from '@material-ui/system'
import CssBaseline from '@material-ui/core/CssBaseline'

const Profile = ({}) => {
  let { path } = useRouteMatch()

  return (
    <Box sx={{ display: 'flex'}}>
      <CssBaseline />
        <POAppBar/>
        <PODrawer>
        {path}
        </PODrawer>
        <POMain>
          <div>
          <Grid container spacing={3} >
            <Grid item md={8} xs={12}>
              <Typography variant='h4' align='left' >
                Profile
              </Typography>
              <AuthProfile/>
            </Grid>
            <Grid item md={4} xs={12}>
              <Typography variant='h4' align='left' >
                Ads 
              </Typography>
              <Typography variant='p' align='left' marginLeft='2rem'>
              </Typography>
            </Grid>
          </Grid>
          </div>
        </POMain>
    </Box>
  )
}

export default Profile