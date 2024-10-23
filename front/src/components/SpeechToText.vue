<template>
    <div class="container">
      <h1 class="title">Dicta para transformar a texto</h1>
      <div class="microphone" @click="toggleRecording">
        <v-icon>{{ isRecording ? 'mdi-stop' : 'mdi-microphone' }}</v-icon>
      </div>
      <div v-if="transcription">{{ transcription }}</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isRecording: false,
        mediaRecorder: null,
        transcription: '',
        audioChunks: [],
      };
    },
    methods: {
      async toggleRecording() {
        if (this.isRecording) {
          // Stop recording
          this.mediaRecorder.stop();
          this.isRecording = false;
        } else {
          // Start recording
          await this.startRecording();
          this.isRecording = true;
        }
      },
      async startRecording() {
        try {
          this.transcription = '';
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          this.mediaRecorder = new MediaRecorder(stream);
          this.audioChunks = [];
  
          this.mediaRecorder.addEventListener("dataavailable", (event) => {
            this.audioChunks.push(event.data);
          });
  
          this.mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(this.audioChunks, { type: "audio/wav" });
            this.sendAudioToBackend(audioBlob);
          });
  
          this.mediaRecorder.start();
        } catch (error) {
          console.error("Error starting recording:", error);
        }
      },
      async sendAudioToBackend(audioBlob) {
        const formData = new FormData();
        formData.append('file', audioBlob, 'recording.wav'); // Name the file
  
        try {
          const response = await fetch('http://localhost:10001/apis/voiceToText', {
            method: 'POST',
            body: formData,
          });
  
          if (!response.ok) throw new Error('Failed to send audio to backend');
          const result = await response.json();
          console.log('Transcription result:', result);
            this.transcription = result.text;
        } catch (error) {
          console.error('Error sending audio to backend:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh; /* Full height for centering */
  }
  
  .title {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .microphone {
    font-size: 100px; /* Adjust icon size */
    cursor: pointer;
    color: #f00; /* Red color for microphone */
    transition: transform 0.2s;
  }
  
  .microphone:hover {
    transform: scale(1.1);
  }
  </style>
  