<!--
 * @Author: Axiuxiu
 * @Date: 2022-02-27 10:21:02
 * @LastEditTime: 2022-03-23 15:06:41
 * @Description: 登录页面
-->

<template>
    <div class="login">
        <div class="form-container">
            <!-- 表格标题 -->
            <div class="form-title">
                XXXX系统
            </div>

            <!-- 表格 -->
            <el-form class="form" :model="loginForm" ref="loginForm" :rules="rules" label-width="80px" :inline="false" size="normal">
                <!-- 邮箱 -->
                <el-form-item label="邮箱" prop="email">
                    <el-input v-model.trim="loginForm.email"></el-input>
                </el-form-item>

                <!-- 密码 -->
                <el-form-item label="密码" prop="pwd">
                    <el-input v-model.trim="loginForm.pwd" type="password"></el-input>
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="onSubmit('loginForm')">登录</el-button>
                    <el-button type="reset" v-on:click="reset('loginForm')">清空</el-button>
                </el-form-item>

                <div class="tips">
                    <p>
                        还没有账号？现在
                        <router-link to="/register">注册</router-link>
                    </p>
                </div>
            </el-form>
            
        </div>
    </div>
</template>

<script>
// 引入jwt-decode
import jwtDecode from 'jwt-decode';

export default {
    name:'Login',
    data() {
        return {
            rules:{
                email:[
                    { required: true, message:'邮箱不能为空', tigger:'blur' },
                    { type:'email', message:'邮箱格式不正确', trigger:'blur' },
                ],
                pwd:[
                    { required: true, message:'密码不能为空', tigger:'blur' },
                    { min: 3, max: 20, message:'密码长度必须在3-20之间', trigger:'blur' },
                ]
            },
            loginForm:{
                email:'',
                pwd:'',
            }
        }
    },
    methods: {
        onSubmit(formName){
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // console.log(this.loginForm);
                    // 提交表单
                    this.$axios.post('/api/users/login',this.loginForm)
                    .then(res => {
                        // console.log(res);
                        let data=res.data;
                        if(data.code==200){
                            const userToken=data.userToken;
                            const avatar_url=data.avatar_url;
                            const username=data.username;
                            const isAdmin=data.isAdmin;
                            // 存储
                            localStorage.setItem('userToken',userToken);
                            localStorage.setItem('avatar_url',avatar_url);
                            localStorage.setItem('username',username);
                            localStorage.setItem('isAdmin', isAdmin);
                            // 解析token, 同步至state
                            let user=jwtDecode(userToken);
                            user.avatar_url=avatar_url;
                            user.username=username;
                            this.$store.dispatch('setLoginState',user);

                            this.$message({
                                showClose: true,
                                type: 'success',
                                message: '登录成功',
                            });
                            // 跳转至 首页
                            this.$router.push('/manage');
                        }
                    })
                    .catch(err => {
                        console.error(err); 
                    })
                } else {
                    console.log('form error');
                    return false;
                }
            });
        },
        reset(formName){
            this.$refs[formName].resetFields();
        }
    },
}
</script>

<style scoped>
.login{
    width: 100%;
    height: 100%;
    background-image: url('../../assets/bg.jpg');
    background-size: 100% 100%;
}

.form-container{
    width: 370px;
    position: absolute;
    top: 15%;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
}

.form-container .form-title{
    font-weight: bold;
    font-size: 26px;
    color: white;
}

.form-container .form{
    background-color: white;
    margin-top: 20px;
    padding: 20px 40px 20px 10px;
    border-radius: 5px;
    box-shadow: 0px 5px 10px #cccc;

}
</style>
