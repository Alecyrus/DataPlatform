<template>
  <div>
  
  
    <section style="margin-top:4em;">
  
      <Row type="flex" justify="start">
        <Col span="12" align="left" offset="2">
        <p class="titlewords">证书详情</p>
        </Col>
      </Row>
  
  
  
  
  
  
  
    </section>
  
  
  
  
  
    <section>
  
      <div class="desc">
  
  
        <Row type="flex" align="top" justify="start" style="margin-top:1em;">
  
          <transition name="fadeUp" appear>
  
            <Col span="5" align="center" offset="0">
  
  
            <Row type="flex" align="middle" justify="start" style="margin-top:1em;">
              <Col span="14" align="left" style="margin-top:1em;" offset="2">
  
              <Breadcrumb>
                <BreadcrumbItem to="/">首页</BreadcrumbItem>
                <BreadcrumbItem to="/results">检索结果</BreadcrumbItem>
                <BreadcrumbItem to="/certificate">证书详情</BreadcrumbItem>
  
              </Breadcrumb>
  
              </Col>
  
            </Row>
  
            <Row type="flex" align="top" justify="start" style="margin-top:0em;">
              <Col span="8" align="center" style="margin-top:3em;" offset="4">
              <p class="title2">{{i_title}}</p>
              </Col>
            </Row>
            <Row type="flex" align="top" justify="start" style="margin-top:0em;">
              <Col span="12" align="left" style="margin-top:4em;" offset="6">
  
              <Menu @on-select="handleMenu" :open-names="['1']" :active-name="1-1" accordion>
                <Submenu name="1">
                  <template slot="title">
                                             <awe-icon name="certificate"  scale="0.8" ></awe-icon>
                                                    &nbsp;&nbsp;证书
</template>
                    <MenuItem name="smmary">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;总结</MenuItem>
                    <MenuItem name="openssl">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open SSL</MenuItem>
                    <MenuItem name="asn1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ASN.1</MenuItem>
                </Submenu>
                <Submenu name="2">
<template slot="title">
  <awe-icon name="lock" scale="0.8">
  </awe-icon>
  &nbsp;&nbsp;授信
</template>
                    <MenuItem name="apple">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/apple"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Apple</MenuItem>
                    <MenuItem name="microsoft">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/microsoft"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Microsoft</MenuItem>
                    <MenuItem name="mozillanss">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/firefox"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Mozilla NSS</MenuItem>
                    <MenuItem name="googlect">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/google"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Google CT</MenuItem>
                </Submenu>
                <!-- <Submenu name="3"> -->

                  

                  <MenuItem name="rawdata"> <awe-icon name="terminal" scale="0.8">  </awe-icon>&nbsp;&nbsp;&nbsp;数据</MenuItem>
<!-- <template slot="title">
  <awe-icon name="database" scale="0.8">
  </awe-icon>
  &nbsp;&nbsp;数据
</template>
                    <MenuItem name="raw">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RAW</MenuItem>
                    <MenuItem name="json">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JSON</MenuItem>
                    <MenuItem name="pem">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PEM</MenuItem>
                    <MenuItem name="der">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DER</MenuItem>
                </Submenu> -->

                 <Submenu name="3">
<template slot="title">
  <awe-icon name="search" scale="0.8">
  
  </awe-icon>
  &nbsp;&nbsp;探索
</template>
                     <MenuItem name="certifiau">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CA 机构</MenuItem>
                     <MenuGroup  align="left" title="相关证书">
                        <MenuItem  name="sameseri">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相同序列号</MenuItem>
                        <MenuItem name="samepk">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相同公钥</MenuItem>
                        <MenuItem name="samecn">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相同标识名称</MenuItem>
                    </MenuGroup>
                    <MenuGroup title="谁在使用这个证书？">
                        <MenuItem name="domains">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;域名</MenuItem>
                        <MenuItem name="ipv4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPv4 地址</MenuItem>
                    </MenuGroup>
                </Submenu>
            </Menu>
              </Col>
            </Row>
  
          
  
  
  
  
  
            </Col>
  
  
          </transition>
  
          <Col span="19" align="left" style="">
  
          

           
  
            <Row type="flex" align="top" justify="start" style="margin-top:0em;">
              <Col span="6" align="left" style="margin-top:2em;margin-bottom:0em" offset="0">
              <transition name="fadeUp" appear>
              <p class="title2">{{contentTitle}}</p>
                 </transition>
              </Col>
            </Row>


          

            

                <Scroll height="680" >
                   <transition name="fade" mode="out-in">
                 <router-view></router-view>
                   </transition>
               </Scroll>
                
           


            
  
  
         
  

          
  
  
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
        contentTitle: "",
      
        titleMap: {
          smmary: "总结",
          openssl: "Open SSL",
          asn1: "ASN.1",
          apple: "Apple",
          microsoft: "Microsoft",
          mozillanss: "Mozilla NSS",
          googlect: "Google CT",
          rawdata:"数据",
          raw: "RAW",
          json: "JSON",
          pem: "PEM",
          der: "DER",
          certifiau: "CA 机构",
          domains: "域名",
          ipv4: "IPv4 地址",
  
        },

  
      }
    },
    created() {

      this.cert = this.$ls.get("selectedCert");
      //console.log(this.cert)
     
  
    },
    computed:{
         i_title() {
          let id = this.cert._id.$oid
          if (id.length > 12){
            return id.substr(0,6) + "....." + id.substr(id.length-6);
          } else {
            return id
          }

      }
    },
    methods: {
      handleMenu() {

        this.contentTitle = eval("this.titleMap." + arguments[0])
        if(arguments[0] == "smmary") {
          this.$router.push("/certificate");
        } else {
            this.$router.push("/certificate/"+arguments[0])
        }
        
      }
    },

  
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

$animationDuration: 0.4s; // specify animation duration. Default value: 1s
@import "vue2-animate/src/sass/vue2-animate.scss";
  .cert {
    transition: all ease-in-out 0.4s;
  }
  
  .cert:hover {
    
  }
  
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
  
  .search {
    opacity: 0.7;
  }
  
  .desc {
    background-color: #fff;
    opacity: 0.7;
    min-height: 65em;
    margin: 2em 6em 0em 6em;
    border-radius: 4px;
  }
</style>
