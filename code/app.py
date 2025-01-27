from application import app

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    # docker login ain3003projectregistryf.azurecr.io
    # docker build -t ain3003-project .
    # docker image push ain3003projectregistryf.azurecr.io/ain3003-project:latest 