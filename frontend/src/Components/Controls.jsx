import React, { useEffect, useRef, useState } from "react";
import ai_speak from "../assets/icons/ai_speak.png";
import user_speak from "../assets/icons/user_speak.png";
import pause_icon from "../assets/icons/pause_icon.png";
import play_icon from "../assets/icons/play_icon.png";
import useVoiceRecorder from "../CustomHooks/useVoiceRecorder";
import sample_audio from "../assets/sample_audio.mp3";
import "./Controls.css";

const Controls = ({
  handleActionClick,
  handleAudioData,
  selectedSentence,
  setSelectedSentence,
  bookContent,
  selectedBook
}) => {
  const {
    isRecording,
    startRecording,
    stopRecording,
    playRecording,
    audioUrl,
  } = useVoiceRecorder(handleAudioData);
  const recordingTimeoutRef = useRef(null);
  const [isPlayingAI, setIsPlayingAI] = useState(false);
  const aiAudio = useRef(new Audio(sample_audio));

  useEffect(() => {
    if (isRecording) {
      recordingTimeoutRef.current = setTimeout(() => {
        if (isRecording) {
          stopRecording();
        }
      }, 15000);
    }

    return () => {
      if (recordingTimeoutRef.current) {
        clearTimeout(recordingTimeoutRef.current);
      }
    };
  }, [isRecording, stopRecording]);

  useEffect(() => {
    if (audioUrl) {
      handleSubmitAudio(audioUrl); // Automatically submit audio when URL is set
    }
  }, [audioUrl]);

  useEffect(() => {
    // Pause AI speaking
    if (isPlayingAI) {
      aiAudio.current.pause();
      setIsPlayingAI(false);
    }
  
    // Stop recording
    if (isRecording) {
      stopRecording();
    }
  
    // Stop playing
    if (aiAudio.current.paused === false) {
      aiAudio.current.pause();
      aiAudio.current.currentTime = 0;
    }
  
    // Reset selected sentence
    setSelectedSentence(null);
  
  }, [selectedBook]);


  useEffect(() => {
    const handlePlay = () => setIsPlayingAI(true);
    const handlePause = () => setIsPlayingAI(false);
    const handleEnded = () => {
      setIsPlayingAI(false);
      // Check if it's not the last sentence
      if (selectedSentence !== null && selectedSentence < bookContent.book_text.length - 1) {
        setSelectedSentence(prev => prev + 1);
      }
    };
  
    // Adding event listeners
    aiAudio.current.addEventListener("play", handlePlay);
    aiAudio.current.addEventListener("ended", handleEnded);
    aiAudio.current.addEventListener("pause", handlePause);
  
    // Cleanup function to remove event listeners
    return () => {
      aiAudio.current.removeEventListener("play", handlePlay);
      aiAudio.current.removeEventListener("ended", handleEnded);
      aiAudio.current.removeEventListener("pause", handlePause);
    };
  }, [selectedSentence, bookContent.book_text.length]); 

  const handleRecordClick = () => {
    if (isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  const handleAIButtonClick = () => {
    if (!isPlayingAI && !isRecording) {
      if (selectedSentence == null) {
        console.log("No sentence selected to synthesize");
        setSelectedSentence(0);
        // alert("Please select a sentence to synthesize.");
      }
      handleSubmitAI();
    }
  };

  const handleSubmitAI = async () => {
    // setIsLoading(true);  // Start loading
    console.log("selectedSentence", selectedSentence, bookContent["book_text"][selectedSentence]);
    const text = bookContent["book_text"][selectedSentence] + "Try the next line. you can do it";
    if(selectedSentence !== null){
      try {
          const response = await fetch("http://127.0.0.1:5000/ai/tts/", {
              method: "POST",
              headers: {
                  "Content-Type": "text/plain",
              },
              body: text,
          });
  
          if (!response.ok) {
              throw new Error("Network response was not ok");
          }
          const blob = await response.blob();
          const audioUrl = URL.createObjectURL(blob);
          aiAudio.current.src = audioUrl;
          aiAudio.current.play();
      } catch (error) {
          console.error("Error submitting text:", error);
          alert("Failed to submit text. Error: " + error.message);
      } finally {
          // setIsLoading(false);  // Stop loading regardless of success or error
      }
    }
};


  const handleSubmitAudio = async (audioUrl) => {
    const audioBlob = await fetch(audioUrl).then((r) => r.blob()); // Convert audio URL to blob
    const formData = new FormData();
    formData.append("file", audioBlob, "user_audio.mp3"); // Append the audio file
    formData.append("text", bookContent["book_text"][selectedSentence]);
    setIsLoading(true);
    console.log("formData", formData);
    if(selectedSentence !== null){
      try {
        const response = await fetch("http://127.0.0.1:5000/ai/stt_tts", {
          method: "POST",
          body: formData,
        });
  
        if (!response.ok) {
          throw new Error("Network response was not ok: " + response.statusText);
        }
  
        // Check the content type of the response
        const contentType = response.headers.get("content-type");
        if (contentType.includes("audio")) {
          const responseBlob = await response.blob(); // Process as blob if it's audio
          const newAudioUrl = URL.createObjectURL(responseBlob);
          aiAudio.current.src = newAudioUrl;
          aiAudio.current.play();
          console.log("Audio response is being played");
        } else if (contentType.includes("json")) {
          const errorData = await response.json(); // Process as JSON if it's an error message
          console.error("Server responded with error:", errorData);
          alert("Server error: " + errorData.message);
        } else {
          throw new Error("Unsupported content type: " + contentType);
        }
        setIsLoading(false)
      } catch (error) {
        console.error("Error submitting audio:", error);
        alert("Failed to submit audio. Error: " + error.message);
        setIsLoading(false)
      }
    }
  };

  const disableOtherControls = isPlayingAI || isRecording ;

  const [isLoading, setIsLoading] = useState(false);

  return (
    <div id="controls-container">
        <button
            className={`controls-button ai ${
                (disableOtherControls && !isPlayingAI || isLoading) ? "disabled" : ""
            } ${isPlayingAI ? "pulsing" : ""}`}
            onClick={handleAIButtonClick}
            disabled={disableOtherControls && !isPlayingAI}
        >
            <img src={ai_speak} alt="AI Speak" />
        </button>
        <button
            className={`controls-button user ${
                (disableOtherControls && !isRecording) ? "disabled" : ""
            } ${isRecording ? "pulsing" : ""}`}
            onClick={handleRecordClick}
            disabled={disableOtherControls && !isRecording}
        >
            {isRecording ? (
                <img src={pause_icon} alt="Pause Recording" />
            ) : (
                <img src={user_speak} alt="User Speak" />
            )}
            {isLoading && <div className="spinner"></div>}  {/* Spinner added here */}
        </button>
        {audioUrl && (
            <button
                className={`controls-button play ${
                    disableOtherControls || isLoading ? "disabled" : ""
                }`}
                onClick={playRecording}
                disabled={disableOtherControls}
            >
                <img src={play_icon} alt="Play Recording" />
            </button>
        )}
    </div>
);

};

export default Controls;
