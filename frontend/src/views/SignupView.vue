<template>
    <div class="signup">
        <h2>로그인</h2>
        <input v-model="email" type="email" placeholder="아이디(이메일)" />
        <input v-model="password" type="password" placeholder="비밀번호" />
        <button @click="signup">로그인</button>

        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from 'axios' 

export default {
    data() {
        return {
            email: '',
            password: '',
            message: ''
        }
    }, 
    methods: {
        async signup() {
            try {
                const res = await axios.post('/api/signup', {
                    email: this.email,
                    password: this.password
                })
                this.message = res.data.message
            } catch (err) {
                this.message = err.response?.data?.error || 'Error!' 
            }
        }
    }
}
</script>

<style scoped>
.signup {
    max-width: 400px;
    margin: 50px auto;
    display: flex;
    flex-direction: column;
}
h2 {
    margin-bottom: 50px;
}
input {
    margin-bottom: 20px;
    padding: 15px;
}
button {
    padding: 15px;
    margin-top: 20px;
    background: black;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 40px;
    cursor: pointer;
}
</style>