<template>
  <div class="search">
    <div class="uk-container-expand pad">

      <div class="uk-flex">
        <div class="uk-width-1-3@m uk-panel" id="filters">
          <div class="uk-section uk-section-muted sticky">
            <div class="uk-container">
              <h3>Choose a Filter</h3> 
              <h1 class="uk-heading-divider"></h1>               
              <h4>Hobbies</h4>
              <button class="uk-button uk-button-primary label uk-button-small" v-for="hobby in allHobbies" :key="hobby.id" @click="showByHobby(hobby.id)">{{ hobby.name }}</button>
              <h1 class="uk-heading-divider"></h1>
              <h4>Technical Interests</h4>
              <button class="uk-button btn-ora label uk-button-small" v-for="skill in allSkills" :key="skill.id" @click="showBySkill(skill.id)">{{ skill.name }}</button>
              <h1 class="uk-heading-divider"></h1>
              <h4>Things to Rant about</h4>
              <button class="uk-button uk-button-danger label uk-button-small" v-for="dislike in allDislikes" :key="dislike.id" @click="showByDislike(dislike.id)">{{ dislike.name }}</button>
              </div>
          </div>
        </div>

        <div class="uk-width-2-3">
          <h2 class="spacing">Results</h2>
          <h1 class="uk-heading-divider"></h1>
          <div :key="showData.by">
            <div v-for="fellow in showData.fellows" :key="fellow">
              <div class="card">
                <fellow-card :fellow="fellow" />
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
  import FellowCard from '@/components/FellowCard.vue'
export default {
  name: 'Search',
  components: {
    FellowCard,
  },
  data() {
    return {
      showData: {},
      allHobbies: [],
      allSkills: [],
      allDislikes: []
    }
  },
  methods: {
    async getHobbies() {
      let response = await fetch(this.$hostname + 'hobbies/all')
      let json = await response.json()
      let hobs = json.hobbies
      let hobbies = []
      for (const i of hobs) {
        hobbies.push({"name": i.name, "id": i.id})
      }
      this.allHobbies = hobbies
    },

    async getSkills() {
      let response = await fetch(this.$hostname + 'skills/all')
      let json = await response.json()
      let sks = json.skills
      let skills = []
      for (const i of sks) {
        skills.push({"name": i.name, "id": i.id})
      }
      this.allSkills = skills
    },

    async getDislikes() {
      let response = await fetch(this.$hostname + 'dislikes/all')
      let json = await response.json()
      let dis = json.dislikes
      let dislikes = []
      for (const i of dis) {
        dislikes.push({"name": i.description, "id": i.id})
      }
      this.allDislikes = dislikes
    },

    async showByHobby(hobby_id) {
      let response = await fetch(this.$hostname + `hobbies/${hobby_id}/users`)
      let json = await response.json()
      let users = json.users
      let showData = {"by": hobby_id, "fellows": []}
      for (const i of users) {
        showData.fellows.push(await this.createFellow(i.id))
        this.showData = showData 
      }
    },
    async showBySkill(skill_id) {
      let response = await fetch(this.$hostname + `skills/${skill_id}/users`)
      let json = await response.json()
      let users = json.users
      let showData = {"by": skill_id, "fellows": []}
      for (const i of users) {
        showData.fellows.push(await this.createFellow(i.id))
        this.showData = showData 
      }
    },
    async showByDislike(dislike_id) {
      let response = await fetch(this.$hostname + `dislikes/${dislike_id}/users`)
      let json = await response.json()
      let users = json.users
      let showData = {"by": dislike_id, "fellows": []}
      for (const i of users) {
        showData.fellows.push(await this.createFellow(i.id))
        this.showData = showData 
      }
    },

  },
  mounted() {
    this.getDislikes()
    this.getSkills()
    this.getHobbies()
  }


}
</script>

<style scoped>
.label {
  margin: 2px 2px;
}

.card {
  margin: 3% 20%;
}

.sticky {
  position: sticky !important;
  top: 0;
}

.btn-ora {
  background-color: orange !important;
}

.spacing {
  margin-top: 3%;
}

</style>
