# -*- coding: utf-8 -*- 
# @Time : 2018/6/12 下午8:04 
# @Author : Leon 
# @File : app.py.py 
# @Software: PyCharm

import json
from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect
from flask import render_template

app = Flask(__name__)

update_data = """
{
  "msg":"update info",
  "pn":"",
  "vc":"1000000",
  "vn":"1.0.0-SNAPSHOT",
  "download_url":"",
  "channel":"dakehu",
  "extra":"",
  "force": 0
}
"""


@app.route('/api/v1/update', methods=['GET', 'POST'])
def band_app_update():
    if request.method == 'GET':
        # a = request.get_data()
        update_json_obj = json.loads(update_data)
        # return json.dumps(update_json_obj["data"])
        return jsonify(update_json_obj)
    else:
        return '<h1>only support method GET！</h1>'


@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


# just download at /static/<filename>
@app.route('/<filename>')
def download(filename):
    return None


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=12345,
        debug=True
    )
