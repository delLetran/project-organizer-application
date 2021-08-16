
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
// import { useHistory } from "react-router";
import { BrowserRouter as Router, Switch, Route, useRouteMatch } from "react-router-dom";
import { getProjectList } from "../../store/actions";

// import { Login } from "../../components/auth";
import ProjectList from '../../components/project_organizer/project_components/projectList';
import { ProjectOrganizer } from "../../components/project_organizer";

import { ProjectProvider } from "../../context/project_context/projectContext";
// import POAppBar from '../../components/appbar'
// import { PODrawer } from '../../components/project_organizer'
// import { POMain } from '../../components/project_organizer'

// import CssBaseline from '@material-ui/core/CssBaseline'
// import Box from '@material-ui/core/Box'
// import { GetDerivedStateFromError } from "react";

const Project = () => {
  let { path } = useRouteMatch()
  // let { path, url } = useRouteMatch()
  // const history = useHistory()
  const dispatch = useDispatch()
  const projects = useSelector(state=>state.project.project_list)
  const isAuthenticated = useSelector(state=>state.auth.isAuthenticated)
  
  useEffect(()=>{
    dispatch(getProjectList())
  },[])
  
  // useEffect(()=>{
  //   !projects && dispatch(getProjectList())
  // },[projects, dispatch])




  return(
    <ProjectProvider>
      { isAuthenticated ? 
        <Router>
          <div>
            <Switch>
              <Route path={path} exact={true} component={()=><ProjectList projects={projects}/>}/>
              <Route path={`${path}/:slug`} component={()=><ProjectOrganizer projects={projects}/>}/>
            </Switch>
          </div>
        </Router>
        : <div> Checking User Authorization... </div> }
    </ProjectProvider>
  )
}


      //  : history.push('/signin', { from: {path} }) 

export default Project