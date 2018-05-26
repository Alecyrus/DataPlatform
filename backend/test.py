
pemm = '''
-----BEGIN CERTIFICATE-----
MIIDXzCCAkegAwIBAgIEWWJhzDANBgkqhkiG9w0BAQsFADBgMQwwCgYDVQQGEwNhc2QxDDAKBgNVBAgTA2FzZDEMMAoGA1UEBxMDYXNkMQwwCgYDVQQKEwNhc2QxDDAKBgNVBAsTA2FzZDEYMBYGA1UEAxMPMTkzLjExMi4xMjIuMTkzMB4XDTE4MDMyMzE2MTc1MFoXDTE4MDYyMTE2MTc1MFowYDEMMAoGA1UEBhMDYXNkMQwwCgYDVQQIEwNhc2QxDDAKBgNVBAcTA2FzZDEMMAoGA1UEChMDYXNkMQwwCgYDVQQLEwNhc2QxGDAWBgNVBAMTDzE5My4xMTIuMTIyLjE5MzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJtxQbd4Itkwq8eoYU/xQTzfJCy8VyEyxH1vh4rilxuC+xUw7N3cku8jOFDbdtaQoTrx7z73urytjzLnzLM5VSi+Tb6Scc9RDeAcvr8l2J1LPtXNJudUW4RakBurCrVJ6UFN30a8tCWw2C9ra7V540DcWLv2swujCZpAD8Bnp6y9BcKv2JGrh/uLGzd2hvA7DwSKatCYOJIC+zbkd41eqECRKKjBFpecxygx4zKLHSzPKObwbfVsJoZRa0T7PLXGtg7C04Z+p6HXbgvyc2EmG/GKpTwMl91GZYSU16XVsbVvwqLdJLMK8t4Hgvc0GYsAEE/08NqeM3HgXbzc9WhWr40CAwEAAaMhMB8wHQYDVR0OBBYEFFOWuj3Q0a74Guj6Mn0ja4u/I+tsMA0GCSqGSIb3DQEBCwUAA4IBAQB8+kMD7egP4f/OhiS0oCXOhr6VFV66ZQg/GoNIhxUwFA21UshKr+haazZkCq0Wk2Kp76jWw4ZAwVX1YwBON7ykLAHxH7LK/Jfr0YHPHFjODr/9n6t+ACnyN0MU2OHpGnXR688V6Lq/M1iOEwqBu0ePoDCbp++1DDtFWceI8nsVf9SxEgrTY4y/TvpmHjaGiIRG6zTvrKl6nw+pHx9XaD1YkzW9Cmnu7/8SVrUmX/vTkJZYbKwX0GszA2jkioKO2kI7m7owYRjiZx/4ZfiO8A6UfdF5B3VgiMm87dHJ1VJ2LJ1USBussQkCdyztwXyX+0rUG4YkSRY5svzn4c3YOa5D
-----END CERTIFICATE-----
'''

#print(pemm)
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography import x509
cert = x509.load_pem_x509_certificate(pemm.encode(encoding="utf-8"), default_backend())

f1 = open("temp1", "wb")
f1.write(cert.public_bytes(encoding=Encoding.DER))
f1.close()

f2 = open("temp2", "wb")
f2.write(cert.public_bytes(encoding=Encoding.PEM))
f2.close()

#commands.getoutput("openssl x509 -noout -text -in a.txt")
p1 = os.popen('asn1dump temp1')
asn1 = p1.read()
print(asn1)
p2 = os.popen('openssl x509 -noout -text -in temp2')
ope = p2.read()
print(ope)
p1.close()
p2.close()
