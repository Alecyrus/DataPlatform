<template>
  <div>
  
  
  
  
  
    <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">



  
      <Col span="22" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
              
  <pre>{{openssl}}</pre>  
  
  
      </Col>
      <!-- <Col span="7" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
  
  
  
      </Col> -->
  
    </Row>
  
  
  
  
  
  </div>
</template>

<script>
  export default {
    data() {
      return {
        t1: '探寻和分析',
        openssl:"",
        cert:{},
        // loading: true,
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
    this.cert = this.$ls.get("selectedCert");


       this.$Loading.start();
            this.$request.post('/api/v1/openssl', {
              "raw":this.cert.raw
            })
              .then((response) => {
               let state = response.data.state;
                if (state) {
  
                  this.$toast.success("加载数据成功", 'Info', this.notificationSystem.options.info);
                  this.$Loading.finish();
                  this.openssl = response.data.data
                  //this.requestIndex++;
                 // console.log("reponse",response.data.data.length)
                  //this.results = this.results.concat(response.data.data);
                 // console.log(this.results.length)
                  //this.total = response.data.total
                  //return response
  
                } else {
  
                  this.$toast.success('获取失败!', 'Info', this.notificationSystem.options.info);
                  this.$Loading.finish();
                }
              }).catch((error) => {
                console.log(error);
                this.$Loading.error();
                 this.$toast.error('服务器繁忙!', 'Info', this.notificationSystem.options.info);
               
              });

    },
    methods: {
      search() {
  
      }
    },
    components: {
  
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /* .backgroundac {
      transition: all ease-in-out 0.6s;
      filter: blur(15px);
    }
    
    .backgroundacde {
      filter: blur(0px);
      transition: all ease-in-out 0.6s;
    } */
  
  pre {
    white-space: pre-wrap;
    white-space: -moz-pre-wrap;
    white-space: -pre-wrap;
    white-space: -o-pre-wrap;
    word-wrap: break-word;
     /* text-shadow: black 0.1em 0.1em 5em; */
  }
  
  .trust {
    color: green;
    opacity: 0.8;
    font-size: 1.0em;
    user-select: none;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 2em;
  }
  
  .brands {
    color: black;
    opacity: 0.8;
    font-size: 1.0em;
    user-select: none;
    font-weight: bolder;
    text-shadow: black 0.1em 0.1em 2em;
  }
  
  .rightTitle {
    color: black;
    opacity: 0.8;
    font-size: 1.2em;
    user-select: none;
    font-weight: bolder;
    text-shadow: black 0.1em 0.1em 2em;
  }
  
  .smmary {
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);
    transition: all ease-in-out 0.4s;
  }
  
  .smmary:hover {
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .2);
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
  
  .search {
    opacity: 0.7;
  }
  
  .desc {
    background-color: #fff;
    opacity: 0.6;
    margin: 12em 0.8em 0em 0.8em;
    border-radius: 4px;
  }
</style>
