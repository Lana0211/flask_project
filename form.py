from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')  # 渲染当前的html页面

if __name__ == '__main__':
		app.run()
