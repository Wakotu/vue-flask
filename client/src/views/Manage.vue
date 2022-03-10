<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-01 14:41:47
 * @LastEditTime: 2022-03-08 13:33:50
 * @Description: 管理页面
-->

<template>
    <div class="manage">
        <el-row style="height: 100%;">
            <el-col :span="4" class="menu-container">
                <el-menu
                    :default-active="defaultActive"
                    class="menu"
                    background-color="#324057"
                    text-color="rgb(191,203,217)"
                    router
                >
                    <el-menu-item index="/manage">
                        <i :style="iconStyle" class="el-icon-menu"></i>首页
                    </el-menu-item>
                    <!-- 子菜单 -->
                    <el-submenu index="2">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-warning"></i>热点事件预警
                        </template>
                        <el-menu-item index="/warning/hotEvents">热点事件展示</el-menu-item>
                        <el-menu-item index="shopList">菜单项</el-menu-item>
                        <el-menu-item index="foodList">菜单项</el-menu-item>
                        <el-menu-item index="orderList">菜单项</el-menu-item>
                        <el-menu-item index="adminList">菜单项</el-menu-item>
                    </el-submenu>
                    <!-- 子菜单 -->
                    <el-submenu index="3">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-plus"></i>水军账号监管
                        </template>
                        <el-menu-item index="addShop">菜单项</el-menu-item>
                        <el-menu-item index="addGoods">菜单项</el-menu-item>
                    </el-submenu>
                    <!-- 子菜单 -->
                    <el-submenu index="4">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-star-on"></i>多级自动检测
                        </template>
                        <el-menu-item index="visitor">菜单项</el-menu-item>
                        <!-- <el-menu-item index="newMember">用户数据</el-menu-item> -->
                    </el-submenu>
                    <!-- 子菜单 -->
                    <el-submenu index="6">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-setting"></i>用户管理
                        </template>
                        <el-menu-item index="adminSet">菜单项</el-menu-item>
                        <!-- <el-menu-item index="sendMessage">发送通知</el-menu-item> -->
                    </el-submenu>
                    <el-submenu index="7">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-document"></i>子菜单
                        </template>
                        <el-menu-item index="explain">菜单项</el-menu-item>
                    </el-submenu>
                </el-menu>
            </el-col>

            <!-- 具体页面 -->
            <el-col :span="20" style="height: 100%;overflow: auto;">
                <keep-alive>
                    <router-view></router-view>
                </keep-alive>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
    name: "Manage",
    data() {
        return {
            iconStyle: {
                color: "#BFCBD9",
            },
        };
    },
    computed: {
        defaultActive: function () {
            return this.$route.path;
        },
    },
    methods: {
        // handleSelect(key, path) {
        //     console.log(key, path);
        // },
    },
};
</script>

<style scoped>
.manage {
    width: 100%;
    height: 100%;
    background-color: white;
}

.menu-container {
    height: 100%;
    min-height: 500px;
    background-color: #324057;
    overflow: auto;
}

.menu {
    height: 100%;
    border: none;

}

::v-deep .el-menu-item:hover {
    background-color: #48576a !important;
}

::v-deep .el-submenu__title:hover {
    background-color: #48576a !important;
}

::v-deep .el-submenu .el-menu-item {
    background-color: #1f2d3d !important;
}

::v-deep .el-submenu .el-menu-item:hover {
    background-color: #48576a !important;
}
</style>
