<template>
<mu-col span="4" xl="2" class="room-list">
  <mu-button @click="addRoom"> Создать комнату </mu-button>
  <div v-for="room in rooms">
    <h3 @click='openDialog(room.id)'>{{room.creater.username}}--room{{room.id}}</h3>
    <small>{{room.date}}</small>
  </div>
</mu-col>
</template>

<script>
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
          console.log('room*************', response)
        }
      })
    },
    openDialog(id) {
      this.$emit("opendialogroom", id)
      console.log('opendialogroom+++++++++++++', id)
    },
    addRoom() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/chat/room/",
        type: "POST",
        success: (response) => {
          this.loadRoom()
        },
        error:(response) =>{
            alert(response.statusText)
        }

      })
    }

  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.room-list {
  margin: 10px;
  box-shadow: 10px 8px 8px #ccc;
}
</style>
