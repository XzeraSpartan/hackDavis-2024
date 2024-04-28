import React from "react";
import "./SideNavContent.css";

const SideNavContent = () => {
  const response = [
    {
      id: 0,
      img: "",
      title: "hobbit",
    },
    {
      id: 1,
      img: "",
      title: "harry potter",
    },
    {
      id: 2,
      img: "",
      title: "wizard of OZ",
    },
  ];
  return (
    <div id="sidenav-content">
      {response.map((book, i) => {
        const { id, img, title } = book;

        return (
          <div className="sidenav-book" key={id}>
            <h4>{title}</h4>
            <img src={img} alt={title} />
          </div>
        );
      })}
    </div>
  );
};

export default SideNavContent;
