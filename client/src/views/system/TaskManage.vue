<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-20 17:57:22
 * @LastEditTime: 2022-03-23 19:37:49
 * @Description: 任务配置页面
 * @Todo: 
-->

<template>
    <div class="task-manage">
        <Header></Header>
        <div class="task-setting">
            <!-- <div class="title-wrapper">
                <h1 class="title">任务配置</h1>
                <p class="subtitle">Task Configuration</p>
            </div>-->
            <el-table :data="tableData" style="width: 100%">
                <el-table-column label="创建时间" width="200">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span style="margin-left: 10px">{{ scope.row.create_time }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="任务名称" width="100">
                    <template slot-scope="scope">
                        <div slot="reference" class="name-wrapper">
                            <el-tag size="medium">{{ scope.row.name }}</el-tag>
                        </div>
                    </template>
                </el-table-column>
                <el-table-column label="关键词" width="100">
                    <template slot-scope="scope">
                        <span>{{ scope.row.keyword }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="结束时间" width="200">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span style="margin-left: 10px">{{ scope.row.end_time }}</span>
                    </template>
                </el-table-column>
                <el-table-column>
                    <template slot="header">
                        <el-button type="primary" size="mini" @click="handleAdd">添加</el-button>
                    </template>
                    <template slot-scope="scope">
                        <!-- <el-button
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)"
                        >编辑</el-button> -->
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
                    <el-form-item label="任务名称" prop="name">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item>
                    <el-form-item label="任务关键词" prop="keyword">
                        <el-input v-model="form.keyword"></el-input>
                    </el-form-item>
                    <el-form-item label="采集时间间隔" prop="interval">
                        <el-select v-model="form.interval" placeholder="请选择">
                            <el-option
                                v-for="item in itv_opts"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            ></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="监控时长" prop="duration">
                        <el-select v-model="form.duration" placeholder="请选择">
                            <el-option
                                v-for="item in drt_opts"
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
    name: "taskManage",
    components: { Header },
    data() {
        return {
            dialogVisible: false,
            form: {
                name: "",
                keyword: "",
                // 单位是分钟
                interval: 5,
                // 单位是小时
                duration: 1,
            },
            itv_opts: [
                {
                    value: 5,
                    label: "5分钟",
                },
                {
                    value: 10,
                    label: "10分钟",
                },
                {
                    value: 15,
                    label: "15分钟",
                },
            ],
            drt_opts: [
                {
                    value: 1,
                    label: "1小时",
                },
                {
                    value: 24,
                    label: "1天",
                },
                {
                    value: 240,
                    label: "10天",
                },
                {
                    value: -1,
                    label: "持续监控",
                },
            ],
            rules: {
                name: [
                    {
                        required: true,
                        message: "请填写任务名称",
                        trigger: "blur",
                    },
                ],
                keyword: [
                    {
                        required: true,
                        message: "请填写任务关键词",
                        trigger: "blur",
                    },
                ],
                interval: [
                    {
                        required: true,
                        message: "请选择采集时间间隔",
                        trigger: "blur",
                    },
                ],
                duration: [
                    {
                        required: true,
                        message: "请填写监控时长",
                        trigger: "blur",
                    },
                ],
            },
            allData:[],
            tableData:[],
            pagin:{
                page_size:5,
                page:1,
            }
        };
    },
    methods: {
        onCancel() {
            this.dialogVisible = false;
        },
        initForm(){
            this.form={
                name:'',
                keyword:'',
                interval:5,
                duration:1, 
            }
        },
        onSubmit(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // 发送请求
                    this.$axios.post('/api/system/addTask',this.form)
                    .then(res => {
                        // console.log(res)
                        this.$message({
                            showClose: true,
                            type: 'success',
                            message: res.data.info,
                        });
                        this.dialogVisible=false;
                        this.getData();
                        this.initForm();
                    })
                    .catch(err => {
                        console.error(err); 
                    })
                } else {
                    console.log("form error");
                    return false;
                }
            });
        },
        handleDelete(index, row) {
            // console.log(index, row);
            this.$axios.post('/api/system/removeTask',{
                id:row.id,
            })
            .then(res => {
                console.log(res);
                this.$message({
                    showClose: true,
                    type: 'success',
                    message: res.data.info,
                });
                // 刷新数据
                this.getData();
            })
            .catch(err => {
                console.error(err); 
            })
        },
        // handleEdit(index, row){
        //     console.log(index, row);
        // },
        handleAdd() {
            this.dialogVisible = true;
        },
        handleCurrentChange(page){
            this.pagin.page=page;
            this.setPagin();
        },
        setPagin(){
            let i=this.pagin.page;
            let n=this.pagin.page_size;
            this.tableData=this.allData.slice((i-1)*n,i*n);
        },
        getData(){
            this.$axios.post('/api/system/getAllTask')
            .then(res => {
                // console.log(res)
                let data=res.data;
                this.allData=data.tasks;
                // 对接收到的数据进行排序
                this.allData.sort((a,b)=>{
                    let len=a.create_time.length;
                    let s=a.create_time;
                    let t=b.create_time;
                    for(let i=0;i<len;i++){
                        if(s[i]===t[i]) continue;
                        return -(s[i].charCodeAt()-t[i].charCodeAt());
                    }
                    return 0;
                });
                this.setPagin();
            })
            .catch(err => {
                console.error(err); 
            })
        }
    },
    mounted() {
        this.getData();
    },
};
</script>

<style scoped>
.task-setting {
    width: 950px;
    margin: 30px auto 0 auto;
    padding: 10px 20px;
    /* height: 100px; */
    /* background-color: violet; */
    box-shadow: 1px 2px 10px rgba(0, 0, 0, 0.2);
    border-radius: 5px;
}

.el-pagination{
    text-align: right;
}
</style>
