<template>
    <div>
    
        <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
    
    
    
            <Col span="18" align="left" style="margin-top:0em;margin-left:1em;background-color:;" offset="0">
    
    
            <Tabs value="textshow">
                <TabPane label="RAW JSON" name="raw">
    
    
                    <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
                        <Col span="22" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
                        <Scroll height="600">
                            <Row type="flex" align="top" justify="start" style="margin-top:0em;background-color:;">
    
                                <Col span="22" align="left" style="margin-top:0em;margin-bottom:0em;background-color:;" offset="1">
    
    
                                <pre>
                              {{rawJson}}
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
                    <Button type="ghost" shape="circle" size="large"><awe-icon name="download"  scale="1.3" ></awe-icon></Button>
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
    export default {
        data() {
            return {
                t1: '探寻和分析',
                textshow: "raw",
                rawJson1: {
                        "_id": {
                            "$oid": "5ad323b96fb85d17237ccfe0"
                        },
                        "raw": {
                            "$binary": "MIIDXzCCAkegAwIBAgIEWWJhzDANBgkqhkiG9w0BAQsFADBgMQwwCgYDVQQGEwNhc2QxDDAKBgNVBAgTA2FzZDEMMAoGA1UEBxMDYXNkMQwwCgYDVQQKEwNhc2QxDDAKBgNVBAsTA2FzZDEYMBYGA1UEAxMPMTkzLjExMi4xMjIuMTkzMB4XDTE4MDMyMzE2MTc1MFoXDTE4MDYyMTE2MTc1MFowYDEMMAoGA1UEBhMDYXNkMQwwCgYDVQQIEwNhc2QxDDAKBgNVBAcTA2FzZDEMMAoGA1UEChMDYXNkMQwwCgYDVQQLEwNhc2QxGDAWBgNVBAMTDzE5My4xMTIuMTIyLjE5MzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJtxQbd4Itkwq8eoYU/xQTzfJCy8VyEyxH1vh4rilxuC+xUw7N3cku8jOFDbdtaQoTrx7z73urytjzLnzLM5VSi+Tb6Scc9RDeAcvr8l2J1LPtXNJudUW4RakBurCrVJ6UFN30a8tCWw2C9ra7V540DcWLv2swujCZpAD8Bnp6y9BcKv2JGrh/uLGzd2hvA7DwSKatCYOJIC+zbkd41eqECRKKjBFpecxygx4zKLHSzPKObwbfVsJoZRa0T7PLXGtg7C04Z+p6HXbgvyc2EmG/GKpTwMl91GZYSU16XVsbVvwqLdJLMK8t4Hgvc0GYsAEE/08NqeM3HgXbzc9WhWr40CAwEAAaMhMB8wHQYDVR0OBBYEFFOWuj3Q0a74Guj6Mn0ja4u/I+tsMA0GCSqGSIb3DQEBCwUAA4IBAQB8+kMD7egP4f/OhiS0oCXOhr6VFV66ZQg/GoNIhxUwFA21UshKr+haazZkCq0Wk2Kp76jWw4ZAwVX1YwBON7ykLAHxH7LK/Jfr0YHPHFjODr/9n6t+ACnyN0MU2OHpGnXR688V6Lq/M1iOEwqBu0ePoDCbp++1DDtFWceI8nsVf9SxEgrTY4y/TvpmHjaGiIRG6zTvrKl6nw+pHx9XaD1YkzW9Cmnu7/8SVrUmX/vTkJZYbKwX0GszA2jkioKO2kI7m7owYRjiZx/4ZfiO8A6UfdF5B3VgiMm87dHJ1VJ2LJ1USBussQkCdyztwXyX+0rUG4YkSRY5svzn4c3YOa5D",
                            "$type": "00"
                        },
                        "rawtbscertificate": {
                            "$binary": "MIICR6ADAgECAgRZYmHMMA0GCSqGSIb3DQEBCwUAMGAxDDAKBgNVBAYTA2FzZDEMMAoGA1UECBMDYXNkMQwwCgYDVQQHEwNhc2QxDDAKBgNVBAoTA2FzZDEMMAoGA1UECxMDYXNkMRgwFgYDVQQDEw8xOTMuMTEyLjEyMi4xOTMwHhcNMTgwMzIzMTYxNzUwWhcNMTgwNjIxMTYxNzUwWjBgMQwwCgYDVQQGEwNhc2QxDDAKBgNVBAgTA2FzZDEMMAoGA1UEBxMDYXNkMQwwCgYDVQQKEwNhc2QxDDAKBgNVBAsTA2FzZDEYMBYGA1UEAxMPMTkzLjExMi4xMjIuMTkzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm3FBt3gi2TCrx6hhT/FBPN8kLLxXITLEfW+HiuKXG4L7FTDs3dyS7yM4UNt21pChOvHvPve6vK2PMufMszlVKL5NvpJxz1EN4By+vyXYnUs+1c0m51RbhFqQG6sKtUnpQU3fRry0JbDYL2trtXnjQNxYu/azC6MJmkAPwGenrL0Fwq/YkauH+4sbN3aG8DsPBIpq0Jg4kgL7NuR3jV6oQJEoqMEWl5zHKDHjMosdLM8o5vBt9WwmhlFrRPs8tca2DsLThn6nodduC/JzYSYb8YqlPAyX3UZlhJTXpdWxtW/Cot0kswry3geC9zQZiwAQT/Tw2p4zceBdvNz1aFavjQIDAQABoyEwHzAdBgNVHQ4EFgQUU5a6PdDRrvga6PoyfSNri78j62w=",
                            "$type": "00"
                        },
                        "rawsubjectpublickeyinfo": {
                            "$binary": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm3FBt3gi2TCrx6hhT/FBPN8kLLxXITLEfW+HiuKXG4L7FTDs3dyS7yM4UNt21pChOvHvPve6vK2PMufMszlVKL5NvpJxz1EN4By+vyXYnUs+1c0m51RbhFqQG6sKtUnpQU3fRry0JbDYL2trtXnjQNxYu/azC6MJmkAPwGenrL0Fwq/YkauH+4sbN3aG8DsPBIpq0Jg4kgL7NuR3jV6oQJEoqMEWl5zHKDHjMosdLM8o5vBt9WwmhlFrRPs8tca2DsLThn6nodduC/JzYSYb8YqlPAyX3UZlhJTXpdWxtW/Cot0kswry3geC9zQZiwAQT/Tw2p4zceBdvNz1aFavjQIDAQAB",
                            "$type": "00"
                        },
                        "rawsubject": {
                            "$binary": "MGAxDDAKBgNVBAYTA2FzZDEMMAoGA1UECBMDYXNkMQwwCgYDVQQHEwNhc2QxDDAKBgNVBAoTA2FzZDEMMAoGA1UECxMDYXNkMRgwFgYDVQQDEw8xOTMuMTEyLjEyMi4xOTM=",
                            "$type": "00"
                        },
                        "rawissuer": {
                            "$binary": "MGAxDDAKBgNVBAYTA2FzZDEMMAoGA1UECBMDYXNkMQwwCgYDVQQHEwNhc2QxDDAKBgNVBAoTA2FzZDEMMAoGA1UECxMDYXNkMRgwFgYDVQQDEw8xOTMuMTEyLjEyMi4xOTM=",
                            "$type": "00"
                        },
                        "signaturegg": {
                            "$binary": "fPpDA+3oD+H/zoYktKAlzoa+lRVeumUIPxqDSIcVMBQNtVLISq/oWms2ZAqtFpNiqe+o1sOGQMFV9WMATje8pCwB8R+yyvyX69GBzxxYzg6//Z+rfgAp8jdDFNjh6Rp10evPFei6vzNYjhMKgbtHj6Awm6fvtQw7RVnHiPJ7FX/UsRIK02OMv076Zh42hoiERus076ypep8PqR8fV2g9WJM1vQpp7u//Ela1Jl/705CWWGysF9BrMwNo5IqCjtpCO5u6MGEY4mcf+GX4jvAOlH3ReQd1YIjJvO3RydVSdiydVEgbrLEJAncs7cF8l/tK1BuGJEkWObL85+HN2DmuQw==",
                            "$type": "00"
                        },
                        "signaturealgorithm": "SHA256WithRSA",
                        "publickeyalgorithm": "RSA",
                        "publickey": {
                            "$binary": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm3FBt3gi2TCrx6hhT/FBPN8kLLxXITLEfW+HiuKXG4L7FTDs3dyS7yM4UNt21pChOvHvPve6vK2PMufMszlVKL5NvpJxz1EN4By+vyXYnUs+1c0m51RbhFqQG6sKtUnpQU3fRry0JbDYL2trtXnjQNxYu/azC6MJmkAPwGenrL0Fwq/YkauH+4sbN3aG8DsPBIpq0Jg4kgL7NuR3jV6oQJEoqMEWl5zHKDHjMosdLM8o5vBt9WwmhlFrRPs8tca2DsLThn6nodduC/JzYSYb8YqlPAyX3UZlhJTXpdWxtW/Cot0kswry3geC9zQZiwAQT/Tw2p4zceBdvNz1aFavjQIDAQAB",
                            "$type": "00"
                        },
                        "version": 3,
                        "serialnumber": "1499619788",
                        "issuer": {
                            "streetaddress": [],
                            "postalcode": [],
                            "serialnumber": "",
                            "names": [{
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        6
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        8
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        7
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        10
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        11
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        3
                                    ],
                                    "value": "193.112.122.193"
                                }
                            ],
                            "extranames": [],
                            "c": [
                                "asd"
                            ],
                            "o": [
                                "asd"
                            ],
                            "ou": [
                                "asd"
                            ],
                            "cn": "193.112.122.193",
                            "l": [
                                "asd"
                            ],
                            "p": [
                                "asd"
                            ]
                        },
                        "subject": {
                            "streetaddress": [],
                            "postalcode": [],
                            "serialnumber": "",
                            "names": [{
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        6
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        8
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        7
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        10
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        11
                                    ],
                                    "value": "asd"
                                },
                                {
                                    "type": [
                                        2,
                                        5,
                                        4,
                                        3
                                    ],
                                    "value": "193.112.122.193"
                                }
                            ],
                            "extranames": [],
                            "c": [
                                "asd"
                            ],
                            "o": [
                                "asd"
                            ],
                            "ou": [
                                "asd"
                            ],
                            "cn": "193.112.122.193",
                            "l": [
                                "asd"
                            ],
                            "p": [
                                "asd"
                            ]
                        },
                        "notbefore": {
                            "$date": 1521821870000
                        },
                        "notafter": {
                            "$date": 1529597870000
                        },
                        "extensions": {
                            "extensions": [{
                                "id": [
                                    2,
                                    5,
                                    29,
                                    14
                                ],
                                "critical": false,
                                "value": {
                                    "$binary": "BBRTlro90NGu+Bro+jJ9I2uLvyPrbA==",
                                    "$type": "00"
                                }
                            }],
                            "extraextensions": [],
                            "unhandledcriticalextensions": [],
                            "unknownextkeyusage": [],
                            "keyusage": [],
                            "basicconstraints": {
                                "isca": false,
                                "maxpathlenzero": false,
                                "maxpathlen": 0
                            },
                            "subjectkeyidentifier": {
                                "$binary": "U5a6PdDRrvga6PoyfSNri78j62w=",
                                "$type": "00"
                            },
                            "authoritykeyidentifier": {
                                "$binary": "",
                                "$type": "00"
                            },
                            "ocspserver": [],
                            "issuingcertificateurl": [],
                            "subjectalternativename": {
                                "dnsnames": [],
                                "emailaddresses": [],
                                "ipaddresses": [],
                                "uris": []
                            },
                            "crldistributionpoints": [],
                            "nameconstraints": {
                                "permitteddnsdomainscritical": false,
                                "permitteddnsdomains": [],
                                "excludeddnsdomains": [],
                                "permittedipranges": [],
                                "excludedipranges": [],
                                "permittedemailaddresses": [],
                                "excludedemailaddresses": [],
                                "permitteduridomains": [],
                                "excludeduridomains": []
                            },
                            "extendedkeyusage": [],
                            "policyidentifiers": []
                        },
                        "fingerprint": {
                            "md5": "09dbec3d111df60b6c421f4fc4aa8549",
                            "sha1": "de5c09ef96a4fb0bfcc2b6b385d71eb0b7e0ff2d",
                            "sha256": "c538112a3497e3bee1972c8f8ea8f8b06a507f3c9200a1cd3ea72245b20973f4"
                        },
                        "trust": {
                            "apple_ios": "Not Include",
                            "apple_macos": "Not Include",
                            "google_aosp": "Not Include",
                            "microsoft_windows": "Not Include",
                            "mozilla_nss": "Not Include"
                        },
                        "fromcrt": {
                            "$oid": "000000000000000000000000"
                        },
                        "hosts": [
                            "193.112.122.193"
                        ],
                        "isrevoked": "Root"
                    
                },
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
        mounted() {
    
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
