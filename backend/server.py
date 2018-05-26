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
from bson.objectid import ObjectId
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography import x509
import functools
import queue
import copy
import zmail
import uuid


app = Sanic()
app.config.REQUEST_TIMEOUT = 60

@app.listener('after_server_start')
async def notify_server_started(app, loop):
    logging.info('Server successfully started!')
    app.conn = AsyncIOMotorClient(host='0.0.0.0', port=27017)
    app.db = app.conn.Interinfo
    app.email = zmail.server('springx_official@163.com', 'aun123')
    if app.email.smtp_able():
        pass
    # SMTP function.
    if app.email.pop_able():
        pass
    # POP 

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
        f1 = open("temp", "wb")
        f1.write(cert.public_bytes(encoding=Encoding.DER))
        f1.close()
        p1 = os.popen('asn1dump temp')
        asn1 = p1.read()
        resp["data"] = asn1
        resp["state"] = True 
    except Exception as e:
        traceback.print_exc()
        pass
  
    return json(eval(dumps(resp).replace("false","False").replace("true","True")))


#springx_official@163.com
@app.post("/v1/getkey")
async def search(request):
    resp = {
        "state":False
    }
    try:   
        param = request.json
        print(param)

        with open('email.html','r') as f:
            content_html = f.read()

        mail = {
            'subject': 'The Key from SpringX Official',  # Anything you want.
            'content_html': content_html.replace("[key]", uuid.uuid4().hex).replace("Hello!", "Mr "+param['name']),  # Anything you want.
            # 'attachments': '/Users/zyh/Documents/example.zip',  # Absolute path will be better.
        }
        app.email.send_mail(param['email'],mail)

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
        f1 = open("temp", "wb")
        f1.write(cert.public_bytes(encoding=Encoding.PEM))
        f1.close()
        p1 = os.popen('openssl x509 -noout -text -in temp')
        asn1 = p1.read()
        resp["data"] = asn1
        resp["state"] = True 
    except Exception as e:
        traceback.print_exc()
        pass
  
    return json(eval(dumps(resp).replace("false","False").replace("true","True")))



@app.post("/v1/search")
async def search(request):
    resp = {
        "data":[],
        "state":False
    }
    try:   
        keywords = request.args.get('keywords', "")
        limit = int(request.args.get('limit',1))
        skip = int(request.args.get('skip',0))
        fuzzy = int(request.args.get('fuzzy',1))
        if not fuzzy:
            _filter = request.json['filter']
        else:
            _filter = {"$text":{ "$search": keywords }}

        temp =  app.db.certificate.find(_filter)
        resp['total'] = await temp.count()
        resp["data"] = await temp.limit(limit).skip(skip).to_list(None)
        resp["state"] = True
       
       
    except Exception as e:
        traceback.print_exc()
        pass
  
    return json(eval(dumps(resp).replace("false","False").replace("true","True")))

def fix_code(cert):
    return eval(dumps(cert).replace("false","False").replace("true","True"))


@app.get("/v1/getpath")
async def get_path(request):
    try:
        res = {}
        current_id = request.args.get('id', "")
        root_store = request.args.get('root_store', "default")
        
   
        root =  await app.db.certificate.find_one({'_id': ObjectId(current_id.replace(" ",''))})
        _root = fix_code(root)
        
        _queue = queue.Queue()
        _queue.put((current_id , _root['issuer']['cn'], _root['subject']['cn']))
        while (not _queue.empty()):
            _current_id, _cn_i, _cn_s = _queue.get()
            if not res.get(_current_id, None):  
                res[_current_id] = {"name":_cn_s, "upper":[]}
            _nodes =  app.db.certificate.find({'subject.cn': _cn_i})
            _upper_list = await _nodes.to_list(None)
            for _upper in _upper_list:
                temp = fix_code(_upper)
                res[_current_id]['upper'].append(temp['_id']['$oid'])
                if (temp['issuer']['cn'] == temp['subject']['cn']):
                  
                    if not res.get(temp['_id']['$oid'], None):  
                        res[temp['_id']['$oid']] = {"name":temp['subject']['cn'], "upper":[]}
                    continue
                _queue.put((temp['_id']['$oid'] , temp['issuer']['cn'], temp['subject']['cn']))


        rootcns = list() 
        nodes = [{"id":root_store, "name":root_store, "_color":"red", "_size":50}]
        for node in res.keys():
            if res[node]['name'] != _root['subject']['cn']:
                _size = 30
            else:
                _size = 20
            nodes.append({"id":node, "name":res[node]['name'], "_size":_size})
            if len(res[node]['upper']) == 0 and res[node]['name'] not in rootcns :
                rootcns.append(res[node]['name'])

        paths = [[{"id":current_id,"name":res[current_id]['name']}]]
        qeu = queue.Queue()
        qeu.put((len(paths)-1,current_id))
        while (not qeu.empty()):
            index, _current_id = qeu.get()
           
            _back = copy.deepcopy(paths[index])
        
            for i in range(len(res[_current_id]['upper'])):
             
                if (i != len(res[_current_id]['upper'])-1 ):
                    temp = copy.deepcopy(_back)
                    temp.append({
                        "name":res[res[_current_id]['upper'][i]]["name"],
                        "id":res[_current_id]['upper'][i]
                    })
                    paths.append(temp)
                    qeu.put((len(paths)-1, res[_current_id]['upper'][i]))
                    continue
               
                paths[index].append({
                        "name":res[res[_current_id]['upper'][i]]["name"],
                        "id":res[_current_id]['upper'][i]
                    })
                qeu.put((index, res[_current_id]['upper'][i]))





        links = list()
        qq = queue.Queue()
        qq.put(current_id.replace(" ",''))
        while (not qq.empty()):
            _curr_id = qq.get()
            if (len(res[_curr_id]['upper']) == 0):
                i = {
                    "sid": _curr_id,
                    "tid": root_store,
                    "_color": 'ce3d31',
                }
                if i not in links:
                    links.append(i)

            for upper in res[_curr_id]['upper']:
                i = {
                    "sid": _curr_id,
                    "tid": upper,
                    "_color": 'ce3d31',
                }
                if i not in links:
                    links.append(i)
                qq.put(upper)
        state = True
    except Exception as e:
        traceback.print_exc()
        state = False
        pass
  
    return json({"state":state,"data":res, "nodes":nodes, "links":links, "rootcns":rootcns, "paths":paths})

@app.post("/v1/getca")
async def get_ca(request):
    try:
        tree = {
            "name":"RootStore",
            "children":[]           
        }
        que = queue.Queue()
        param = request.json
        for cn in param['root_cn']:
            tree['children'].append({"name":cn,"children":[]})
            que.put((tree['children'][tree['children'].index({"name":cn,"children":[]})]['children'], cn))
        while(not que.empty()):
            _tree, _current_cn = que.get()
            #print(_current_cn)
            if param['end_user']:
                _nodes =  app.db.certificate.find({'issuer.cn': _current_cn,"extensions.basicconstraints.isca":True})
            else:
                _nodes =  app.db.certificate.find({'issuer.cn': _current_cn})
            _node_list = await _nodes.to_list(None)
            #print(len(_node_list), que.qsize())

            _temp = [_current_cn]
            for node in _node_list:
                if node['subject']['cn'] in _temp:
                    continue
                temp = {
                    "name":node['subject']['cn'],
                    "children":[]
                }
                _tree.append(temp)
                #print(temp)
                que.put((_tree[len(_tree)-1]['children'], node['subject']['cn']))
                _temp.append(node['subject']['cn'])

        state = True

    except Exception as e:
        traceback.print_exc()
        state = False
        pass
  
    return json({"state":state, "tree":tree})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3456, workers=1)