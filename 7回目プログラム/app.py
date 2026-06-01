from flask import Flask,render_template,request, redirect ,jsonify
from model import init_db
from route import create_route

def create_app():
    app = Flask(__name__)
    init_db(app)
    create_route(app)
    return app

@app.route('/req_item', methods=['GET', 'POST'])
def req_item():
    if request.method == 'POST':
        # フォームからデータが送られてきた時の処理
        return redirect('/')
    
    # 画面を表示する処理
    return render_template('req_item.html')

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
