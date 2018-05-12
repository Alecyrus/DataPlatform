<template>
  <div v-bind:class="{ backgroundac: adminlogin,backgroundacde: !adminlogin }">
  
  
    <section>
      <img class="background" src="../assets/4.jpg" alt="">
    </section>
  
  
    <transition name="fadeDown" appear>
      <section style="margin:0.6em 3em 0em 3em;">
        <Affix :offset-top="10">
          <Menu style="opacity:0.6;
                                      box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);
                                      transparent;border-radius:4px" ref="mainMenu" mode="horizontal" theme="light" :active-name="activeMenu" @on-select="handleMenuSelect">
            <div class="layout-logo" align="center">
  
  
              <Row type="flex" justify="start" align="top">
                <Col span="2" offset="6" align="right" >
                <!-- <Icon size="38" color="black" style="margin-top:12px;opacity:0.8;" type="ios-flower-outline"></Icon> -->
                <Spinner name="ball-scale-multiple" style="margin-top:30px;opacity:0.8;" color="#ce3d31"/>
                </Col>
                <Col span="10" align="left">
                <p style="font-size:1.9em;color:#222;;font-weight:bolder;user-select:none;font-family:"> <i> SpringX</i> </p>
                </Col>
  
              </Row>
            </div>
            <div class="layout-nav">
              <MenuItem name="/"> 首页
              </MenuItem>
              <MenuItem name="/reports"> 报告
              </MenuItem>
              <MenuItem name="/about"> 关于
              </MenuItem>
            </div>
          </Menu>
  
        </Affix>
  
      </section>
    </transition>
  
  
  
  
    <transition name="fadeUp" mode="out-in">
      <router-view></router-view>
    </transition>
  
  
  
  <transition name="fadeUp" appear>
  
    <section>
      <Row type="flex" justify="center" class="copy">
        <Col span="12">
        <p class="shadow copy-text">Copyright © 2018
          <Tooltip content="点击进入后台管理页面" placement="top-end">
            <b class="adminbutton" @click="setAdminShow()">SpringX</b>
          </Tooltip> All rights reserved.
  
        </p>
        </Col>
      </Row>
    </section>
  
  
</transition>

</transition>
  
    <section>
  
      <Modal :styles="{top: '30%'}" :transition-names="trans" @on-ok="adminLogin" @on-cancel="cancelLogin" :width="400" style="opacity:0.65;box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .2);" v-model="adminlogin">
        <div>
  
          <Row type="flex" justify="start">
            <Col span="12" align="left">
            <p style="text-shadow: grey 0.1em 0.1em 0.9em;font-size:2em;user-select:none">后台管理登录</p>
            </Col>
          </Row>
  
          <Row type="flex" justify="center" style="margin-top:4em;;">
            <Col span="16" align="center" offset="" style="">
  
  
            <Form ref="adminlogin" :model="adminInfo" :rules="ruleInline" inline>
              <FormItem prop="user">
                <Input size="large" type="text" style="width:250px;" v-model="adminInfo.username" placeholder="账号">
                <Icon type="person" slot="prepend"></Icon>
                </Input>
              </FormItem>
              <FormItem prop="password">
                <Input size="large" type="password" style="width:250px;" v-model="adminInfo.password" placeholder="口令">
                <Icon type="android-lock" slot="prepend"></Icon>
                </Input>
              </FormItem>
              <!-- <FormItem>
                    <Button type="primary" @click="handleSubmit('adminlogin')">Signin</Button>
                  </FormItem> -->
            </Form>
  
  
            </Col>
          </Row>
  
  
  
  
  
  
        </div>
  
  
  
      </Modal>
  
    </section>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        activeMenu: '',
        adminlogin: false,
        trans: ['zoom', "fade"],
        adminInfo: {
          username: "",
          password: ""
        },
        ruleInline: {
          username: [{
            required: true,
            message: 'Please fill in the user name',
            trigger: 'blur'
          }],
          password: [{
              required: true,
              message: 'Please fill in the password.',
              trigger: 'blur'
            },
            // { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
          ]
        }
        // backpath: "../assets/back1.jpg",
      }
    },
    mounted() {
      // let index = 1;
      // setInterval(() => {
      //   this.backpath = "../assets/" + "back"+index+".jpg";
      //   this.$Message.success(this.backpath);
      //   index += 1;
      //   index  = index % 5;
      // }, 20000);
    },
    watch: {
      // 如果 `question` 发生改变，这个函数就会运行
      adminlogin: function(newQuestion, oldQuestion) {
  
        // this.$toast.error("asdasd", 'Error', {
        //       position: "topCenter"
        //     });
        if (oldQuestion) {
          this.adminInfo.username = "";
          this.adminInfo.password = "";
          this.$refs['adminlogin'].resetFields();
  
        }
  
      }
  
    },
    methods: {
      adminLogin() {
  
        // this.$toast.success('已初始化后台管理系统', 'Success', {
        //   position: "topCenter"
        // });
        this.$toast.error('尚未开放,敬请期待', 'Error', {
          position: "topCenter"
        });
  
      },
      cancelLogin() {
  
        this.adminInfo.username = "";
        this.adminInfo.password = "";
        this.$refs['adminlogin'].resetFields();
  
      },
      handleMenuSelect() {
        if (arguments[0] != "/" && arguments[0] != "/reports") {
          this.$toast.error('尚未开放,敬请期待', 'Error', {
            position: "topCenter"
          });
  
        } else {
          this.$router.push(arguments[0]);
        }
  
      },
      setAdminShow() {
        this.adminlogin = true;
  
  
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

$animationDuration: 0.7s;
@import "vue2-animate/src/sass/vue2-animate.scss";
  .backgroundac {
    transition: all ease-in-out 0.5s;
    filter: blur(10px);
  }
  
  .backgroundacde {
    filter: blur(0px);
    transition: all ease-in-out 0.2s;
  }
  
  .adminbutton {
    transition: all ease-in-out 0.3s;
  }
  
  .adminbutton:hover {
    color: #999;
    text-shadow: black 0.2em 0.2em 2em;
  }
  
  .copy {
    margin-top: 2em;
  }
  
  .copy-text {
    color: aliceblue;
    opacity: 0.7;
    user-select: none;
    text-shadow: black 0.1em 0.1em 0.6em;
  }
  
  .background {
    position: fixed;
    right: 0;
    bottom: 0;
    width: 100%;
    z-index: -100;
    -webkit-filter: blur(5px);
    filter: blur(15px);
  }
  
  .layout-logo-in {
    z-index: 999;
  }
  
  .layout-logo {
    width: 20%;
    height: 4em;
    /* background-color: #85004B; */
    opacity: 0.8;
    border-radius: 0.18em;
    float: left;
    position: relative;
    /* top: 15px;
                        left: 20px; */
    /*    -webkit-filter: blur(20px);
                        -moz-filter: blur(2px);
                        -ms-filter: blur(2px);
                        -o-filter: blur(2px);
                        filter: blur(15px);    */
  }
  
  .layout-nav {
    width: 20em;
    margin: 0 auto;
    float: right;
    position: relative;
  }
</style>
