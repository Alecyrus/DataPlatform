<template>
  <div>
  
    <section style="margin-top:16em;">
  
      <Row type="flex" justify="start">
        <Col span="12" align="left" offset="5">
        <p class="titlewords">{{t1}}</p>
        </Col>
      </Row>
      <Row type="flex" justify="start">
        <Col span="12" align="left" offset="5">
        <p class="titlewords">{{t2}}</p>
        </Col>
      </Row>
      <Row type="flex" justify="start">
        <Col span="12" align="left" offset="5">
        <p class="titlewords">{{t3}}</p>
        </Col>
      </Row>
  
  
      <Row type="flex" align="middle" justify="start" style="margin-top:3em;">
        <Col span="8" align="left" offset="5">
        <input autocomplete="off" spellcheck="false" type="text" placeholder="输入IPv4地址或域名字符串" class="ivu-input shadow search ivu-input-large">
        </input>
        </Col>
  
        <Col span="2" align="center">
        <Button type="primary" style="opacity:0.8;" class="shadow" size="large" shape="circle" icon="ios-search">  Search</Button>
        </Col>
      </Row>
    </section>
  
  
  
  
  
    <section>
  
      <div class="desc">
  
  
        <Carousel autoplay :autoplay-speed="2000" :radius-dot="1" loop> 
          <CarouselItem>
            <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
              <Col span="6" align="center" offset="6">
              <Icon size="160" type="earth"></Icon>
              </Col>
  
              <Col span="12" align="center">
  
              <Row type="flex" align="middle" justify="start" style="margin-top:4em;">
                <Col span="8" align="left">
                <p style="font-size:2.8em;">什么是 <i><strong>SpringX</strong></i> </p>
                </Col>
              </Row>
  
              <Row type="flex" align="middle" justify="start" style="margin-top:1em;margin-bottom:5em">
                <Col span="12" align="left">
                <p style="font-size:1.4em;"><i><strong>SpringX</strong></i> 是一个互联网公钥基础设施信息检索系统。
                  <br>系统对整个互联网(目前主要针对中国)的互联网公钥基础设施(Public Key Infrastructure)信息进行了全面的收集维护。<br>为研究者和普通用户提供信息检索和数据分析服务.</p>
                </Col>
              </Row>
  
  
              </Col>
            </Row>
          </CarouselItem>
          <CarouselItem  >
            <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
              <Col span="6" align="center" offset="6">
              <Icon size="160" type="cube"></Icon>
              </Col>
  
              <Col span="12" align="center">
  
              <Row type="flex" align="middle" justify="start" style="margin-top:4em;">
                <Col span="8" align="left">
                <p style="font-size:2.8em;"><i><strong>SpringX</strong></i>的能力 </p>
                </Col>
              </Row>
  
              <Row type="flex" align="middle" justify="start" style="margin-top:1em;margin-bottom:5em">
                <Col span="12" align="left">
                <p style="font-size:1.4em;"><i><strong>SpringX</strong></i> 是一个互联网公钥基础设施信息检索系统。
                  <br>系统对整个互联网(目前主要针对中国)的互联网公钥基础设施(Public Key Infrastructure)信息进行了全面的收集维护。<br>为研究者和普通用户提供信息检索和数据分析服务.</p>
                </Col>
              </Row>
  
  
              </Col>
            </Row>
          </CarouselItem>
        </Carousel>
  
  
  
      </div>
  
    </section>
  
  
  
  
  
  
  
  
  
  
  
  
  </div>
</template>

<script>
  export default {
    data() {
      return {
        t1: '探寻和分析',
        t2: '庞大的互联网公钥基础设施',
        t3: '的每一个角落',
        desc: "",
        search: "",
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  input.ivu-input.ivu-input-large {
    height: 3.4em;
    width: 100%;
  }
  
  .titlewords {
    color: white;
    opacity: 0.8;
    font-size: 3.8em;
    font-weight: bolder;
  }
  
  .search {
    opacity: 0.7;
  }
  
  .desc {
    background-color: #fff;
    opacity: 0.6;
    margin: 14em 0.8em 0em 0.8em;
    border-radius: 4px;
  }
</style>
