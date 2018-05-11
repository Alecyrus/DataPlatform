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
            <Col span="6" align="center" offset="0">
  
  
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
              <p class="title2">www.baidu.com</p>
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
                    <MenuItem name="t11">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;总结</MenuItem>
                    <MenuItem name="t12">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open SSL</MenuItem>
                    <MenuItem name="t13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ASN.1</MenuItem>
                </Submenu>
                <Submenu name="2">
<template slot="title">
  <awe-icon name="lock" scale="0.8">
  </awe-icon>
  &nbsp;&nbsp;授信
</template>
                    <MenuItem name="t21">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/apple"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Apple</MenuItem>
                    <MenuItem name="t22">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/windows"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Microsoft</MenuItem>
                    <MenuItem name="t23">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/firefox"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Mozilla NSS</MenuItem>
                    <MenuItem name="t24">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<awe-icon name="brands/google"  scale="0.8" ></awe-icon>&nbsp;&nbsp;Google CT</MenuItem>
                </Submenu>
                <Submenu name="3">
<template slot="title">
  <awe-icon name="database" scale="0.8">
  </awe-icon>
  &nbsp;&nbsp;数据
</template>
                    <MenuItem name="t31">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RAW</MenuItem>
                    <MenuItem name="t32">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JSON</MenuItem>
                    <MenuItem name="t33">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PEM</MenuItem>
                    <MenuItem name="t34">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DER</MenuItem>
                </Submenu>

                 <Submenu name="3">
<template slot="title">
  <awe-icon name="search" scale="0.8">
  
  </awe-icon>
  &nbsp;&nbsp;探索
</template>
                     <MenuItem name="t41">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CA 机构</MenuItem>
                     <MenuGroup  align="left" title="相关证书">
                        <MenuItem  name="t42">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相同序列号</MenuItem>
                        <MenuItem name="t43">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相同公钥</MenuItem>
                        <MenuItem name="t44">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相同标识名称</MenuItem>
                    </MenuGroup>
                    <MenuGroup title="谁在使用这个证书？">
                        <MenuItem name="t45">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;域名</MenuItem>
                        <MenuItem name="t46">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPv4 地址</MenuItem>
                    </MenuGroup>
                </Submenu>
            </Menu>




              </Col>
            </Row>
  
          
  
  
  
  
  
            </Col>
  
          </transition>
  
          <Col span="12" align="left" style="background-color:#bbb">
  
          <transition name="fadeUp" appear>
  
            <Row type="flex" align="top" justify="start" style="margin-top:0em;">
              <Col span="6" align="left" style="margin-top:2em;margin-bottom:2em" offset="0">
              <p class="title2">{{contentTitle}}</p>
              </Col>
            </Row>
  
  
          </transition>
  

          
  
  
          </Col>
  
  
          <transition name="fadeUp" appear>
  
          <Col span="6" align="center" style="background-color:#aaa">
  

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
  export default {
    data() {
      return {
        desc: "",
        contentTitle: "总结",
        titleMap:{
          t11:"总结",
          t12:"Open SSL",
          t13:"ANC.1",
          t21:"Apple",
          t22:"Microsoft",
          t23:"Mozilla NSS",
          t24:"Google CT",
          t31:"RAW",
          t32:"JSON",
          t33:"PEM",
          t34:"DER",
          t41:"CA 机构",
          t42:"相同序列号",
          t43:"相同公钥",
          t44:"相同标识名称",
          t45:"域名",
          t46:"IPv4 地址",

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
        },
      }
    },
    mounted() {
  
  
  
    },
    methods: {
      handleMenu() {
        this.$toast.success('' + arguments[0], 'Info', this.notificationSystem.options.success);
        this.contentTitle = eval("this.titleMap."+arguments[0])
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .cert {
    transition: all ease-in-out 0.4s;
  }
  
  .cert:hover {}
  
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
