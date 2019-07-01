<template>
<mu-col span="4" xl="2" class="room-list">
  <div v-for="room in rooms">
    <h3 @click='openDialog(room.id)'>{{room.creater.username}}--room{{room.id}}</h3>
    <small>{{room.date}}</small>
  </div>
</mu-col>
</template>

<script>
import $ from 'jquery'
export default {
  name: "Room",
  data() {
    return {
      rooms: '',
    }
  },
  created() {
    $.ajaxSetup({
      headers: {
        'Authorization': "Token " + sessionStorage.getItem('auth_token')
      },
    });
    this.loadRoom()
  },
  methods: {
    loadRoom() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/chat/room/",
        type: "GET",
        success: (response) => {
          this.rooms = response.data.data
          console.log('room*************', response.data)
        }
      })
    },
    openDialog(id) {
      this.$emit("opendialogroom", id)
      console.log('opendialogroom+++++++++++++', id)
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.room-list{
    margin: 10px;
    box-shadow: 10px 8px 8px #ccc;
}
</style>
