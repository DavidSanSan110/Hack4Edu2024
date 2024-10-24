<template>
  <v-container class="background-container" fluid>
    <v-row justify="center">
      <v-col cols="12" class="text-center">
        <h1 class="welcome-text">¡Hola, Tomás! 😊</h1>
        <p class="encouragement-text">¡¡Estás haciendo un gran trabajo!!</p>
      </v-col>
    </v-row>
    <v-row justify="center" align="center" class="mb-16">
      <v-col cols="12" md="6">
        <v-card
          class="mx-auto pa-4 mr-16 activity-card kid-friendly"
          max-width="600"
        >
          <div class="activity-header">📚 Actividades</div>
          <v-list class="kid-friendly-list" variant="text">
            <v-list-item
              @click="onListItemClick('cuento')"
              clickable
              rounded="l"
            >
              <v-list-item-title>Cuento Curioso 📚</v-list-item-title>
            </v-list-item>
            <v-list-item
              @click="onListItemClick('juguetes')"
              clickable
              rounded="l"
            >
              <v-list-item-title>Recuerda Juguetes 🎄</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="12" md="6">
        <v-card
          class="mx-auto pa-4 ml-16 learn-card kid-friendly"
          max-width="600"
        >
          <div class="learn-header">🌊 Aprender</div>
          <v-list class="kid-friendly-list" variant="text">
            <v-list-item @click="goToAmbos" clickable rounded="l">
              <v-list-item-title>{{ title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { toRaw } from "vue";
import { useDataStore } from "../stores/useDataStore";

export default {
  name: "Alumnos",
  data() {
    return {
      title: "",
    };
  },
  mounted() {
    const dataStore = useDataStore();
    this.title = toRaw(dataStore.getLeccion);
    console.log("Fetched lesson title:", this.title);
  },
  computed: {
    title() {
      const dataStore = useDataStore();
      return dataStore.getLeccion;
    },
  },
  methods: {
    onListItemClick(activity) {
      console.log(`Elegiste la actividad: ${activity}`);
    },
    goToAmbos() {
      this.$router.push("/ambos?tipo=resaltado");
    },
  },
};
</script>

<style scoped>
html,
body {
  height: 100%;
  margin: 0;
  padding: 0;
}

.background-container {
  background-color: #f5f3ef;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  border-radius: 0;
}

/* Text Styles */
.welcome-text {
  color: #333333;
  font-family: "Montserrat", sans-serif;
  font-weight: bold;
  font-size: 66px;
  margin-top: 30px;
  margin-bottom: 10px;
}

.encouragement-text {
  color: #5c5c5c;
  font-family: "Montserrat", sans-serif;
  font-size: 24px;
  margin-top: 0;
  font-weight: bold;
}

/* Card Styles */
.activity-card {
  background-color: #40e0d0;
  border: 2px solid #30b0a3;
  border-radius: 24px;
  text-align: center;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.learn-card {
  background-color: #ffa500;
  border: 2px solid #ff6f00;
  border-radius: 24px;
  text-align: center;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  width: 400px;
}

.kid-friendly {
  cursor: pointer;
  transition: transform 0.3s;
}

.kid-friendly:hover {
  transform: scale(1.05);
}

.kid-friendly-list {
  border-radius: 16px;
  padding: 10px;
}

.activity-header {
  color: #000000;
  font-weight: bold;
  font-size: 32px;
  text-align: center;
  margin-bottom: 16px;
}

.learn-header {
  color: #000000;
  font-weight: bold;
  font-size: 32px;
  text-align: center;
  margin-bottom: 16px;
}

.v-list-item {
  background-color: transparent;
  border-radius: 12px;
  padding: 10px;
  border: none;
}

/* Remove hover effect */
.v-list-item:hover {
  background-color: transparent;
}

.v-list-item-title {
  color: #333333;
  font-family: "Montserrat", sans-serif;
  font-size: 20px;
  font-weight: bold;
}

.v-icon {
  color: #ff8c00;
}

.highlight-text {
  color: #333333;
}

.card-image {
  border-radius: 16px;
  margin-bottom: 16px;
}

.v-btn {
  font-family: "Montserrat", sans-serif;
  background-color: #ff9d00;
  color: white;
  font-weight: bold;
  text-transform: uppercase;
  transition: background-color 0.3s;
}

.v-btn:hover {
  background-color: #e88b00;
}

.v-list-item:hover {
  background-color: transparent;
}
</style>
