<template>
<div>
  <select v-model="optionUser">
    <option v-for="user in list" :value="user.id">
      {{user.username}}
    </option>
  </select>
  <mu-button class="btn-send" round color="success" @click="AddUser">Добавить пользователя</mu-button>
</div>
</template>

<script>
export default {
  name: "AddUsers",

    data() {
      return {
        optionUser: '',
        list: ''
      }
    },
    props: {
        room:''
    },
    created() {
      //do something after creating vue instance
      this.LoadUsers()
      console.log('kkkkkkkkkkkkkkk');
    },
    methods: {
        // Получаю список пользователей
             LoadUsers() {
                 $.ajax({
                     url: "http://127.0.0.1:8000/api/v1/chat/users/",
                     type: "GET",
                     success: (response) => {
                         this.list = response.data.data
                         console.log('ddddddddd',response.data);
                     }
                 })
             },
      AddUser(){
          $.ajax({
              url: "http://127.0.0.1:8000/api/v1/chat/users/",
              type: "POST",
              data:{
                  room: this.room,
                  user: parseInt(this.optionUser)
              },
              success: (response) => {
                  alert('Пользователь добавлен')
              },
              error:(response) =>{
                  alert('error')
              }
      })
  },
},
}
  </script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
