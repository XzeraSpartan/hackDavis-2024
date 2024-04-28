import React, { useEffect, useState } from "react";
import "./SideNavContent.css";

const SideNavContent = ({setSelectedBook}) => {
  const [response, setResponse] = useState([
    // {
    //   id: 0,
    //   img: "",
    //   title: "hobbit",
    // },
    // {
    //   id: 1,
    //   img: "",
    //   title: "harry potter",
    // },
    // {
    //   id: 2,
    //   img: "",
    //   title: "wizard of OZ",
    // },
  ]);


  // useEffect(() => {
  //   fetch("http://127.0.0.1:5000/book/get_metadata/")
  //     .then((res) => {
  //       response = res.json();
  //       console.log(res, response);
  //     })
  //     .catch((error) => {
  //       console.error(error);
  //     });
  // }, []);

  useEffect(() => {
    // Fetch data from the API
    console.log("fetching...")
    fetch("http://127.0.0.1:5000/book/get_metadata/")
      .then((res) => res.json())  // Convert the response to JSON
      .then((data) => {
        // Update state with the fetched books
        setResponse(data.result);
        console.log(response)
      })
      .catch((error) => {
        // Log any errors to the console
        console.error("Error fetching books:", error);
      });
  }, []); 

  const handleSidebarBookClick = (i) =>{
    console.log(i, response[i]);
    setSelectedBook(response[i]);
  }

  return (
    <div id="sidenav-content">
      {response.map((book, i) => {
        const { book_id, book_image, book_name } = book;
//         book_id: 1
// book_image: null
// book_name: "HIDE AND SEEK"


        return (
          <div className="sidenav-book" key={i} onClick={() => handleSidebarBookClick(i)}>
            <p>{book_name}</p>
            <img src={book_image} alt={book_name}  />
          </div>
        );
      })}
    </div>
  );
};

export default SideNavContent;
