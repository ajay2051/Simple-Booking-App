from backends import routes

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
    app.run(ssl_context=('cert.pem','key.pem'))