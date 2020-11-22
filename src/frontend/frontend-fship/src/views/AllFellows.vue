<template>
  <div class="all-fellows">
    <div class="uk-container-expand">
      <h1>All Registered Fellows and Alumni</h1>
      <h1 class="uk-heading-divider"></h1>
      <div id="spinner"><span uk-spinner="ratio: 4.5"></span></div>
      <div class="uk-child-width-1-4@s uk-grid-match fellows-div" uk-grid>

        <div v-for="fellow in fellows" :key="fellow.bio">
          <fellow-card :fellow="fellow"/>
        </div>

      </div>
    </div>
  </div>

</template>

<script>
// @ is an alias to /src
  import FellowCard from '@/components/FellowCard.vue'
  export default {
    name: 'AllFellows',
    components: {
      FellowCard,
    },
    data() {
      return {
        fellows: []
      }
    },
    methods: {

      async getAllFellows() {
        try {
          const response = await fetch(this.$hostname)
          let response_json = await response.json()
          let fellow_ids = []
          let fellows = []
          for (const i of response_json) {
            fellow_ids.push(i['id'])
          }
          for (const j of fellow_ids) {
            fellows.push(await this.createFellow(j))
          }

          this.fellows = fellows
        }
        catch (error) {
          this.fellows = []
        }
      }
      
    },

    mounted() {
      this.getAllFellows()
    },
    updated() {
      var spinner = document.querySelector('#spinner');
      spinner.parentNode.removeChild(spinner);

    },

  }
</script>

<style scoped>
.fellows-div {
  margin: 10px;
}

</style>
