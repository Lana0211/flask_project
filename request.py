from flask import Flask, render_template, request, jsonify, escape
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
        data['user'] = request.form.get('user')   # 名字和前端要保持一致
        data['password'] = request.form.get('password')

        # 返回到前端去
        return render_template('index2.html', data=data)

    return render_template('index.html')

@app.route('/problem')
def problem():
    data = {"w":1,"problem":"Breakfast"}
    return jsonify(data)

@app.route('/problem/<problem_id>')
def show_problem(problem_id):
    return f"problem: {escape(problem_id)}"


app.run()
