import { defineStore } from 'pinia';

export const useDataStore = defineStore('data', {
  state: () => ({
    courses: {},
    empathy: [],
    isLeccionModalOpen: false,
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
    }
  },
  persist: true,
});
