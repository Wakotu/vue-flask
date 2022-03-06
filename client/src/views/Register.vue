<!--
 * @Author: Axiuxiu
 * @Date: 2022-02-27 14:02:02
 * @LastEditTime: 2022-02-27 17:55:04
 * @Description: 注册页面
-->
<template>
    <div class="register">
        <div class="form-container">
            <!-- 表格标题 -->
            <div class="form-title">XXXX系统</div>

            <!-- 表格 -->
            <el-form
                class="form"
                :model="registerForm"
                ref="registerForm"
                :rules="rules"
                label-width="80px"
                :inline="false"
                size="normal"
            >
                <!-- 邮箱 -->
                <el-form-item label="邮箱" prop="email">
                    <el-input v-model.trim="registerForm.email"></el-input>
                </el-form-item>

                <!-- 用户名 -->
                <el-form-item label="用户名" prop="username">
                    <el-input v-model.trim="registerForm.username"></el-input>
                </el-form-item>

                <!-- 密码 -->
                <el-form-item label="密码" prop="pwd">
                    <el-input v-model.trim="registerForm.pwd" type="password"></el-input>
                </el-form-item>

                <!-- 确认密码 -->
                <el-form-item label="确认密码" prop="pwd2">
                    <el-input v-model.trim="registerForm.pwd2" type="password"></el-input>
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="onSubmit('registerForm')">注册</el-button>
                    <el-button type="reset" v-on:click="reset('registerForm')">清空</el-button>
                </el-form-item>

                <div class="tips">
                    <p>
                        直接
                        <router-link to="/login">登录</router-link>
                    </p>
                </div>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
    name: "Register",
    data() {
        // 注意要使用箭头函数
        const checkPwd2 = (rule, value, callback) => {
            if(value==this.registerForm.pwd){
                callback();
            }else{
                callback(new Error('两次输入密码不一致!'));
            }
        }

        return {
            registerForm: {
                email: "",
                username: "",
                pwd: "",
                pwd2: "",
            },
            rules: {
                email: [
                    {
                        required: true,
                        message: "邮箱不能为空",
                        trigger: "blur",
                    },
                    {
                        type: "email",
                        message: "邮箱格式不正确",
                        trigger: "blur",
                    },
                ],
                username: [
                    {
                        required: true,
                        message: "用户名不能为空",
                        trigger: "blur",
                    },
                ],
                pwd: [
                    { required: true, message: "密码不能为空", tigger: "blur" },
                    {
                        min: 3,
                        max: 20,
                        message: "密码长度必须在3-20之间",
                        trigger: "blur",
                    },
                ],
                pwd2:[
                    { required: true, message: "请再次输入密码", tigger: "blur" },
                    { validator: checkPwd2, trigger:'blur' },
                ]
            },
        };
    },
    methods: {
        onSubmit(formName){
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // console.log(this.registerForm);
                    // 发送请求进行注册
                    let {pwd2, ...form}=this.registerForm;
                    console.log(form);
                    this.$axios.post('/api/users/register',form)
                    .then(res => {
                        // console.log(res)
                        let data=res.data;
                        if (data.code==200){
                            this.$message({
                                showClose: true,
                                type: 'success',
                                message: '注册成功',
                            });
                        this.$router.push('/login');
                        }else{
                            this.$message({
                                showClose: true,
                                type: 'error',
                                message: '注册失败'
                            });
                        }
                    })
                    .catch(err => {
                        console.error(err); 
                    })
                } else {
                    return false;
                }
            });
        },
        reset(formName){
            this.$refs[formName].resetFields();
        }
    },
};
</script>

<style scoped>
.register {
    width: 100%;
    height: 100%;
    background-image: url("../assets/bg.jpg");
    background-size: 100% 100%;
}

.form-container{
    width: 370px;
    position: absolute;
    top: 10%;
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