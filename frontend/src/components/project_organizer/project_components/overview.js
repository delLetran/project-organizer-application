
import POMain  from '../main'

import { Typography } from "@material-ui/core"

const Overview = ({projects}) => {

  return (
      <POMain>
      { projects ? projects.map((project, index)=>(
        <div key={index}>
          <Typography variant='h4' align='left' >
            OverView 
          </Typography>

          <Typography variant='h6' align='left' margin='1rem'>
            { project.name }
          </Typography>

          <Typography variant='p' align='left' marginLeft='2rem'>
            { project.description }
          </Typography>
        </div>
      ))
        
        : null
      }
      </POMain>
  )
}



export default Overview