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
  
          <Col span="19" align="left" style="">
  
          <transition name="fadeUp" appear>

           
  
            <Row type="flex" align="top" justify="start" style="margin-top:0em;">
              <Col span="6" align="left" style="margin-top:2em;margin-bottom:0em" offset="0">
              <p class="title2">{{contentTitle}}</p>
              </Col>
            </Row>


             </transition>

             <transition name="fadeUp" mode="out-in">

                <Scroll height="680" >
                 <router-view></router-view>
               </Scroll>
                
             </transition>


            
  
  
         
  

          
  
  
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
        contentTitle: "总结",
        titleMap: {
          t11: "总结",
          t12: "Open SSL",
          t13: "ANC.1",
          t21: "Apple",
          t22: "Microsoft",
          t23: "Mozilla NSS",
          t24: "Google CT",
          t31: "RAW",
          t32: "JSON",
          t33: "PEM",
          t34: "DER",
          t41: "CA 机构",
          t42: "相同序列号",
          t43: "相同公钥",
          t44: "相同标识名称",
          t45: "域名",
          t46: "IPv4 地址",
  
        },
        certificate: {
          _id: "5ad2ca216fb85d0cb0a4a4c2",
          raw: "MIIGMzCCBRugAwIBAgIJAL9HzW0nC4PaMA0GCSqGSIb3DQEBCwUAMIG0MQswCQYDVQQGEwJVUzEQMA4GA1UECBMHQXJpem9uYTETMBEGA1UEBxMKU2NvdHRzZGFsZTEaMBgGA1UEChMRR29EYWRkeS5jb20sIEluYy4xLTArBgNVBAsTJGh0dHA6Ly9jZXJ0cy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5LzEzMDEGA1UEAxMqR28gRGFkZHkgU2VjdXJlIENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTE4MDQxMDAyMjcwMFoXDTE5MDQwOTE0NTkwMVowODEhMB8GA1UECxMYRG9tYWluIENvbnRyb2wgVmFsaWRhdGVkMRMwEQYDVQQDEwpuYjg4eWguY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApdaczI07bQnEo1CcQfPUdSnSjZNhUSnVEYtkNnJLTB3eLe886oq8xbubKJkA8pYTJTupsWyPBbCE4F34yP39ygfgVT+xwI9q6jehOqIHOg4OepuqlulBF2U6fFlgmzfmfapCjBkTvtZPKcsWsS8Ml7D7jTlMRoQuSiDmEuTVeDoWENZy7UfzJZxpUhi4n0buh//MMZa3nj5BSGDb5nmT72QGDT00eGghPwWDg1EMPSuiH+11TOqL4cGm+PUpKMUGIO8XFpc3sQB/DyFTUHCnRPozY5AjebMl8Sq8Za2O7yNFcwUrLeJce6bxXNYCl9JzsMwKff4DpDqvgzFLzBTlSwIDAQABo4ICwTCCAr0wDAYDVR0TAQH/BAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDgYDVR0PAQH/BAQDAgWgMDcGA1UdHwQwMC4wLKAqoCiGJmh0dHA6Ly9jcmwuZ29kYWRkeS5jb20vZ2RpZzJzMS04MjEuY3JsMF0GA1UdIARWMFQwSAYLYIZIAYb9bQEHFwEwOTA3BggrBgEFBQcCARYraHR0cDovL2NlcnRpZmljYXRlcy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5LzAIBgZngQwBAgEwdgYIKwYBBQUHAQEEajBoMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5nb2RhZGR5LmNvbS8wQAYIKwYBBQUHMAKGNGh0dHA6Ly9jZXJ0aWZpY2F0ZXMuZ29kYWRkeS5jb20vcmVwb3NpdG9yeS9nZGlnMi5jcnQwHwYDVR0jBBgwFoAUQMK9J47MNIMwojPX+2yz8LQsgM4wJQYDVR0RBB4wHIIKbmI4OHloLmNvbYIOd3d3Lm5iODh5aC5jb20wHQYDVR0OBBYEFAQ1kkGY7sVgY8rYhFWnIkyBC5kdMIIBBQYKKwYBBAHWeQIEAgSB9gSB8wDxAHYApLkJkLQYWBSHuxOizGdwCjw1mAT5G9+443fNDsgN3BAAAAFirWE4EgAABAMARzBFAiEAuz/igTGSfyBQUXte2yzhdWeKsHZneMH78uwIOA1xm5wCIAfWr3tmFmzYy8ivkiFbFG1d6Ria+iWo/xo/xKnJlpNJAHcAdH7agzGtMxCRIZzOJU9CcMK//V5CIAjGNzV55hB7zFYAAAFirWE5kgAABAMASDBGAiEA7Mdv96G8sqMj4WyKPkay+BavJEqgMYPhly+w1t7W4FQCIQD9DTyYsVFxllx92c79O9CWzvZjxjxSWU8iyeyluYWHwDANBgkqhkiG9w0BAQsFAAOCAQEAfZ4ZRnxjgE7Km0bpfFYFiCuucpbJ8I1hnaI3NtSCiqzyHVHd2M4onVGu00dtYhjt/uwNJPLgBuFTteG6ekpoyLT1AhSre8I2MpiLgSX0bzJ032t/gg3vU026rB4oY6ygTCTjFKhg83u5eW07xJkYdArq4xkQaDMiTmu2T63KtkLp7ltVqAwGKqHGKS8uw4erlZ8bwvQCca0nqnEpEMOasxEgnBHXDN1U8h8YZk+o2/rS7QuKn8EWhqiEmu8lUUPjdbfufYHbFNhHn9jJElJR5zAIDFrc33NxaAqCrdaDt8TGYzoq/KwqfflE+I4enZHI4hf5wrfuefUyHJY5PrKRig==",
          rawtbscertificate: "MIIFG6ADAgECAgkAv0fNbScLg9owDQYJKoZIhvcNAQELBQAwgbQxCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdBcml6b25hMRMwEQYDVQQHEwpTY290dHNkYWxlMRowGAYDVQQKExFHb0RhZGR5LmNvbSwgSW5jLjEtMCsGA1UECxMkaHR0cDovL2NlcnRzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMTMwMQYDVQQDEypHbyBEYWRkeSBTZWN1cmUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IC0gRzIwHhcNMTgwNDEwMDIyNzAwWhcNMTkwNDA5MTQ1OTAxWjA4MSEwHwYDVQQLExhEb21haW4gQ29udHJvbCBWYWxpZGF0ZWQxEzARBgNVBAMTCm5iODh5aC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCl1pzMjTttCcSjUJxB89R1KdKNk2FRKdURi2Q2cktMHd4t7zzqirzFu5somQDylhMlO6mxbI8FsITgXfjI/f3KB+BVP7HAj2rqN6E6ogc6Dg56m6qW6UEXZTp8WWCbN+Z9qkKMGRO+1k8pyxaxLwyXsPuNOUxGhC5KIOYS5NV4OhYQ1nLtR/MlnGlSGLifRu6H/8wxlreePkFIYNvmeZPvZAYNPTR4aCE/BYODUQw9K6If7XVM6ovhwab49SkoxQYg7xcWlzexAH8PIVNQcKdE+jNjkCN5syXxKrxlrY7vI0VzBSst4lx7pvFc1gKX0nOwzAp9/gOkOq+DMUvMFOVLAgMBAAGjggLBMIICvTAMBgNVHRMBAf8EAjAAMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAOBgNVHQ8BAf8EBAMCBaAwNwYDVR0fBDAwLjAsoCqgKIYmaHR0cDovL2NybC5nb2RhZGR5LmNvbS9nZGlnMnMxLTgyMS5jcmwwXQYDVR0gBFYwVDBIBgtghkgBhv1tAQcXATA5MDcGCCsGAQUFBwIBFitodHRwOi8vY2VydGlmaWNhdGVzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMAgGBmeBDAECATB2BggrBgEFBQcBAQRqMGgwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmdvZGFkZHkuY29tLzBABggrBgEFBQcwAoY0aHR0cDovL2NlcnRpZmljYXRlcy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5L2dkaWcyLmNydDAfBgNVHSMEGDAWgBRAwr0njsw0gzCiM9f7bLPwtCyAzjAlBgNVHREEHjAcggpuYjg4eWguY29tgg53d3cubmI4OHloLmNvbTAdBgNVHQ4EFgQUBDWSQZjuxWBjytiEVaciTIELmR0wggEFBgorBgEEAdZ5AgQCBIH2BIHzAPEAdgCkuQmQtBhYFIe7E6LMZ3AKPDWYBPkb37jjd80OyA3cEAAAAWKtYTgSAAAEAwBHMEUCIQC7P+KBMZJ/IFBRe17bLOF1Z4qwdmd4wfvy7Ag4DXGbnAIgB9ave2YWbNjLyK+SIVsUbV3pGJr6Jaj/Gj/EqcmWk0kAdwB0ftqDMa0zEJEhnM4lT0Jwwr/9XkIgCMY3NXnmEHvMVgAAAWKtYTmSAAAEAwBIMEYCIQDsx2/3obyyoyPhbIo+RrL4Fq8kSqAxg+GXL7DW3tbgVAIhAP0NPJixUXGWXH3Zzv070JbO9mPGPFJZTyLJ7KW5hYfA",
          rawsubjectpublickeyinfo: "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApdaczI07bQnEo1CcQfPUdSnSjZNhUSnVEYtkNnJLTB3eLe886oq8xbubKJkA8pYTJTupsWyPBbCE4F34yP39ygfgVT+xwI9q6jehOqIHOg4OepuqlulBF2U6fFlgmzfmfapCjBkTvtZPKcsWsS8Ml7D7jTlMRoQuSiDmEuTVeDoWENZy7UfzJZxpUhi4n0buh//MMZa3nj5BSGDb5nmT72QGDT00eGghPwWDg1EMPSuiH+11TOqL4cGm+PUpKMUGIO8XFpc3sQB/DyFTUHCnRPozY5AjebMl8Sq8Za2O7yNFcwUrLeJce6bxXNYCl9JzsMwKff4DpDqvgzFLzBTlSwIDAQAB",
          rawsubject: "MDgxITAfBgNVBAsTGERvbWFpbiBDb250cm9sIFZhbGlkYXRlZDETMBEGA1UEAxMKbmI4OHloLmNvbQ==",
          rawissuer: "MIG0MQswCQYDVQQGEwJVUzEQMA4GA1UECBMHQXJpem9uYTETMBEGA1UEBxMKU2NvdHRzZGFsZTEaMBgGA1UEChMRR29EYWRkeS5jb20sIEluYy4xLTArBgNVBAsTJGh0dHA6Ly9jZXJ0cy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5LzEzMDEGA1UEAxMqR28gRGFkZHkgU2VjdXJlIENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcy",
          signaturegg: "fZ4ZRnxjgE7Km0bpfFYFiCuucpbJ8I1hnaI3NtSCiqzyHVHd2M4onVGu00dtYhjt/uwNJPLgBuFTteG6ekpoyLT1AhSre8I2MpiLgSX0bzJ032t/gg3vU026rB4oY6ygTCTjFKhg83u5eW07xJkYdArq4xkQaDMiTmu2T63KtkLp7ltVqAwGKqHGKS8uw4erlZ8bwvQCca0nqnEpEMOasxEgnBHXDN1U8h8YZk+o2/rS7QuKn8EWhqiEmu8lUUPjdbfufYHbFNhHn9jJElJR5zAIDFrc33NxaAqCrdaDt8TGYzoq/KwqfflE+I4enZHI4hf5wrfuefUyHJY5PrKRig==",
          signaturealgorithm: "SHA256WithRSA",
          publickeyalgorithm: "RSA",
          publickey: "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApdaczI07bQnEo1CcQfPUdSnSjZNhUSnVEYtkNnJLTB3eLe886oq8xbubKJkA8pYTJTupsWyPBbCE4F34yP39ygfgVT+xwI9q6jehOqIHOg4OepuqlulBF2U6fFlgmzfmfapCjBkTvtZPKcsWsS8Ml7D7jTlMRoQuSiDmEuTVeDoWENZy7UfzJZxpUhi4n0buh//MMZa3nj5BSGDb5nmT72QGDT00eGghPwWDg1EMPSuiH+11TOqL4cGm+PUpKMUGIO8XFpc3sQB/DyFTUHCnRPozY5AjebMl8Sq8Za2O7yNFcwUrLeJce6bxXNYCl9JzsMwKff4DpDqvgzFLzBTlSwIDAQAB",
          version: 3,
          serialnumber: "13783211053280887770",
          issuer: {
            "country": [
              "US"
            ],
            "organization": [
              "GoDaddy.com, Inc."
            ],
            "organizationalunit": [
              "http://certs.godaddy.com/repository/"
            ],
            "locality": [
              "Scottsdale"
            ],
            "province": [
              "Arizona"
            ],
            "streetaddress": [],
            "postalcode": [],
            "serialnumber": "",
            "commonname": "Go Daddy Secure Certificate Authority - G2",
            "names": [{
                "type": [
                  2,
                  5,
                  4,
                  6
                ],
                "value": "US"
              },
              {
                "type": [
                  2,
                  5,
                  4,
                  8
                ],
                "value": "Arizona"
              },
              {
                "type": [
                  2,
                  5,
                  4,
                  7
                ],
                "value": "Scottsdale"
              },
              {
                "type": [
                  2,
                  5,
                  4,
                  10
                ],
                "value": "GoDaddy.com, Inc."
              },
              {
                "type": [
                  2,
                  5,
                  4,
                  11
                ],
                "value": "http://certs.godaddy.com/repository/"
              },
              {
                "type": [
                  2,
                  5,
                  4,
                  3
                ],
                "value": "Go Daddy Secure Certificate Authority - G2"
              }
            ],
            "extranames": []
          },
          "subject": {
            "country": [],
            "organization": [],
            "organizationalunit": [
              "Domain Control Validated"
            ],
            "locality": [],
            "province": [],
            "streetaddress": [],
            "postalcode": [],
            "serialnumber": "",
            "commonname": "nb88yh.com",
            "names": [{
                "type": [
                  2,
                  5,
                  4,
                  11
                ],
                "value": "Domain Control Validated"
              },
              {
                "type": [
                  2,
                  5,
                  4,
                  3
                ],
                "value": "nb88yh.com"
              }
            ],
            "extranames": []
          },
          "notbefore": "2018-04-10T02:27:00.000Z",
          "notafter": "2019-04-09T14:59:01.000Z",
          "extensions": {
            "extensions": [{
                "id": [
                  2,
                  5,
                  29,
                  19
                ],
                "critical": true,
                "value": {
                  "$binary": "MAA=",
                  "$type": "00"
                }
              },
              {
                "id": [
                  2,
                  5,
                  29,
                  37
                ],
                "critical": false,
                "value": {
                  "$binary": "MBQGCCsGAQUFBwMBBggrBgEFBQcDAg==",
                  "$type": "00"
                }
              },
              {
                "id": [
                  2,
                  5,
                  29,
                  15
                ],
                "critical": true,
                "value": {
                  "$binary": "AwIFoA==",
                  "$type": "00"
                }
              },
              {
                "id": [
                  2,
                  5,
                  29,
                  31
                ],
                "critical": false,
                "value": {
                  "$binary": "MC4wLKAqoCiGJmh0dHA6Ly9jcmwuZ29kYWRkeS5jb20vZ2RpZzJzMS04MjEuY3Js",
                  "$type": "00"
                }
              },
              {
                "id": [
                  2,
                  5,
                  29,
                  32
                ],
                "critical": false,
                "value": {
                  "$binary": "MFQwSAYLYIZIAYb9bQEHFwEwOTA3BggrBgEFBQcCARYraHR0cDovL2NlcnRpZmljYXRlcy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5LzAIBgZngQwBAgE=",
                  "$type": "00"
                }
              },
              {
                "id": [
                  1,
                  3,
                  6,
                  1,
                  5,
                  5,
                  7,
                  1,
                  1
                ],
                "critical": false,
                "value": {
                  "$binary": "MGgwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmdvZGFkZHkuY29tLzBABggrBgEFBQcwAoY0aHR0cDovL2NlcnRpZmljYXRlcy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5L2dkaWcyLmNydA==",
                  "$type": "00"
                }
              },
              {
                "id": [
                  2,
                  5,
                  29,
                  35
                ],
                "critical": false,
                "value": {
                  "$binary": "MBaAFEDCvSeOzDSDMKIz1/tss/C0LIDO",
                  "$type": "00"
                }
              },
              {
                "id": [
                  2,
                  5,
                  29,
                  17
                ],
                "critical": false,
                "value": {
                  "$binary": "MByCCm5iODh5aC5jb22CDnd3dy5uYjg4eWguY29t",
                  "$type": "00"
                }
              },
              {
                "id": [
                  2,
                  5,
                  29,
                  14
                ],
                "critical": false,
                "value": {
                  "$binary": "BBQENZJBmO7FYGPK2IRVpyJMgQuZHQ==",
                  "$type": "00"
                }
              },
              {
                "id": [
                  1,
                  3,
                  6,
                  1,
                  4,
                  1,
                  11129,
                  2,
                  4,
                  2
                ],
                "critical": false,
                "value": {
                  "$binary": "BIHzAPEAdgCkuQmQtBhYFIe7E6LMZ3AKPDWYBPkb37jjd80OyA3cEAAAAWKtYTgSAAAEAwBHMEUCIQC7P+KBMZJ/IFBRe17bLOF1Z4qwdmd4wfvy7Ag4DXGbnAIgB9ave2YWbNjLyK+SIVsUbV3pGJr6Jaj/Gj/EqcmWk0kAdwB0ftqDMa0zEJEhnM4lT0Jwwr/9XkIgCMY3NXnmEHvMVgAAAWKtYTmSAAAEAwBIMEYCIQDsx2/3obyyoyPhbIo+RrL4Fq8kSqAxg+GXL7DW3tbgVAIhAP0NPJixUXGWXH3Zzv070JbO9mPGPFJZTyLJ7KW5hYfA",
                  "$type": "00"
                }
              }
            ],
            "extraextensions": [],
            "unhandledcriticalextensions": [],
            "unknownextkeyusage": [],
            "keyusage": [
              "DigitalSignature",
              "KeyEncipherment"
            ],
            "basicconstraints": {
              "isca": false,
              "maxpathlenzero": false,
              "maxpathlen": -1
            },
            "subjectkeyidentifier": {
              "$binary": "BDWSQZjuxWBjytiEVaciTIELmR0=",
              "$type": "00"
            },
            "authoritykeyidentifier": {
              "$binary": "QMK9J47MNIMwojPX+2yz8LQsgM4=",
              "$type": "00"
            },
            "ocspserver": [
              "http://ocsp.godaddy.com/"
            ],
            "issuingcertificateurl": [
              "http://certificates.godaddy.com/repository/gdig2.crt"
            ],
            "subjectalternativename": {
              "dnsnames": [
                "nb88yh.com",
                "www.nb88yh.com"
              ],
              "emailaddresses": [],
              "ipaddresses": [],
              "uris": []
            },
            "crldistributionpoints": [
              "http://crl.godaddy.com/gdig2s1-821.crl"
            ],
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
            "extendedkeyusage": [
              "ServerAuth",
              "ClientAuth"
            ],
            "policyidentifiers": [
              [
                2,
                16,
                840,
                1,
                114413,
                1,
                7,
                23,
                1
              ],
              [
                2,
                23,
                140,
                1,
                2,
                1
              ]
            ]
          },
          "fingerprint": {
            "md5": "2b43b7eb280908fa3687e44616369419",
            "sha1": "323fd0d2c94dca887821b33ac2175a5fd3f56c08",
            "sha256": "c0b4fa33e229ec7188bf9ec92b8d6f4758e1f8bb48cf7b9251aeab5c7ceba0bf"
          },
          "trust": {
            "apple_ios": "Included",
            "apple_macos": "Included",
            "google_aosp": "Included",
            "microsoft_windows": "Included",
            "mozilla_nss": "Included"
          },
          "fromcrt": "5ad2ca236fb85d0cb0a4a6a4",
          "hosts": [
            "103.193.240.218"
          ],
          "isrevoked": "No"
        }
  
      }
    },
    mounted() {
  
  
  
    },
    methods: {
      handleMenu() {
        this.$toast.success('' + arguments[0], 'Info', {
          position: 'topCenter'
        }, );
        this.contentTitle = eval("this.titleMap." + arguments[0])
      }
    },
  
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
