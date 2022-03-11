/*
 * @Author: Axiuxiu
 * @Date: 2022-02-27 09:19:28
 * @LastEditTime: 2022-02-27 19:48:54
 * @Description: 配置axios拦截器
 */

import axios from 'axios';
import { Message, Loading } from 'element-ui';
import router from './router';

let loading;

function startLoading() {
    loading = Loading.service({
        lock: true,
        text: '拼命加载中...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
    })
}

function endLoading(){
    loading.close();
}

// 配置请求拦截器
axios.interceptors.request.use(config => {
    // 开始加载动画
    startLoading();

    // 请求头添加token
    const userToken=localStorage.getItem('userToken');
    if(userToken){
        config.headers['Authorization']=userToken;
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

    const status=error.response.status;
    if(status==401){
        Message.error({
            showClose:true,
            message:'token过期，请重新登录',
        }); 
        router.push('/login');
    }else{
        Message.error({
            showClose:true,
            message:error.response.data
        });
    }

    return Promise.reject(error);
});


export default axios;
