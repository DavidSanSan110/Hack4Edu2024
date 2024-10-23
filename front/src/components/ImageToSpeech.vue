<template>
  <div class="container mx-auto p-4">
    <div class="mb-4">
      <input
        type="file"
        @change="onFileSelected"
        accept="image/*"
        class="hidden"
        ref="fileInput"
      />
      <span v-if="selectedFile">{{ selectedFile.name }}</span>
    </div>
    <button
      @click="convertToSpeech"
      class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      :disabled="isLoading || !selectedFile"
    >
      {{ isLoading ? 'Converting...' : 'Convert to Voice' }}
    </button>
    <div v-if="audioSrc" class="mt-4">
      <div class="flex items-center space-x-2">
        <button @click="toggleAudio" class="text-blue-500">
          {{ isPlaying ? 'Pause' : 'Play' }}
        </button>
        <span>{{ formatDuration(audioDuration) }}</span>
      </div>
      <audio 
        ref="audioPlayer" 
        :src="audioSrc" 
        @loadedmetadata="onAudioLoaded"
        @ended="onAudioEnded"
      ></audio>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const fileInput = ref(null);
    const selectedFile = ref(null);
    const isLoading = ref(false);
    const audioSrc = ref('');
    const audioDuration = ref(0);
    const isPlaying = ref(false);
    const audioPlayer = ref(null);

    const onFileSelected = (event) => {
      selectedFile.value = event.target.files[0];
    };

    const convertToSpeech = async () => {
      if (!selectedFile.value) return;

      isLoading.value = true;
      const formData = new FormData();
      formData.append('file', selectedFile.value);

      try {
        const response = await fetch('http://localhost:10001/apis/imageToVoice', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) throw new Error('Failed to convert image to speech');

        const audioBlob = await response.blob();
        audioSrc.value = URL.createObjectURL(audioBlob);
      } catch (error) {
        console.error('Error converting image to speech:', error);
        alert('Failed to convert image to speech. Please try again.');
      } finally {
        isLoading.value = false;
      }
    };

    const onAudioLoaded = () => {
      audioDuration.value = audioPlayer.value.duration;
    };

    const toggleAudio = () => {
      if (isPlaying.value) {
        audioPlayer.value.pause();
      } else {
        audioPlayer.value.play();
      }
      isPlaying.value = !isPlaying.value;
    };

    const onAudioEnded = () => {
      isPlaying.value = false;
    };

    const formatDuration = (seconds) => {
      const minutes = Math.floor(seconds / 60);
      const remainingSeconds = Math.floor(seconds % 60);
      return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
    };

    return {
      fileInput,
      selectedFile,
      isLoading,
      audioSrc,
      audioDuration,
      isPlaying,
      audioPlayer,
      onFileSelected,
      convertToSpeech,
      onAudioLoaded,
      toggleAudio,
      onAudioEnded,
      formatDuration,
    };
  },
};
</script>