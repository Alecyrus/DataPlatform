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
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="center" style="margin-top:2em;" offset="3">
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
  
          <Col span="12" align="center">
  
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="6" align="left" style="margin-top:2em;" offset="0">
            <p class="title2">证书列表</p>
            </Col>
          </Row>
  
          <Row type="flex" align="middle" justify="start" style="margin-top:1em;margin-bottom:5em">
            <Col span="24" align="left">
            <p style="font-size:1.4em;"><i><strong>SpringX</strong></i> 是一个互联网公钥基础设施信息检索系统。
              <br>系统对整个互联网(目前主要针对中国)的互联网公钥基础设施(Public Key Infrastructure)信息进行了全面的收集维护。<br>为研究者和普通用户提供信息检索和数据分析服务.</p>
            </Col>
          </Row>
  
  
          </Col>
  
  
  
  
          <Col span="6" align="center">
  
          <Row type="flex" align="middle" justify="center" style="margin-top:4em;">
            <Col span="14" align="center" style="margin-top:2em;" offset="2">
  
            <Input v-model="searchKeyword" style="box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .02);" placeholder="Enter something..."></Input>
  
  
            </Col>
            <Col span="7" align="left" style="margin-top:2em;" offset="1">
  
            <Button type="ghost" style="opacity:0.9;box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .02);" class="shadow" size="normal" shape="circle" icon="ios-search" @click="search"> Search</Button>
  
  
            </Col>
          </Row>
  
          <hr style="height:1px;border:none;border-top:1px solid #555555;
                                          margin:4em 0em 1em 0em;
                                          width:80%;opacity:0.5;
                                          border-radius:1px;
                                          box-shadow: 0px 4px 16px 0px rgba(255, 255, 0, .1), 0px 0px 8px 0px rgba(0, 0, 0, .5);
                                          " />
  
          <Row type="flex" align="top" justify="center" style="margin-top:0em;">
            <Col span="20" align="center" style="margin-top:2em;" offset="1">
            <p class="title2"><i></i></p>
            </Col>
          </Row>
  
  
  
  
          <Row type="flex" align="middle" justify="center" style="margin-top:1em;margin-bottom:5em">
            <Col span="20" align="center">
            <Card class="smmary" style="width:320px">
              <div style="text-align:center">

                 <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                  <Col span="22" align="center" style="margin-top:3em;" offset="1">
                  <p style="font-size:1.2em"><Icon type="ios-pricetags-outline"></Icon> 关联数据<strong> 12120 </strong>条</p>
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
                  <p style="font-size:1.2em"><Icon type="lock-combination"></Icon> 端证书<strong> 1000 </strong>条</p>
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
                     <p style="font-size:1.2em"><Icon type="android-time"></Icon> 检索用时<strong> 0.23 </strong>s</p>
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
      }
    },
    mounted() {
      console.log(this.$route.query);
      this.searchKeyword = this.$route.query.keywords;
      this.$Message.info(this.searchKeyword)
  
    },
    methods: {
      search() {
  
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
    font-weight: bolder;
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title2 {
    color: black;
    opacity: 0.8;
    font-size: 2.5em;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .title3 {
    color: black;
    opacity: 0.8;
    font-size: 1.5em;
    /* font-weight: bolder; */
    text-shadow: black 0.1em 0.1em 1.5em;
  }
  
  .search {
    opacity: 0.7;
  }
  
  .desc {
    background-color: #fff;
    opacity: 0.7;
    min-height: 62em;
    margin: 3em 6em 0em 6em;
    border-radius: 4px;
  }
</style>
