#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from flask import Flask
from flask import json
from flask import request
import config as cfg

app = Flask(__name__)

""" https://oauth.vk.com/authorize?client_id=6700721&display=page&
group_ids=168998689&
redirect_uri=http://89.223.88.106/auto_bot_connect&
scope=manage&response_type=code&v=5.80"""


def get_token(code):
    url = 'https://oauth.vk.com/access_token?' \
          'client_id=6700721&' \
          'client_secret=7Qj2REiRNqQW71oJ6xy0&' \
          'redirect_uri=http://89.223.88.106/auto_bot_connect&' \
          'code={}'.format(code)
    response = requests.post(url)
    #t = 'access_token_{}'.format(cfg.group_id)
    print("get_token response: ")
    d = json.loads(response.text)
    t = list(d.keys())[1]
    print(t)
    print(d)
    try:
        d = json.loads(response.text)[t]
        print(d)
        return d
    except Exception as e:
        print(e)
        print(print(response.text))
        return None


def get_confirm_token(token):
    data = {
        "group_id": cfg.group_id,
        "version": 5.80,
        'access_token': token,
        'v': cfg.api_ver
    }
    res = requests.post(cfg.vk_api_url + 'groups.getCallbackConfirmationCode', data=data)
    try:
        d = json.loads(res.text)['response']['code']
        print(d)
        return d
    except Exception:
        print(res.text)
        return None


def add_server(token):
    data = {
        "group_id": cfg.group_id,
        "url": "http://85.143.172.134/vk_bot_roman",
        "title": 'vk_bot',
        "secret_key": cfg.secret_key,
        'access_token': token,
        'v': cfg.api_ver
    }
    res = requests.post(cfg.vk_api_url + 'groups.addCallbackServer', data=data)
    print(res.text)
    try:
        d = json.loads(res.text)['response']['server_id']
        print(d)
        return d
    except Exception:
        print(res.text)
        return None


def set_server_settings(token, server_id):
    data = {
        "group_id": cfg.group_id,
        "api_version": cfg.api_ver,
        "message_new": 1,
        "message_allow": 1,
        "message_deny": 1,
        "group_join": 1,
        "group_leave": 1,
        "server_id": server_id,
        'access_token': token,
        'v': cfg.api_ver
    }
    res = requests.post(cfg.vk_api_url + 'groups.setCallbackSettings', data=data)
    print(res.text)


def save_token(token):
    f = open('config.py', 'a')
    f.write("token = " + token + '\n')
    f.close()


def save_confirm_token(confirmation_token):
    f = open('config.py', 'a')
    f.write("confirmation_token = " + confirmation_token + '\n')
    f.close()


@app.route(rule='/auto_bot_connect'.format(cfg.bot_name), methods=['GET'])
def debug():
    code = request.args.get('code')
    print("code: ")
    print(code)
    token = get_token(code)
    print("token: ")
    print(token)
    save_token(token)
    confirm_token = get_confirm_token(token)
    save_confirm_token(confirm_token)
    server_id = add_server(token)
    set_server_settings(token, server_id)
    return "ok"


if __name__ == '__main__':
    app.run(port=9088)