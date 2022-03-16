/*
 * @Author: Axiuxiu
 * @Date: 2022-02-27 09:19:28
 * @LastEditTime: 2022-03-14 20:47:21
 * @Description: 配置axios拦截器
 */

import axios from 'axios';
import { Message, Loading } from 'element-ui';
import router from './router';
import _ from 'loadsh';

let loadingInstance;
let loadingCount=0;

function startLoading() {
    if(!loadingCount&&!loadingInstance){
        loadingInstance = Loading.service({
            lock: true,
            text: '拼命加载中...',
            spinner: 'el-icon-loading',
            background: 'rgba(0, 0, 0, 0.7)'
        });
    }
    loadingCount++;
}

function endLoading() {
    loadingCount--;
    if(loadingCount<0) loadingCount=0;
    if(!loadingCount){
        toEndLoading();
    }
}

var toEndLoading=_.debounce(()=>{
    loadingInstance.close();
    loadingInstance = null;
  }, 300);

// 配置请求拦截器
axios.interceptors.request.use(config => {
    // 开始加载动画
    startLoading();

    // 请求头添加token
    const userToken = localStorage.getItem('userToken');
    if (userToken) {
        config.headers['Authorization'] = userToken;
    }

    return config;
}, error => {
    // Do something with request error
    return Promise.reject(error);
});

// 配置响应拦截器
axios.interceptors.response.use(response => {
    // Do something before response is sent

    // 关闭加载动画
    endLoading();

    return response;
}, error => {
    // Do something with response error

    // 关闭加载动画
    endLoading();

    const status = error.response.status;

    Message.error({
        showClose: true,
        message: error.response.data
    });

    if(status===401){
        router.push('/login');
    }

    return Promise.reject(error);
});


export default axios;
