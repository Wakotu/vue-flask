<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-23 15:08:23
 * @LastEditTime: 2022-03-24 10:22:30
 * @Description: 检测结果展示页面
 * @Todo: 
-->

<template>
    <div class="res-list-wrapper">
        <Header></Header>
        <div class="res-wrapper">
            <div class="title-wrapper">
                <h1 class="title">任务列表</h1>
                <p class="subtitle">Task List</p>

                <div class="query">
                    <el-input v-model="input" placeholder="查询" @keyup.enter.native="onQuery"></el-input>
                    <button class="query-btn" @click="onQuery">
                        <i class="el-icon-search"></i>
                    </button>
                </div>
            </div>

            <ul class="res-list clearfix">
                <li class="res-item" :class="item.status?'finish':''" v-for="(item) in showData" :key="item.id" @click="checkImage(item.id, item.status)">
                    <el-card shadow="always">
                        <div class="name">{{item.name}}</div>
                        <div class="status">
                            <el-tag
                                v-show="item.status"
                                type="success"
                                size="medium"
                                effect="light"
                            >已完成</el-tag>
                            <el-tag
                                v-show="!item.status"
                                type="warning"
                                size="medium"
                                effect="light"
                            >运行中</el-tag>
                        </div>
                    </el-card>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import Header from "../../components/Header.vue";

export default {
    name: "ResultList",
    components: { Header },
    data() {
        return {
            input: "",
            showData: [],
            allData: [],
        };
    },
    
    methods: {
        onQuery(){
            // console.log(this.input);
            this.showData=this.allData.filter((item)=>{
                return item.name.includes(this.input);
            });
        },
        getData(){
            this.$axios.post('/api/single/getAllTask')
            .then(res => {
                // console.log(res)
                let data=res.data;
                this.allData=data.task_list;
                this.showData=this.allData;
            })
            .catch(err => {
                console.error(err); 
            })
        },
        checkImage(id, status){
            // console.log(id);
            if(!status) return;
            this.$router.push({
                name:'userImage',
                query:{
                    id,
                }
            });
        },
    
    },
    mounted() {
        this.getData();
        
    },
};
</script>

<style scoped>
.res-wrapper {
    width: 800px;
    margin: 30px auto 0 auto;
    border-radius: 5px;
    box-shadow: 1px 2px 10px rgba(0, 0, 0, 0.2);
    padding: 10px 20px;
}

.title-wrapper {
    position: relative;
}
.title-wrapper .title {
    font-weight: bold;
    font-size: 25px;
    line-height: 45px;
    letter-spacing: 2px;
}
.title-wrapper .subtitle {
    font-size: 16px;
    line-height: 20px;
    color: #979797;
    word-spacing: 5px;
}
.title-wrapper .query {
    position: absolute;
    right: 20px;
    width: 250px;
    height: 40px;
    top: 0;
    bottom: 0;
    margin: auto 0;
}
.title-wrapper .query > * {
    float: left;
}

.title-wrapper .query .el-input{
    width: 200px;
}
.title-wrapper .query .query-btn{
    border-radius: 5px;
    border: 1px solid #D8DBE2;
    background: white;
    height: 40px;
    width: 40px;
    margin-left: 10px;

    cursor: pointer;
    transition: all 0.2s;
}
.title-wrapper .query .query-btn:hover{
    color: white;
    background-color: skyblue;
}

.title-wrapper::after {
    content: "";
    display: block;
    background-color: #eaeaea;
    width: 100%;
    height: 1px;
    margin-top: 10px;
}

.res-list {
    padding: 10px 0;
}
.res-list .res-item {
    width: 180px;
    margin-left: 15px;
    margin-top: 10px;
    float: left;
    transform: none;
    position: relative;

    transition: all 0.1s;
}
.res-list .res-item.finish{
    cursor: pointer;
}
.res-list .res-item.finish:hover {
    transform: translateY(-5px);
}
.res-list .res-item.finish:hover .el-card {
    border-color: skyblue;
}
.res-list .res-item .name {
    font-size: 22px;
    line-height: 30px;
}
.res-list .res-item .status {
    position: absolute;
    height: 25px;
    right: 20px;
    top: 0;
    bottom: 0;
    margin: auto 0;
}
</style>