#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from flask import Flask
# from flask import json
from flask import request
# import logging as log
#
# import config
# import service as s
#
#
# token = config.token
# confirmation_token = config.confirmation_token
# secret_key = config.secret_key
# group_id = config.group_id
# admin_id = config.admin_id
# admin_name = config.admin_name
# db_name = config.db_name
# bot_name = config.bot_name
# vk_api_url = config.vk_api_url


app = Flask(__name__)


@app.route(rule='/auto_bot_connect', methods=['GET'])
def debug():
    code = request.args.get('code')
    print(code)

    url = 'https://oauth.vk.com/access_token?' \
          'client_id=6700721&' \
          'client_secret=7Qj2REiRNqQW71oJ6xy0&' \
          'redirect_uri=http://89.223.88.106/auto_bot_connect&' \
          'code={}'.format(code)
    response = requests.post(url)
    print(response)
    print(response.text)
    # dict_data = json.loads(response.text)
    return "ok"

if __name__ == '__main__':
    app.run()




# @app.route(rule='/{0}'.format(bot_name), methods=['POST'])
# def processing():
