<template>
  <div class="container mx-auto p-4">
    <textarea
      v-model="text"
      class="w-full p-2 border rounded mb-4"
      placeholder="Enter text to convert to speech"
      rows="4"
    ></textarea>
    <button
      @click="convertToSpeech"
      class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      :disabled="isLoading"
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
    const text = ref('');
    const isLoading = ref(false);
    const audioSrc = ref('');
    const audioDuration = ref(0);
    const isPlaying = ref(false);
    const audioPlayer = ref(null);

    const convertToSpeech = async () => {
      if (!text.value.trim()) return;

      isLoading.value = true;
      try {
        const response = await fetch('http://localhost:10001/apis/textToVoice', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: text.value }),
        });

        if (!response.ok) throw new Error('Failed to convert text to speech');

        const audioBlob = await response.blob();
        console.log(audioBlob);
        audioSrc.value = URL.createObjectURL(audioBlob);
      } catch (error) {
        console.error('Error converting text to speech:', error);
        alert('Failed to convert text to speech. Please try again.');
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
      text,
      isLoading,
      audioSrc,
      audioDuration,
      isPlaying,
      audioPlayer,
      convertToSpeech,
      onAudioLoaded,
      toggleAudio,
      onAudioEnded,
      formatDuration,
    };
  },
};
</script>