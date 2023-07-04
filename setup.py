from flaskr import create_app

# flaskr/__init__.py/create_app()を実行
app = create_app()

if __name__ == '__main__':
    app.run(port=8080,debug=True)