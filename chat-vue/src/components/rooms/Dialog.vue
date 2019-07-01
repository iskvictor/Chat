<template>
<mu-col span='8' xl='9' >
  <mu-container class="dialog">
    <mu-row direction="column" justify-content="start" align-items="end" v-for="dialog in dialogs" v-bind:key="dialog.key">
      <p><strong>{{dialog.user.username}}</strong></p>
      <p>{{dialog.text}}</p>
      <span>{{dialog.date}}</span>
  </mu-row>
  </mu-container>
  <mu-container>
      <mu-row align-items="end">
          <mu-text-field
                v-model="form.textarea"
                multi-line :rows="4"
                full-width
                placeholder="Введите текст сообщения" >
            </mu-text-field>
        <mu-button round color="success">Отправить</mu-button>
      </mu-row>
  </mu-container>
</mu-col>
</template>
<script>
import $ from 'jquery'
export default {
  name: "Dialog",
  props: {
    id: '',
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
    this.loadDialog()
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
    }
  }
}
</script>

<style scoped>
.dialog {
  border: 1px solid #000;
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
