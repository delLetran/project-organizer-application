
import { useSelector } from 'react-redux'
import { 
  Button,
  Card,
  CardActionArea,
  CardActions,
  CardMedia, 
  Grid,
  // Paper,
  Typography,
} from '@material-ui/core'
import { makeStyles } from '@material-ui/styles'
import clsx from 'clsx'

import { drawerWidth } from '.'

const Main = () => { 
  const dashb = useSelector(state=>state.dashboard)
  const drawerOpen = dashb.drawer.isOpen
  const classes = useStyles()

  return (
    <main className={
      clsx([classes.content, classes.root], drawerOpen && classes.contentShift)
    }>
    <div className={classes.appBarSpacer}/>
      <Grid container spacing={3} >
        <Grid item md={8} xs={12}>
            <Component1/>
        </Grid>
        <Grid item md={4} xs={12}>
            <Component2/>
        </Grid>
      </Grid>
    </main>
  )
}




















const Component1 = () => {
  const classes = useStyles()

  return (
    <Card className={clsx(classes.card, classes.fixHeight)}>
    <Typography gutterBottom variant="h5" component="h2">
        Left 
      </Typography>
      <Typography component="p">
        Some Text Wrap with Typography. 
        Some Text Wrap with Typography. 
        Some Text Wrap with Typography. 
      </Typography>
      <CardActions>
        <Button>Learn More</Button>
      </CardActions>
    </Card>
    )
}

const Component2 = () => {
  const classes = useStyles()

  return (
    <Card className={clsx(classes.card, classes.fixHeight)}> 
      <CardActionArea>
        <CardMedia
          image="/static/images/cards/contemplative-reptile.jpg"
          title="Contemplative Reptile"
        />
        <Typography gutterBottom variant="h5" component="h2">
          Right
        </Typography>
        <Typography component="p">
          Some Text Wrap with Typography. 
          Some Text Wrap with Typography. 
          Some Text Wrap with Typography. 
        </Typography>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          Share
        </Button>
        <Button size="small" color="primary">
          Learn More
        </Button>
      </CardActions>
    </Card>
  )
}

const useStyles =  makeStyles((theme)=>({
  root: {
    flexGrow: 1,
  },
  appBarSpacer: {
    // theme.mixins.toolbar,
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  // paper: {
  //   padding: theme.spacing(2),
  //   textAlign: 'center',
  //   color: theme.palette.text.secondary,
  // },
  card: {
    padding: theme.spacing(3),
    textAlign: 'left',
    color: theme.palette.text.secondary,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
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
  fixHeight: {
    height: 200,
  }
  
}))

export default Main