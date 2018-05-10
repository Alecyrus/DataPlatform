<template>
  <div>
  
    <section style="margin-top:4em;">
  
      <Row type="flex" justify="start">
        <Col span="12" align="left" offset="2">
        <p class="titlewords">检索结果</p>
        </Col>
      </Row>
    </section>
  
  
  
  
  
    <section>
  
      <div class="desc">
  
  
  
  
  
        <Row type="flex" align="top" justify="start" style="margin-top:1em;">
          <Col span="6" align="center" offset="0">
  
  
          <Row type="flex" align="middle" justify="center" style="margin-top:3em;">
            <Col span="14" align="center" style="margin-top:2em;" offset="2">
  
            <Input v-model="searchKeyword" style="box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .02);" placeholder="Enter something..."></Input>
  
  
            </Col>
            <Col span="7" align="left" style="margin-top:2em;" offset="1">
  
            <Button type="ghost" style="opacity:0.9;box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .02);" class="shadow" shape="circle" icon="ios-search" @click="search"> Search</Button>
  
  
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:4em;" offset="3">
            <p class="title2">筛选</p>
            </Col>
          </Row>
  
          <Row type="flex" align="bottom" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:2em;" offset="4">
            <p class="title3">颁发者</p>
            </Col>
          </Row>
  
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:1em;" offset="5">
  
            <Select v-model="issuer" clearable style="width:200px;box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .02);">
                                      <Option v-for="item in issuerList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                  </Select>
  
            </Col>
          </Row>
  
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:2em;" offset="4">
            <p class="title3">状态</p>
            </Col>
          </Row>
  
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:1em;" offset="5">
  
            <Select v-model="status" clearable style="width:200px;box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .02);">
                                      <Option v-for="item in statusList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                  </Select>
  
            </Col>
          </Row>
  
  
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:2em;" offset="4">
            <p class="title3">地区</p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:1em;" offset="5">
  
            <Select v-model="region" clearable style="width:200px;box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .02);backround-color:white;opacity:0.9">
                                      <Option v-for="item in regionList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                  </Select>
  
            </Col>
          </Row>
  
  
  
  
  
  
          </Col>
  
          <Col span="12" align="left">
  
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="left" style="margin-top:2em;margin-bottom:2em" offset="0">
            <p class="title2">证书列表</p>
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
  
          <Scroll :on-reach-bottom="handleReachBottom" height="650">
            <Row type="flex" align="middle" justify="start" style="margin-top:0.2em;margin-bottom:5em">
              <Col span="22" align="left">
              <Card padding="0" v-for="(item, index) in certlist" :key="index" style="margin-bottom:1em">
  
                <Row type="flex" justify="start" align="middle" style="margin-top:0.5em;margin-left:0.8em;">
                  <Col span="1" align="right" style="margin-top:0em;" offset="0">
  
                  <Icon size="22" color="green" type="android-lock"></Icon>
  
                  </Col>
                  <Col span="22" align="left" style="margin-left:0.5em;" offset="0">
  
                  <p style="font-size:1.2em;text-shadow: black 0.05em 0.05em 2em;;opacity:0.9">{{item.title}}</p>
  
                  </Col>
                </Row>
  
                <Row type="flex" justify="start" align="middle" style="margin-top:0.1em;margin-left:0.8em;">
                  <Col span="1" align="right" style="margin-top:0em;" offset="1">
  
                  <Icon size="18" color="black" style="opacity:0.5" type="network"></Icon>
  
                  </Col>
                  <Col span="20" align="left" style="margin-left:0.5em;" offset="0">
  
                  <p style="font-size:1em;text-shadow: black 0.05em 0.05em 3em;;opacity:0.9">{{item.Issuer}}</p>
  
                  </Col>
                </Row>
  
                <Row type="flex" justify="start" align="middle" style="margin-top:0.1em;margin-left:0.8em;">
                  <Col span="1" align="right" style="margin-top:0em;" offset="1">
  
                  <Icon size="18" color="black" style="opacity:0.5" type="android-calendar"></Icon>
  
  
  
                  </Col>
                  <Col span="20" align="left" style="margin-left:0.5em;" offset="0">
  
                  <p style="font-size:1em;text-shadow: black 0.05em 0.05em 3em;;opacity:0.9">{{item.Date}}</p>
  
                  </Col>
                </Row>
  
                <Row type="flex" justify="start" align="middle" style="margin-top:0.1em;margin-left:0.8em;">
                  <Col span="1" align="right" style="margin-top:0em;" offset="1">
  
                  <Icon size="18" color="black" style="opacity:0.5" type="ios-home"></Icon>
  
                  </Col>
                  <Col span="20" align="left" style="margin-left:0.5em;" offset="0">
  
                  <p style="font-size:1em;text-shadow: black 0.05em 0.05em 3em;;opacity:0.9">{{item.domain}}</p>
  
                  </Col>
                </Row>
  
  
  
  
  
  
              </Card>
              </Col>
            </Row>
          </Scroll>
  
  
          </Col>
  
  
  
  
          <Col span="6" align="center">
  
  
  
          <Row type="flex" align="middle" justify="start" style="margin-top:2em;">
            <Col span="14" align="left" style="margin-top:2em;" offset="3">
  
            <Breadcrumb>
              <BreadcrumbItem to="/">首页</BreadcrumbItem>
              <BreadcrumbItem to="/results">检索结果</BreadcrumbItem>
  
            </Breadcrumb>
  
            </Col>
  
          </Row>
  
  
  
  
          <!-- <hr style="height:1px;border:none;border-top:1px solid #555555;
                                                    margin:2em 0em 1em 0em;
                                                    width:80%;opacity:0.5;
                                                    border-radius:1px;
                                                    box-shadow: 0px 4px 16px 0px rgba(255, 255, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .5);
                                                    " /> -->
  
          <Row type="flex" align="top" justify="center" style="margin-top:0em;">
            <Col span="20" align="center" style="margin-top:2em;" offset="1">


            <Tabs value="name1">
              <TabPane label="结果统计" name="name1">
  
  
                <Row type="flex" align="middle" justify="center" style="margin-top:4em;margin-bottom:5em">
                  <Col span="20" align="center">
                  <Card class="smmary" style="width:320px">
                    <div style="text-align:center">
  
                      <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                        <Col span="22" align="center" style="margin-top:3em;" offset="1">
                        <p style="font-size:1.2em">
                          <Icon type="ios-pricetags-outline"></Icon> 关联数据<strong> 12120 </strong>条</p>
                        </Col>
                      </Row>
  
                      <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                        <Col span="22" align="center" style="margin-top:0em;" offset="1">
                        <hr style="height:1px;border:none;border-top:1px solid grey;
                                                    margin:2em 0em 1em 0em;
                                                    width:90%;opacity:0.5;
                                                    border-radius:1px;
                                                    box-shadow: 0px 4px 16px 0px rgba(255, 255, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .5);
                                                    " />
                        </Col>
                      </Row>
  
  
  
                      <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                        <Col span="22" align="center" style="margin-top:1em;" offset="1">
                        <p style="font-size:1.2em">
                          <Icon type="lock-combination"></Icon> 端证书<strong> 1000 </strong>条</p>
                        </Col>
                      </Row>
  
  
                      <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                        <Col span="22" align="center" style="margin-top:0em;" offset="1">
                        <hr style="height:1px;border:none;border-top:1px solid grey;
                                                    margin:2em 0em 1em 0em;
                                                    width:90%;opacity:0.5;
                                                    border-radius:1px;
                                                    box-shadow: 0px 4px 16px 0px rgba(255, 255, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .5);
                                                    " />
  
                        </Col>
                      </Row>
  
                      <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                        <Col span="22" align="center" style="margin-top:1em;" offset="1">
                        <p style="font-size:1.2em">
                          <Icon type="android-time"></Icon> 检索用时<strong> 0.23 </strong>s</p>
                        </Col>
                      </Row>
  
  
                      <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                        <Col span="22" align="center" style="margin-top:0em;" offset="1">
                        <hr style="height:1px;border:none;border-top:1px solid grey;
                                                    margin:2em 0em 3em 0em;
                                                    width:90%;opacity:0.5;
                                                    border-radius:1px;
                                                    box-shadow: 0px 4px 16px 0px rgba(255, 255, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .5);
                                                    " />
  
                        </Col>
                      </Row>
                    </div>
                  </Card>
                  </Col>
                </Row>
              </TabPane>
              <TabPane label="搜索帮助" name="name2">标签二的内容</TabPane>
             
            </Tabs>
            </Col>
          </Row>
          </Col>

        </Row>
      </div>
    </section>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        desc: "",
        searchKeyword: "",
        certlist: [{
            title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
            Issuer: "thawte SSL CA - G2 ",
            Date: "2016-10-07 – 2019-10-07 ",
            domain: "da.macfarlanes.com "
          },
          {
            title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
            Issuer: "thawte SSL CA - G2 ",
            Date: "2016-10-07 – 2019-10-07 ",
            domain: "da.macfarlanes.com "
          },
          {
            title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
            Issuer: "thawte SSL CA - G2 ",
            Date: "2016-10-07 – 2019-10-07 ",
            domain: "da.macfarlanes.com "
          },
          {
            title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
            Issuer: "thawte SSL CA - G2 ",
            Date: "2016-10-07 – 2019-10-07 ",
            domain: "da.macfarlanes.com "
          },
          {
            title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
            Issuer: "thawte SSL CA - G2 ",
            Date: "2016-10-07 – 2019-10-07 ",
            domain: "da.macfarlanes.com "
          },
          {
            title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
            Issuer: "thawte SSL CA - G2 ",
            Date: "2016-10-07 – 2019-10-07 ",
            domain: "da.macfarlanes.com "
          },
  
        ],
        issuer: "",
        issuerList: [{
            value: '1',
            label: 'Symantec Corporation'
          },
          {
            value: '2',
            label: 'GlobalSign nv-sa'
          },
          {
            value: '3',
            label: 'COMODO CA Limited'
          },
        ],
        status: "",
        statusList: [{
            value: '1',
            label: 'Valid'
          },
          {
            value: '2',
            label: 'Expired'
          },
          {
            value: '3',
            label: 'Out of date'
          },
        ],
        region: "",
        regionList: [{
            value: '1',
            label: 'China'
          },
          {
            value: '2',
            label: 'America'
          },
          {
            value: '3',
            label: 'Russion'
          },
        ],
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
              position: 'bottomRight'
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
  
      this.$toast.show('Welcome!', 'Hello', this.notificationSystem.options.info);
  
    },
    methods: {
      search() {
  
      },
      handleReachBottom() {


  
        this.certlist.push({
          title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
          Issuer: "thawte SSL CA - G2 ",
          Date: "2016-10-07 – 2019-10-07 ",
          domain: "da.macfarlanes.com "
        });
        this.certlist.push({
          title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
          Issuer: "thawte SSL CA - G2 ",
          Date: "2016-10-07 – 2019-10-07 ",
          domain: "da.macfarlanes.com "
        })
        this.certlist.push({
          title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
          Issuer: "thawte SSL CA - G2 ",
          Date: "2016-10-07 – 2019-10-07 ",
          domain: "da.macfarlanes.com "
        })
        this.certlist.push({
          title: "C=GB, ST=London, L=London, O=Macfarlanes LLP, OU=IT, CN=da.macfarlanes.com",
          Issuer: "thawte SSL CA - G2 ",
          Date: "2016-10-07 – 2019-10-07 ",
          domain: "da.macfarlanes.com "
        })
  
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
    user-select:none;
    font-weight: bolder;
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title2 {
    color: black;
    opacity: 0.8;
    font-size: 2.5em;
    user-select:none;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title3 {
    color: black;
    opacity: 0.8;
    font-size: 1.5em;
    user-select:none;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .search {
    opacity: 0.7;
  }
  
  .desc {
    background-color: #fff;
    opacity: 0.7;
    min-height: 65em;
    margin: 3em 6em 0em 6em;
    border-radius: 4px;
  }
</style>
