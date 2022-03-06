/*
 * @Author: Axiuxiu
 * @Date: 2022-02-27 09:51:50
 * @LastEditTime: 2022-02-27 11:41:03
 * @Description: vue项目配置文件
 */

module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:8000/',
          ws: true,
          changeOrigin: true
        },
      }
    },
    lintOnSave:'warning',
  }
