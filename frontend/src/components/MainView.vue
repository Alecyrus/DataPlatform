<template>
  <div class="hello">
  
  
    <section>
      <img class="background" src="../assets/back1.jpg" alt="">
    </section>
  
    <section style="margin:0.6em 0.6em 0em 0.6em;">
      <Affix>
        <Menu style="opacity:0.6;
                    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);
                    transparent;border-radius:4px" ref="mainMenu" mode="horizontal" theme="light" :active-name="activeMenu" @on-select="handleMenuSelect">
          <div class="layout-logo">
            <p style="font-size:1.9em;margin-left:20px;color:#222;font-family:STSong;font-weight:bolder;">SpringX</p>
          </div>
          <div class="layout-nav">
            <MenuItem name="/"> 首页
            </MenuItem>
            <MenuItem name="/"> 帮助
            </MenuItem>
            <MenuItem name="/"> 关于
            </MenuItem>
          </div>
        </Menu>
  
      </Affix>
  
    </section>
  
  
  
  
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        activeMenu: '',
      }
    },
    methods:{
      handleMenuSelect() {
         this.$router.push(arguments[0]);
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
