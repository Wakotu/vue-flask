<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-01 14:41:47
 * @LastEditTime: 2022-03-26 12:39:21
 * @Description: 管理页面
-->

<template>
    <div class="manage">
        <el-row style="height: 100%;">
            <el-col :span="4" class="sidebar">
                <div class="logo-container">
                    <!-- 这里有个<b>logo</b> -->
                    <img class="logo" src="../assets/ideoloc.png" alt="">
                </div>
                <div class="menu-container">
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
                                <i :style="iconStyle" class="el-icon-warning"></i>热点事件
                            </template>
                            <el-menu-item index="/events/hotEvents">热点事件展示</el-menu-item>
                            <el-menu-item index="/events/eventAnalysis">热点事件分析</el-menu-item>
                        </el-submenu>
                        <!-- 子菜单 -->
                        <el-submenu index="3">
                            <template slot="title">
                                <i :style="iconStyle" class="el-icon-plus"></i>单体水军检测
                            </template>
                            <el-menu-item index="/single/userReco">特定用户识别</el-menu-item>
                            <el-menu-item index="/single/resultList">检测结果展示</el-menu-item>
                            <el-menu-item index="/single/userImage">水军用户画像</el-menu-item>
                        </el-submenu>
                        <!-- 子菜单 -->
                        <el-submenu index="4">
                            <template slot="title">
                                <i :style="iconStyle" class="el-icon-star-on"></i>水军群体展示
                            </template>
                            <el-menu-item index="visitor">水军群体列表</el-menu-item>
                            <el-menu-item index="visitor">水军群体画像</el-menu-item>
                            <el-menu-item index="visitor">水军群体概览</el-menu-item>
                            <!-- <el-menu-item index="newMember">用户数据</el-menu-item> -->
                        </el-submenu>
                        <!-- 子菜单 -->
                        <el-submenu index="6">
                            <template slot="title">
                                <i :style="iconStyle" class="el-icon-setting"></i>用户管理
                            </template>
                            <el-menu-item index="/user/userInfo">个人信息</el-menu-item>
                            <el-menu-item index="/user/userList">用户列表</el-menu-item>
                        </el-submenu>
                        <el-submenu index="7">
                            <template slot="title">
                                <i :style="iconStyle" class="el-icon-document"></i>系统管理
                            </template>
                            <el-menu-item index="/system/taskManage">任务配置</el-menu-item>
                            <el-menu-item index="/system/spiderManage">爬虫程序监测</el-menu-item>
                            <el-menu-item index="/system/analysisManage">分析程序监测</el-menu-item>
                        </el-submenu>
                    </el-menu>
                </div>
            </el-col>

            <!-- 具体页面 -->
            <el-col :span="20" style="height: 100%;overflow: auto;">
                <!-- <keep-alive>
                    <router-view></router-view>
                </keep-alive> -->
                <router-view></router-view>
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

.sidebar{
    height: 100%;
}

.logo-container{
    height: 64px;
    background-color: #304156;
    color: white;
    line-height: 64px;
    font-size: 25px;
    text-align: center;
    overflow: hidden;
    /* position: relative; */
}
 
.logo-container .logo{
    width: 90%;
    height: 100%;
}

.menu-container {
    height: calc(100% - 64px);
    /* min-height: 500px; */
    background-color: #324057;
    overflow-y: auto;
    overflow-x: hidden;
}

/* 设置menu-container滚动条样式 */
.menu-container::-webkit-scrollbar {
    width: 10px;
    height: 1px;
}

.menu-container::-webkit-scrollbar-thumb {
    border-radius: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2) inset;
    background-color: #c1c1c1;
}

.menu-container::-webkit-scrollbar-thumb:hover {
    background-color: #6b6666;
}

.menu-container::-webkit-scrollbar-track {
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2) inset;
    border-radius: 10px;
    background-color: #ededed;
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
