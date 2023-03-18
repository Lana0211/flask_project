from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 使用裝飾器來定義路由地址
@app.route('/')
def root():
    # 返回前端頁面
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

from flask import render_template

