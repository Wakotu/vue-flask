<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-27 10:32:31
 * @LastEditTime: 2022-03-27 16:47:30
 * @Description: 受众分析标签页
 * @Todo: 
-->

<template>
    <div class="audience-analysis">
        <div class="region-distri" id="region-distri"></div>
        <div class="age-distri" id="age-distri"></div>
        <div class="gender-distri" id="gender-distri"></div>
    </div>
</template>

<script>
import * as echarts from "echarts";

export default {
    name: "AudiAna",
    props:['audiData'],
    methods: {
        regionRender() {
            // 渲染中国地图
            const chart = echarts.init(
                document.getElementById("region-distri")
            );

            chart.setOption({
                title: {
                    text: "地域分布",
                },
                tooltip: {
                    formatter(params, ticket, callback) {
                        return (
                            params.seriesName +
                            "<br>" +
                            params.name +
                            ": " +
                            params.value
                        );
                    },
                },
                visualMap: {
                    min: 0,
                    max: 1500,
                    left: "left",
                    top: "bottom",
                    text: ["高", "低"],
                    inRange: {
                        color: ["#fff4e6", "#dd2002"],
                    },
                    show: true,
                },
                geo: {
                    map: "china",
                    roam: false, //不开启缩放和平移
                    zoom: 1.23, //视角缩放比例
                    label: {
                        normal: {
                            show: true,
                            fontSize: "10",
                            color: "rgba(0,0,0,0.7)",
                        },
                    },
                    itemStyle: {
                        normal: {
                            borderColor: "rgba(0,0,0,0.2)",
                        },
                        emphasis: {
                            areaColor: "#F3B329",
                            shadowOffsetX: 0,
                            shadowOffsetY: 0,
                            shadowBlur: 20,
                            borderWidth: 0,
                            shadowColor: "rgba(0,0,0,0.5)",
                        },
                    },
                },
                series: [
                    {
                        name: "热度",
                        type: "map",
                        geoIndex: 0,
                        data: this.audiData.regionData,
                    },
                ],
            });
        },
        ageRender() {
            const chart = echarts.init(document.getElementById("age-distri"));
            chart.setOption({
                title: {
                    text: "年龄分布",
                },
                tooltip: {
                    trigger: "item",
                },
                legend: {
                    left:'50%',
                },
                series: [
                    {
                        name: "年龄分布",
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
                        data: this.audiData.ageData,
                    },
                ],
            });
        },
        genderRender() {
            const chart = echarts.init(document.getElementById("gender-distri"));
            chart.setOption({
                title: {
                    text: "性别分布",
                },
                tooltip: {
                    trigger: "item",
                },
                legend: {
                    x: "right",
                },
                series: [
                    {
                        name: "新分别分布",
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
                        data: this.audiData.genderData,
                    },
                ],
            });
        },
    },
    mounted() {
        this.regionRender();
        this.ageRender();
        this.genderRender();
    },
};
</script>

<style scoped>
.region-distri,
.age-distri,
.gender-distri {
    float: left;
}

.region-distri {
    width: 600px;
    height: 400px;
}

.age-distri,
.gender-distri {
    width: 300px;
    height: 200px;
}
</style>