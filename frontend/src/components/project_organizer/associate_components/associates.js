// import { useHistory } from "react-router"
// import { useSelector } from "react-redux"
import { useParams } from "react-router"
// import { useState } from "react"

// import POAppBar from '../../appbar'
// import PODrawer from "../drawer"
// import POMain  from '../main'

// import { Typography } from "@material-ui/core"
// import { Grid } from '@material-ui/core'
import { Box } from '@material-ui/system'
// // import { Box } from "@material-ui/core"

// import { Button } from '@material-ui/core'
// import { Card } from '@material-ui/core'
// import { CardActionArea } from '@material-ui/core'
// import { CardActions } from '@material-ui/core'
// import { CardMedia } from '@material-ui/core' 
import CssBaseline from '@material-ui/core/CssBaseline'

const Associates = ({associates}) => {
  let { slug } = useParams()

  return (
    <Box sx={{ display: 'flex'}}>
      <CssBaseline />
        <POAppBar/>
        <PODrawer>
          {/* <AssociateDrawer associates={associates}/> */}
        </PODrawer>
        <POMain>
          <div>
          {/* <Grid container spacing={3} >
            <Grid item md={8} xs={12}>
              <Typography variant='h4' align='left' >
                OverView 
              </Typography>

              <Typography variant='h6' align='left' margin='1rem'>
                { project.name }
              </Typography>

              <Typography variant='p' align='left' marginLeft='2rem'>
                { project.description }
              </Typography>
            </Grid>
            <Grid item md={4} xs={12}>
              <Typography variant='h4' align='left' >
                Progress 
              </Typography>

              <Typography variant='h6' align='left' margin='1rem'>
                { project.name }
              </Typography>

              <Typography variant='p' align='left' marginLeft='2rem'>
                { project.description }
              </Typography>
            </Grid>
          </Grid> */}
          </div>
        </POMain>
    </Box>
  )
}

export default Associates