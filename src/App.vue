<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title><h1 class="font-italic">Fship </h1></v-toolbar-title>
      <div class="d-flex align-center">
        <v-img
          alt="Fship logo"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="./assets/FSHIPLOGO.png"
          width="60"
          height="60"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
       @click="$router.push('/')"
       text
      >
        <span class="mr-2">Home</span>
       
        
      </v-btn>
      <v-btn
       @click="$router.push('/login')"
       text
      >
        <span class="mr-2">Signup</span>
        
        
      </v-btn>
    </v-app-bar>

    <v-main>
     
        <router-view></router-view>
     
    </v-main>
  </v-app>
</template>

<script>


export default {
  name: "App",



  data: () => ({
    //
  }),
};
</script>


