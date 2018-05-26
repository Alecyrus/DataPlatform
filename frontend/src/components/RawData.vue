<template>
    <div>
    
        <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
    
    
    
            <Col span="18" align="left" style="margin-top:0em;margin-left:1em;background-color:;" offset="0">
    
    
            <Tabs @on-click="getactive" :value="textshow">
                <TabPane   @ label="RAW JSON" name="raw">
    
    
                    <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
                        <Col span="22" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
                        <Scroll height="600">
                            <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
                                <Col span="22" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
    
    
                                <pre>{{rawJson}}
                                    </pre>
    
                                </Col>
    
                            </Row>
    
                        </Scroll>
    
                        </Col>
    
    
    
                    </Row>
    
                </TabPane>
                <TabPane label="PEM" name="pem">

                        <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
                        <Col span="22" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
                        <Scroll height="600">
                            <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
                                <Col span="22" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
                                    <pre>{{rawPEM}}</pre>
                                </Col>
    
                            </Row>
    
                        </Scroll>
    
                        </Col>
    
    
    
                    </Row>
                </TabPane>
               
            </Tabs>
    
    
    
    
    
    
            </Col>
    
    
            <Col span="4" align="center">
    
            <Row type="flex" align="top" justify="start" style="margin-top:2em;">
                <Col span="24" align="center" style="margin-top:2em;margin-bottom:0em" offset="0">
    
                <Tooltip content="下载" placement="right">
                    <Button type="ghost" shape="circle" @click="downloadfile" size="large"><awe-icon name="download"  scale="1.3" ></awe-icon></Button>
                </Tooltip>
    
                </Col>
    
            </Row>
    
            <Row type="flex" align="top" justify="start" style="margin-top:0em;">
                <Col span="24" align="center" style="margin-top:1em;margin-bottom:0em" offset="0">
    
                <Tooltip content="复制" placement="right">
                    <Button type="ghost" v-clipboard:copy="copyContent" v-clipboard:success="onCopy" v-clipboard:error="onError" shape="circle" size="large"><awe-icon name="regular/copy"  scale="1.3" ></awe-icon></Button>
                </Tooltip>
    
                </Col>
    
            </Row>
    
    
    
    
    
    
            </Col>
    
    
        </Row>
    
    
    </div>
</template>

<script>

    import filesaver from "../FileSaver.js"
    export default {
        data() {
            return {
                t1: '探寻和分析',
                textshow: "raw",
                rawJson1: {}
                ,
                loading: true,
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
        created() {
             this.rawJson1 = this.$ls.get("selectedCert");
    
        },
        computed: {
            rawJson() {
    
                return JSON.stringify(this.rawJson1, null, 2);
            },
            rawPEM() {
                return "-----BEGIN CERTIFICATE-----\n"+this.rawJson1.raw.$binary+"\n-----END CERTIFICATE-----";
            },
            copyContent() {

                if (this.textshow == "raw") {
                    return this.rawJson;
                } else if (this.textshow == "pem") {
                    return this.rawPEM;
                } else {
                    return ""
                }

            }
        },
        methods: {
            getactive() {
                this.textshow = arguments[0];
            },
            search() {
    
            },
            onCopy: function(e) {
                this.$toast.success('已复制到剪切板', 'Info', {
                    position: 'topCenter'
                }, );
            },
            onError: function(e) {
                alert('Failed to copy texts')
            },
            downloadfile() {
                if (this.textshow == "raw") {
                    var file = new File([this.copyContent], "certificate.json", { type: "text/json;charset=utf-8" });
                    filesaver.saveAs(file);
                } else if (this.textshow == "pem")  {
                     var file = new File([this.copyContent], "certificate.crt", { type: "application/x-x509-ca-cert;charset=utf-8" });
                     filesaver.saveAs(file);
                } 
            }


                
                
        },
        components: {
    
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    /* .backgroundac {
              transition: all ease-in-out 0.6s;
              filter: blur(15px);
            }
            
            .backgroundacde {
              filter: blur(0px);
              transition: all ease-in-out 0.6s;
            } */
    
    pre {
        white-space: pre-wrap;
        white-space: -moz-pre-wrap;
        white-space: -pre-wrap;
        white-space: -o-pre-wrap;
        word-wrap: break-word;
        /* text-shadow: black 0.1em 0.1em 5em; */
    }
    
    .trust {
        color: green;
        opacity: 0.8;
        font-size: 1.0em;
        user-select: none;
        /* font-weight: bolder; */
        text-shadow: black 0.1em 0.1em 2em;
    }
    
    .brands {
        color: black;
        opacity: 0.8;
        font-size: 1.0em;
        user-select: none;
        font-weight: bolder;
        text-shadow: black 0.1em 0.1em 2em;
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
        text-shadow: black 0.1em 0.1em 1.5em;
    }
    
    .title3 {
        color: #222;
        opacity: 0.8;
        user-select: none;
        font-size: 1.0em;
        font-family: Helvetica;
        text-shadow: black 0.1em 0.1em 2em;
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
    
    .box {
        box-shadow: 0 0 4pt rgba(0, 0, 0, 0.25);
        border-radius: 20pt;
        background-color: rgba(255, 255, 255, 0.25);
        user-select: none;
        cursor: context-menu;
        z-index: 99999;
    }
</style>
