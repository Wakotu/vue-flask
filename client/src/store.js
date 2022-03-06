/*
 * @Author: Axiuxiu
 * @Date: 2022-02-26 20:44:44
 * @LastEditTime: 2022-02-27 19:04:14
 * @Description: 
 */

import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
    state:{
        user:{},
        isAuth:false
    },
    mutations:{
        setUser(state, user){
            state.user=user;
        },
        setAuth(state, flag){
            state.isAuth=flag;
        }
    },
    actions:{
        // 设置登录状态
        setLoginState(context,user){
            context.commit('setUser',user);
            context.commit('setAuth',true);
        },
        // 清除登录状态
        clearLoginState(context){
            context.commit('setUser',{});
            context.commit('setAuth',false);
        }
    }
})

export default store;