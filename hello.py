import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    if 'CF_REPO_NAME' in os.environ:
        return_string = "Hello World. This is service {0} built from branch {1}"\
        .format(os.environ['CF_REPO_NAME'], os.environ['CF_BRANCH_TAG_NORMALIZED'])
    else:
        return_string = "Hello World" 
    return return_string 

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port='8080')