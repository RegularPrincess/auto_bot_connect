#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
    app.run()


@app.route(rule='/', methods=['GET'])
def debug():
    code = request.args.get('code')
    print(code)
    return "ok"


# @app.route(rule='/{0}'.format(bot_name), methods=['POST'])
# def processing():
