<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-23 19:53:35
 * @LastEditTime: 2022-03-28 13:21:56
 * @Description: 水军用户画像
 * @Todo: 
-->

<template>
    <div class="user-image">
        <Header></Header>

        <div class="topbar clearfix">
            <div class="user-info">
                <div class="img-wrapper">
                    <img :src="showData.userInfo.avatar_url" alt class="avatar" />
                </div>
                <div class="fans">
                    <p class="data">{{fansShow}}</p>
                    <div class="title">粉丝</div>
                </div>
                <div class="follow">
                    <p class="data">{{followShow}}</p>
                    <div class="title">关注</div>
                </div>
            </div>

            <div class="profile">
                <div class="name-wrapper clearfix">
                    <div class="username">{{showData.userInfo.username}}</div>
                    <div class="gender">
                        <i
                            v-show="showData.userInfo.isMale"
                            class="el-icon-male"
                            style="color: skyblue;"
                        ></i>
                        <i
                            v-show="!showData.userInfo.isMale"
                            class="el-icon-female"
                            style="color: pink;"
                        ></i>
                    </div>
                </div>

                <div class="intro">
                    <i class="el-icon-document"></i>
                    {{showData.userInfo.intro}}
                </div>

                <div class="home">
                    <a :href="showData.userInfo.home_url" class="home-btn">
                        <i class="el-icon-link"></i>用户首页
                    </a>
                </div>
            </div>

            <div class="pr" id="pr"></div>
        </div>

        <ul class="charts clearfix">
            <li class="word-cloud" id="word-cloud"></li>
            <li id="frequency"></li>
            <li id="fan-compose"></li>
            <li id="follow-compose"></li>
            <li id="emotion"></li>
            <li id="emotion-trend"></li>
        </ul>
    </div>
</template>

<script>
import Header from "../../components/Header.vue";
import * as echarts from "echarts";
import "echarts-wordcloud";

export default {
    name: "UserImage",
    components: { Header },
    data() {
        return {
            showData: {
                userInfo: {
                    avatar_url:
                        "https://wx1.sinaimg.cn/mw2000/006dfXnily8glou2izi1uj30sz0szmy1.jpg",
                    fans: 11000,
                    follow: 22000,
                    username: "HelloGitHub",
                    isMale: 1,
                    intro: "互联网科技博主",
                    home_url: "https://weibo.com/u/5692692520",
                    // 概率
                    pr: 0.5,
                },
                blogFrequency: {
                    origin: [120, 132, 101, 134, 90, 230, 210],
                    forward: [220, 182, 191, 234, 290, 330, 310],
                },
                fans: {
                    auth: 1048,
                    common: 735,
                    navy: 580,
                },
                follow: {
                    auth: 1048,
                    common: 735,
                    navy: 580,
                },
                emotions: {
                    pos: 20,
                    neg: 100,
                    neu: 5,
                },
                emotionTrend: [89, 93, 27, 88, 96, 55, 71],
            },
            days: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            worddata: [
                {
                    name: "老婆产假",
                    value: 15000,
                },
                {
                    name: "产假",
                    value: 10081,
                },
                {
                    name: "身体不舒服",
                    value: 9386,
                },
                {
                    name: "生病",
                    value: 7500,
                },
                {
                    name: "休假休息",
                    value: 7500,
                },
                {
                    name: "亲人去世",
                    value: 6500,
                },
                {
                    name: "腹泻",
                    value: 6500,
                },
                {
                    name: "头痛",
                    value: 6000,
                },
                {
                    name: "朋友婚礼",
                    value: 4500,
                },
                {
                    name: "亲戚来了",
                    value: 3800,
                },
                {
                    name: "办理证件",
                    value: 3000,
                },
                {
                    name: "家里有事",
                    value: 2500,
                },
                {
                    name: "老婆坐月子",
                    value: 2300,
                },
                {
                    name: "急性阑尾炎",
                    value: 2000,
                },
                {
                    name: "呕吐",
                    value: 1900,
                },
                {
                    name: "感冒",
                    value: 1800,
                },
                {
                    name: "拉肚子",
                    value: 1700,
                },
                {
                    name: "小孩生病",
                    value: 1600,
                },
                {
                    name: "搬家",
                    value: 1500,
                },
                {
                    name: "工作疲惫",
                    value: 1200,
                },
                {
                    name: "喜酒",
                    value: 1100,
                },
                {
                    name: "堵车",
                    value: 900,
                },
                {
                    name: "睡过头",
                    value: 800,
                },
            ],
        };
    },
    methods: {
        getData() {
            console.log("get data");
        },
        formatNum(num) {
            if (num < 1000) return num;
            else if (1000 <= num && num < 10000) {
                // 返回x.x千
                let a = Math.round(num / 1000);
                let b = Math.round((num % 1000) / 100);
                return a.toString() + "." + b.toString() + "千";
            } else {
                let a = Math.round(num / 10000);
                if (a >= 10) return a.toString() + "万";
                let b = Math.round((num % 10000) / 1000);
                return a.toString() + "." + b.toString() + "万";
            }
        },
        isLeap(y) {
            if (y % 4) return false;
            if (y % 100 == 0 && y % 400) return false;
            return true;
        },
        subDate(m, d, days, flag) {
            if (d > days) {
                return this.formatDate(m, d - days);
            }
            d = d + this.days[(m - 1 + 12) % 12] - days;
            m = (m + 12 - 1) % 12;
            if (m == 1 && flag) d = d + 1;
            return this.formatDate(m, d);
        },
        formatDate(m, d) {
            return (m + 1).toString() + "-" + d.toString();
        },
        getWeek() {
            const d = new Date();
            let year = d.getFullYear();
            let flag = this.isLeap(year);
            let month = d.getMonth();
            let date = d.getDate();

            let week = [];
            for (let i = 6; i > 0; i--) {
                week.push(this.subDate(month, date, i, flag));
            }
            week.push(this.formatDate(month, date));
            return week;
        },
        renderPr() {
            const chart = echarts.init(document.getElementById("pr"));
            chart.setOption({
                tooltip: {
                    formatter: "{a} <br/>{b} : {c}%",
                },
                series: [
                    {
                        name: "Probability",
                        type: "gauge",
                        progress: {
                            show: true,
                        },
                        detail: {
                            valueAnimation: true,
                            formatter: "{value}",
                        },
                        data: [
                            {
                                value: this.showData.userInfo.pr * 100,
                                name: "水军概率",
                            },
                        ],
                    },
                ],
            });
        },
        renderWc() {
            //基于准备好的dom，初始化ECharts图表
            var myChart = echarts.init(document.getElementById("word-cloud"));
            var option = {
                //指定图表的配置项和数据
                title: {
                    //配置标题组件
                    text: "用户博文词云图",
                },
                tooltip: { show: true }, //配置提示框组件
                series: [
                    {
                        type: "wordCloud",
                        shape: "circle",
                        // maskImage: maskImage,
                        // 位置相关代码
                        left: "center",
                        top: "center",
                        width: "70%",
                        height: "80%",
                        right: null,
                        bottom: null,

                        sizeRange: [12, 60],
                        rotationRange: [-90, 90],
                        rotationStep: 45,
                        gridSize: 8,
                        drawOutOfBound: false,
                        layoutAnimation: true,
                        textStyle: {
                            fontFamily: "sans-serif",
                            fontWeight: "bold",
                            color: function () {
                                return (
                                    "rgb(" +
                                    [
                                        Math.round(Math.random() * 160),
                                        Math.round(Math.random() * 160),
                                        Math.round(Math.random() * 160),
                                    ].join(",") +
                                    ")"
                                );
                            },
                        },
                        emphasis: {
                            focus: "self",

                            textStyle: {
                                shadowBlur: 10,
                                shadowColor: "#333",
                            },
                        },
                        data: this.worddata,
                    },
                ],
            }; //option结束
            myChart.setOption(option); //为echarts对象加载数据
            console.log("render wc done");
        },
        renderFr() {
            let week = this.getWeek();

            const chart = echarts.init(document.getElementById("frequency"));
            chart.setOption({
                title: {
                    text: "发文频率",
                },
                tooltip: {
                    trigger: "axis",
                },
                legend: {},
                grid: {
                    left: "3%",
                    right: "4%",
                    bottom: "3%",
                    containLabel: true,
                },
                toolbox: {
                    feature: {
                        saveAsImage: {},
                    },
                },
                xAxis: {
                    type: "category",
                    boundaryGap: false,
                    data: week,
                },
                yAxis: {
                    type: "value",
                },
                series: [
                    {
                        name: "原创博文",
                        type: "line",
                        stack: "Total",
                        data: this.showData.blogFrequency.origin,
                    },
                    {
                        name: "转发博文",
                        type: "line",
                        stack: "Total",
                        data: this.showData.blogFrequency.forward,
                    },
                ],
            });
        },
        renderFc() {
            const chart = echarts.init(
                document.getElementById("fan-compose"),
                null,
                {
                    width: 400,
                    height: 270,
                }
            );
            chart.setOption({
                title: {
                    text: "粉丝组成",
                },
                tooltip: {
                    trigger: "item",
                },
                legend: {
                    x: "right",
                },
                series: [
                    {
                        name: "粉丝组成",
                        type: "pie",
                        radius: ["40%", "70%"],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: "#fff",
                            borderWidth: 2,
                        },
                        label: {
                            show: false,
                            position: "center",
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: "40",
                                fontWeight: "bold",
                            },
                        },
                        labelLine: {
                            show: false,
                        },
                        data: [
                            {
                                value: this.showData.fans.common,
                                name: "普通用户",
                            },
                            {
                                value: this.showData.fans.auth,
                                name: "认证用户",
                            },
                            {
                                value: this.showData.fans.navy,
                                name: "水军用户",
                            },
                        ],
                    },
                ],
            });
        },
        renderFoc() {
            const chart = echarts.init(
                document.getElementById("follow-compose"),
                null,
                {
                    width: 400,
                    height: 270,
                }
            );
            chart.setOption({
                title: {
                    text: "关注组成",
                },
                tooltip: {
                    trigger: "item",
                },
                legend: {
                    x: "right",
                },
                series: [
                    {
                        name: "关注组成",
                        type: "pie",
                        radius: ["40%", "70%"],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: "#fff",
                            borderWidth: 2,
                        },
                        label: {
                            show: false,
                            position: "center",
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: "40",
                                fontWeight: "bold",
                            },
                        },
                        labelLine: {
                            show: false,
                        },
                        data: [
                            {
                                value: this.showData.follow.common,
                                name: "普通用户",
                            },
                            {
                                value: this.showData.follow.auth,
                                name: "认证用户",
                            },
                            {
                                value: this.showData.follow.navy,
                                name: "水军用户",
                            },
                        ],
                    },
                ],
            });
        },
        renderEm() {
            const chart = echarts.init(document.getElementById("emotion"));
            const colorList = {
                积极: "#91CC75",
                消极: "#F56C6C",
                中立: "#FAC858",
            };
            chart.setOption({
                title: {
                    text: "博文情感分布",
                },
                tooltip: {
                    trigger: "axis",
                    axisPointer: {
                        type: "shadow",
                    },
                },
                grid: {
                    left: "3%",
                    right: "4%",
                    bottom: "3%",
                    containLabel: true,
                },
                xAxis: {
                    type: "value",
                    boundaryGap: [0, 0.01],
                },
                dataset: {
                    source: this.emotionShow,
                },
                yAxis: {
                    type: "category",
                },
                series: [
                    {
                        itemStyle: {
                            normal: {
                                color(params) {
                                    // console.log(params);
                                    return colorList[params.data[0]];
                                },
                            },
                        },
                        name: "博文数量",
                        type: "bar",
                        barWidth: "50%",
                    },
                ],
            });
        },
        renderEt() {
            let week = this.getWeek();
            const chart = echarts.init(
                document.getElementById("emotion-trend")
            );
            chart.setOption({
                title: {
                    text: "情感变化趋势",
                },
                color: ["#FF9181"],
                legend: {},
                tooltip: {},
                xAxis: {
                    type: "category",
                    data: week,
                },
                yAxis: {},
                series: [
                    {
                        type: "line",
                        data: this.showData.emotionTrend,
                    },
                ],
            });
        },
    },
    computed: {
        id() {
            return this.$route.query.id;
        },
        fansShow() {
            return this.formatNum(this.showData.userInfo.fans);
        },
        followShow() {
            return this.formatNum(this.showData.userInfo.follow);
        },
        emotionShow() {
            let emotionList = [];
            let keyMap = {
                pos: "积极",
                neg: "消极",
                neu: "中立",
            };
            for (let key in this.showData.emotions) {
                let item = [];
                item.push(keyMap[key]);
                item.push(this.showData.emotions[key]);
                emotionList.push(item);
            }
            emotionList.sort((a, b) => {
                return a[1] - b[1];
            });
            // console.log(emotionList);
            return emotionList;
        },
    },
    mounted() {
        // console.log(this.id);
        if (!this.id) {
            this.$message({
                showClose: true,
                type: "warning",
                message: "未传入任务信息，当前展示默认样例",
            });
        } else {
            this.getData();
        }

        // 渲染图表
        this.renderPr();
        this.renderWc();
        this.renderFr();
        this.renderFc();
        this.renderFoc();
        this.renderEm();
        this.renderEt();
    },
};
</script>

<style scoped>
.topbar {
    width: 850px;
    box-shadow: 1px 2px 10px rgba(0, 0, 0, 0.2);
    padding: 0 20px;
    height: 264px;
    overflow: hidden;
    margin: 20px auto 0 auto;
    border-radius: 5px;
}

.topbar .user-info {
    float: left;
    margin-top: 15px;
}
.topbar .user-info .img-wrapper {
    padding: 10px 30px 0 30px;
}
.topbar .user-info .img-wrapper .avatar {
    height: 150px;
    width: 150px;
    border-radius: 50%;
}
.topbar .user-info .fans,
.topbar .user-info .follow {
    width: 105px;
    float: left;
    text-align: center;
}
.topbar .user-info .data {
    font-size: 18px;
    font-weight: bold;
    line-height: 30px;
}
.topbar .user-info .title {
    color: #999999;
}

.topbar .profile {
    float: left;
    margin-left: 20px;
    overflow: hidden;
    margin-top: 25px;
}
.topbar .profile .name-wrapper {
    margin-top: 30px;
    margin-left: 10px;
}
.topbar .profile .name-wrapper > * {
    float: left;
}
.topbar .profile .name-wrapper .username {
    font-size: 30px;
    font-weight: bold;
    line-height: 40px;
}
.topbar .profile .name-wrapper .gender {
    font-size: 40px;
    margin-left: 10px;
}
.topbar .profile .intro {
    color: #998964;
    font-size: 16px;
    margin-top: 20px;
    padding-left: 20px;
}
.topbar .profile .home {
    margin-top: 30px;
    margin-left: 20px;
}
.topbar .profile .home .home-btn {
    display: block;
    width: 150px;
    height: 40px;
    border: 1px solid #b3d8ff;
    background-color: #ecf5ff;
    color: #60aeff;
    text-decoration: none;
    text-align: center;
    line-height: 40px;
    border-radius: 10px;

    transition: all 0.2s;
}
.topbar .profile .home .home-btn:hover {
    background-color: #409eff;
    color: white;
}

.topbar .pr {
    float: right;
    margin-top: -10px;
    margin-right: 30px;
    width: 300px;
    height: 300px;
}

.charts {
    width: 860px;
    margin: 20px auto 0 auto;
    padding-bottom: 20px;
}

.charts li {
    margin-bottom: 20px;
    box-shadow: 1px 2px 10px rgba(0, 0, 0, 0.2);
    border-radius: 5px;
    width: 400px;
    height: 250px;
    float: left;
}

.charts li:nth-child(2n) {
    margin-left: 30px;
}
</style>