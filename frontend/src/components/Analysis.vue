<template>
  <div>
    <fullscreen ref="fullscreen" @change="fullscreenChange">
    <section style="margin-top:4em;">
  
      <Row type="flex" justify="start">
        <Col span="12" align="left" offset="2">
        <p class="titlewords">数据分析</p>
        </Col>
      </Row>
    </section>
  
  
  
  
  
   
          <Row type="flex" align="middle" justify="end" style="margin-top:0em;">
  


              <Col span="4">

     
              <Tooltip content="切换全屏" placement="right">
                    <Button   @click="toggle" type="text" shape="circle" size="large"><awe-icon  name="expand"  scale="1.3" ></awe-icon></Button>
                </Tooltip>

           </Col> 
        </Row>
              

                   <section>
  
      <div class="">
  
  
        <!-- <Row type="flex" align="top" justify="start" style="margin-top:0em;">
  


              <Col span="24"> -->
              <!-- <vue-friendly-iframe :className="'frame'" :src="'http://localhost:5601/'"></vue-friendly-iframe> -->
            <iframe class="desc1" src="http://localhost:5601/app/kibana#/dashboard/e7ad4da0-601e-11e8-b9ae-17169379de14"   :width="width" :height="height" frameborder="0"></iframe>
            
      </div>
    </section>
    </fullscreen>
  </div>
</template>

<script>
import VueFriendlyIframe from '@/components/frame'
  export default {
    data() {
      return {
        desc: "",
        total: 0,
        width:"1775",
        height:"760",
        results: [],
        fullscreen: true,
        notificationSystem: {
          options: {
            show: {
              theme: 'dark',
              icon: 'icon-person',
              position: 'topCenter',
              progressBarColor: 'rgb(0, 255, 184)',
              buttons: [
                ['<button>Ok</button>', function(instance, toast) {
                  alert("Hello world!");
                }, true],
                ['<button>Close</button>', function(instance, toast) {
                  instance.hide({
                    transitionOut: 'fadeOutUp',
                    onClosing: function(instance, toast, closedBy) {
                      console.info('closedBy: ' + closedBy);
                    }
                  }, toast, 'buttonName');
                }]
              ],
              onOpening: function(instance, toast) {
                console.info('callback abriu!');
              },
              onClosing: function(instance, toast, closedBy) {
                console.info('closedBy: ' + closedBy);
              }
            },
            ballon: {
              balloon: true,
              position: 'bottomRight'
            },
            info: {
              // position: 'bottomLeft'
              position: 'topCenter',
              theme: 'light',
              transitionIn: 'flipInX'
  
            },
            success: {
  
              position: 'topCenter'
            },
            warning: {
              position: 'topLeft'
            },
            error: {
              position: 'topLeft'
            },
            question: {
              timeout: 20000,
              close: false,
              overlay: true,
              toastOnce: true,
              id: 'question',
              zindex: 999,
              position: 'center',
              buttons: [
                ['<button><b>YES</b></button>', function(instance, toast) {
                  instance.hide({
                    transitionOut: 'fadeOut'
                  }, toast, 'button');
                }, true],
                ['<button>NO</button>', function(instance, toast) {
                  instance.hide({
                    transitionOut: 'fadeOut'
                  }, toast, 'button');
                }]
              ],
              onClosing: function(instance, toast, closedBy) {
                console.info('Closing | closedBy: ' + closedBy);
              },
              onClosed: function(instance, toast, closedBy) {
                console.info('Closed | closedBy: ' + closedBy);
              }
            }
          }
        }
      }
    },
    mounted() {
      console.log(this.$route.query);
  
    },
     components: { 'vue-friendly-iframe':VueFriendlyIframe},
    computed: {
      // loading() {
      //   if (this.results.length == 0) {
      //     return true
      //   } else {
  
      //     setTimeout(() => {
  
  
      //       return false;
  
  
      //     }, 2000);
      //   }
      // }
    },
    methods: {
     
  
      toggle () {
        if (this.height == "760"){
          this.height = "900";
          this.width = "1820";
        } else {
          this.height = "760";
          this.width = "1775";
        }
     
        this.$refs['fullscreen'].toggle()


      },
      fullscreenChange (fullscreen) {
        this.fullscreen = fullscreen
      }
  
  
  
  
      
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .cert {
    transition: all ease-in-out 0.4s;
  }
  
  .cert:hover {}
  
  .iziToast-capsule {
    margin-top: 100px !important;
  }
  
  .smmary {
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);
    transition: all ease-in-out 0.4s;
  }
  
  .smmary:hover {
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .2);
  }
  
  .titlewords {
    color: white;
    opacity: 0.8;
    font-size: 3.2em;
    user-select: none;
    font-weight: bolder;
    // text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title2 {
    color: black;
    opacity: 0.8;
    font-size: 2.5em;
    user-select: none;
    /* font-weight: bolder; */
    // text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title3 {
    color: black;
    opacity: 0.8;
    font-size: 1.5em;
    user-select: none;
    /* font-weight: bolder; */
    // text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .search {
    opacity: 0.7;
  }
  
  .desc1 {
    opacity: 0.7;
     border-radius: 10px;
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
