// import { useEffect } from "react"
import { createContext } from "react"
import { useSelector } from "react-redux"
// import { useDispatch } from "react-redux"
// import { getProjectList } from "../../store/actions"

const ProjectContext = createContext()

const ProjectProvider = ({children}) => {
  // const dispatch = useDispatch()
  const projects = useSelector(state=>state.project.project_list)
  
  // useEffect(()=>{
  //   if (projects === null)
  //     dispatch(getProjectList())
  // },[])


  return (
    <ProjectContext.Provider
      value={projects}>
      {children}
    </ProjectContext.Provider>  
  )
}

export default ProjectContext 
export {
  ProjectProvider, 
  ProjectContext
}