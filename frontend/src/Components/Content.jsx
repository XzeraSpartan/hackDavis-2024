import React, { useEffect, useState } from "react";
import "./Content.css";
import SideNavContent from "./SideNavContent";
import test from "../assets/story_images/test.webp";
import Controls from "./Controls";
import bg_img from "../assets/bg_img.gif";

const url = "https://hackdavis-9dc802d0506c.herokuapp.com/";

const Content = ({ viewSidebar }) => {
  const [response, setResponse] = useState(
    //   [
    //   "The gentle breeze whispered through the towering oaks, carrying with it the scent of jasmine.",
    //   "In the bustling market, the vibrant colors of fresh fruits and spices painted a vivid tapestry.",
    //   "A curious cat peered from behind the alley, its eyes glinting with the secret knowledge of the streets.",
    //   "Overhead, the sky shifted from a pale dawn to a brilliant azure, heralding the day's warmth.",
    //   "A distant bell chimed, marking the passage of time in a town forgotten by the rush of the modern world.",
    //   "An old man recounted tales of yore, his voice a soft murmur blending with the rustling leaves.",
    //   "Children's laughter echoed across the park, a joyful symphony amidst the whisper of the wind.",
    //   "Pages turned in the quiet corner of the library, each one a gateway to untold stories.",
    //   "As twilight approached, the horizon dressed itself in a cloak of crimson and gold, bidding the sun farewell.",
    //   "Night settled softly upon the village, stars peeking through the velvet darkness, each a silent sentinel of the vast universe.",
    // ]
    null
  );

  const [selectedBook, setSelectedBook] = useState(null);

  useEffect(() => {
    // fetch("")
    // console.log("fetching...");
    if (selectedBook) {
      fetch(`${url}book/get_book_data/${selectedBook.book_id}`)
        .then((res) => res.json()) // Convert the response to JSON
        .then((data) => {
          // Update state with the fetched books
          setResponse(data.result[0]);
          SetSelectedSentence(0);
          // console.log(response);
        })
        .catch((error) => {
          // Log any errors to the console
          console.error("Error fetching books:", error);
        });
    }
  }, [selectedBook]);

  const title = "Hide and Seek";

  const [aiReading, setAiReading] = useState(false);
  const [userReading, setUserReading] = useState(false);
  const [selectedSentence, SetSelectedSentence] = useState(0);

  const handleActionClick = (actionBy) => {
    // console.log(actionBy);
    if (actionBy == "user") {
      // let user speak
      setUserReading(true);

      // console.log("user reading", userReading, selectedSentence);
    } else if (actionBy == "ai") {
      // let ai speak
      setAiReading(true);
      console.log("ai reading", aiReading, selectedSentence);
      handleSubmitAI();
    }
  };

  const handleSentenceClick = (i) => {
    console.log(i, response["book_text"][i]);
    SetSelectedSentence((prev) => i);
    console.log(selectedSentence);
  };

  const handleAudioData = (audioBlob) => {
    // Logic to send audio data to the backend...
    // console.log(audioBlob);
  };

  const handleSelectRecommendedClick = () => {
    setSelectedBook({
      book_id: 1,
    });
  };

  return (
    <div id="content-container">
      {viewSidebar && <SideNavContent setSelectedBook={setSelectedBook} />}
      <div id="content">
        {!response && (
          <div id="no-content-msg">
            <img src={bg_img} alt="" id="bg-img" />
            <div className="bg-text">
              <div id="title-main">Mātrā AI</div>
              <p>Empowering non-native children</p>
              <button onClick={handleSelectRecommendedClick}>
                Start Learning
              </button>
            </div>
          </div>
        )}
        {response && (
          <div id="book-container">
            <div className="book-page">
              <h1 id="book-title" className="andika-bold">
                {response["book_name"]}
              </h1>
              <img src={response["book_image"]} className="book-page-image" />
              <div className="book-page-text">
                {response["book_text"].map((sen, i) => {
                  return (
                    <span
                      key={i}
                      className={`sentence andika-bold ${
                        aiReading && selectedSentence == i ? "ai-reading" : ""
                      } ${
                        userReading && selectedSentence == i
                          ? "user-reading"
                          : ""
                      } ${
                        selectedSentence == i
                          ? "sentence-selected"
                          : "sentence-not-selected"
                      }`}
                      onClick={() => handleSentenceClick(i)}
                    >
                      {sen}
                    </span>
                  );
                })}
              </div>
            </div>

            <Controls
              handleActionClick={handleActionClick}
              handleAudioData={handleAudioData}
              selectedSentence={selectedSentence}
              bookContent={response}
              setSelectedSentence={SetSelectedSentence}
              selectedBook={selectedBook}
            />
          </div>
        )}
      </div>
    </div>
  );
};

export default Content;
