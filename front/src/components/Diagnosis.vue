<template>
    <v-app>
      <v-app-bar app>
        <v-toolbar-title>Iniciar Diagnóstico</v-toolbar-title>
      </v-app-bar>
  
      <v-main>
        <v-container v-if="!startedDiagnosis" class="fill-height" fluid>
          <v-row align="center" justify="center">
            <v-btn x-large color="primary" @click="startDiagnosis">
              Iniciar Diagnóstico
            </v-btn>
          </v-row>
        </v-container>
  
        <v-container v-else>
          <v-carousel v-model="currentSlide" :continuous="false" :show-arrows="true">
            <v-carousel-item v-for="(text, i) in diagnosisTexts" :key="i">
              <v-sheet height="100%" tile>
                <v-row class="fill-height" align="center" justify="center">
                  <v-col class="text-center">
                    <div class="text-body-1 mb-4" style="white-space: pre-line;">{{ text }}</div>
                    <v-btn
                      fab
                      large
                      :color="isRecording ? 'red' : 'primary'"
                      @click="toggleRecording(i)"
                      :disabled="recordings[i] !== null"
                    >
                      <v-icon>{{ isRecording ? 'mdi-stop' : 'mdi-microphone' }}</v-icon>
                    </v-btn>
                    <div v-if="recordings[i]" class="mt-2">Grabación completada</div>
                  </v-col>
                </v-row>
              </v-sheet>
            </v-carousel-item>
          </v-carousel>
  
          <v-row justify="center" class="mt-4">
            <v-btn
              color="success"
              :disabled="!allRecordingsCompleted"
              @click="runDetectionModel"
            >
              Ejecutar Modelo de Detección
            </v-btn>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        startedDiagnosis: false,
        currentSlide: 0,
        isRecording: false,
        mediaRecorder: null,
        recordings: [null, null, null, null, null, null],
        diagnosisTexts: [
          `¿Cómo se siente hoy?
  Por favor, describa su estado de ánimo general.
  ¿Ha notado algún cambio significativo en su energía o motivación?
  ¿Está experimentando algún tipo de dolor o malestar físico?
  Si es así, ¿podría calificar su intensidad en una escala del 1 al 10?`,
  
          `Describa cualquier síntoma que esté experimentando.
  Sea lo más específico posible sobre la ubicación, intensidad y duración de cada síntoma.
  ¿Estos síntomas interfieren con sus actividades diarias?
  ¿Ha notado algún patrón en cuándo aparecen o empeoran los síntomas?
  ¿Hay algo que parezca aliviar o empeorar estos síntomas?`,
  
          `¿Cuándo comenzaron estos síntomas?
  ¿Aparecieron de repente o gradualmente?
  ¿Ha experimentado síntomas similares en el pasado?
  Si es así, ¿recuerda cuándo fue la última vez?
  ¿Hubo algún evento o cambio en su vida que coincidiera con el inicio de estos síntomas?`,
  
          `¿Ha tomado algún medicamento para tratar estos síntomas?
  Si es así, ¿cuáles y en qué dosis?
  ¿Ha notado alguna mejoría o efecto secundario con estos medicamentos?
  ¿Está tomando algún otro medicamento regularmente por otras condiciones?
  ¿Utiliza algún suplemento dietético o remedio natural?`,
  
          `¿Tiene alguna alergia conocida?
  Esto incluye alergias a medicamentos, alimentos, polen, animales, etc.
  ¿Cómo se manifiestan estas alergias?
  ¿Ha experimentado alguna reacción alérgica grave en el pasado?
  ¿Tiene un auto-inyector de epinefrina o algún otro medicamento de emergencia para alergias?`,
  
          `¿Hay alguna información adicional que le gustaría compartir?
  ¿Ha habido cambios recientes en su dieta, ejercicio o rutina de sueño?
  ¿Está pasando por alguna situación estresante en su vida personal o profesional?
  ¿Tiene antecedentes familiares de alguna condición médica relevante?
  ¿Hay algo más que cree que deberíamos saber para entender mejor su situación de salud actual?`
        ]
      };
    },
    computed: {
      allRecordingsCompleted() {
        return this.recordings.every(recording => recording !== null);
      }
    },
    methods: {
      startDiagnosis() {
        this.startedDiagnosis = true;
      },
      async toggleRecording(index) {
        if (this.isRecording) {
          await this.stopRecording(index);
        } else {
          await this.startRecording();
        }
      },
      async startRecording() {
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          this.mediaRecorder = new MediaRecorder(stream);
          
          let audioChunks = [];
          this.mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
          });
  
          this.mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
            this.recordings[this.currentSlide] = audioBlob;
          });
  
          this.mediaRecorder.start();
          this.isRecording = true;
        } catch (error) {
          console.error("Error al iniciar la grabación:", error);
        }
      },
      async stopRecording(index) {
        if (this.mediaRecorder && this.mediaRecorder.state !== "inactive") {
          this.mediaRecorder.stop();
          this.isRecording = false;
          this.mediaRecorder.stream.getTracks().forEach(track => track.stop());
        }
      },
      async runDetectionModel() {
        try {
          const formData = new FormData();
          this.recordings.forEach((recording, index) => {
            formData.append(`audio${index + 1}`, recording, `recording${index + 1}.wav`);
          });
  
          const response = await fetch('/api/run-detection-model', {
            method: 'POST',
            body: formData
          });
  
          if (!response.ok) {
            throw new Error('Error al enviar las grabaciones al servidor');
          }
  
          const result = await response.json();
          console.log('Resultado del modelo de detección:', result);
          // Aquí puedes manejar la respuesta del servidor, por ejemplo, mostrar los resultados al usuario
        } catch (error) {
          console.error('Error al ejecutar el modelo de detección:', error);
          // Aquí puedes manejar el error, por ejemplo, mostrar un mensaje al usuario
        }
      }
    }
  };
  </script>