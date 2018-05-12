<template>
  <div>
  
  
  
    <section style="margin-top:4em;">
  
      <Row type="flex" justify="start">
        <Col span="12" align="left" offset="2">
        <p class="titlewords">报告</p>
        </Col>
      </Row>
  
  
  
  
  
  
  
    </section>
  
  
  
  
  
    <section>
  
      <div class="desc">
  
  
        <Row type="flex" align="top" justify="start" style="margin-top:1em;">
  
          <transition name="fadeUp" appear>
            <Col span="6" align="center" offset="0">
  
  
            <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
              <Col span="14" align="left" style="margin-top:1em;" offset="2">
  
              <Breadcrumb>
                <BreadcrumbItem to="/">首页</BreadcrumbItem>
                <BreadcrumbItem to="/results">报告</BreadcrumbItem>
  
              </Breadcrumb>
  
              </Col>
  
            </Row>
  
  
  
  
  
  
  
  
            </Col>
  
          </transition>
  
          <Col span="12" align="left">
  
          <transition name="fadeUp" appear>
  
            <Row type="flex" align="top" justify="start" style="margin-top:0em;">
              <Col span="8" align="left" style="margin-top:2em;margin-bottom:2em" offset="0">
              <p class="title2">全球443端口开放情况</p>
              </Col>
            </Row>
  
  
          </transition>
  
  
          <Row type="flex" align="middle" justify="start" style="margin-top:2em;margin-bottom:5em">
            <Col span="22" align="left">
  
            <highmaps :options="options"></highmaps>
  
  
            </Col>
          </Row>
  
  
  
  
          <!-- <Row type="flex" align="top" justify="start" style="margin-top:0em;">
                                    <Col span="22" align="left" style="margin-top:0em;" offset="0">
                                    <hr style="height:1px;border:none;border-top:1px solid grey;
                                                                            z-index:999;
                                                                            margin:2em 0em 0.2em 0em;
                                                                            width:90%;opacity:0.5;
                                                                            border-radius:1px;
                                                                            box-shadow: 0px 4px 16px 0px rgba(255, 255, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .5);
                                                                            " />
                                    </Col>
                                  </Row> -->
  
          <!-- <Scroll loading-text="获取数据中" :on-reach-bottom="handleReachBottom" height="650">
                              <Row type="flex" align="middle" justify="start" style="margin-top:0.2em;margin-bottom:5em">
                                <Col span="22" align="left">
                    
                                <transition-group name="fadeUp" tag="div" appear>
                    
                                 
                    
                                </transition-group>
                    
                                </Col>
                              </Row>
                            </Scroll> -->
  
  
          </Col>
  
  
          <transition name="fadeUp" appear>
  
            <Col span="6" align="center">
  
  
  
  
  
  
  
  
            <!-- <hr style="height:1px;border:none;border-top:1px solid #555555;
                                                                            margin:2em 0em 1em 0em;
                                                                            width:80%;opacity:0.5;
                                                                            border-radius:1px;
                                                                            box-shadow: 0px 4px 16px 0px rgba(255, 255, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .5);
                                                                            " /> -->
  
            <Row type="flex" align="top" justify="center" style="margin-top:4em;">
              <Col span="20" align="center" style="margin-top:2em;" offset="1">
  
  
  
              </Col>
            </Row>
            </Col>
  
          </transition>
  
        </Row>
      </div>
    </section>
  
  </div>
</template>

<script>
  import china from '../assets/china.json'
  import world from '../assets/world.json'
  export default {
    data() {
      return {
        desc: "",
        searchKeyword: "",
        options: {
          chart: {
            borderWidth: 0,
            height: 500,
            className: "highcharts-background",
            events: {
              drilldown: function(e) {
                if (!e.seriesOptions) {
                  var chart = this
  
                  //   // mapKey = 'countries/us/' + e.point.drilldown + '-all',
                  //   // Handle error, the timeout is cleared on success
                  //   // fail = setTimeout(function() {
                  //   //   if (!Highcharts.maps[mapKey]) {
                  //   //     chart.showLoading('<i class="icon-frown"></i> Failed loading ' + e.point.name);
                  //   //     fail = setTimeout(function() {
                  //   //       chart.hideLoading();
                  //   //     }, 1000);
                  //   //   }
                  //   // }, 3000);
  
                  // // Show the spinner
                  // chart.showLoading('<i class="icon-spinner icon-spin icon-3x"></i>'); // Font Awesome spinner
  
                  // Load the drilldown map
                  // $.getScript('https://code.highcharts.com/mapdata/' + mapKey + '.js', function() {
  
                  let data = [{
                      "name": "北京",
                      "value": 276079
                    },
                    {
                      "name": "天津",
                      "value": 17352
                    },
                    {
                      "name": "河北",
                      "value": 27106
                    },
                    {
                      "name": "山西",
                      "value": 14914
                    },
                    {
                      "name": "内蒙古",
                      "value": 67682
                    },
                    {
                      "name": "辽宁",
                      "value": 24486
                    },
                    {
                      "name": "吉林",
                      "value": 21509
                    },
                    {
                      "name": "黑龙江",
                      "value": 17246
                    },
                    {
                      "name": "上海",
                      "value": 93343
                    },
                    {
                      "name": "江苏",
                      "value": 87971
                    },
                    {
                      "name": "浙江",
                      "value": 119478
                    },
                    {
                      "name": "安徽",
                      "value": 13184
                    },
                    {
                      "name": "福建",
                      "value": 32736
                    },
                    {
                      "name": "江西",
                      "value": 18535
                    },
                    {
                      "name": "山东",
                      "value": 133398
                    },
                    {
                      "name": "河南",
                      "value": 40904
                    },
                    {
                      "name": "湖北",
                      "value": 22660
                    },
                    {
                      "name": "湖南",
                      "value": 20233
                    },
                    {
                      "name": "广东",
                      "value": 267772
                    },
                    {
                      "name": "广西",
                      "value": 15218
                    },
                    {
                      "name": "海南",
                      "value": 1980
                    },
                    {
                      "name": "重庆",
                      "value": 11025
                    },
                    {
                      "name": "四川",
                      "value": 22456
                    },
                    {
                      "name": "贵州",
                      "value": 5259
                    },
                    {
                      "name": "云南",
                      "value": 16783
                    }, {
                      "name": "西藏",
                      "value": 719
                    }, {
                      "name": "陕西",
                      "value": 20183
                    }, {
                      "name": "甘肃",
                      "value": 4172
                    }, {
                      "name": "青海",
                      "value": 2697
                    }, {
                      "name": "宁夏",
                      "value": 2122
                    }, {
                      "name": "新疆",
                      "value": 3361
                    }, {
                      "name": "台湾",
                      "value": 229
                    }, {
                      "name": "香港",
                      "value": 41131
                    }, {
                      "name": "澳门",
                      "value": 5516
                    }, {
                      "name": "南海诸岛",
                      "value": 93
                    }
                  ];
  
                  // Set a non-random bogus value
                  // $.each(data, function(i) {
                  //   this.value = i;
                  // });
  
                  // Hide loading and add series
                  chart.hideLoading();
  
                  chart.addSeriesAsDrilldown(e.point, {
                    name: "中国",
                    mapData: china,
                    data: data,
                    joinBy: 'name',
                    // dataLabels: {
                    //   enabled: true,
                    //   format: '{point.name}'
                    // }
                  });
  
                }
  
                this.setTitle(null, {
                  text: "中国"
                });
              },
              drillup: function() {
  
                this.setTitle(null, {
                  text: ''
                });
              }
  
  
            },
          },
          colorAxis: {
            className: "mapcolor",
            minColor: "#F1EEF6",
            maxColor: "#ce3d31",
          },
          mapNavigation: {
            enabled: true,
            buttonOptions: {
              verticalAlign: 'bottom'
            }
          },
          color: ['#4572A7', ],
          credits: {
            enabled: true,
            text: "Copyright",
            href: "springx.com"
          },
          title: {
            text: ""
          },
          drilldown: {
            drillUpButton: {
              relativeTo: 'spacingBox',
              position: {
                x: 0,
                y: 60
              }
            }
  
          },
          series: [{
            name: '全球',
            mapData: world,
            data: [{
              name: "China",
              value: 1678350,
              drilldown: 'CN'
            }],
            // dataLabels: {
            //   enabled: true,
            //   color: '#FFFFFF',
            //   formatter: function() {
            //     if (this.point.value) {
            //       return this.point.name;
            //     }
            //   }
            // },
            joinBy: 'name',
            tooltip: {
              headerFormat: '',
              pointFormat: '{point.name}，{point.value}'
            }
          }]
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
    mounted() {
      console.log(this.$route.query);
      this.searchKeyword = this.$route.query.keywords;
      //this.$Message.info(this.searchKeyword)
  
      this.$toast.show('检索成功!', 'Info', this.notificationSystem.options.info);
  
    },
    methods: {
  
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .mapcolor {
    opacity: 0.1;
  }
  
  .highcharts-background {
    opacity: 0.1;
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .titlewords {
    color: white;
    opacity: 0.8;
    font-size: 3.2em;
    user-select: none;
    font-weight: bolder;
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title2 {
    color: black;
    opacity: 0.8;
    font-size: 2.5em;
    user-select: none;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title3 {
    color: black;
    opacity: 0.8;
    font-size: 1.5em;
    user-select: none;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .desc {
    background-color: #fff;
    opacity: 0.7;
    min-height: 65em;
    margin: 2em 6em 0em 6em;
    border-radius: 4px;
  }
</style>
