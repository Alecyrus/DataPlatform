<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


.shadow {
  box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);
}

  .parent {
    position: relative;
    z-index: 0
  }
  
  .mask {
    position: absolute;
    z-index: 1000;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    /* background-color: #10AEFF; */
    
    /* opacity: 0; */
  }
  
</style>
