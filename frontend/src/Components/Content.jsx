import React from "react";
import "./Content.css";
import SideNavContent from "./SideNavContent";

const Content = ({ viewSidebar }) => {
  return (
    <div id="content-container">
      {viewSidebar && <SideNavContent />}
      <div id="content">Content</div>
    </div>
  );
};

export default Content;
