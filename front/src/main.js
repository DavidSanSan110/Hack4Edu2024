import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import '@mdi/font/css/materialdesignicons.css'
import './assets/index.css';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
  },
});

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

createApp(App)
  .use(vuetify)
  .use(pinia)
  .use(router)
  .mount("#app");
