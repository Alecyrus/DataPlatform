#coding:utf-8
import asyncio
from sanic import Sanic
from sanic.response import json
from sanic.exceptions import ServerError
from motor.motor_asyncio import AsyncIOMotorClient
import traceback
import logging
import ujson
from bson import Binary, Code
from bson.json_util import dumps, RELAXED_JSON_OPTIONS

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography import x509
import functools

app = Sanic()
app.config.REQUEST_TIMEOUT = 30

@app.listener('after_server_start')
async def notify_server_started(app, loop):
    logging.info('Server successfully started!')
    app.conn = AsyncIOMotorClient(host='0.0.0.0', port=27017)
    app.db = app.conn.internetinfo

@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    logging.info('Server shutting down!')
    app.conn.close()


@app.post("/v1/asn")
async def search(request):
    resp = {
        "data":[],
        "state":False
    }
    try:   
        param = request.json
        pem = "-----BEGIN CERTIFICATE-----\n"+request.json['raw']["$binary"]+"\n-----END CERTIFICATE-----"
        cert = x509.load_pem_x509_certificate(pem.encode(encoding="utf-8"), default_backend())
        f1 = open("temp1", "wb")
        f1.write(cert.public_bytes(encoding=Encoding.DER))
        f1.close()
        p1 = os.popen('asn1dump temp1')
        asn1 = p1.read()
        resp["data"] = asn1
        resp["state"] = True 
    except Exception as e:
        traceback.print_exc()
        pass
  
    return json(eval(dumps(resp).replace("false","False").replace("true","True")))

@app.post("/v1/openssl")
async def search(request):
    resp = {
        "data":[],
        "state":False
    }
    try:   
        param = request.json
        pem = "-----BEGIN CERTIFICATE-----\n"+request.json['raw']["$binary"]+"\n-----END CERTIFICATE-----"
        cert = x509.load_pem_x509_certificate(pem.encode(encoding="utf-8"), default_backend())
        f1 = open("temp1", "wb")
        f1.write(cert.public_bytes(encoding=Encoding.PEM))
        f1.close()
        p1 = os.popen('openssl x509 -noout -text -in temp2')
        asn1 = p1.read()
        resp["data"] = asn1
        resp["state"] = True 
    except Exception as e:
        traceback.print_exc()
        pass
  
    return json(eval(dumps(resp).replace("false","False").replace("true","True")))



@app.get("/v1/search")
async def search(request):
    resp = {
        "data":[],
        "state":False
    }
    try:   
        keywords = request.args.get('keywords', "")
        limit = request.args.get('limit',1)
        skip = request.args.get('skip',0)

        temp =  app.db.https.find({"$text":{ "$search": keywords }})
        resp['total'] = await temp.count()
        resp["data"] = await temp.limit(limit).skip(skip).to_list(None)
        resp["state"] = True
       
       
    except Exception as e:
        traceback.print_exc()
        pass
  
    return json(eval(dumps(resp).replace("false","False").replace("true","True")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3456, workers=1)