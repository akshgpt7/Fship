<template>
  <div class="fellow-card">
    <div class="uk-card uk-card-default uk-card-hover uk-card-body">
      <h3 class="uk-card-title fellow-name">{{ fellow.primary_details.name }} (@{{ fellow.primary_details.gitHandle }})</h3>
      <p></p>
      <p class="bio">{{ fellow.bio }}</p>
      <p>Country: <strong><em>{{ fellow.location.country }} ({{ fellow.location.timezone }})</em></strong></p>
      <p>Hobbies: <span class="uk-label label" v-for="hobby in fellow.hobbies" :key="hobby">{{ hobby }}</span></p>
      <p>Technical Interests: <span class="uk-label uk-label-warning label" v-for="skill in fellow.skills" :key="skill">{{ skill }}</span></p>
      <p>Loves to rant about: <span class="uk-label uk-label-danger label" v-for="dislike in fellow.dislikes" :key="dislike">{{ dislike }}</span></p>
      <a :href="'mailto:' + fellow.primary_details.email + '?subject=Reaching%20out%20via%20Fship&body=Join%20this%20meeting%20link%3A%20https%3A%2F%2Fmeet%2Ejit%2Esi%2F' + fellow.primary_details.gitHandle + 'MeetingFship'">
        <button class="uk-button uk-button-primary connect-button"><span class="uk-margin-small-right" uk-icon="mail"></span>Connect</button>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FellowCard',
  data () {
    return {
      hostname: this.$hostname
    }
  },
  props: {
    fellow: Object,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.fellow-name {
  padding-top: 0px !important;
}

.label {
  margin: 0 1px;
  font-size: 0.7em !important;
  padding: 0.3em;
}

.connect-button {
  background-color: green;
}

.bio {
  line-height: 1.2rem;
}

</style>

