<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-01 16:47:03
 * @LastEditTime: 2022-03-16 09:18:07
 * @Description: 头部区域
-->

<template>
    <div class="header">
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/manage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item v-for="(item, index) in meta" :key="index">{{item}}</el-breadcrumb-item>
        </el-breadcrumb>

        <div class="user-info">
            <img :src="user.avatar_url" alt class="avatar" />

            <div class="welcome">
                <el-dropdown @command="handleCommand">
                    <span class="el-dropdown-link">
                        欢迎，
                        <b>{{user.username}}</b>
                        <i class="el-icon-arrow-down el-icon--right"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item command="logout">退出</el-dropdown-item>
                        <el-dropdown-item command="userInfo">个人信息</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    name: "Header",
    computed: {
        ...mapState(["user"]),
        meta() {
            return this.$route.meta;
        },
    },
    methods: {
        handleCommand(cmd) {
            if (!cmd) {
                this.$message({
                    showClose: true,
                    type: "error",
                    message: "菜单项缺少command属性！",
                });
                return;
            }
            // 处理命令
            switch (cmd) {
                case "logout":
                    this.logout();
                    break;
                case "userInfo":
                    this.userInfo();
                    break;
            }
        },
        logout(){
            // 清除登录状态
            localStorage.removeItem('userToken');
            localStorage.removeItem('avatarUrl');
            this.$store.dispatch('clearLoginState');

            // 返回登录页面
            this.$router.push('/login');
        },
        userInfo(){
            this.$router.push('/user/userInfo');
        }
    },
};
</script>

<style scoped>
.header {
    height: 45px;
    padding-left: 10px;
    background-color: #eff2f7;
    color: #a4b3c7;
    position: relative;
}

.header ::v-deep .el-breadcrumb {
    line-height: 45px;
    font-size: 14px;
}

/* 用户信息展示 */
.user-info {
    /* width: 200px;
    height: 100%; */
    position: absolute;
    /* background-color: #bfa; */
    right: 30px;
    top: 0;
}

.user-info > * {
    float: left;
}

.user-info .avatar {
    width: 40px;
    height: 40px;
    margin-top: 2px;
    /* display: inline-block; */
    border-radius: 50%;
}

.user-info .welcome {
    line-height: 45px;
    margin-left: 10px;
    /* cursor: pointer; */
}

.el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
</style>