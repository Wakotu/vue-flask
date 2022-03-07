<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-07 10:32:50
 * @LastEditTime: 2022-03-07 13:55:44
 * @Description: 热点事件展示
-->
<template>
    <div class="hot-events-wrapper">
        <Header></Header>
        <div class="hot-events">
            <div class="header">
                <h1 class="title">七日热点事件</h1>

                <form class="search">
                    <input type="text" placeholder="点击选择地区" />

                    <i class="el-icon-arrow-down" v-on:click="sayHello"></i>
                </form>

                <h2 class="more">查看更多</h2>
            </div>

            <div id="map" class="map"></div>

            <div class="event-list"></div>
        </div>
    </div>
</template>

<script>
import Header from "../components/Header.vue";
const echarts = require("echarts");
// const bmap = require("echarts/extension/bmap/bmap");

export default {
    name: "HotEvents",
    components: { Header },
    methods: {
        sayHello() {
            // console.log(echarts);
            console.log("hello");
        },
        mapRender() {
            const chart = echarts.init(document.getElementById("map"));

            const option = {
                // 加载 bmap 组件
                bmap: {
                    // 百度地图中心经纬度
                    center: [120.13066322374, 30.240018034923],
                    // 百度地图缩放
                    zoom: 14,
                    // 是否开启拖拽缩放，可以只设置 'scale' 或者 'move'
                    roam: true,
                    // 百度地图的自定义样式，见 http://developer.baidu.com/map/jsdevelop-11.htm
                    mapStyle: {},
                },
                series: [
                    {
                        type: "scatter",
                        // 使用百度地图坐标系
                        coordinateSystem: "bmap",
                        // 数据格式跟在 geo 坐标系上一样，每一项都是 [经度，纬度，数值大小，其它维度...]
                        data: [[120, 30, 1]],
                    },
                ],
            };

            chart.setOption(option);
        },
    },
    mounted() {
        this.mapRender();
    },
};
</script>

<style scoped>
.hot-events-wrapper {
    width: 100%;
    height: 100%;
}

.hot-events {
    width: 100%;
    height: calc(100% - 45px);
}

/* 头部样式 */
.hot-events .header {
    height: 65px;
    overflow: hidden;
}

.hot-events .header .title {
    height: 30px;
    margin-top: 10px;
    font-weight: bold;
    line-height: 30px;
    padding-left: 15px;
    position: relative;
    float: left;
}

.hot-events .header .title::before {
    content: "";
    display: block;
    position: absolute;
    top: 6px;
    left: 10px;
    background-color: #2799df;
    width: 3px;
    height: 18px;
}

.hot-events .header .search {
    display: block;
    float: left;
    margin-left: 250px;
    margin-top: 15px;
    position: relative;
}

.hot-events .header .search input {
    border: 1px solid #dddddd;
    border-radius: 5px;
    display: block;
    width: 270px;
    height: 40px;
    padding-left: 10px;
}

.hot-events .header .search input:focus {
    border: 1px solid skyblue;
    outline: none;
}

.hot-events .header .search i {
    display: block;
    position: absolute;
    right: 10px;
    top: 0px;
    line-height: 40px;
    color: #b4b4b4;
    font-size: 20px;
    cursor: pointer;
}

.header .more {
    color: #2799df;
    float: right;
    font-size: 14px;
    margin-top: 20px;
    margin-right: 50px;
}

/* 地图部分 */
.map {
    height: calc(100% - 65px);
    width: 700px;
    /* background-color: #bfa; */
    float: left;
}

.event-list {
    float: left;
    height: calc(100% - 65px);
    width: calc(100% - 700px);
    background-color: violet;
}
</style>
