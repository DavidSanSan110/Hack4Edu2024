<template>
  <v-container class="test-container" fluid>
    <v-row class="justify-center align-center">
      <v-col cols="12" md="10">
        <v-card class="mx-auto pa-6 test-card" max-width="90vw">
          <!-- Puntuación, Temporizador y Título -->
          <v-row class="top-info">
            <v-col cols="2">
              <div class="score-display">
                <div>Puntos:</div>
                <div class="score-number">{{ score }}</div>
              </div>
            </v-col>
            <v-col cols="8">
              <v-card-title class="headline text-center question-title">{{
                question.text
              }}</v-card-title>
            </v-col>
            <v-col cols="2">
              <div class="timer-display">
                <div>Tiempo restante:</div>
                <div class="timer-number">{{ timer }}s</div>
              </div>
            </v-col>
          </v-row>

          <!-- Respuestas -->
          <v-spacer></v-spacer>
          <v-card-actions class="options-container">
            <v-btn
              v-for="(option, index) in question.options"
              :key="index"
              :style="getOptionStyle(index)"
              outlined
              class="option-button"
              rounded="lg"
              @click="selectAnswer(option)"
              :class="getButtonClass(option)"
              :disabled="showFeedback"
              height="90"
            >
              {{ option }}
            </v-btn>
          </v-card-actions>

          <!-- Feedback -->
          <v-alert
            v-if="showFeedback"
            :type="feedbackType"
            class="mt-5 feedback-alert"
            prominent
          >
            {{ feedbackMessage }}
          </v-alert>

          <v-card-actions>
            <v-btn
              rounded="lg"
              @click="nextQuestion"
              v-if="showNextButton"
              class="mx-auto next-button"
              size="x-large"
            >
              Siguiente
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useDataStore } from "../stores/useDataStore";
import { toRaw } from "vue";

export default {
  name: "TestView",
  data() {
    return {
      questions: [
        {
          text: "¿Cuál es el río más largo del mundo?",
          options: ["Nilo", "Amazonas", "Yangtsé", "Mississippi"],
          correctAnswer: "Amazonas",
        },
        {
          text: "¿Cuál es la capital de Francia?",
          options: ["Berlín", "Madrid", "París", "Roma"],
          correctAnswer: "París",
        },
        {
          text: "¿Qué planeta es conocido como el Planeta Rojo?",
          options: ["Marte", "Júpiter", "Saturno", "Venus"],
          correctAnswer: "Marte",
        },
      ],
      currentQuestionIndex: 0,
      selectedAnswer: null,
      showFeedback: false,
      feedbackMessage: "",
      feedbackType: "",
      showNextButton: false,
      score: 0, 
      timer: 60, 
      timerInterval: null, 
    };
  },
  computed: {
    question() {
      return this.questions[this.currentQuestionIndex];
    },
  },
  methods: {
    selectAnswer(option) {
      this.selectedAnswer = option;
      this.checkAnswer();
    },
    checkAnswer() {
      if (this.selectedAnswer) {
        this.showFeedback = true;
        if (this.selectedAnswer === this.question.correctAnswer) {
          this.feedbackMessage = "¡Correcto! 😊";
          this.feedbackType = "success";
          this.score += 1; 
        } else {
          this.feedbackMessage =
            "Incorrecto"
          this.feedbackType = "error";
        }
        this.showNextButton = true;
      }
    },
    nextQuestion() {
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
        this.selectedAnswer = null;
        this.showFeedback = false;
        this.showNextButton = false;
      } else {
        this.stopTimer();
      }
    },
    startTimer() {
      if (this.timerInterval) {
        clearInterval(this.timerInterval); 
      }
      this.timerInterval = setInterval(() => {
        if (this.timer > 0) {
          this.timer--;
        } else {
          this.stopTimer();
          this.feedbackMessage = "Te has quedado sin tiempo.";
          this.feedbackType = "error";
          this.showFeedback = true;
          this.showNextButton = false; 
        }
      }, 1000);
    },
    stopTimer() {
      if (this.timerInterval) {
        clearInterval(this.timerInterval);
        this.timerInterval = null;
      }
    },
    getButtonClass(option) {
      if (!this.showFeedback) {
        return "";
      }

      if (option === this.selectedAnswer) {
        return option === this.question.correctAnswer
          ? "correct-border"
          : "wrong-border";
      }

      return "";
    },
    getOptionColor(index) {
      const colors = ["deep-orange", "light-blue", "lime", "pink"];
      return colors[index % colors.length];
    },
    getOptionStyle(index) {
      const backgroundColors = [
        "#FF4500",
        "#1E90FF",
        "#32CD32",
        "#FF1493",
      ];
      return {
        backgroundColor: backgroundColors[index % backgroundColors.length],
        color: "white",
      };
    },
  },
  mounted() {
    const dataStore = useDataStore();
    const empathy = toRaw(dataStore.getEmpathy)["message"]["preguntas"]
    console.log(empathy)
    this.questions = empathy;
    this.startTimer();
    
  },
  beforeDestroy() {
    this.stopTimer();
  },
};
</script>

<style scoped>
.test-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f3ef;
  position: relative;
}

.test-card {
  background-color: #fff4e5;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  border-radius: 30px;
  min-height: 85vh;
  display: flex;
  flex-direction: column;
  padding-bottom: 40px;
  margin-top: 20px;
  position: relative;
}

.top-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
}

.score-display {
  font-size: 1em;
  font-weight: bold;
  color: #ff8c00;
  background-color: #fff4e5;
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #ff8c00;
  z-index: 10;
  text-align: center;
}

.timer-display {
  font-size: 1em;
  font-weight: bold;
  color: #ff6f00;
  background-color: #ffe4b5;
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #ff6f00;
  z-index: 10;
  text-align: center;
}

.score-number, .timer-number {
  font-size: 2em;
  font-weight: bold;
  margin-top: 5px;
}

.question-title {
  font-size: 2em;
  font-weight: bold;
  text-align: center;
  margin: 0;
  max-width: 100%;
  white-space: normal;
  overflow: visible;
}

.options-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 30px;
  margin-bottom: 30px;
}

.option-button {
  font-family: "Montserrat", sans-serif;
  width: 45%;
  margin-bottom: 25px;
  font-size: 1.5em;
  height: 80px;
  color: white;
  font-weight: 800;
}

.correct-border {
  border-color: #28a745 !important;
}

.wrong-border {
  border-color: #dc3545 !important;
}

.mt-5 {
  margin-top: 40px;
}

.feedback-alert {
  font-size: 1.5em;
  text-align: center;
  margin: 0 auto;
  max-width: 80%;
}

.next-button {
  margin-top: 20px;
  background-color: #ff9d00;
  color: white;
}
</style>
