<template>
  <div>
    <fullscreen ref="fullscreen" @change="fullscreenChange">





      <Row type="flex" align="middle" justify="end" style="margin-top:2em;">



        <Col span="4">


        <Tooltip content="切换全屏" placement="right">
          <Button @click="toggle" type="text" shape="circle" size="large">
            <awe-icon name="expand" scale="1.3"></awe-icon>
          </Button>
        </Tooltip>

        </Col>
      </Row>


      <section>

        <div class="desc">
          <Carousel >
            <CarouselItem>

              <Scroll height="800">
                <Row type="flex" align="middle" justify="start" style="margin-top:13em;">
                  <Col span="14" align="center" style="background-color:;" offset="0">

                  <div class="gifmp4p">

                    <video controls autoplay loop muted class="gifmp4" style="">

                      <source src="../assets/aaa.mp4" type="video/mp4">
                    </video>
                  </div>
                  </Col>

                  <Col span="10" style="background-color:;" align="center">

                  <Row type="flex" align="middle" justify="start" style="margin-top:4em;">
                    <Col span="20" align="left">
                    <p style="font-size:4em;font-weight:bolder">先进的数据分析引擎 </p>
                    </Col>
                  </Row>

                  <Row type="flex" align="middle" justify="start" style="margin-top:1em;margin-bottom:5em">
                    <Col span="18" align="left">
                    <p style="font-size:1.4em;"><br>面对如何庞大的数据，如何高效且快速的进行分析处理？
                      <br><br>我们采用
                      <i>Elasticsearch</i> 作为底层技术支持， ES是一个基于 JSON 的分布式搜索和分析引擎，专为实现水平扩展、高可用和管理便捷性而设计。
                      <br><br>
                      系统允许执行和合并多种类型的搜索 <br>— 结构化、非结构化、地理位置、度量指标 <br>— 搜索方式由你而定。
                      <br><br>先从一个简单的问题出发，比如进字符串“CN”的模糊搜索，试试看能够从中发现些什么。
                    </p>
                    </Col>
                  </Row>

                  </Col>
                </Row>
              </Scroll>

            </CarouselItem>

            <CarouselItem>
              <Scroll height="800">
                <Row type="flex" align="middle" justify="start" style="margin-top:13em;">


                     <Col span="10" style="background-color:;" align="center">

                  <Row type="flex" align="middle" justify="end" style="margin-top:4em;">
                    <Col span="20" align="right">
                    <p style="font-size:4em;font-weight:bolder">可视化与探索 </p>
                    </Col>
                  </Row>

                  <Row type="flex" align="middle" justify="end" style="margin-top:1em;margin-bottom:5em">
                    <Col span="18" align="right">
                    <p style="font-size:1.4em;">
                      <br>我们采用
                      <i>Kibana</i> 作为数据可视化分析套件，<br>Kibana 让您能够自由地选择如何呈现您的数据。
                      <br><br>支持多种可视化形式，柱状图、线状图、饼图、环形图，等等。<br>并且支持地理空间数据的可视化，
                      <br><br>借助Kibana精细的时序性 UI，<br>对您 Elasticsearch 中的数据执行高级时间序列分析。<br>您可以利用功能强大、简单易学的表达式来描述查询、转换和可视化。
                      <br><br>
                     
                    </p>
                    </Col>
                  </Row>

                  </Col>
                  <Col span="14" align="center" style="background-color:;" offset="0">

                  <div class="gifmp4p">

                    <video controls autoplay loop muted class="gifmp4" style="">

                      <source src="../assets/bbb.mp4" type="video/mp4">
                    </video>
                  </div>
                  </Col>

                 
                </Row>
              </Scroll>



             </CarouselItem>
                <CarouselItem>
              <Scroll height="800">
                <Row type="flex" align="middle" justify="start" style="margin-top:13em;">


                     <Col span="10" style="background-color:;" align="center">

                  <Row type="flex" align="middle" justify="end" style="margin-top:4em;">
                    <Col span="20" align="right">
                    <p style="font-size:4em;font-weight:bolder">申请测试密钥</p>
                    </Col>
                  </Row>

                  <Row type="flex" align="middle" justify="end" style="margin-top:1em;margin-bottom:5em">
                    <Col span="18" align="right">
                    <p style="font-size:1.4em;">
                      <!-- <br>我们采用
                      <i>Kibana</i> 作为数据可视化分析套件，<br>Kibana 让您能够自由地选择如何呈现您的数据。
                      <br><br>支持多种可视化形式，柱状图、线状图、饼图、环形图，等等。<br>并且支持地理空间数据的可视化，
                      <br><br>借助Kibana精细的时序性 UI，<br>对您 Elasticsearch 中的数据执行高级时间序列分析。<br>您可以利用功能强大、简单易学的表达式来描述查询、转换和可视化。
                      <br><br> -->
                     
                    </p>
                    </Col>
                  </Row>

                  </Col>
                  <Col span="14" align="center" style="background-color:;" offset="0">

                  <div class="gifmp4p">

                    <video controls autoplay loop muted class="gifmp4" style="">

                      <source src="../assets/ccc.mp4" type="video/mp4">
                    </video>
                  </div>
                  </Col>

                 
                </Row>
              </Scroll>



             </CarouselItem>      
          </Carousel>















        </div>
      </section>
    </fullscreen>
  </div>
</template>

<script>
  import VueFriendlyIframe from "@/components/frame";
  export default {
    data() {
      return {
        desc: "",
        total: 0,
        width: "1775",
        height: "760",
        results: [],
        fullscreen: true,
        notificationSystem: {
          options: {
            show: {
              theme: "dark",
              icon: "icon-person",
              position: "topCenter",
              progressBarColor: "rgb(0, 255, 184)",
              buttons: [
                [
                  "<button>Ok</button>",
                  function (instance, toast) {
                    alert("Hello world!");
                  },
                  true
                ],
                [
                  "<button>Close</button>",
                  function (instance, toast) {
                    instance.hide({
                        transitionOut: "fadeOutUp",
                        onClosing: function (instance, toast, closedBy) {
                          console.info("closedBy: " + closedBy);
                        }
                      },
                      toast,
                      "buttonName"
                    );
                  }
                ]
              ],
              onOpening: function (instance, toast) {
                console.info("callback abriu!");
              },
              onClosing: function (instance, toast, closedBy) {
                console.info("closedBy: " + closedBy);
              }
            },
            ballon: {
              balloon: true,
              position: "bottomRight"
            },
            info: {
              // position: 'bottomLeft'
              position: "topCenter",
              theme: "light",
              transitionIn: "flipInX"
            },
            success: {
              position: "topCenter"
            },
            warning: {
              position: "topLeft"
            },
            error: {
              position: "topLeft"
            },
            question: {
              timeout: 20000,
              close: false,
              overlay: true,
              toastOnce: true,
              id: "question",
              zindex: 999,
              position: "center",
              buttons: [
                [
                  "<button><b>YES</b></button>",
                  function (instance, toast) {
                    instance.hide({
                        transitionOut: "fadeOut"
                      },
                      toast,
                      "button"
                    );
                  },
                  true
                ],
                [
                  "<button>NO</button>",
                  function (instance, toast) {
                    instance.hide({
                        transitionOut: "fadeOut"
                      },
                      toast,
                      "button"
                    );
                  }
                ]
              ],
              onClosing: function (instance, toast, closedBy) {
                console.info("Closing | closedBy: " + closedBy);
              },
              onClosed: function (instance, toast, closedBy) {
                console.info("Closed | closedBy: " + closedBy);
              }
            }
          }
        }
      };
    },
    mounted() {
      console.log(this.$route.query);
    },
    components: {
      "vue-friendly-iframe": VueFriendlyIframe
    },
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
      toggle() {
        if (this.height == "760") {
          this.height = "900";
          this.width = "1820";
        } else {
          this.height = "760";
          this.width = "1775";
        }

        this.$refs["fullscreen"].toggle();
      },
      fullscreenChange(fullscreen) {
        this.fullscreen = fullscreen;
      }
    }
  };

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
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, 0.05),
    0px 0px 8px 0px rgba(0, 0, 0, 0.04);
    transition: all ease-in-out 0.4s;
  }

  .smmary:hover {
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, 0.05),
    0px 0px 8px 0px rgba(0, 0, 0, 0.2);
  }

  .titlewords {
    color: white;
    opacity: 0.8;
    font-size: 3.2em;
    user-select: none;
    font-weight: bolder; // text-shadow: black 0.1em 0.1em 1.5em;
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
    z-index: 0;
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

  .desc {
    // background-color: #fff;
    background-color: rgba(255, 255, 255, 0.5) !important;
    background-color: #000;
    filter: Alpha(opacity=50);
    min-height: 68em;
    margin: 2em 6em 0em 6em;
    border-radius: 4px;
  }

  .gifmp4 {
    position: relative;
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, 0.2),
    0px 16px 48px 0px rgba(100, 100, 100, 0.6);
    border-radius: 4px;
    opacity: 0.9;
    width: 900px;
    height: 100%;
  }

  .gifmp4p {
    position: relative;
  }

</style>
