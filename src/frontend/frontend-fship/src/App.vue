<template>
  <div id="app">
    <nav class="uk-navbar-container navBar" uk-navbar>
      <div class="uk-navbar-left">
          <a class="uk-navbar-item uk-logo logo" href="/"><img src="@/assets/fship-logo.jpg"></a>
      </div>
      <div class="uk-navbar-right">
        <ul class="uk-navbar-nav">
          <li> <router-link to="/">Home</router-link> </li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/about">Profile</router-link></li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.navBar {
    background-color: black !important;
    padding: 0 5% !important;
}

.fellow-div {
  background-color: #8db596;
}

.logo {
  width: 35% !important;
}

</style>
