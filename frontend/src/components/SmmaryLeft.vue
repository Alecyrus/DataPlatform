<template>
  <div>
  
    <section>
  
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
        <p class="title3">{{getIssuer(cert)}}</p>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">使用者 DN</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{getSubject(cert)}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">序列号</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{parseInt(cert.serialnumber).toString(16)}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">有效期</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{getDate(cert)}}</p>
        </Col>
      </Row>
      <Row v-if="hassan(cert)" type="flex" align="top" justify="start" style="margin-top:0.5em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">名称</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <Scroll height="50">
          <Button @click="toName(item)" type="text" v-for="(item, index) in namelist" :key="index"><p style="text-shadow: grey 0.1em 0.1em 2em;">{{item}}</p></Button>
        </Scroll>
  
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
        <p class="title3">{{cert.fingerprint.md5}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">SHA1</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.fingerprint.sha1}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">SHA256</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.fingerprint.sha256}}</p>
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
        <p class="title3">{{cert.publickeyalgorithm}}</p>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Binary</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3" style="word-break:break-all;">{{cert.publickey.$binary}}</p>
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
        <p class="title3">{{cert.signaturealgorithm}}</p>
        </Col>
      </Row>
      <Row type="flex" align="top" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Binary</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3" style="word-break:break-all;">{{cert.signaturegg.$binary}}</p>
        </Col>
      </Row>
  
      <Row type="flex" align="top" justify="start" style="margin-top:0em;">
        <Col span="6" align="left" style="margin-top:2em;margin-bottom:0em" offset="0">
        <p class="title1">扩展</p>
        </Col>
      </Row>
      <Row v-if="cert.extensions.authoritykeyidentifier.$binary" type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Auth Key ID</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.extensions.authoritykeyidentifier.$binary}}</p>
        </Col>
      </Row>
      <Row  v-if="cert.extensions.subjectkeyidentifier.$binary" type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="4" align="right" style="margin-bottom:0em" offset="0">
        <p class="title2">Subject Key ID</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.extensions.subjectkeyidentifier.$binary}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="4" align="right" style="margin-bottom:0em" offset="0">
        <p class="title2">Key Usage</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.extensions.keyusage.join(', ')}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="4" align="right" style="margin-bottom:0em" offset="0">
        <p class="title2">Ext. Key Usage</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.extensions.extendedkeyusage.join(', ')}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">CRL Paths</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.extensions.crldistributionpoints.join(', ')}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Policies</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{cert.extensions.policyidentifiers.join(', ')}}</p>
        </Col>
      </Row>
      <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
        <Col span="3" align="right" style="margin-bottom:0em" offset="1">
        <p class="title2">Constraints</p>
        </Col>
        <Col span="19" align="left" style="margin-bottom:0em" offset="0">
        <p class="title3">{{getConstrains(cert.extensions.basicconstraints)}} </p>
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
      <Row v-if="hassan(cert)" type="flex" align="top" justify="start" style="margin-top:1em;">
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
        cert: {},
  
      }
  
    },
    created() {
      this.cert = this.$ls.get("selectedCert");
      console.log(this.cert.notbefore.$date);
      console.log(this.cert.extensions.subjectalternativename.dnsnames.length);
    },
    computed: {
      namelist() {
        return this.cert.extensions.subjectalternativename.dnsnames
      }
    },
    methods: {
      search() {
  
      },
      toName(item) {
        this.$router.push("/results?keywords=" + item);
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
      hassan(cert) {
        return cert.extensions.subjectalternativename.dnsnames.length
      },
      getDate(cert) {
  
        let res = ""
        let a = new Date(cert.notbefore.$date)
        // console.log(a.toDateString()) 
        let b = new Date(cert.notafter.$date)
        // console.log(a.toDateString()) 
  
        return a.toDateString() + "  -  " + b.toDateString()
      },
      getSubject(cert) {
        //console.log(cert)
        let res = ""
        if (cert.subject.c.length != 0) {
          res += "C=" + cert.subject.c[0]
        }
  
        if (cert.subject.l.length != 0) {
          res += ", L=" + cert.subject.l[0]
        }
        if (cert.subject.o.length != 0) {
          res += ", O=" + cert.subject.o[0]
        }
        if (cert.subject.ou.length != 0) {
          res += ", OU=" + cert.subject.ou[0]
        }
        if (cert.subject.cn.length != 0) {
          res += ", CN=" + cert.subject.cn[0]
        }
        if (cert.subject.p.length != 0) {
          res += ", Province=" + cert.subject.p[0]
        }
        return res
      },
      getIssuer(cert) {
        //console.log(cert)
        let res = ""
        if (cert.issuer.c.length != 0) {
          res += "C=" + cert.issuer.c[0]
        }
  
        if (cert.issuer.l.length != 0) {
          res += ", L=" + cert.issuer.l[0]
        }
        if (cert.issuer.o.length != 0) {
          res += ", O=" + cert.issuer.o[0]
        }
        if (cert.issuer.ou.length != 0) {
          res += ", OU=" + cert.issuer.ou[0]
        }
        if (cert.issuer.cn.length != 0) {
          res += ", CN=" + cert.issuer.cn[0]
        }
        if (cert.issuer.p.length != 0) {
          res += ", Province=" + cert.issuer.p[0]
        }
        return res
      },
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
    /* text-shadow: black 0.1em 0.1em 1.5em; */
  }
  
  .title3 {
    color: #222;
    opacity: 0.8;
    user-select: none;
    font-size: 1.2em;
    font-family: Helvetica;
    /* text-shadow: black 0.1em 0.1em 1.5em; */
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
