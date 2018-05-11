<template>
  <div>

    <section >
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="left" style="margin-top:2em;margin-bottom:0em" offset="0">
        <p class="title1">基本信息</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">颁发者 DN</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">OU=Domain Control Validated, OU=PositiveSSL Multi-Domain, CN=www.163-baidu-360.com</p>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">使用者 DN</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">C=GB, ST=Greater Manchester, L=Salford, O=COMODO CA Limited, CN=COMODO RSA Domain Validation Secure Server CA</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">序列号</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">213890377560961246190995359282626776192</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">有效期</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">213890377560961246190995359282626776192</p>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">名称</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
  
  
        <Button @click="toName(item)" type="text" v-for="(item, index) in namelist" :key="index"><p style="text-shadow: grey 0.1em 0.1em 2em;">{{item}}</p></Button>
        </Col>
      </Row>
  
  
  
  
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="left" style="margin-top:1em;margin-bottom:0em" offset="0">
        <p class="title1">指纹</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">MD5</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">3f1dcc7e6ec2b14a23771afae6709e5c</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">SHA1</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">70cd67f9995b3f083025dc798ebed30c98acd15d</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">SHA256</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">41a40e29c1e29e27e7b865327f0413bce5866983c902cf8377bd3348a782a873</p>
        </Col>
      </Row>
  
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="left" style="margin-top:2em;margin-bottom:0em" offset="0">
        <p class="title1">公钥</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">算法</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">SHA-256</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Binary</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">41a40e29c1e29e27e7b865327f0413bce5866983c902cf8377bd3348a782a873</p>
        </Col>
      </Row>
  
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="left" style="margin-top:2em;margin-bottom:0em" offset="0">
        <p class="title1">签名</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">算法</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">SHA-256</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Binary</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">41a40e29c1e29e27e7b865327f0413bce5866983c902cf8377bd3348a782a873</p>
        </Col>
      </Row>
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="left" style="margin-top:2em;margin-bottom:0em" offset="0">
        <p class="title1">扩展</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Auth Key ID</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">90af6a3a945a0bd890ea125673df43b43a28dae7</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="4" align="right" style="margin-bottom:0em" offset="0">
        <p class="title2">Subject Key ID</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">a7ded86972a1660856d5314310fc64467241dbef</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="4" align="right" style="margin-bottom:0em" offset="0">
        <p class="title2">Key Usage</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">Digital Signature, Key Encipherment</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="4" align="right" style="margin-bottom:0em" offset="0">
        <p class="title2">Ext. Key Usage</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">Client Auth, Server Auth</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">CRL Paths</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">http://crl.comodoca.com/COMODORSADomainValidationSecureServerCA.crl</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Policies</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">Comodo TLS DV (1.3.6.1.4.1.6449.1.2.2.7) CA/B Forum Domain Validated (2.23.140.1.2.1)</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Constraints</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">Is CA: False </p>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">AIA Paths</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">OCSP: http://ocsp.comodoca.com</p>
        <p class="title3">Issuer: http://crt.comodoca.com/COMODORSADomainValidationSecureServerCA.crt</p>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">SANs</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <Button @click="toName(item)" type="text" v-for="(item, index) in namelist" :key="index"><p style="text-shadow: grey 0.1em 0.1em 2em;">{{item}}</p></Button>
        </Col>
        </Col>
      </Row>
  
  
  
  
  
  
  
  </section>
  
  
  
  </div>
</template>

<script>
  export default {
    data() {
      return {
        loading: true,
        t1: '探寻和分析',
        namelist: ["www.123.com",
          "www.ba324idu.com",
          "www.bai234du.com",
          "www.bai123du.com",
          "www.baidu.com",
          "www.baidu.com",
          "www.baidu.com",
          "www.baidu.com",
          "www.baidu.com",
          "www.baidu.com"
        ]
      }
  
    },
    methods: {
      search() {
  
      },
      toName(item) {
        this.$router.push("/results?keywords=" + item);
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>



  
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
    font-size: 1.2em;
    font-family: Helvetica;
    text-shadow: black 0.1em 0.1em 1.5em;
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
