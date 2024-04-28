import React, { useEffect, useRef, useState } from "react";
import ai_speak from "../assets/icons/ai_speak.png";
import user_speak from "../assets/icons/user_speak.png";
import pause_icon from "../assets/icons/pause_icon.png";
import play_icon from '../assets/icons/play_icon.png';
import useVoiceRecorder from "../CustomHooks/useVoiceRecorder";
import sample_audio from "../assets/sample_audio.mp3"
import "./Controls.css";

const Controls = ({ handleActionClick, handleAudioData, selectedSentence, setSelectedSentence }) => {
  const { isRecording, startRecording, stopRecording, playRecording, audioUrl } = useVoiceRecorder(handleAudioData);
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
    aiAudio.current.addEventListener('play', () => setIsPlayingAI(true));
    aiAudio.current.addEventListener('ended', () => setIsPlayingAI(false));
    aiAudio.current.addEventListener('pause', () => setIsPlayingAI(false));

    return () => {
      aiAudio.current.removeEventListener('play', () => setIsPlayingAI(true));
      aiAudio.current.removeEventListener('ended', () => setIsPlayingAI(false));
      aiAudio.current.removeEventListener('pause', () => setIsPlayingAI(false));
    };
  }, []);

  const handleRecordClick = () => {
    if (isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  const handleAIButtonClick = () => {
    if (!isPlayingAI && !isRecording) {
      if(selectedSentence == null){
        setSelectedSentence(0);
      }
      aiAudio.current.play();
    }
  };

  const disableOtherControls = isPlayingAI || isRecording;

  return (
    <div id="controls-container">
      <button
        className={`controls-button ai ${disableOtherControls && !isPlayingAI ? "disabled" : ""} ${isPlayingAI ? "pulsing" : ""}`}
        onClick={handleAIButtonClick}
        disabled={disableOtherControls && !isPlayingAI}
      >
        <img src={ai_speak} alt="AI Speak" />
      </button>
      <button
        className={`controls-button user ${disableOtherControls && !isRecording ? "disabled" : ""} ${isRecording ? "pulsing" : ""}`}
        onClick={handleRecordClick}
        disabled={disableOtherControls && !isRecording}
      >
        {isRecording ? (
          <img src={pause_icon} alt="Pause Recording" />
        ) : (
          <img src={user_speak} alt="User Speak" />
        )}
      </button>
      {audioUrl && (
        <button
          className={`controls-button play ${disableOtherControls ? "disabled" : ""}`}
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
