<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-10 14:17:33
 * @LastEditTime: 2022-03-21 13:24:27
 * @Description: 用户列表
 * @Todo: 实现添加功能
-->

<template>
    <div class="user-list-wrapper">
        <Header></Header>

        <div class="user-list">
            <el-form :inline="true" :model="searchForm" class="demo-form-inline">
                <el-form-item label>
                    <el-input v-model="searchForm.input" placeholder="输入用户信息"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitSearch">查询</el-button>
                </el-form-item>

                <el-button class="add-btn" type="primary" size="default" @click="handleAdd">添加</el-button>
            </el-form>
            <!-- 表格 -->
            <el-table :data="tableData" border style="width: 100%" height="370">
                <!-- prop属性指定键值，label属性标明列名 -->
                <el-table-column fixed prop="username" label="用户名" width="120" align="center"></el-table-column>
                <el-table-column prop="email" label="邮箱" width="150" align="center"></el-table-column>
                <el-table-column prop="phone" label="手机" width="120" align="center"></el-table-column>
                <el-table-column prop="gender" label="性别" sortable width="90" align="center"></el-table-column>
                <el-table-column prop="identity" label="身份" sortable width="120" align="center"></el-table-column>
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

            <!-- 分页 -->
            <div class="footer">
                <el-pagination
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="pagination.currentPage"
                    :page-sizes="pagination.pageSizes"
                    :page-size="pagination.pageSize"
                    layout="total, sizes, prev, pager, next, jumper"
                    :total="allData.length"
                ></el-pagination>
            </div>
        </div>

        <AdminDialog :dialog="dialog" @closeDialog="closeDialog" @update="getData"></AdminDialog>
    </div>
</template>

<script>
import Header from "../components/Header.vue";
import AdminDialog from "../components/AdminDialog.vue";

export default {
    name: "UserList",
    components: { Header, AdminDialog },
    data() {
        return {
            tableData: [],
            allData: [],
            queryRes: [],
            searchForm: {
                input: "",
            },
            dialog: {
                title: "",
                visible: false,
                form: {
                    email: "",
                    pwd: "",
                    username: "",
                    phone: "",
                    identity: "user",
                    gender: "male",
                    unit: "",
                    address: "",
                },
                user_id: "",
            },
            pagination: {
                pageSizes: [5, 10],
                currentPage: 1,
                pageSize: 5,
            },
        };
    },
    methods: {
        submitSearch() {
            const info = this.searchForm.input;
            // console.log(info);
            this.queryRes = this.allData.filter((item) => {
                // console.log(item);
                for (let key in item) {
                    // console.log(key);
                    if (key === "id" || key === "identity" || key === "gender")
                        continue;
                    if (item[key] && item[key].includes(info)) return true;
                }

                return false;
            });

            this.setPagination(this.queryRes);
        },
        handleEdit(index, row) {
            const { id, ...form } = row;
            form.identity = form.identity === "管理员" ? "admin" : "user";
            form.gender = form.gender === "男" ? "male" : "female";
            this.dialog.form = form;
            this.dialog.user_id = id;
            this.dialog.title = "编辑";
            this.dialog.visible = true;
        },
        handleDelete(index, row) {
            this.$axios
                .post("/api/users/removeUser", {
                    user_id: row.id,
                })
                .then((res) => {
                    this.$message({
                        showClose: true,
                        type: "warning",
                        message: res.data.info,
                    });
                    this.getData();
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        handleAdd() {
            // 唤醒添加表单对话框
            this.dialog.title = "添加";
            this.dialog.visible = true;
        },
        closeDialog() {
            this.dialog.visible = false;
        },
        getData() {
            this.$axios
                .post("/api/users/getAllUsers")
                .then((res) => {
                    // console.log(res)
                    let data = res.data;
                    this.allData = data.users;
                    // 排序
                    this.allData.sort((a, b) => {
                        let aLen = a.username.length;
                        let bLen = b.username.length;
                        let len = aLen < bLen ? aLen : bLen;
                        for (let i = 0; i < len; i++) {
                            let x = a.username.substr(i, i+1).charCodeAt();
                            let y = b.username.substr(i, i+1).charCodeAt();
                            if(x===y) continue;
                            return x-y;
                        }
                        return 0;
                    });
                    this.setPagination(this.allData);
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        handleSizeChange(size) {
            this.pagination.pageSize = size;
            this.setPagination();
        },
        handleCurrentChange(page) {
            this.pagination.currentPage = page;
            this.setPagination(this.allData);
        },
        setPagination(dataList) {
            let i = this.pagination.currentPage;
            let size = this.pagination.pageSize;
            this.tableData = dataList.slice((i - 1) * size, i * size);
        },
    },
    mounted() {
        this.getData();
    },
};
</script>

<style scoped>
.user-list .el-form {
    margin: 10px 20px 0 20px;
}

.user-list .el-form .add-btn {
    float: right;
}

.footer .el-pagination {
    float: right;
    margin-right: 50px;
}

</style>