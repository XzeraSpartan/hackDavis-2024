import React, { useState } from "react";
import "./SideNav.css";
import book_icon from "../assets/icons/book_icon.png";

const SideNav = ({setViewSidebar}) => {

  const handleIconClick = (e) => {
    console.log(e);
    setViewSidebar((prev) => !prev);
  };

  return (
    <div id="sidenav-container">
      <div id="icons-container">
        <div
          className="icon-container"
          id="book-icon"
          onClick={handleIconClick}
        >
          <img src={book_icon} className="icon" />
        </div>

      </div>
    </div>
  );
};

export default SideNav;
