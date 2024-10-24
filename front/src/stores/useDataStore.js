import { defineStore } from 'pinia';

export const useDataStore = defineStore('data', {
  state: () => ({
    courses: {},
    empathy: [],
    isLeccionModalOpen: false,
    lecciones: [],
    leccion: "",
  }),
  actions: {
    setCourses(courses) {
      this.courses = courses;
    },
    openLeccionModal() {
      this.isLeccionModalOpen = true;
    },
    closeLeccionModal() {
      this.isLeccionModalOpen = false;
    },
    setEmpathy(empathy) {
      this.empathy = empathy;
    },
    setLecciones(lecciones) {
      this.lecciones = lecciones
    },
    setLeccion(leccion) {
      this.leccion = leccion;
    }
  },
  getters: {
    getCourses(state) {
      return state.courses;
    },
    getIsLeccionModalOpen(state) {
      return state.isLeccionModalOpen;
    },
    getEmpathy(state) {
      return state.empathy;
    },
    getLecciones(state) {
      return state.lecciones;
    },
    getLeccion(state) {
      return state.leccion;
    }
  },
  persist: true,
});
