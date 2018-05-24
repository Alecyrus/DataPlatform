<template>
  <div>
  
  
  
  
  
    <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
  
  
  
  
      <Col span="18" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="0">
  
      <div class="parent">
        <tree :type="treetype" :data="tree" :radius="nodesize" node-text="name" :zoomable="true" style="height:700px; width:100%;" :layoutType="layoutype">
        </tree>
        <div v-if="loading"  class="mask">
  
          <Row type="flex" align="top" justify="center" style="margin-top:20em;background-color:;">
            <Col span="18" align="center" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="0">
  
            <Spinner  name="line-scale-pulse-out" width="100" height="100" color="#ce3d31" />
  
            </Col>
          </Row>
  
        </div>
      </div>
  
      </Col>
      <Col span="6" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="0">
  
      <Row type="flex" align="top" justify="start" style="margin-top:2em;">
        <Col span="22" align="center" style="margin-top:2em;margin-bottom:0em" offset="0">
  
        <!-- <Tooltip content="下载" placement="right">
                    <Button type="ghost" shape="circle" size="large"><awe-icon name="download"  scale="1.3" ></awe-icon></Button>
                  </Tooltip>
          
                  
             -->
  
        <!-- <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                  <Col span="16" align="center" style="margin-top:1em;margin-bottom:0em" offset="0"> -->
        <Card class="smmary" style="width:100%">
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="10" align="left" style="margin-bottom:0em" offset="0">
            <p class="rightTitle"> 显示设置</p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:1em;">
            <Col span="4" align="right" style="margin-bottom:0em" offset="2">
            <p class="brands">空间</p>
            </Col>
            <Col span="16" align="left" style="margin-bottom:0em" offset="2">
            <RadioGroup v-model="layoutype">
              <Radio label="circular"></Radio>
              <Radio label="euclidean"></Radio>
            </RadioGroup>
            </Col>
          </Row>
  
          <Row type="flex" align="top" justify="start" style="margin-top:1em;">
            <Col span="4" align="right" style="margin-bottom:0em" offset="2">
            <p class="brands">布局</p>
            </Col>
            <Col span="16" align="left" style="margin-bottom:0em" offset="2">
            <RadioGroup v-model="treetype">
              <Radio label="tree"></Radio>
              <Radio label="cluster"></Radio>
            </RadioGroup>
            </Col>
          </Row>
  
          <Row type="flex" align="top" justify="start" style="margin-top:1em;">
            <Col span="5" align="right" style="margin-bottom:0em" offset="1">
            <p class="brands">节点大小</p>
            </Col>
            <Col span="16" align="left" style="margin-bottom:0em" offset="2">
            <!-- <Slider v-model="nodesize"  max='10' min='1'></Slider> -->
            <Slider v-model="nodesize" :max='10' :min='1'></Slider>
            </Col>
          </Row>
  
  
          <!-- <Row type="flex" align="top" justify="start" style="margin-top:1em;">
                    <Col span="4" align="right" style="margin-bottom:0em" offset="2">
                    <p class="brands"> 缩放</p>
                    </Col>
                    <Col span="16" align="left" style="margin-bottom:0em" offset="2">
                           <i-switch v-model="zoomable" ></i-switch>
                    </Col>
                  </Row> -->
  
  
  
  
  
        </Card>
  
  
  
  
        </Col>
  
      </Row>
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="24" align="center" style="margin-top:1em;margin-bottom:0em" offset="0">
  
        <Tooltip content="复制" placement="right">
          <Button type="ghost" shape="circle" size="large"><awe-icon name="regular/copy"  scale="1.3" ></awe-icon></Button>
        </Tooltip>
  
        </Col>
  
      </Row>
  
      </Col>
  
    </Row>
  
  
  
  
  
  </div>
</template>

<script>
  import {
    tree
  } from 'vued3tree'
  
  
  export default {
    data() {
      return {
        // zoomable:false,
        treetype: "tree",
        nodesize: 3,
        layoutype: "euclidean",
        tree: {
        },
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
    computed: {
      loading() {
        if (! this.tree.name) {
          return true
        }
        else{
          return false
        }
      }
  },
    mounted() {
      this.cert = this.$ls.get("selectedCert");
  
  
      this.$Loading.start();
      this.$request.get('/api/v1/getpath?id=' + this.cert._id.$oid + "&root_store=Apple")
        .then((response) => {
          let state = response.data.state;
          if (state) {
  
  
            this.$request.post('/api/v1/getca', {
                root_cn: response.data.rootcns,
                end_user: true
  
              })
              .then((response) => {
                let state = response.data.state;
                if (state) {
                  this.$toast.success('加载成功!', 'Info', this.notificationSystem.options.info);
                  this.$Loading.finish();
                  this.tree = response.data.tree
  
                } else {
  
                  this.$toast.success('未检索到更多数据!', 'Info', this.notificationSystem.options.info);
                  this.$Loading.finish();
                }
              }).catch((error) => {
                console.log(error);
                this.$Loading.error();
                this.$Message.error('服务器繁忙');
              });
  
  
  
  
  
  
          } else {
  
            this.$toast.success('未检索到更多数据!', 'Info', this.notificationSystem.options.info);
            this.$Loading.finish();
          }
        }).catch((error) => {
          console.log(error);
          this.$Loading.error();
          this.$Message.error('服务器繁忙');
        });
  
  
  
    },
    methods: {
  
    },
    components: {
  
      tree
  
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .brands {
    color: black;
    opacity: 0.8;
    font-size: 1.1em;
    user-select: none;
    /* text-shadow: black 0.1em 0.1em 2em; */
  }
  
  .rightTitle {
    color: black;
    opacity: 0.8;
    font-size: 1.2em;
    user-select: none;
    font-weight: bolder;
    text-shadow: black 0.1em 0.1em 2em;
  }
  
  .title1 {
    color: black;
    opacity: 0.8;
    user-select: none;
    font-size: 1.7em;
    font-weight: bolder;
    /* text-shadow: black 0.1em 0.1em 2em; */
  }
  
  .title2 {
    color: black;
    opacity: 0.8;
    user-select: none;
    font-size: 1.45em;
    font-family: Helvetica;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title3 {
    color: #222;
    opacity: 0.8;
    user-select: none;
    font-size: 1.0em;
    font-family: Helvetica;
    text-shadow: black 0.1em 0.1em 2em;
    margin-left: 0.5em;
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
  
  
  /*hover状态（按你的需求）控制显示。opacity/display/z-index都可以*/
  
  
  /* .parent:hover .mask {
      opacity: .5;
    } */
</style>
