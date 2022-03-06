<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-01 14:41:47
 * @LastEditTime: 2022-03-01 17:26:45
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
                    v-on:select="handleSelect"
                >
                    <el-menu-item index="manage">
                        <i :style="iconStyle" class="el-icon-menu"></i>首页
                    </el-menu-item>
                    <el-submenu index="2">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-document"></i>数据管理
                        </template>
                        <el-menu-item index="userList">用户列表</el-menu-item>
                        <el-menu-item index="shopList">商家列表</el-menu-item>
                        <el-menu-item index="foodList">食品列表</el-menu-item>
                        <el-menu-item index="orderList">订单列表</el-menu-item>
                        <el-menu-item index="adminList">管理员列表</el-menu-item>
                    </el-submenu>
                    <el-submenu index="3">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-plus"></i>添加数据
                        </template>
                        <el-menu-item index="addShop">添加商铺</el-menu-item>
                        <el-menu-item index="addGoods">添加商品</el-menu-item>
                    </el-submenu>
                    <el-submenu index="4">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-star-on"></i>图表
                        </template>
                        <el-menu-item index="visitor">用户分布</el-menu-item>
                        <!-- <el-menu-item index="newMember">用户数据</el-menu-item> -->
                    </el-submenu>
                    <el-submenu index="5">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-edit"></i>编辑
                        </template>
                        <!-- <el-menu-item index="uploadImg">上传图片</el-menu-item> -->
                        <el-menu-item index="vueEdit">文本编辑</el-menu-item>
                    </el-submenu>
                    <el-submenu index="6">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-setting"></i>设置
                        </template>
                        <el-menu-item index="adminSet">管理员设置</el-menu-item>
                        <!-- <el-menu-item index="sendMessage">发送通知</el-menu-item> -->
                    </el-submenu>
                    <el-submenu index="7">
                        <template slot="title">
                            <i :style="iconStyle" class="el-icon-warning"></i>说明
                        </template>
                        <el-menu-item index="explain">说明</el-menu-item>
                    </el-submenu>
                </el-menu>
            </el-col>
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
            return this.$route.path.replace("/", "");
        },
    },
    methods: {
        handleSelect(key, path) {
            console.log(key, path);
        },
    },
};
</script>

<style scoped>
.manage {
    width: 100%;
    height: 100%;
    /* background-color: #232323; */
    background-color: white;
}

.menu-container {
    height: 100%;
    min-height: 500px;
    background-color: #324057;
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
