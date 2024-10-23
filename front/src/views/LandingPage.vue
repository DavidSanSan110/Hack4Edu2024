<template>
  <v-container fluid class="landing-page px-16">
    <v-row class="hero-section" align="center">
      <v-col cols="12" md="6">
        <div class="left-align">
          <h1 class="display-1 font-weight-bold">
            Go beyond and create your space
          </h1>
          <p class="subtitle-1">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cursus imperdiet sed idt.
          </p>
          <button class="custom-btn mt-6">Get started</button>
        </div>
      </v-col>
      <v-col cols="12" md="6">
        <div class="references">
          <p class="reference-text">E = mc<sup>2</sup></p>
          <p class="reference-text">Pythagorean theorem: a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></p>
          <p class="reference-text">Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
          <p class="reference-text">Integrals: ∫ f(x) dx</p>
        </div>
      </v-col>
    </v-row>
    <v-row class="card-section mt-10" justify="center">
      <v-col cols="12" md="3" v-for="n in 4" :key="n" class="d-flex justify-center">
        <v-card class="card-style pa-3" elevation="2">
          <v-card-title>
            <v-icon left>star</v-icon>
            Title
          </v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cursus imperdiet sed id elementum.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap");

.landing-page {
  background-color: #000;
  color: #fff;
  font-family: "Montserrat", sans-serif;
  min-height: 100vh;
}

.hero-section {
  padding-top: 100px;
  padding-bottom: 50px;
}

.display-1 {
  font-size: 3.5rem;
  line-height: 1.2;
}

.left-align {
  text-align: left;
}

.references {
  margin-top: 50px;
}

.reference-text {
  color: #888;
  font-style: italic;
  transform: rotate(-5deg);
  margin-bottom: 20px;
}

.card-section {
  padding-bottom: 100px;
}

.card-style {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(15px);
  border-radius: 16px;
  box-shadow: 0 0 5px 2px rgba(255, 255, 255, 0.5) inset;
  border: 1px solid #fff;
  color: #fff;
}

.subtitle-1 {
  color: #ccc;
  text-align: left;
}

.custom-btn {
  border-radius: 24px;
  font-size: 1.1rem;
  padding: 12px 24px;
  background-color: #fff;
  color: #000;
  border: 2px solid #fff;
  cursor: pointer;
  text-align: left;
  display: inline-block;
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}
</style>
