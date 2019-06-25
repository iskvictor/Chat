<template>
  <div>
  <h1> Room</h1>
  ${{rooms}}
  <ul
      <li v-for="room in rooms">fsdfsdf{{room}} </li>
  </ul>


  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Room',
  data(){
      return{
          rooms:'',
          }
  },
  created(){
      $.ajaxSetup({
          headers:{'Authorization':'Token '+sessionStorage.getItem('auth_token')}
      });
      this.loadRoom()
  },
  methods:{
      loadRoom(){
          $.ajax({
              url:"http://127.0.0.1:8000/api/v1/chat/room/",
              type:'GET',
              success:(response)=>{
                  this.rooms = response.data
                  console.log(response)
                  }
          });


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
