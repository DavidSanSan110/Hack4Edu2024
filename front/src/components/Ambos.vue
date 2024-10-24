<template>
  <v-container class="outer-container" fluid>
    <v-row class="justify-center align-center">
      <v-col cols="12" md="10" lg="10">
        <div class="card-container">
          <v-btn icon @click="goBack" class="back-button">
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>

          <h1 class="text-center" style="margin-bottom: 30px; font-weight: 600">
            {{ title }}
          </h1>

          <p v-html="currentText"></p>

          <div class="button-container">
            <v-btn
              v-if="currentIndex > 0"
              prepend-icon="mdi-chevron-left"
              variant="outlined"
              class="orange-button"
              @click="previous"
            >
              Anterior
            </v-btn>

            <v-btn
              v-if="currentIndex < texts.length - 1"
              append-icon="mdi-chevron-right"
              variant="outlined"
              class="orange-button"
              @click="next"
              :class="{ 'align-right': currentIndex === 0 }"
            >
              Siguiente
            </v-btn>
            <v-btn
              v-if="currentIndex === texts.length - 1"
              append-icon="mdi-check"
              variant="outlined"
              class="align-right orange-button"
            >
              Fin
            </v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useDataStore } from "../stores/useDataStore";
import { toRaw } from "vue";

export default {
  name: "Ambos",
  data() {
    return {
      title: "",
      texts: [],
      currentIndex: 0, 
    };
  },
  computed: {
    currentText() {
      return this.texts[this.currentIndex];
    },
  },
  methods: {
    previous() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    },
    next() {
      if (this.currentIndex < this.texts.length - 1) {
        this.currentIndex++;
      }
    },
    goBack() {
      window.history.back(); 
    },
    generateHtml(texts) {
      return texts.map((text) => {
        return text.replace(/\*\*(.*?)\*\*/g, "<b>$1</b>");
      });
    },
  },
  mounted() {
    const dataStore = useDataStore();
    console.log(toRaw(dataStore.getCourses));
    this.title = dataStore.getLeccion;
    console.log(this.title);
    this.tipo = this.$route.query.tipo;
    if (this.tipo == "iconos") {
      this.texts = toRaw(dataStore.getCourses)["emoji"];
    } else if (this.tipo == "normal") {
      this.texts = toRaw(dataStore.getCourses)["normal"];
    } else if (this.tipo == "resaltado") {
      this.texts = toRaw(dataStore.getCourses)["resaltado"];
      this.texts = this.generateHtml(this.texts);
    }
    this.currentIndex = 0;
    console.log(this.currentText);
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap");

.outer-container {
  background-color: #f5f3ef;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.card-container {
  background-color: white;
  border-radius: 20px;
  padding: 60px;
  max-width: 90vw;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.back-button {
  position: absolute;
  top: 20px;
  left: 20px;
  color: #ff8c00;
  border-radius: 10px; 
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 30px;
}

.align-right {
  margin-left: auto; 
}

p {
  font-family: "Montserrat", "Noto Color Emoji", "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", sans-serif;
  font-size: 1.2em;
  line-height: 1.5;
}

.orange-button {
  background-color: white;
  color: #ff8c00;
  font-weight: bold;
  text-transform: uppercase;
  transition: background-color 0.3s;
}

.orange-button:hover {
  background-color: #ff6f00;
  color: #f5f3ef;
}

.outlined-button {
  border-color: #ff9d00;
  color: #ff9d00;
}

.outlined-button:hover {
  background-color: #fff4e5;
  border-color: #e88b00;
  color: #e88b00;
}

.white-text {
  color: white;
}

.squared-button {
  border-radius: 0; 
}

.outlined-button:hover .white-text {
  color: #ff8c00 !important;
}
</style>
