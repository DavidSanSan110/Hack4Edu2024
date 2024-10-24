<template>
  <div>
    <router-view />
  </div>
</template>

<script>
import MainPage from "./views/MainPage.vue";
import TextToSpeech from "./components/TextToSpeech.vue";
import ImageToSpeech from "./components/ImageToSpeech.vue";
import Diagnosis from "./components/Diagnosis.vue";
import SpeechToText from "./components/SpeechToText.vue";

export default {
  name: "App",
  components: {
    MainPage,
    TextToSpeech,
    ImageToSpeech,
    Diagnosis,
    SpeechToText,
  },
};
</script>
