<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-21 16:41:57
 * @LastEditTime: 2022-03-23 15:04:26
 * @Description: 分析程序监测页面
 * @Todo: 
-->

<template>
    <div class="analysis-manage">
        <Header></Header>

        <div class="table-container">
            <el-table :data="tableData" style="width: 100%">
                <el-table-column label="任务名称" width="100">
                    <template slot-scope="scope">
                        <div slot="reference" class="name-wrapper">
                            <el-tag size="medium">{{ scope.row.name }}</el-tag>
                        </div>
                    </template>
                </el-table-column>
                <el-table-column label="创建时间" width="200">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span style="margin-left: 10px">{{ scope.row.create_time }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="运行状态" width="100">
                    <template slot-scope="scope">
                        <el-tag
                            v-show="scope.row.status"
                            size="medium"
                            type="success"
                            effect="dark"
                        >运行中</el-tag>
                        <el-tag
                            v-show="!scope.row.status"
                            size="medium"
                            type="warning"
                            effect="dark"
                        >暂停</el-tag>
                    </template>
                </el-table-column>

                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button
                            size="mini"
                            type="danger"
                            @click="handleDelete(scope.$index, scope.row)"
                        >删除</el-button>
                    </template>
                </el-table-column>
            </el-table>

            <el-pagination
                @current-change="handleCurrentChange"
                :current-page.sync="pagin.page"
                :page-size="pagin.page_size"
                layout="prev, pager, next, jumper"
                :total="tableData.length"
            ></el-pagination>
        </div>
        <!-- 弹出框 -->
        <el-dialog title="任务配置" :visible.sync="dialogVisible" top="8vh">
            <div class="setting-form">
                <el-form :model="form" ref="form" :rules="rules" :inline="false" size="normal">
                    <el-form-item label="运行状态" prop="status">
                        <el-select v-model="form.status" placeholder="请选择">
                            <el-option
                                v-for="item in stat_opts"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            ></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit('form')">提交</el-button>
                        <el-button @click="onCancel">取消</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import Header from "../../components/Header.vue";

export default {
    name: "AnalysisManage",
    components: { Header },
    data() {
        return {
            tableData: [],
            allData: [],
            pagin: {
                page: 1,
                page_size: 5,
            },
            form: {
                id: "",
                status: "",
            },
            dialogVisible: false,
            stat_opts: [
                {
                    label: "运行中",
                    value: "run",
                },
                {
                    label: "暂停",
                    value: "stop",
                },
            ],
            rules: {
                status: [
                    {
                        required: true,
                        message: "请选择状态",
                        trigger: "blur",
                    },
                ],
                
            },
        };
    },
    methods: {
        handleCurrentChange(page) {
            this.pagin.page = page;
            this.setPagin();
        },
        setPagin() {
            let i = this.pagin.page;
            let n = this.pagin.page_size;
            this.tableData = this.allData.slice((i - 1) * n, i * n);
        },
        getData() {
            this.$axios
                .post("/api/system/getAllStatus",{
                    section:'analysis',
                })
                .then((res) => {
                    // console.log(res)
                    let data = res.data;
                    this.allData = data.status_list;
                    this.setPagin();
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        handleEdit(index, row) {
            this.dialogVisible = true;
            this.form = {
                id:row.id,
                status: row.status ? "run" : "stop",
            };
        },
        handleDelete(index, row) {
            this.$axios
                .post("/api/system/removeStatus", {
                    id: row.id,
                })
                .then((res) => {
                    // console.log(res)
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
        onSubmit(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    
                    this.$axios
                        .post("/api/system/editStatus", {
                            ...this.form,
                            section:'analysis',
                        })
                        .then((res) => {
                            // console.log(res.data);
                            this.$message({
                                showClose: true,
                                type: "success",
                                message: res.data.info,
                            });
                            this.dialogVisible = false;
                            this.getData();
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
        onCancel() {
            this.dialogVisible = false;
        },
    },
    mounted() {
        this.getData();
    },
};
</script>

<style scoped>
.table-container {
    box-shadow: 1px 2px 10px rgba(0, 0, 0, 0.2);
    width: 900px;
    padding: 10px 20px;
    margin: 30px auto 0 auto;
    border-radius: 5px;
}

.el-pagination {
    text-align: right;
}
</style>
