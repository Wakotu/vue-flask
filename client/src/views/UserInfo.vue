<!--
 * @Author: Axiuxiu
 * @Date: 2022-03-10 14:13:01
 * @LastEditTime: 2022-03-11 11:07:50
 * @Description: 个人信息页面
-->

<template>
    <div class="user-info-wrapper">
        <Header></Header>
        <div class="user-profile">
            <el-tabs v-model="activeName">
                <!-- 基本信息 -->
                <el-tab-pane label="基本信息" name="basicInfo" class="basic-info">
                    <div class="header">
                        <!-- 添加用户头像 -->
                        <!-- <img src="/static/user.png" alt class="avatar" /> -->

                        <el-upload
                            class="avatar-uploader"
                            action="https://jsonplaceholder.typicode.com/posts/"
                            :show-file-list="false"
                            :on-success="handleAvatarSuccess"
                            :before-upload="beforeAvatarUpload"
                        >
                            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                            <i v-else class="el-icon-plus avatar-uploader-icon"></i>

                            <div class="tip">
                                修改头像
                            </div>
                        </el-upload>

                        <div class="right-side">
                            <div class="up">
                                <div class="username">
                                    <span class="name">用户名</span>
                                    <i class="el-icon-male gender"></i>
                                </div>

                                <button class="edit" v-on:click="openEdit">编辑个人信息</button>
                            </div>
                            <div class="down">
                                <span>账号ID：/账号ID/</span>
                                <span>注册时间：/注册时间/</span>
                                <span>身份：/身份/</span>
                            </div>
                        </div>
                    </div>

                    <ul class="main">
                        <li>
                            <span class="key">所属单位：</span>
                            <span class="value">XXXX</span>
                        </li>
                        <li>
                            <span class="key">居住地址：</span>
                            <span class="value">XXXX</span>
                        </li>
                        <li class="intro">
                            <span class="key">介绍自己：</span>
                            <span
                                class="value"
                            >个人简介可以是 表格 的形式，也可以是其他 形式 。 一般用于初次见面时个人介绍中或者个人 履历 表中等。 忌硬套格式 安排结构、运用笔墨应遵循古人所说“定体则无，大体须有”的原则才是。 也就是说，既要考虑一般规律，又要结合自身实际来确立重点、谋篇布局、组织材料，绝不可死搬硬套。 从群体上看，中专 毕业生 的劣势是 阅历 较少、知识层次相对不高;优势是学校专业设置大多贴近市场实际、贴近一线需要，且中专毕业生年青、肯吃苦、可塑性强。 从个体来说，每位毕业生的优势与长项又各不相同，如有相当一部分毕业生动手操作能力较好;有些学生非常上进，上学期间还同时参加了职业资格考试或自学考试。 所以，在实事求是，不弄虚作假的前提下，要特别注意扬长避短，从而在竞争中取得优势，打动聘任者。</span>
                        </li>
                    </ul>
                </el-tab-pane>
                <!-- 安全信息 -->
                <el-tab-pane label="安全信息" name="secInfo" class="sec-info">
                    <div class="header">
                        <div class="right-side">
                            <div class="up">
                                <div class="username">
                                    <span class="name">用户名</span>
                                    <i class="el-icon-male gender"></i>
                                </div>
                            </div>
                            <div class="down">
                                <span>账号ID：/账号ID/</span>
                                <span>上次登录事件：/上次登录时间/</span>
                            </div>
                        </div>
                    </div>

                    <ul class="main">
                        <li>
                            <span class="key">验证邮箱：</span>

                            <span class="value" v-show="!isEmailEdit">XXXXXX</span>
                            <input
                                ref="emailInput"
                                type="text"
                                class="value"
                                v-show="isEmailEdit"
                                v-on:blur="handleBlur('email',$event)"
                            />

                            <span class="amend" v-on:click="edit('email')">修改</span>
                        </li>
                        <li>
                            <span class="key">手机绑定：</span>

                            <span class="value" v-show="!isPhoneEdit">XXXXXX</span>
                            <input
                                ref="phoneInput"
                                type="text"
                                class="value"
                                v-show="isPhoneEdit"
                                v-on:blur="handleBlur('phone',$event)"
                            />

                            <span class="amend" v-on:click="edit('phone')">修改</span>
                        </li>
                        <li>
                            <span class="key">账户密码：</span>

                            <span class="value" v-show="!isPwdEdit">······</span>
                            <input
                                ref="pwdInput"
                                type="password"
                                name
                                id
                                class="value"
                                v-show="isPwdEdit"
                                v-on:blur="handleBlur('pwd',$event)"
                            />

                            <span class="amend" v-on:click="edit('pwd')">修改</span>
                        </li>
                    </ul>
                </el-tab-pane>
            </el-tabs>
        </div>

        <div class="overlay" v-show="isEditBasic">
            <div class="popup">
                <!-- 标题 -->
                <h1 class="title">基本信息</h1>
                <!-- 表单 -->
                <el-form ref="form" :rules="rules" :model="form" label-width="80px">
                    <el-form-item label="用户名" prop="username">
                        <el-input v-model.trim="form.username"></el-input>
                    </el-form-item>
                    <el-form-item label="所属单位" prop="unit">
                        <el-input v-model.trim="form.unit"></el-input>
                    </el-form-item>
                    <el-form-item label="居住地址" prop="address">
                        <el-input v-model.trim="form.address"></el-input>
                    </el-form-item>
                    <el-form-item label="个人介绍" prop="intro">
                        <el-input type="textarea" v-model.trim="form.intro"></el-input>
                    </el-form-item>

                    <el-form-item>
                        <el-button type="primary" @click="onSubmit('form')">修改</el-button>
                        <el-button v-on:click="cancelEdit">取消</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import Header from "../components/Header.vue";
import { mapState } from "vuex";

export default {
    name: "UserInfo",
    components: { Header },
    data() {
        return {
            activeName: "basicInfo",
            isEmailEdit: false,
            isPhoneEdit: false,
            isPwdEdit: false,

            imageUrl: "/static/user.png",
            isEditBasic: false,
            // 编辑表单
            form: {
                // 这里要替换为全局user的对应值
                username: "",
                unit: "",
                address: "",
                intro: "",
            },
            rules: {
                username: [
                    {
                        required: true,
                        message: "请输入用户名",
                        trigger: "blur",
                    },
                ],
                unit: [
                    {
                        required: true,
                        message: "请输入所属单位",
                        trigger: "blur",
                    },
                ],
                address: [
                    {
                        required: true,
                        message: "请输入居住地址",
                        trigger: "blur",
                    },
                ],
                intro: [
                    {
                        required: true,
                        message: "请输入介绍信息",
                        trigger: "blur",
                    },
                ],
            },
        };
    },
    computed: {
        ...mapState(["user"]),
    },
    methods: {
        handleAvatarSuccess(res, file) {
            this.imageUrl = URL.createObjectURL(file.raw);
        },
        beforeAvatarUpload(file) {
            const isJPG = file.type === "image/jpeg"|| file.type==="image/png";
            const isLt4M = file.size / 1024 / 1024 < 4;

            if (!isJPG) {
                this.$message.error("上传头像图片只能是 JPG 格式!");
            }
            if (!isLt4M) {
                this.$message.error("上传头像图片大小不能超过 2MB!");
            }
            return isJPG && isLt4M;
        },
        onSubmit(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // 提交表单数据
                } else {
                    console.log("form error");
                    return false;
                }
            });
        },
        openEdit() {
            this.isEditBasic = true;
        },
        cancelEdit() {
            this.isEditBasic = false;
        },
        // 安全信息页面修改
        edit(cmd) {
            switch (cmd) {
                case "email":
                    this.editEmail();
                    break;
                case "phone":
                    this.editPhone();
                    break;
                case "pwd":
                    this.editPwd();
                    break;
            }
        },
        editEmail() {
            this.isEmailEdit = true;

            this.$nextTick(() => {
                this.$refs.emailInput.focus();
            });
        },
        editPhone() {
            this.isPhoneEdit = true;

            this.$nextTick(() => {
                this.$refs.phoneInput.focus();
            });
        },
        editPwd() {
            this.isPwdEdit = true;

            this.$nextTick(() => {
                this.$refs.pwdInput.focus();
            });
        },
        handleBlur(key, e) {
            // 获取输入框内容
            const input = e.target.value;
            if (input.trim() === "") {
                alert("输入内容不能为空！");
                return;
            }
            // 更改vuex中的数据

            // 发送请求修改数据请求

            // 变回原状
            switch (key) {
                case "email":
                    this.isEmailEdit = false;
                    break;
                case "phone":
                    this.isPhoneEdit = false;
                    break;
                case "pwd":
                    this.isPwdEdit = false;
                    break;
            }
        },
    },
};
</script>

<style scoped>
/* .user-info-wrapper{
    width: 100%;
    height: 100%;
    position: relative;
} */

.user-profile {
    width: 800px;
    margin: 0 auto;
}

.basic-info {
    padding-left: 100px;
}

.basic-info .header {
    height: 100px;
    /* background-color: #bfa; */
}

.basic-info .header > * {
    float: left;
}

/* .basic-info .header .avatar {
    height: 100px;
    width: 100px;
    border-radius: 50%;
} */

/* 头像上传控件样式 */
.basic-info .header .avatar-uploader ::v-deep .el-upload {
    /* border: 1px dashed #d9d9d9; */
    position: relative;
    border-radius: 50%;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}
/* .basic-info .header .avatar-uploader ::v-deep .el-upload:hover {
    border-color: #409eff;
} */
.basic-info .header .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 100px;
    height: 100px;
    line-height: 100px;
    text-align: center;
}
.basic-info .header .avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    display: block;
}

.basic-info .header .tip{
    position: absolute;
    /* visibility: hidden; */
    left: 0;
    bottom: 0;
    height: 0px;
    width: 100%;
    background-color: rgba(0, 0, 0, .7);
    color: white;
    font-size: 12px;
    line-height: 30px;
    text-align: center;
    
    transition: height 0.2s;
}

.basic-info .header .avatar-uploader ::v-deep .el-upload:hover .tip{
    height: 30px;
}


.header .right-side {
    margin-left: 30px;
    margin-top: 20px;
}

.header .right-side .up {
    height: 45px;
    width: 400px;
    position: relative;
}

.header .right-side .up .username {
    vertical-align: top;
}

.header .right-side .up .username .name {
    font-size: 16px;
    line-height: 45px;
    font-weight: bold;
}

.header .right-side .up .username .gender {
    margin-left: 10px;
    font-size: 24px;
    color: #9aacbe;
    vertical-align: middle;
}

.header .right-side .up .edit {
    position: absolute;
    right: 0;
    background-color: white;
    padding: 5px;
    font-size: 12px;
    color: #8b8b8b;
    border: 1px solid #949394;
    border-radius: 5px;
    top: 9px;
    cursor: pointer;
}

.header .right-side .up .edit:hover {
    background-color: #ecf5ff;
}

.header .right-side .down {
    font-size: 12px;
    color: #a4a4a4;
    margin-top: 10px;
}

.header .right-side .down span:not(:first-child) {
    margin-left: 30px;
}

.main {
    margin-top: 30px;
}

.main li {
    font-weight: bold;
    font-size: 16px;
    padding: 10px 0;
}

.main li.intro {
    overflow: hidden;
}

.main li.intro span {
    display: block;
    float: left;
}

.main li.intro span.value {
    width: 480px;
    font-weight: normal;
    font-size: 14px;
    line-height: 1.5;
}

/* 安全信息样式 */
.sec-info {
    padding-left: 100px;
}

.sec-info .header .right-side .username .name {
    font-size: 18px;
}

.sec-info .header .right-side .down {
    color: #6b6b6b;
    font-size: 13px;
}

.sec-info .main {
    margin-left: 20px;
}

.sec-info .main li {
    position: relative;
    padding: 15px;
}

.sec-info .main li:not(:last-child)::after {
    content: "";
    position: absolute;
    height: 1px;
    width: 400px;
    background-color: #e8e8e8;
    bottom: 0;
    left: 0;
}

.sec-info .main li {
    font-weight: normal;
}

.sec-info .main li span.key {
    font-weight: bold;
}

.sec-info .main li .amend {
    color: #2364ba;
    margin-left: 10px;
    font-size: 12px;
    vertical-align: middle;
    cursor: pointer;
}

/* 弹出层样式 */
.overlay {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 999;
}

.popup {
    background-color: #ffffff;
    position: fixed;
    width: 300px;
    top: 100px;
    left: 0;
    right: 0;
    margin: 0 auto;
    padding: 10px 30px 10px 10px;
    border-radius: 10px;
}

.popup .title {
    font-size: 20px;
    font-weight: bold;
    height: 30px;
    line-height: 30px;
    text-align: center;
    margin-bottom: 20px;
}
</style>
