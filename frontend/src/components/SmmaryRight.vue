<template>
  <div>
  
    <section>
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="center" style="margin-top:1em;margin-bottom:0em" offset="2">
  
  
  
  
        <Card class="smmary" style="width:320px">
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="20" align="left" style="margin-bottom:0em" offset="0">
            <p class="rightTitle">浏览器信任状态</p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:1em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">Safafi</p>
            </Col>
            <Col span="14" align="left" style="margin-bottom:0em" offset="0">
  
        
                   <p class="trust" style="color:green" v-if="getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="green"> </awe-icon>&nbsp;{{getTrustStatus(cert.trust.apple_macos)}}</p>
            <p class="trust"  style="color:red" v-if="!getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="red"> </awe-icon> &nbsp;{{getTrustStatus(cert.trust.apple_macos)}}</p>

            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">Chrome</p>
            </Col>
            <Col span="14" align="left" style="margin-bottom:0em" offset="0">
  
         

               <p class="trust" style="color:green" v-if="getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="green"> </awe-icon>&nbsp;{{getTrustStatus(cert.trust.google_aosp)}}</p>
            <p class="trust"  style="color:red" v-if="!getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="red"> </awe-icon> &nbsp;{{getTrustStatus(cert.trust.google_aosp)}}</p>

            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">Firefox</p>
            </Col>
            <Col span="14" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="trust" style="color:green" v-if="getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="green"> </awe-icon>&nbsp;{{getTrustStatus(cert.trust.mozilla_nss)}}</p>
            <p class="trust"  style="color:red" v-if="!getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="red"> </awe-icon> &nbsp;{{getTrustStatus(cert.trust.mozilla_nss)}}</p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">Edge</p>
            </Col>
            <Col span="14" align="left" style="margin-bottom:0em" offset="0">
  
                   <p class="trust" style="color:green" v-if="getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="green"> </awe-icon>&nbsp;{{getTrustStatus(cert.trust.microsoft_windows)}}</p>
            <p class="trust"  style="color:red" v-if="!getTrust(cert.trust.mozilla_nss)">&nbsp;&nbsp;
              <awe-icon name="lock"  scale="0.8" color="red"> </awe-icon> &nbsp;{{getTrustStatus(cert.trust.microsoft_windows)}}</p>

            </Col>
          </Row>
        </Card>
        </Col>
      </Row>
  
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="center" style="margin-top:2em;margin-bottom:0em" offset="2">
  
        <Card class="smmary" style="width:320px">
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="20" align="left" style="margin-bottom:0em" offset="0">
            <p class="rightTitle">密钥用途 &nbsp;
              <Icon type="android-attach"></Icon> &nbsp;基本约束</p>
            </Col>
          </Row>
          <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">密钥用途</p>
            </Col>
            <Col span="14" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">{{cert.extensions.keyusage.join(', ')}}</p>
            </Col>
          </Row>
          <Row type="flex" align="middle" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">额外密钥用途</p>
            </Col>
            <Col span="14" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">{{cert.extensions.extendedkeyusage.join(', ')}}</p>
            </Col>
          </Row>
          <Row type="flex" align="middle" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">约束条件</p>
            </Col>
            <Col span="14" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">{{getConstrains(cert.extensions.basicconstraints)}}</p>
            </Col>
          </Row>
        </Card>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="center" style="margin-top:2em;margin-bottom:0em" offset="2">
  
        <Card class="smmary" style="width:320px">
  
          <Row type="flex" align="top" justify="start" style="margin-top:0em;">
            <Col span="20" align="left" style="margin-bottom:0em" offset="0">
            <p class="rightTitle"><i>SpringX</i> 元信息</p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:1em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">标签</p>
            </Col>
            <Col span="16" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">
              <Tag>
                <Icon type="pricetag"></Icon> Unexpired</Tag>
              <Tag>
                <Icon type="pricetag"></Icon> Trusted</Tag>
              <Tag>
                <Icon type="pricetag"></Icon> Root</Tag>
            </p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">数据来源</p>
            </Col>
            <Col span="12" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">HTTPS信息采集 </p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">扫描可见</p>
            </Col>
            <Col span="12" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">True </p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">添加时间</p>
            </Col>
            <Col span="12" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">2017-09-22 18:40:13</p>
            </Col>
          </Row>
          <Row type="flex" align="top" justify="start" style="margin-top:0.2em;">
            <Col span="8" align="right" style="margin-bottom:0em" offset="0">
            <p class="brands">更新时间</p>
            </Col>
            <Col span="12" align="left" style="margin-bottom:0em" offset="0">
  
            <p class="title3">2017-12-13 22:07:37</p>
            </Col>
          </Row>
  
        </Card>
        </Col>
      </Row>
  
  
  
  
  
  
  
    </section>
  
  
  
  </div>
</template>

<script>
  export default {
    data() {
      return {
        t1: '探寻和分析',
        cert:{},
  
      }
  
    },
    created() {
      this.cert = this.$ls.get("selectedCert");
      //console.log(this.cert.notbefore.$date);
      //console.log(this.cert.extensions.subjectalternativename.dnsnames.length);
    },
    methods: {
      getTrustStatus(status) {
        if (status == "Included") {
          return "Browser Trusted"
        }
        if (status == "Not Include") {
          return "Browser Untrusted"
        }
  
  
      },
       getConstrains(con) {
        let res = "";
        if (con.isca) {
          res += "Is CA: True, "
        } else {
          res += "Is CA: False, "
        }
        if (con.maxpathlenzero) {
          res += "MaxPathlenZero: True, "
        } else {
          res += "MaxPathlenZero: False, "
        }
  
        res += "MaxPathlen: " + con.maxpathlen

        return res
  
      },
       getTrust(status) {
        if (status == "Included") {
          return true
        }
        if (status == "Not Include") {
          return false
        }
  
  
      },
  
  
      toName(item) {
        this.$router.push("/results?keywords=" + item);
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .trust {
  
    opacity: 0.8;
    font-size: 1.0em;
    user-select: none;
    /* font-weight: bolder; */
    /* text-shadow: black 0.1em 0.1em 2em; */
  }
  
  .brands {
    color: black;
    opacity: 0.8;
    font-size: 1.0em;
    user-select: none;
    font-weight: bolder;
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
    /* text-shadow: black 0.1em 0.1em 1.5em; */
  }
  
  .title3 {
    color: #222;
    opacity: 0.8;
    user-select: none;
    font-size: 1.0em;
    font-family: Helvetica;
    /* text-shadow: black 0.1em 0.1em 2em; */
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
