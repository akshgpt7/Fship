<template>
  <div class="register">
    <div class="uk-container spacing">
      <h1>Register new Fellow</h1>
      <h1 class="uk-heading-divider"></h1>

      <p v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li class="error" v-for="error in errors" :key="error">{{ error }}</li>
        </ul>
      </p>

      <form @submit.prevent="getFormValues" class="uk-form-horizontal uk-margin-large">

        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Name: </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="name">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">GitHub username: </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="github">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Email: </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="email">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Password: </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="password" name="password">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Bio: </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="bio">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Country, Timezone[eg. GMT+1:00] (comma separated): </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="location">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Hobbies (comma separated): </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="hobbies">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Tech skills (comma separated): </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="skills">
          </div>
        </div>
        <div class="uk-margin">
          <label class="uk-form-label" for="form-horizontal-text">Things you'd love to rant about (comma separated): </label>
          <div class="uk-form-controls">
            <input class="uk-input" id="form-horizontal-text" type="text" name="dislikes">
          </div>
        </div>
        <button class="uk-button uk-button-secondary">Done</button>

      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  components: {
  },
  data() {
    return {
      errors: [],
      details: {}
    }
  },
  methods: {
    getFormValues(submitEvent) {
      this.errors = []

      this.details.name = submitEvent.target.elements.name.value
      this.details.github = submitEvent.target.elements.github.value
      this.details.email = submitEvent.target.elements.email.value
      this.details.password = submitEvent.target.elements.password.value
      this.details.bio = submitEvent.target.elements.bio.value
      this.details.hobbies = submitEvent.target.elements.hobbies.value.split(',')
      this.details.skills = submitEvent.target.elements.skills.value.split(',')
      this.details.dislikes = submitEvent.target.elements.dislikes.value.split(',')
      this.details.location = submitEvent.target.elements.location.value.split(',')

      if (this.details.name === '') {
        this.errors.push('Name required.');
      }
      if (this.details.github === '') {
        this.errors.push('GitHub username required.');
      }
      if (this.details.email === '') {
        this.errors.push('Email required.');
      }
      if (this.details.password === '') {
        this.errors.push('Password required.');
      }

      if (!this.errors.length) {
        this.createUser()
      }

    },
    async createUser() {
      let post = await fetch(this.$hostname + 'user/register', { 
      method: 'POST', body: JSON.stringify(this.details)}
      )
      if (await post.status == 200) {
        this.$router.push('/');

      }

    }



  },
}

</script>

<style scoped>

.error {
  color: red;
}

.spacing {
  padding: 2%;
}

</style>
