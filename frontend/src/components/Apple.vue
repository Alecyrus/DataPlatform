<template>
  <div>
  
    <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
  
      <Col span="15" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="0">
      <div class="parent">
        <d3-network :net-nodes="nodes" :net-links="links" :options="options" />
  
  
        <div v-if="loading" class="mask">
  
          <Row type="flex" align="top" justify="center" style="margin-top:20em;background-color:;">
            <Col span="18" align="center" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="0">
  
            <Spinner name="line-scale-pulse-out" width="100" height="100" color="#ce3d31" />
  
            </Col>
          </Row>
  
        </div>
      </div>
  
      </Col>
  
  
      <Col span="8" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="0">
  
  
  
      <Row type="flex" align="top" justify="center" style="margin-top:0em;">
        <Col span="16" align="center" style="margin-top:1em;margin-bottom:0em" offset="0">
        <Card class="smmary" style="width:100%">
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="20" align="left" style="margin-bottom:0em" offset="0">
            <p class="rightTitle">授信状态</p>
            </Col>
          </Row>
  
  
  
          <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">
              <awe-icon name="brands/apple" scale="0.9"></awe-icon>&nbsp;Apple</p>
            </Col>
            <Col span="12" align="left" style="margin-bottom:0em" offset="1">
  
            <p class="trust">&nbsp;&nbsp;
              <awe-icon name="lock" scale="1" color="green"> </awe-icon> &nbsp;Trusted</p>
            </Col>
          </Row>
  
        </Card>
        </Col>
      </Row>
  
  
      <Row type="flex" align="top" justify="start" style="margin-top:5em;">
        <Col span="24" align="center" style="margin-top:1em;margin-bottom:0em" offset="0">
        <Card class="smmary" style="width:100%">
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="20" align="left" style="margin-bottom:0em" offset="0">
            <p class="rightTitle">授信路径</p>
            </Col>
          </Row>
  
          <Row type="flex" align="top" justify="center" style="margin-top:1.5em;">
            <Col span="24" align="left" style="margin-bottom:0em" offset="0">
  
            <Collapse align="left" v-model="value2" accordion>
              <Panel v-for="(item, index) in pathlist" :key="index" :name="''+index">
                Path {{index+1}}
                <div slot="content">
  
                  <Row v-for="(cert, cindex) in item" :key="cindex" :name="''+cindex" type="flex" justify="start" align="bottom" style="margin-top:0em;margin-left:0.8em;">
                    <Col span="8" align="right" style="margin-top:0.2em;" offset="0">
                    <p style="font-size:1em;font-weight:bolder"> {{cert.id}}</p>
  
                    </Col>
                    <Col span="15" align="left" style="margin-left:1.1em;" offset="1">
                    <p> {{cert.name}}</p>
  
                    </Col>
                  </Row>
  
  
                </div>
              </Panel>
  
            </Collapse>
            </Col>
          </Row>
        </Card>
        </Col>
      </Row>
  
  
  
  
  
      </Col>
  
    </Row>
  
  
  
  
  
  </div>
</template>

<script>
  import D3Network from 'vue-d3-network'
  export default {
    data() {
      return {
        t1: '探寻和分析',
        value2: "0",
        pathlist: [
          [{
              id: "0b02ea7c...d57ed3c9",
              name: "Apple"
  
            },
            {
              id: "0b02ea7c...d57ed3c9",
  
              name: '	StartCom Class 1 DV Server CA'
            },
            {
              id: "0b02ea7c...d57ed3c9",
  
              name: 'StartCom Certification Authority',
  
            },
            {
              id: "0b02ea7c...d57ed3c9",
  
              name: 'zzStartCom Certification Authority G2'
            },
            {
              id: "0b02ea7c...d57ed3c9",
              name: 'www.ajsmarketing.com'
            }
          ],
          [{
              id: "0b02ea7c...d57ed3c9",
              name: "Apple"
  
            },
            {
              id: "0b02ea7c...d57ed3c9",
  
              name: '	StartCom Class 1 DV Server CA'
            },
            {
              id: "0b02ea7c...d57ed3c9",
  
              name: 'StartCom Certification Authority',
  
            },
            {
              id: "0b02ea7c...d57ed3c9",
  
              name: 'zzStartCom Certification Authority G2'
            },
            {
              id: "0b02ea7c...d57ed3c9",
              name: 'www.ajsmarketing.com'
            }
          ]
  
        ],
  
        nodes: [],
        links: [],
        options: {
          force: 9000,
          nodeSize: 20,
          nodeLabels: true,
          linkWidth: 5,
          canvas: false,
  
        },
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
      this.$request.get('/api/v1/getpath?id=' + this.cert._id.$oid + "&root_store=Apple")
        .then((response) => {
          let state = response.data.state;
          if (state) {
  
            //this.$toast.success('检索到' + response.data.total + "条数据", 'Info', this.notificationSystem.options.info);
            this.$Loading.finish();
            this.links = response.data.links
            this.nodes = response.data.nodes
  
            console.log("reponse", response.data)
            // this.results = this.results.concat(response.data.data);
            // console.log(this.results.length)
            //this.total = response.data.total
            //return response
  
          } else {
  
            this.$toast.success('未检索到更多数据!', 'Info', this.notificationSystem.options.info);
            this.$Loading.finish();
          }
        }).catch((error) => {
          console.log(error);
          this.$Loading.error();
          this.$Message.error('服务器繁忙');
        });
  
      //a.map(function (x) {x.call=3;return x});
  
    },
    methods: {
      search() {
  
      },
  
    },
    computed: {
      loading() {
        if (this.nodes.length == 0) {
          return true
        } else {
          return false
        }
      }
    },
    components: {
      D3Network
  
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  pre {
    white-space: pre-wrap;
    white-space: -moz-pre-wrap;
    white-space: -pre-wrap;
    white-space: -o-pre-wrap;
    word-wrap: break-word;
    text-shadow: black 0.1em 0.1em 5em;
  }
  
  .trust {
    color: green;
    opacity: 0.8;
    font-size: 1.0em;
    user-select: none;
    font-weight: bolder;
    text-shadow: black 0.1em 0.1em 2em;
  }
  
  .brands {
    color: black;
    opacity: 0.8;
    font-size: 1.2em;
    user-select: none;
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
