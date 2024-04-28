import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SideNav from './Components/SideNav'
import Content from './Components/Content'
import SideNavContent from './Components/SideNavContent'

function App() {
  const [viewSidebar, setViewSidebar] = useState(false);


  return (
    <div className='app-container'>
      <SideNav setViewSidebar = {setViewSidebar}/>
      {/* {viewSidebar && <SideNavContent />} */}
      <Content viewSidebar={viewSidebar} />
    </div>
  )
}

export default App
