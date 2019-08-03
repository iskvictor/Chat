<template>
<mu-col span='8' xl='9'>
    <AddUsers :room='id'></AddUsers>
  <mu-container class="dialog">
    <mu-row direction="column" justify-content="start" align-items="end" v-for="dialog in dialogs" v-bind:key="dialog.key">
      <p><strong>{{dialog.user.username}}</strong></p>
      <p>{{dialog.text}}</p>
      <span>{{dialog.date}}</span>
    </mu-row>
  </mu-container>
  <mu-container>
    <mu-row align-items="end">
      <mu-text-field v-model="form.textarea" multi-line :rows="4" full-width placeholder="Введите текст сообщения">
      </mu-text-field>
      <mu-button round color="success" @click='sendMes()'>Отправить</mu-button>
    </mu-row>
  </mu-container>
</mu-col>
</template>
<script>
import AddUsers from "@/components/rooms/AddUsers.vue"
export default {
  name: "Dialog",
  props: {
            id: '',
        },
  components: {
    AddUsers
  },
  data() {
    return {
      dialogs: '',
      form: {
        textarea: '',
      }
    }
  },

  created() {
    $.ajaxSetup({
      headers: {
        'Authorization': "Token " + sessionStorage.getItem('auth_token')
      },
    });
    this.loadDialog();
    setInterval(() => {
       console.log('setinterval-------')
      this.loadDialog()
  }, 5000)
  },
  methods: {
    loadDialog() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
        type: "GET",
        data: {
          room: this.id
        },
        success: (response) => {
          this.dialogs = response.data.data
          console.log('Dialog')
        }
      })
    },
    sendMes() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
        type: "POST",
        data: {
          room: this.id,
          text: this.form.textarea
        },
        success: (response) => {
          this.loadDialog()
        },
        error: (response) => {
          alert(response.statusText)
        }
      })

    }
  }
}
</script>

<style scoped>
.dialog {
  border: 1px solid #000;
  margin-top: 100px;
}

h1,
h2 {
  font-weight: normal;
}

h3 {
  cursor: pointer;
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
