<!--
 * @Author: Axiuxiu
 * @Date: 2022-02-26 20:39:12
 * @LastEditTime: 2022-03-23 10:17:57
 * @Description: App
-->

<template>
    <div class="app">
        <!-- <keep-alive :include="['Login','Register']">
            <router-view></router-view>
        </keep-alive>-->
        <router-view></router-view>
    </div>
</template>

<script>
import jwtDecode from "jwt-decode";

export default {
    name: "App",
    created() {
        // 判断是否登录
        const userToken = localStorage.getItem("userToken");
        const avatar_url=localStorage.getItem('avatar_url');
        const username=localStorage.getItem('username');
        if (userToken) {
            let user = jwtDecode(userToken);
            user.avatar_url=avatar_url;
            user.username=username;
            // 同步vuex状态
            this.$store.dispatch("setLoginState", user);
        }
    },
};
</script>

<style>
html,
body,
.app {
    width: 100%;
    height: 100%;
    /* min-width: 1000px; */
    min-height: 600px;
}

.clearfix::before,
.clearfix::after{
    content: '';
    display: table;
    clear: both;
}
</style>
