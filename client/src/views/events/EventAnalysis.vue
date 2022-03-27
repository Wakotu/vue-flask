<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-26 12:41:50
 * @LastEditTime: 2022-03-27 16:52:06
 * @Description: 热点事件分析页面
 * @Todo: 
-->

<template>
    <div class="event-analysis">
        <Header></Header>

        <div class="container">
            <el-tabs v-model="activeName">
                <el-tab-pane label="趋势分析" name="first">
                    <TrendAna :trendData="trendData" ref="trendAna"></TrendAna>
                </el-tab-pane>
                <el-tab-pane label="受众分析" name="second">
                    <AudiAna :audiData="audiData"></AudiAna>
                </el-tab-pane>
                <el-tab-pane label="水军分析" name="third">角色管理</el-tab-pane>
            </el-tabs>
        </div>
    </div>
</template>

<script>
import Header from "../../components/Header.vue";
import TrendAna from "../../components/ea/TrendAna.vue";
import AudiAna from "../../components/ea/AudiAna.vue";

export default {
    name: "EventAnalysis",
    components: { Header, TrendAna, AudiAna },
    data() {
        return {
            activeName: "first",
            trendData: {
                topicDisc: 10000,
                involUsers: 10000,
                heatTrend: [820, 932, 901, 934, 1290, 1330, 1320],
            },
            audiData: {
                regionData: [
                    { name: "南海诸岛", value: 0 },
                    { name: "北京", value: 2170.7 },
                    { name: "天津", value: 1559.6 },
                    { name: "上海", value: 2423.78 },
                    { name: "重庆", value: 3048.43 },
                    { name: "河北", value: 7556.3 },
                    { name: "河南", value: 9605 },
                    { name: "云南", value: 4800.5 },
                    { name: "辽宁", value: 4359.3 },
                    { name: "黑龙江", value: 3788.7 },
                    { name: "湖南", value: 6860.2 },
                    { name: "安徽", value: 100.6 },
                    { name: "山东", value: 1047.2 },
                    { name: "新疆", value: 244.67 },
                    { name: "江苏", value: 802.3 },
                    { name: "浙江", value: 577 },
                    { name: "江西", value: 422.1 },
                    { name: "湖北", value: 597 },
                    { name: "广西", value: 485 },
                    { name: "甘肃", value: 625.71 },
                    { name: "山西", value: 370.35 },
                    { name: "内蒙古", value: 34 },
                    { name: "陕西", value: 35.44 },
                    { name: "吉林", value: 217.43 },
                    { name: "福建", value: 941 },
                    { name: "贵州", value: 3580 },
                    { name: "广东", value: 1346 },
                    { name: "青海", value: 83.8 },
                    { name: "西藏", value: 371.5 },
                    { name: "四川", value: 841 },
                    { name: "宁夏", value: 61.79 },
                    { name: "海南", value: 925.76 },
                    { name: "台湾", value: 2369 },
                    { name: "香港", value: 748.25 },
                    { name: "澳门", value: 63.2 },
                ],
                ageData: [
                    { value: 1048, name: "<20" },
                    { value: 735, name: "20-40" },
                    { value: 580, name: "40-60" },
                    { value: 484, name: ">60" },
                ],
                genderData: [
                    { value: 1048, name: "男" },
                    { value: 735, name: "女" },
                ],
            },
        };
    },
    methods: {
        getData(){

        }
    },
    computed: {
        id(){
            return this.$route.query.id;
        }
    },
    mounted() {
        // console.log(this.id);
        if(!this.id){
            this.$message({
                showClose: true,
                type: 'warning',
                message: '未传入事件信息，当前展示测试用例',
            });
        }else{
            this.getData();
        }
    },
};
</script>

<style scoped>
.container {
    margin: 20px auto 0 auto;
    width: 900px;
    border-radius: 5px;
    box-shadow: 1px 2px 10px rgba(0, 0, 0, 0.2);
    padding: 10px 20px;
}
</style>
