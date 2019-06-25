<template>
  <div>
  <h1> Чат на vue.js</h1>
  <button  @click="goLogin"> Вход </button>
  <room></room>
  </div>
</template>

<script>

import Room from  '@/components/Room.vue'
export default {
  name: 'Home',
  components:{
  Room
  },
  methods:{
      goLogin(){
          this.$router.push({name:'login'})
      },
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
