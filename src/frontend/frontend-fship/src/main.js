import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
Vue.prototype.$hostname = 'http://localhost:8000/'

Vue.mixin({
  methods: {
    createFellow: async function (id) {
      let details = {}

      let response = await fetch(this.$hostname + `user/${id}`)
      let resp = await response.json()
      details['primary_details'] = resp


      response = await fetch(this.$hostname + `user/${id}/hobbies`)
      let hobbies = await response.json()
      let hobby_list = []
      for (const i of hobbies['hobbies']) {
        hobby_list.push(i['name'])
      }
      details['hobbies'] = hobby_list

      response = await fetch(this.$hostname + `user/${id}/skills`)
      let skills = await response.json()
      let skills_list = []
      for (const i of skills['skills']) {
        skills_list.push(i['name'])
      }
      details['skills'] = skills_list

      response = await fetch(this.$hostname + `user/${id}/bio`)
      let _bio = await response.json()
      details['bio'] = _bio.bio.description

      response = await fetch(this.$hostname + `user/${id}/location`)
      let location = await response.json()
      details['location'] = location['location']

      response = await fetch(this.$hostname + `user/${id}/dislikes`)
      let dislikes = await response.json()
      let dislikes_list = []
      for (const i of dislikes['dislikes']) {
        dislikes_list.push(i['description'])
      }
      details['dislikes'] = dislikes_list.filter(dis => dis != '')

      return details
      
    },
  },
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
