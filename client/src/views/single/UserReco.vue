<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-23 09:00:07
 * @LastEditTime: 2022-03-23 19:42:54
 * @Description: 用户识别页面
 * @Todo: 
-->

<template>
    <div class="user-reco">
        <Header></Header>
        <div class="detect-wrapper clearfix">
            <div class="title-wrapper">
                <h1 class="title">用户识别配置</h1>
                <p class="subtitle">Configuration of User Detection</p>
            </div>

            <div class="form-wrapper">
                <el-form
                    :model="form"
                    ref="form"
                    :rules="rules"
                    label-position="top"
                    :inline="false"
                    size="medium"
                >
                    <el-form-item class="inline-half" prop="target_user_url">
                        <span slot="label">
                            <span class="label">目标用户</span>
                        </span>
                        <el-input v-model="form.target_user_url" placeholder="请输入用户首页url"></el-input>
                    </el-form-item>

                    <el-form-item class="inline-half" prop="name">
                        <span slot="label">
                            <span class="label">任务名称</span>
                        </span>
                        <el-input v-model="form.name" placeholder="请输入任务名称"></el-input>
                    </el-form-item>

                    <el-form-item class="inline-half" prop="interval">
                        <span slot="label">
                            <span class="label">采集时间间隔</span>
                        </span>
                        <el-select v-model="form.interval" placeholder="请选择">
                            <el-option
                                v-for="item in itv_opts"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            ></el-option>
                        </el-select>
                    </el-form-item>

                    <el-form-item class="inline-half inline-right" prop="blog_page_cnt">
                        <span slot="label">
                            <span class="label">采集博文页数</span>
                        </span>
                        <el-select v-model="form.blog_page_cnt" placeholder="请选择">
                            <el-option
                                v-for="item in page_opts"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            ></el-option>
                        </el-select>
                    </el-form-item>

                    <el-form-item class="inline-half" prop="fans_page_cnt">
                        <span slot="label">
                            <span class="label">粉丝列表采集页数</span>
                        </span>
                        <el-select v-model="form.fans_page_cnt" placeholder="请选择">
                            <el-option
                                v-for="item in page_opts"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            ></el-option>
                        </el-select>
                    </el-form-item>

                    <el-form-item class="inline-half inline-right" prop="follow_page_cnt">
                        <span slot="label">
                            <span class="label">关注列表采集页数</span>
                        </span>
                        <el-select v-model="form.follow_page_cnt" placeholder="请选择">
                            <el-option
                                v-for="item in page_opts"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            ></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item class="footer">
                        <el-button type="primary" @click="onSubmit('form')">立即创建</el-button>
                        <!-- <el-button>取消</el-button> -->
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import Header from "../../components/Header.vue";

export default {
    name: "UserReco",
    components: { Header },
    data() {
        const urlReg =/^https?:\/\/(([a-zA-Z0-9]+-?)+[a-zA-Z0-9]+\.)+(([a-zA-Z0-9]+-?)+[a-zA-Z0-9]+)/;
        const checkUrl = (rule, value, callback) => {
            if (urlReg.test(value)) callback();
            else callback(new Error("url格式不正确"));
        };
        return {
            form: {
                target_user_url: "",
                name: "",
                // 以秒为单位
                interval: 1,
                blog_page_cnt: 1,
                fans_page_cnt: 1,
                follow_page_cnt: 1,
            },
            rules: {
                target_user_url: [
                    { required: true, message: "请输入url", trigger: "blur" },
                    { validator: checkUrl, trigger: "blur" },
                ],
                name: [
                    {
                        required: true,
                        message: "请输入任务名称",
                        trigger: "blur",
                    },
                ],
                interval: [
                    { required: true, message: "请选择", trigger: "blur" },
                ],
                blog_page_cnt: [
                    { required: true, message: "请选择", trigger: "blur" },
                ],
                fans_page_cnt: [
                    { required: true, message: "请选择", trigger: "blur" },
                ],
                follow_page_cnt: [
                    { required: true, message: "请选择", trigger: "blur" },
                ],
            },
            itv_opts: [
                { value: 1, label: "1秒" },
                { value: 30, label: "30秒" },
                { value: 60, label: "1分钟" },
            ],
            page_opts: [
                { value: 1, label: "1页" },
                { value: 10, label: "10页" },
                { value: 100, label: "100页" },
            ],
        };
    },
    methods: {
        clearForm() {
            this.form = {
                target_user_url: "",
                name: "",
                interval: 1,
                blog_page_cnt: 1,
                fans_page_cnt: 1,
                follow_page_cnt: 1,
            };
        },
        onSubmit(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.$axios
                        .post("/api/single/addSingleTask", this.form)
                        .then((res) => {
                            // console.log(res);
                            this.$message({
                                showClose: true,
                                type: "success",
                                message: res.data.info,
                            });
                            this.clearForm();
                        })
                        .catch((err) => {
                            console.error(err);
                        });
                } else {
                    console.log("form error");
                    return false;
                }
            });
        },
    },
};
</script>

<style scoped>
.detect-wrapper {
    width: 650px;
    margin: 30px auto 0 auto;
    padding: 10px 20px;
    box-shadow: 1px 2px 10px rgba(0, 0, 0, 0.2);
    border-radius: 5px;
}

.title-wrapper {
    position: relative;
}

.title-wrapper::after {
    content: "";
    display: block;
    position: absolute;
    bottom: 0;
    height: 1px;
    width: 100%;
    background-color: #eaeaea;
}

.detect-wrapper .title-wrapper .title {
    font-size: 25px;
    font-weight: bold;
    padding: 10px 0;
    letter-spacing: 2px;
}

.detect-wrapper .title-wrapper .subtitle {
    font-size: 14px;
    color: #979797;
    padding-bottom: 10px;
}

.detect-wrapper .form-wrapper {
    margin-top: 20px;
}

.form-wrapper .el-form .el-form-item .el-form-item__label .label {
    font-weight: bold;
    font-size: 18px;
}
.form-wrapper ::v-deep .el-form .el-form-item .el-form-item__label {
    padding-bottom: 0 !important;
    padding-left: 5px;
}
.form-wrapper .target {
    width: 85%;
    margin: 0 auto 20px auto;
}
.form-wrapper .inline-half {
    width: 250px;
    margin-left: 60px;
    float: left;
}
/* .form-wrapper .inline-right{
    margin-left: 50px;
} */
.form-wrapper .footer {
    float: left;
    margin-left: 248px;
    text-align: center;
}
</style>
