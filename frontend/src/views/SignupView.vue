<template>
    <div class="signup">
        <h2>Sign up</h2>
        <input v-model="email" type="email" placeholder="email" />
        <input v-model="password" type="password" placeholder="password" />
        <button @click="signup">Sign up</button>

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
input {
    margin-bottom: 10px;
    padding: 10px;
    font-size: 1rem;
}
button {
    padding: 10px;
    background: #4caf50;
    color: white;
    font-weight: bold;
    border: none;
    cursor: pointer;
}
</style>