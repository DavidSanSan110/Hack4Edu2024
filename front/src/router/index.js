import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../views/MainPage.vue";
import LandingPage from "../views/LandingPage.vue";
import ImageToSpeech from "../components/ImageToSpeech.vue";
import TextToSpeech from "../components/TextToSpeech.vue";
import Diagnosis from "../components/Diagnosis.vue";
import SpeechToText from "../components/SpeechToText.vue";
import Alumnos from "../components/Alumnos.vue";
import Ambos from "../components/Ambos.vue";
import Empatia from "../components/Empatia.vue";

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: MainPage,
  },
  {
    path: "/image-to-speech",
    name: "ImageToSpeech",
    component: ImageToSpeech,
  },
  {
    path: "/text-to-speech",
    name: "TextToSpeech",
    component: TextToSpeech,
  },
  {
    path: "/speech-to-text",
    name: "SpeechToText",
    component: SpeechToText,
  },
  {
    path: "/diagnosis",
    name: "Diagnosis",
    component: Diagnosis,
  },
  {
    path: "/landing",
    name: "LandingPage",
    component: LandingPage,
  },
  {
    path: "/alumnos",
    name: "Alumnos",
    component: Alumnos,
  },
  {
    path: "/ambos",
    name: "Ambos",
    component: Ambos,
  },
  {
    path: "/empatia",
    name: "Empatia",
    component: Empatia,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
