<!--
 * @Author: Axiuxiu
 * @Date: 2022-02-26 20:39:12
 * @LastEditTime: 2022-03-01 14:51:39
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
        if (userToken) {
            const user = jwtDecode(userToken);
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
    min-width: 1000px;
    min-height: 600px;
}

html,
body {
    overflow: hidden;
}
</style>
