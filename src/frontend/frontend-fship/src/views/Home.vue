<template>
  <div class="home">
    <div class="uk-container-expand">
      <h1 class="uk-heading-medium">Fship</h1>
      <h3><span uk-icon="icon: users; ratio: 2.5"></span> (Friend|Fellow)ship</h3>
      <h1 class="uk-heading-divider"></h1>

      <p uk-margin class="buttons">
        <router-link to="/search"><button class="uk-button uk-button-large uk-button-secondary"><span class="uk-margin-small-right" uk-icon="commenting"></span> Find Like-minded Fellows</button></router-link>
        <router-link to="/all-fellows"><button class="uk-button uk-button-large uk-button-secondary"><span class="uk-margin-small-right" uk-icon="social"></span>See All Fellows</button></router-link>
      </p>

    </div>
  </div>

</template>

<script>
// @ is an alias to /src
export default {
  name: 'Home',
  components: {
  }
}
</script>

<style scoped>
.home {
  margin-top: 3%
}

h1 {
  font-family: Impact, Charcoal, sans-serif;
  padding-bottom: 0;
}

h3 {
  font-family: "Courier New", Courier, monospace;
}

p.buttons {
  margin-top: 6% !important;
}

.uk-button {
  margin: 0.5% !important;
}
</style>
