<template>
    <div>
    
        <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
    
    
    
            <Col span="16" align="left" style="margin-top:0em;margin-left:1em;background-color:;" offset="2">
    
            <Scroll height="600">
                <Button @click="toName(item)" type="text" v-for="(item, index) in namelist" :key="index"><p style="text-shadow: grey 0.1em 0.1em 2em;">{{item}}</p></Button>
            </Scroll>
    
    
    
    
            </Col>
    
    
            <Col span="6" align="right">
    
            <Row type="flex" align="middle" justify="center" style="margin-top:2em;margin-bottom:4em">
                <Col span="20" align="center">
                <Card class="smmary" style="width:200px">
                    <div style="text-align:center">
    
                        <Row type="flex" align="top" justify="center" style="margin-top:0em;">
                            <Col span="22" align="center" style="margin-top:2em;" offset="1">
                            <p style="font-size:1.2em">
                                <Icon type="ios-pricetags-outline"></Icon> 关联数据<strong> {{namelist.length}} </strong>条</p>
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
    
                    </div>
                </Card>
                </Col>
            </Row>
    
    
    
            </Col>
    
    
        </Row>
    
    
    </div>
</template>

<script>
    export default {
        data() {
            return {
                t1: '探寻和分析',
                textshow: "raw",
                cert: {},
                // loading: true,
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
            this.cert = this.$ls.get("selectedCert");
    
        },
        computed: {
            namelist() {
                return this.cert.extensions.subjectalternativename.dnsnames
            },
    
        },
        methods: {
            randomFrom(lowerValue, upperValue) {
                return Math.floor(Math.random() * (upperValue - lowerValue + 1) + lowerValue);
            },
            toName(item) {
                this.$router.push("/results?keywords=" + item);
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
