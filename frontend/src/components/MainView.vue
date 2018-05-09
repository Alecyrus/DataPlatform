<template>
  <div class="hello">
  
  
    <section>
      <img class="background" src="../assets/back1.jpg" alt="">
    </section>
  
    <section style="margin:0.6em 3em 0em 3em;">
      <Affix :offset-top="10">
        <Menu style="opacity:0.6;
                          box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);
                          transparent;border-radius:4px" ref="mainMenu" mode="horizontal" theme="light" :active-name="activeMenu" @on-select="handleMenuSelect">
          <div class="layout-logo" align="center">
            <p style="font-size:1.9em;margin-left:20px;color:#222;;font-weight:bolder;user-select:none;"><Icon  size="38" style="margin-top:10px;"  type="ios-flower-outline"></Icon> <i> SpringX</i></p>
          </div>
          <div class="layout-nav">
            <MenuItem name="/"> 首页
            </MenuItem>
            <MenuItem name="/help"> 帮助
            </MenuItem>
            <MenuItem name="/about"> 关于
            </MenuItem>
          </div>
        </Menu>
  
      </Affix>
  
    </section>

    

     <transition name="fadeDown" mode="out-in">
          <router-view></router-view>
     </transition>
  
  
  
  
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
  </div>
</template>

<script>
  export default {
    data() {
      return {
        activeMenu: '',
        adminlogin: false,
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
    methods: {
      handleMenuSelect() {
        this.$router.push(arguments[0]);
      },
      setAdminShow() {
        this.adminlogin = true;
        this.$Message.success('已初始化后台管理系统');
  
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
    min-width: 100%;
    min-height: 100%;
    height: auto;
    z-index: -100;
    -webkit-filter: blur(5px);
    filter: blur(15px);
    width: auto;
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
