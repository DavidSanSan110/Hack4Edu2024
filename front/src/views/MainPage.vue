<template>
  <div class="d-flex justify-start align-center background">
    <!-- Sidebar para los cursos -->
    <v-col cols="3" class="sidebar full-height">
      <div
        class="d-flex flex-column justify-space-between course-selector full-height"
      >
        <div>
          <div class="course-header">
            <div class="avatar-wrapper">
              <div class="avatar">
                <v-icon>mdi-account</v-icon>
              </div>
            </div>
            <div class="teacher-name">Manuel</div>
          </div>
          <hr />
          <div class="course-list mt-2">
            <div
              v-for="curso in cursosDisponibles"
              :key="curso"
              @click="cambiarCurso(curso)"
              class="course-item"
              :class="{ selected: selectedCurso === curso }"
            >
              Curso {{ curso }}
            </div>
            <div @click="añadirCurso;" class="course-item add-course-button">
              <v-icon left class="mr-2">mdi-plus</v-icon>
              Añadir curso
            </div>
          </div>
        </div>

        <div>
          <v-row>
            <v-col cols="7">
              <div
                @click="abrirConfiguracion"
                class="course-item settings-button"
              >
                <v-icon left class="mr-2">mdi-cog</v-icon>
                Configurar
              </div>
            </v-col>
            <v-col cols="5">
              <div @click="cerrarSesion" class="course-item logout-button">
                <v-icon left class="mr-2">mdi-logout</v-icon>
                Salir
              </div>
            </v-col>
          </v-row>
        </div>
      </div>
    </v-col>

    <!-- Contenido principal -->
    <v-col cols="9">
      <v-row class="w-100">
        <!-- Bienvenida -->
        <v-col cols="12" class="welcome-container">
          <h2 class="welcome-message">
            Estos son los alumnos del curso {{ selectedCurso }}
          </h2>
        </v-col>

        <!-- Tabla de alumnos -->
        <v-col cols="12" class="d-flex align-center ml-3">
          <div class="alumnos-table">
            <div class="table-header">
              <div class="header-cell">Alumno</div>
              <div class="header-cell">Dislexia</div>
              <div class="header-cell">TDAH</div>
              <div class="header-cell">Discalculia</div>
            </div>
            <div class="table-content">
              <div
                v-for="alumno in alumnosPorCurso"
                :key="alumno.nombre"
                class="table-row"
              >
                <div class="row-cell">{{ alumno.nombre }}</div>
                <div class="row-cell">
                  <v-icon v-if="alumno.dislexia" color="blue"
                    >mdi-check-circle</v-icon
                  >
                </div>
                <div class="row-cell">
                  <v-icon v-if="alumno.tdh" color="green"
                    >mdi-check-circle</v-icon
                  >
                </div>
                <div class="row-cell">
                  <v-icon v-if="alumno.discalculia" color="purple"
                    >mdi-check-circle</v-icon
                  >
                </div>
              </div>
            </div>
          </div>
        </v-col>
      </v-row>

      <!-- Botón para crear lección -->
      <v-row class="create-button-container mt-2">
        <button
          @click="abrirDialogCrearLeccion"
          class="create-button px-12 py-5"
          style="font-weight: bold"
        >
          CREAR LECCIÓN
        </button>
        <button
          @click="abrirDialogCrearActividad"
          class="create-button px-12 py-5 ml-5"
          style="font-weight: bold"
        >
          CREAR ACTIVIDAD
        </button>
      </v-row>
    </v-col>

    <!-- Modal para crear lección -->
    <v-dialog v-model="dialogCrearLeccion" max-width="700">
      <v-card class="rounded-card px-3 py-4">
        <v-card-title class="modal-title">
          <span>Crear lección para el curso {{ selectedCurso }}</span>
        </v-card-title>
        <v-card-text>
          <v-textarea
            v-model="tema"
            label="Introduce el tema para generar una lección"
            variant="outlined"
          ></v-textarea>

          <div
            class="file-upload-container mt-4"
            @dragover.prevent
            @drop.prevent="onDropFile"
            @click="triggerFileInput"
            :class="{ 'drag-over': isDragging, 'file-selected': nombreArchivo }"
          >
            <v-icon left class="mr-2">mdi-file-upload</v-icon>
            <span v-if="!nombreArchivo"
              >Arrastra un archivo o haz clic aquí para subirlo</span
            >
            <span v-if="nombreArchivo" class="file-name-selected">{{
              nombreArchivo
            }}</span>

            <input
              type="file"
              ref="fileInput"
              class="file-upload-input"
              @change="onFileChange"
              style="display: none"
            />
          </div>

          <div v-if="filePreview" class="file-preview mt-4">
            <img
              v-if="isImage"
              :src="filePreview"
              class="uploaded-image-preview"
            />
            <div v-else class="file-placeholder">
              Archivo subido: {{ nombreArchivo }}
            </div>
          </div>
        </v-card-text>
        <v-spacer></v-spacer>
        <v-btn
          size="x-large"
          class="generate-button"
          @click="generarLeccion"
          :loading="isGenerating"
        >
          {{ "GENERAR" }}
        </v-btn>
      </v-card>
    </v-dialog>

    <!-- Modal de lecciones -->
    <v-dialog
      v-model="isLeccionModalOpenFromStore"
      max-width="700"
      @click:outside="cerrarModalLeccion"
    >
      <v-card class="rounded-card px-3 py-4">
        <v-card-title class="modal-title">
          <span>Lecciones generadas para el curso {{ selectedCurso }}</span>
        </v-card-title>
        <v-card-text>
          <v-list>
            <v-list-item
              v-for="(leccion, index) in lecciones"
              :key="index"
              class="my-2 list-item-bordered"
              @click="onLeccionClick(leccion)"
              style="cursor: pointer; font-weight: 600"
            >
              <v-hover v-slot:default="{ isHovering }">
                <v-row
                  align="center"
                  no-gutters
                  :class="{ hovered: isHovering }"
                >
                  <v-col>
                    <span>{{ leccion.titulo }}</span>
                  </v-col>

                  <v-col class="text-center" style="max-width: 40px">
                    <v-icon :color="leccion.color">mdi-circle</v-icon>
                  </v-col>

                  <v-col class="text-right" style="max-width: 50px">
                    <v-icon color="blue">mdi-cloud-upload</v-icon>
                  </v-col>
                </v-row>
              </v-hover>
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-spacer></v-spacer>
        <button class="generate-button pa-3" @click="subirLeccion">
          SUBIR
        </button>
      </v-card>
    </v-dialog>

    <v-dialog v-model="successModalVisible" max-width="500">
      <v-card class="rounded-card px-3 py-4">
        <v-card-title class="modal-title">
          <span>¡Lecciones subidas! ✅</span>
        </v-card-title>

        <v-card-text class="text-center" style="font-size: 20px">
          <p>
            Las lecciones han sido subidas correctamente para el curso
            <strong>{{ selectedCurso }}</strong>
            😃
          </p>
        </v-card-text>
        <v-card-text class="text-center">
          <button class="cerrar-button pa-3" @click="cerrarSuccessModal">
            Cerrar
          </button>
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogCrearActividad" max-width="700">
      <v-card class="rounded-card px-3 py-4">
        <v-card-title class="modal-title">
          <span>{{ actividadSeleccionada.titulo }}</span>
        </v-card-title>
        <v-card-text>
          <div v-if="actividadSeleccionada.descripcion">
            <v-row
              align="center"
              no-gutters
              :class="{ hovered: isHovering }"
              @click="iraEmpatia"
            >
              <v-col>
                <span> Test Interactivo Discalculia </span>
              </v-col>

              <v-col class="text-center" style="max-width: 40px">
                <v-icon color="purple" @click.stop>mdi-circle</v-icon>
              </v-col>

              <v-col class="text-right" style="max-width: 50px">
                <v-icon color="blue" @click.stop>mdi-cloud-upload</v-icon>
              </v-col>

              <v-col class="text-right" style="max-width: 50px">
                <v-icon color="green" @click.stop>mdi-reload</v-icon>
              </v-col>
            </v-row>

            <div
              style="
                border: 1px solid #facc61;
                border-radius: 8px;
                padding: 10px;
                margin-top: 20px;
              "
            >
              <p>{{ actividadSeleccionada.descripcion }}</p>
            </div>
            <v-spacer></v-spacer>
            <div
              style="display: flex; justify-content: center; margin-top: 20px"
            >
              <v-btn
                size="x-large"
                class="generate-button"
                @click="accederEmpatia"
                :loading="isGeneratingEmpatia"
              >
                {{ "ACCEDER" }}
              </v-btn>
            </div>
          </div>

          <v-list v-else>
            <v-list-item
              v-for="(actividad, index) in actividades"
              :key="index"
              class="my-2 list-item-bordered"
              @click="onActividadClick(actividad)"
              style="cursor: pointer"
            >
              <v-hover v-slot:default="{ isHovering }">
                <v-row
                  align="center"
                  no-gutters
                  :class="{ hovered: isHovering }"
                >
                  <v-col>
                    <span>{{ actividad.nombre }}</span>
                  </v-col>

                  <!-- Punto de color -->
                  <v-col class="text-center" style="max-width: 40px">
                    <v-icon :color="actividad.color">mdi-circle</v-icon>
                  </v-col>
                </v-row>
              </v-hover>
            </v-list-item>

            <v-list-item
              v-if="isGeneratingEmpatia"
              class="d-flex justify-center align-center my-4"
            >
              <v-progress-circular
                indeterminate
                color="orange"
              ></v-progress-circular>
              <span style="font-size: 21px; font-weight: 600" class="ml-4"
                >Generando actividad de empatía</span
              >
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-spacer></v-spacer>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { useDataStore } from "../stores/useDataStore";
import { toRaw } from "vue";

export default {
  data() {
    return {
      isGenerating: false,
      isGeneratingEmpatia: false,
      selectedCurso: "C",
      cursosDisponibles: ["A", "B", "C"],
      actividades: [
        { nombre: "TDAH", color: "blue" },
        { nombre: "Dislexia", color: "green" },
        { nombre: "Discalculia", color: "purple" },
      ],
      actividadSeleccionada: {
        titulo: "Selecciona la actividad a crear",
        descripcion: "",
      },
      cursos: {
        A: [
          { nombre: "Ana", dislexia: true, tdh: true, discalculia: false },
          { nombre: "Marco", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Leo", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Lucía", dislexia: false, tdh: false, discalculia: true },
          { nombre: "Carlos", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Emma", dislexia: false, tdh: true, discalculia: false },
          { nombre: "David", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Sara", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Mateo", dislexia: true, tdh: true, discalculia: false },
          { nombre: "Isabel", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Hugo", dislexia: false, tdh: false, discalculia: false },
          {
            nombre: "Valeria",
            dislexia: false,
            tdh: true,
            discalculia: false,
          },
        ],
        B: [
          {
            nombre: "Gabriella",
            dislexia: false,
            tdh: false,
            discalculia: false,
          },
          { nombre: "Asta", dislexia: false, tdh: true, discalculia: false },
          { nombre: "Carlos", dislexia: true, tdh: false, discalculia: false },
          { nombre: "Dinsel", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Sofía", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Lucas", dislexia: false, tdh: false, discalculia: true },
          { nombre: "Noah", dislexia: false, tdh: true, discalculia: false },
          { nombre: "Olivia", dislexia: false, tdh: false, discalculia: false },
          {
            nombre: "Gabriel",
            dislexia: true,
            tdh: false,
            discalculia: false,
          },
          {
            nombre: "Martina",
            dislexia: false,
            tdh: false,
            discalculia: false,
          },
          { nombre: "Diego", dislexia: false, tdh: true, discalculia: false },
          { nombre: "Julia", dislexia: false, tdh: false, discalculia: false },
        ],
        C: [
          { nombre: "Paul", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Kara", dislexia: true, tdh: false, discalculia: false },
          { nombre: "Luis", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Elena", dislexia: false, tdh: true, discalculia: false },
          { nombre: "Javier", dislexia: false, tdh: false, discalculia: true },
          { nombre: "Clara", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Andrés", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Nuria", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Pedro", dislexia: true, tdh: false, discalculia: false },
          { nombre: "Alba", dislexia: false, tdh: false, discalculia: false },
          { nombre: "Raúl", dislexia: false, tdh: false, discalculia: true },
          { nombre: "Marta", dislexia: false, tdh: false, discalculia: false },
        ],
      },
      headers: [
        { text: "Alumno", value: "nombre" },
        { text: "Dislexia", value: "dislexia" },
        { text: "TDH", value: "tdh" },
        { text: "Discalculia", value: "discalculia" },
      ],
      dialogCrearLeccion: false,
      dialogCrearActividad: false,
      dialogCreadasLecciones: false,
      tema: "",
      nombreArchivo: "",
      lecciones: [
        {
          id: 2,
          color: "blue",
        },
        {
          id: 3,
          color: "green",
        },
        {
          id: 1,
          color: "purple",
        }
      ],
      selectedLeccion: null,
      successModalVisible: false,
      selectedLeccion: null,
    };
  },
  computed: {
    alumnosPorCurso() {
      return this.cursos[this.selectedCurso];
    },
    isLeccionModalOpenFromStore() {
      return this.store.isLeccionModalOpen;
    },
  },
  created() {
    this.store = useDataStore();
  },
  mounted() {
    this.selectedCurso = "C";
    let storeLecciones = toRaw(this.store.getLecciones);
    console.log(storeLecciones);
    if (storeLecciones && storeLecciones.length > 0) {
      console.log("Lecciones encontradas en el store");
      this.lecciones = storeLecciones;
    }
  },
  methods: {
    onLeccionClick(leccion) {
      this.selectedLeccion = leccion;
      console.log("Has hecho clic en:", leccion.id);
      if (leccion.id === 1) {
        this.$router.push("/ambos?tipo=normal");
      } else if (leccion.id === 2) {
        this.$router.push("ambos?tipo=iconos");
      } else if (leccion.id === 3) {
        this.$router.push("ambos?tipo=resaltado");
      }

      this.store.openLeccionModal();
    },
    onActividadClick(actividad) {
      this.isGeneratingEmpatia = true;
        fetch("http://143.47.45.118:5000/generation-api/v1/generation/absurdity_final", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: this.actividadSeleccionada.descripcion,
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Success:", data);
            this.datosEmpatia = data["message"];
            this.actividadSeleccionada = {
              titulo: `Actividad de Inclusion Generada`,
              descripcion: `Este es un juego de puntuación en el que los alumnos tratarán de conseguir la máxima pontuación contestando correctamente las preguntas. Sin embargo, habrá varias absurdas que no tendrán solución, y servirá como introducirán a la discalculia. 
              Pregunta después de la actividad sobre esas preguntas a los alumnos y sobre como se han sentido. Explica que hay compañeros que viven eso diariamente y que se tienen que apoyar entre ellos para facilitarselo un poco`,
            };
            this.isGeneratingEmpatia = false;
          })
          .catch((error) => {
            console.error("Error:", error);
            this.isGeneratingEmpatia = false;
          });
      console.log("Actividad seleccionada:", actividad.nombre);
    },
    abrirDialogCrearLeccion() {
      this.dialogCrearLeccion = true;
    },
    abrirDialogCrearActividad() {
      this.dialogCrearActividad = true;
    },
    generarLeccion() {
      this.isGenerating = true;

      this.lecciones.map((leccion) => {
        leccion.titulo = this.tema;
      });
      console.log(this.lecciones);
      this.store.setLecciones(this.lecciones);
      this.store.setLeccion(this.tema);
      console.log(this.store.getLecciones);

      console.log(
        `Generar lección para el tema: ${this.tema} en el curso ${this.selectedCurso}`
      );
        fetch("http://143.47.45.118:5000/generation-api/v1/generation/course", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: this.tema,
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Success:", data);
            this.store.setCourses(data["message"]);
            this.dialogCrearLeccion = false;
            this.isGenerating = false;
            store.openLeccionModal();
          })
          .catch((error) => {
            console.error("Error:", error);
            this.dialogCrearLeccion = false;
            this.isGenerating = false;
            this.store.openLeccionModal();
          });
    },
    accederEmpatia() {
      //useDataStore().setEmpathy(this.datosEmpatia);
      this.store.setEmpathy(this.datosEmpatia);
      this.$router.push("empatia");
    },
    iraEmpatia() {
      console.log("ir a empatia");
    },

    cambiarCurso(curso) {
      this.selectedCurso = curso;
    },
    añadirCurso() {
      console.log("Añadir un nuevo curso");
    },
    abrirConfiguracion() {
      console.log("Abrir configuración");
    },
    cerrarSesion() {
      console.log("Cerrar sesión");
    },
    mostrarNombreArchivo(event) {
      this.nombreArchivo = event.target.files[0]?.name || "";
    },
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      const file = event.target.files[0];
      this.processFile(file);
    },
    onDropFile(event) {
      this.isDragging = false;
      const file = event.dataTransfer.files[0];
      this.processFile(file);
    },
    processFile(file) {
      if (file) {
        this.nombreArchivo = file.name;

        if (file.type.startsWith("image/")) {
          this.isImage = true;
          const reader = new FileReader();
          reader.onload = (e) => {
            this.filePreview = e.target.result;
          };
          reader.readAsDataURL(file);
        } else {
          this.isImage = false;
          this.filePreview = null;
        }
      }
    },
    cerrarModalLeccion() {
      this.store.closeLeccionModal();
    },
    subirLeccion() {
      this.successModalVisible = true;
      this.store.closeLeccionModal();
    },
    cerrarSuccessModal() {
      this.successModalVisible = false;
    },
  },
};
</script>

<style scoped src="../style.css"></style>
