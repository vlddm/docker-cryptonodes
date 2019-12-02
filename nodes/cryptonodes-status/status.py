#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import os, sys, traceback
import bitcoin.rpc 
from web3 import Web3
from jsonrpcclient.clients.http_client import HTTPClient
from requests.auth import HTTPDigestAuth
import requests
try:
        import urllib.parse as urlparse
except ImportError:
        import urlparse


env_prefix = 'BRPC_URL_'

def getMoneroBlockCount(url):
    client = HTTPClient(url)
    u = urlparse.urlparse(url)
    client.session.auth = HTTPDigestAuth(u.username, u.password)
    response = client.request('getblockcount')
    blocks = response.data.result['count']
    return blocks

def getNeoBlockCount(url):
    r = requests.get(url+'/?jsonrpc=2.0&method=getblockcount&params=[]&id=1')
    blocks = r.json()['result']
    return blocks

def getNemBlockCount(url):
    r = requests.get(url+'/chain/height')
    blocks = r.json()['height']
    return blocks

def getEthBlockCount(url):
    w3 = Web3(Web3.HTTPProvider(url))
    return w3.eth.blockNumber

def getBitcoinBlockCount(url):
    rpc = bitcoin.rpc.Proxy(service_url = url)
    blocks = rpc.call('getblockcount')
    return blocks

def worker():
    result = ''
    for var in os.environ:
        if var.startswith(env_prefix):
            coin = var[len(env_prefix):]
            url = os.environ[var]
            try:
                if coin == 'Monero':
                    blocks = getMoneroBlockCount(url)
                elif coin == 'Neo':
                    blocks = getNeoBlockCount(url)
                elif coin == 'Eth':
                    blocks = getEthBlockCount(url)
                elif coin == 'Nem':
                    print(coin)
                    blocks = getNemBlockCount(url)
                else:
                    blocks = getBitcoinBlockCount(url)
                output = "{0} block height: {1}\n".format(coin, blocks)
            except Exception as e:
                #traceback.print_exc()
                output = "{0}: Error: {1}\n".format(coin, str(e))
            result += output
    return result
 
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type',        'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><pre>')
        result = worker()
        print(result)
        self.wfile.write(result.encode('utf-8'))
        self.wfile.write(b'</pre></body></html>')


if len(sys.argv) == 1:
    httpd = HTTPServer(('0.0.0.0', int(os.environ['STATUS_PORT'])), SimpleHTTPRequestHandler)
    httpd.serve_forever()
else:
    print(worker())
