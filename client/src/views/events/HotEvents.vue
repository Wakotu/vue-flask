<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-07 10:32:50
 * @LastEditTime: 2022-03-27 16:42:44
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

            </div>

            <!-- 地图 -->
            <div id="map" class="map"></div>

            <!-- 事件列表 -->
            <ul class="event-list">
                <h2 class="more">查看更多</h2>

                <li v-for="(item, index) in eventList" :key="item.id" @click="checkEvent(item.id)">
                    <span class="index">{{index+1}}</span>   
                    <span class="text">{{item.title}}</span>
                    <span class="heat">{{item.heat}}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import Header from "../../components/Header.vue";
const echarts = require("echarts");
import "../../js/china";

export default {
    name: "HotEvents",
    components: { Header },
    data() {
        return {
            mapData: [
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
            eventList:[
                {
                    id:'1',
                    title:'收藏！这是冬奥回带来的开学第一课',
                    heat:'72380',
                },
                {
                    id:'2',
                    title:'收藏！这是冬奥回带来的开学第一课',
                    heat:'72380',
                },
                {
                    id:'3',
                    title:'收藏！这是冬奥回带来的开学第一课',
                    heat:'72380',
                },
                {
                    id:'4',
                    title:'收藏！这是冬奥回带来的开学第一课',
                    heat:'72380',
                },
                {
                    id:'5',
                    title:'收藏！这是冬奥回带来的开学第一课',
                    heat:'72380',
                },
                {
                    id:'6',
                    title:'收藏！这是冬奥回带来的开学第一课',
                    heat:'72380',
                },
                {
                    id:'7',
                    title:'收藏！这是冬奥回带来的开学第一课',
                    heat:'72380',
                },
            ]
        };
    },
    methods: {
        sayHello() {
            // console.log(echarts);
            console.log("hello");
        },
        mapRender() {
            // 渲染中国地图
            const chart = echarts.init(document.getElementById("map"));

            chart.setOption({
                title: {
                    text: "区域热度分布图",
                },
                tooltip: {
                    formatter(params,ticket,callback){
                        return params.seriesName+'<br>'+params.name+': '+params.value;
                    }
                },
                visualMap:{
                    min:0,
                    max:1500,
                    left:'left',
                    top:'bottom',
                    text:['高','低'],
                    inRange:{
                        color:['#fff4e6','#dd2002'],
                    },
                    show:true,
                },
                geo:{
                    map:'china',
                    roam:false, //不开启缩放和平移
                    zoom:1.23, //视角缩放比例
                    label:{
                        normal:{
                            show:true,
                            fontSize:'10',
                            color:'rgba(0,0,0,0.7)',
                        },
                    },
                    itemStyle:{
                        normal:{
                            borderColor: 'rgba(0,0,0,0.2)'
                        },
                        emphasis:{
                            areaColor:'#F3B329',
                            shadowOffsetX:0,
                            shadowOffsetY:0,
                            shadowBlur:20,
                            borderWidth:0,
                            shadowColor:'rgba(0,0,0,0.5)'
                        }
                    }
                },
                series: [
                    {
                        name:'热度',
                        type:'map',
                        geoIndex:0,
                        data: this.mapData,
                    },
                ]
            });
        },
        checkEvent(id){
            this.$router.push({
                name:'eventImage',
                query:{
                    id,
                }
            })
        }
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



/* 地图部分 */
.map {
    margin-left: 20px;
    margin-top: 30px;
    height: 400px;
    width: 600px;
    /* background-color: #bfa; */
    float: left;
}

/* 事件列表部分 */
.event-list {
    float: left;
    margin-top: 40px;
    margin-left: 20px;
    padding-left: 10px;
    width: 320px;
    position: relative;
}

.event-list .more {
    color: #2799df;
    font-size: 14px;
    position: absolute;
    right: 0;
    top: -30px;
}

.event-list li{
    height: 20px;
    width: 100%;
    line-height: 20px;
    padding: 15px 0;
    font-size: 15px;
    position: relative;
}


.event-list li::after{
    content: '';
    position: absolute;
    display: block;
    background-color: #EBEBEB;
    height: 1px;
    width: 330px;
    bottom: 0;
    right: 0;
}

.event-list li .index{
    display: block;
    float: left;
    background-color: #EDF1F7;
    width: 20px;
    height: 20px;
    text-align: center;
}

.event-list li:nth-of-type(1) .index,
.event-list li:nth-of-type(2) .index,
.event-list li:nth-of-type(3) .index{
    color: white;
}

.event-list li:nth-of-type(1) .index{
    background-color: #E52E45;
}

.event-list li:nth-of-type(2) .index{
    background-color: #E5D22E;
}

.event-list li:nth-of-type(3) .index{
    background-color: #2EABE5;
}

.event-list li .text{
    display: block;
    float: left;
    margin-left: 10px;
    width: 170px;
    /* 设置段落省略 */
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    cursor: pointer;
}

.event-list li .text:hover{
    color: #409EFF;
}

.event-list li .heat{
    display: block;
    float: right;
    font-size: 15px;
    font-weight: bold;
}
</style>
