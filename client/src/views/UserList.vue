<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-10 14:17:33
 * @LastEditTime: 2022-03-17 22:30:30
 * @Description: 用户列表
 * @Todo: 实现添加功能
-->

<template>
    <div class="user-list-wrapper">
        <Header></Header>

        <div class="user-list">
            <el-form :inline="true" :model="searchForm" class="demo-form-inline">
                <el-form-item label="">
                    <el-input v-model="searchForm.input" placeholder="输入用户信息进行查询"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitSearch">查询</el-button>
                </el-form-item>

                <el-button class="add-btn" type="primary" size="default" @click="handleAdd">添加</el-button>
                
            </el-form>
            <el-table :data="tableData" border style="width: 100%" max-height="400">
                <!-- prop属性指定键值，label属性标明列名 -->
                <el-table-column fixed prop="email" label="邮箱" width="150" align="center"></el-table-column>
                <el-table-column prop="username" label="用户名" width="120" align="center"></el-table-column>
                <el-table-column prop="phone" label="手机" width="120" align="center"></el-table-column>
                <el-table-column prop="gender" label="性别" width="70" align="center"></el-table-column>
                <el-table-column prop="identity" label="身份" width="120" align="center"></el-table-column>
                <el-table-column prop="unit" label="所属单位" width="120" align="center"></el-table-column>
                <el-table-column prop="address" label="地址" width="300" align="center"></el-table-column>
                <el-table-column fixed="right" label="操作" width="150">
                    <template slot-scope="scope">
                        <el-button
                            type="warning"
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)"
                        >编辑</el-button>
                        <el-button
                            size="mini"
                            type="danger"
                            @click="handleDelete(scope.$index, scope.row)"
                        >删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <AdminDialog :dialog="dialog" @closeDialog="closeDialog" @update="getData"></AdminDialog>
    </div>
</template>

<script>
import Header from "../components/Header.vue";
import AdminDialog from '../components/AdminDialog.vue';

export default {
    name: "UserList",
    components: { Header, AdminDialog },
    data() {
        return {
            tableData: [],
            searchForm:{
                input:'',
            },
            dialog:{
                title:'',
                visible:false,
                form:{
                    email:'',
                    pwd:'',
                    username:'',
                    phone:'',
                    identity:'user',
                    gender:'male',
                    unit:'',
                    address:'',
                },
                user_id:'',
            }
        };
    },
    methods: {
        submitSearch(){

        },
        handleEdit(index, row) {
            const { id,  ...form} = row;
            form.identity= form.identity==='管理员'?'admin':'user';
            form.gender=form.gender==='男'?'male':'female';
            this.dialog.form=form;
            this.dialog.user_id=id;
            this.dialog.title='编辑';
            this.dialog.visible=true;
        },
        handleDelete(index, row) {
            this.$axios.post('/api/users/removeUser',{
                user_id:row.id,
            })
            .then(res => {
                this.$message({
                    showClose: true,
                    type: 'warning',
                    message: res.data.info,
                });
                this.getData();
            })
            .catch(err => {
                console.error(err); 
            })
        },
        handleAdd(){
            // 唤醒添加表单对话框
            this.dialog.title='添加';
            this.dialog.visible=true;
        },
        closeDialog(){
            this.dialog.visible=false;
        },
        getData(){
            this.$axios
            .post("/api/users/getAllUsers")
            .then((res) => {
                // console.log(res)
                let data = res.data;
                this.tableData = data.users;
            })
            .catch((err) => {
                console.error(err);
            });
        },
    },
    mounted() {
        this.getData();
    },
};
</script>

<style scoped>
.user-list .el-form{
    margin: 10px 20px 0 20px;
}

.user-list .el-form .add-btn{
    float: right;
}
</style>