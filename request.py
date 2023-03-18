from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # 渲染index页面
        return render_template('index.html')
    elif request.method == 'POST':
        # 获取数据
        data = {}
        data['user'] = request.form.get('user')   # 后面这个name和前端的name保持一致
        data['password'] = request.form.get('password')

        # 返回到前端去
        return render_template('index2.html', data=data)

    return render_template('index.html')

app.run()
