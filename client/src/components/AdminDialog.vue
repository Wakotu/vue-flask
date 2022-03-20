<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-17 19:52:26
 * @LastEditTime: 2022-03-20 15:50:25
 * @Description: 用户管理对话框
 * @Todo: 
-->

<template>
    <div class="admin-dialog">
        <el-dialog :title="dialog.title" :visible.sync="dialog.visible" width="30%">
            <el-form
                :model="dialog.form"
                ref="form"
                :rules="rules"
                label-width="80px"
                :inline="false"
                size="normal"
            >
                <el-form-item label="邮箱" prop="email">
                    <el-input v-model="dialog.form.email"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="pwd">
                    <el-input type="password" v-model="dialog.form.pwd"></el-input>
                </el-form-item>
                <el-form-item label="用户名" prop="username">
                    <el-input v-model="dialog.form.username"></el-input>
                </el-form-item>
                <el-form-item label="身份" prop="identity">
                    <el-radio v-model="dialog.form.identity" label="admin">管理员</el-radio>
                    <el-radio v-model="dialog.form.identity" label="user">普通用户</el-radio>
                </el-form-item>
                <el-form-item label="性别" prop="gender">
                    <el-radio v-model="dialog.form.gender" label="male">男</el-radio>
                    <el-radio v-model="dialog.form.gender" label="female">女</el-radio>
                </el-form-item>
                <el-form-item label="所属单位" prop="unit">
                    <el-input v-model="dialog.form.unit"></el-input>
                </el-form-item>
                <el-form-item label="地址" prop="address">
                    <el-input v-model="dialog.form.address"></el-input>
                </el-form-item>
            </el-form>

            <span slot="footer">
                <el-button @click="closeDialog">取消</el-button>
                <el-button type="primary" @click="onSubmit('form')">提交</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
export default {
    name: "AdminDialog",
    props: ["dialog"],
    data() {
        return {
            rules: {
                email: [
                    { required: true, message: "请输入邮箱", trigger: "blur" },
                    {
                        type: "email",
                        message: "邮箱格式不正确",
                        trigger: "blur",
                    },
                ],
                pwd:[
                    // { required: true, message: "请输入密码", trigger: "blur" },
                    { min: 3, max: 20, message: "密码长度必须在3到20之间", trigger: "blur" },
                ],
                username:[
                    { required: true, message: "请输入用户名", trigger: "blur" },
                ],
                identity:[
                    { required: true, message: "请选择身份", trigger: "blur" },
                ],
                gender:[
                    { required: true, message: "请选择性别", trigger: "blur" },
                ],
                unit:[
                    { required: true, message: "请输入所属单位", trigger: "blur" },
                ],
                address:[
                    { required: true, message: "请输入地址", trigger: "blur" },
                ]
            },
        };
    },
    methods: {
        closeDialog() {
            this.$emit("closeDialog");
        },
        onSubmit(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    let reqUrl = "";
                    if (this.dialog.title === "添加") {
                        reqUrl = "/api/users/addUser";
                    }
                    else if(this.dialog.title==='编辑'){
                        reqUrl='/api/users/editUser';
                    }
                    this.$axios
                        .post(reqUrl, {
                            form: this.dialog.form,
                            user_id: this.dialog.user_id,
                        })
                        .then((res) => {
                            this.$message({
                                showClose: true,
                                type: "success",
                                message: res.data.info,
                            });
                            this.$emit("update");
                            this.$emit("closeDialog");
                        })
                        .catch((err) => {
                            console.error(err);
                        });
                } else {
                    console.log("form error");
                    return false;
                }
            });
        },
    },
};
</script>

<style>
</style>