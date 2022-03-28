<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-27 09:23:39
 * @LastEditTime: 2022-03-28 14:13:56
 * @Description: 趋势分析组件
 * @Todo: 
-->

<template>
    <div class="trend-analysis">
        <div class="cards clearfix">
            <el-card class="card" shadow="always">
                <div class="title">话题讨论量</div>
                <div class="data">{{trendData.topicDisc}}</div>

                <div class="icon-container">
                    <i class="el-icon-view"></i>
                </div>
            </el-card>
            <el-card class="card" shadow="always">
                <div class="title">参与用户</div>
                <div class="data">{{trendData.involUsers}}</div>

                <div class="icon-container">
                    <i class="el-icon-user"></i>
                </div>
            </el-card>
        </div>

        <div id="trend-chart" class="trend-chart"></div>
    </div>
</template>

<script>
import * as echarts from "echarts";

export default {
    name: "TrendAna",
    props: ["trendData"],
    methods: {
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
        renderChart() {
            const chart = echarts.init(document.getElementById("trend-chart"),null,{
                height:300,
            });
            let week=this.getWeek();
            chart.setOption({
                title: {
                    text: "热度趋势",
                },
                tooltip: {},
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
                        data: this.trendData.heatTrend,
                        type: "line",
                        smooth: true,
                        areaStyle: {},
                    },
                ],
            });
        },
    },
    mounted() {
        this.renderChart();
    },
};
</script>

<style scoped>
.cards {
    margin: 20px auto 0 auto;
    width: 610px;
    padding-bottom: 20px;
}
.cards .card {
    float: left;
    border-radius: 10px;
    width: 250px;
    position: relative;
}
.cards .card::after {
    content: "";
    display: block;
    width: 100%;
    height: 2px;
    position: absolute;
    bottom: 0;
    background-color: #409eff;
}
.cards .card:nth-child(2) {
    margin-left: 100px;
}
.cards .title {
    font-size: 16px;
    line-height: 25px;
}
.cards .data {
    font-size: 30px;
    font-weight: bold;
    line-height: 40px;
}
.cards .icon-container {
    position: absolute;
    right: 20px;
    height: 50px;
    width: 50px;
    top: 0;
    bottom: 0;
    margin: auto 0;
    line-height: 50px;
    text-align: center;
    font-size: 40px;
    border: 2px solid #79bbff;
    border-radius: 50%;
    color: #79bbff;
}

.trend-chart {
    width: 800px;
    height: 270px;
    margin: 0 auto;
}
</style>