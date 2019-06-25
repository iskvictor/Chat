
<template>
  <div>
  <input v-model='login' type='text' placeholder ="Логин" />
  <input v-model='password' type='password' placeholder ="Пароль" />
  <button  @click="setLogin"> Вход </button>
  </div>
</template>

<script>
import $ from 'jquery'
 export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/create/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },

                    success: (response) => {
                        console.log('response///',response.data.attributes.auth_token)
                        alert("Спасибо что Вы с нами")
                        sessionStorage.setItem('auth_token',response.data.attributes.auth_token)
                        this.$router.push({name:'home'})
                    },
                    error: (response) => {

                        if (response.status ===400){
                        alert("Пароль или логин не верен")}
                         console.log(response)
                    }
                })
            },
        }
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
