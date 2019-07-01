<template>
<mu-container>
  <mu-appbar style="width: 100%;" color="primary">
      <mu-button flat slot="right" v-if="!auth" @click="goLogin"> Вход </mu-button>
      <mu-button flat slot="right" v-else @click="logout"> Выход </mu-button>
    Чат на vue.js
  </mu-appbar>

  <mu-row>
    <Room v-if="auth" @opendialogroom="openDialog"></Room>
    <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
  </mu-row>
</mu-container>
</template>

<script>
import Room from '@/components/rooms/Room.vue'
import Dialog from '@/components/rooms/Dialog.vue'
export default {
  name: "Home",
  components: {
    Room,
    Dialog,
  },
  data() {
    return {
      dialog: {
        id: '',
        show: false,
      }
    }
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("auth_token")) {
        return true
      }
    }
  },
  methods: {
    goLogin() {
      this.$router.push({
        name: "login"
      })
    },
    logout() {
      sessionStorage.removeItem("auth_token")
      window.location = '/'
    },
    openDialog(id) {
      this.dialog.id = id
      this.dialog.show = true
      console.log('opendialoghome*****+++', this.dialog.show)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
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
