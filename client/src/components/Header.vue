<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-01 16:47:03
 * @LastEditTime: 2022-03-07 10:49:08
 * @Description: 头部区域
-->

<template>
    <div class="header">
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/manage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item v-for="(item, index) in meta" :key="index">
                {{item}}
            </el-breadcrumb-item>
        </el-breadcrumb>
    </div>
</template>

<script>
export default {
    name: "Header",
    computed: {
        meta() {
            return this.$route.meta;
        },
    },
};
</script>

<style scoped>
.header{
    height: 45px;
    padding-left: 10px;
    background-color: #EFF2F7;
    color: #A4B3C7;
}

.header ::v-deep .el-breadcrumb{
    line-height: 45px;
    font-size: 14px;

}
</style>