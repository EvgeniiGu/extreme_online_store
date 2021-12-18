from flask import Flask
import os
import sys
import FlaskWebProject1.Admin
project_root = os.path.dirname(__file__)
print(project_root)
static_path = os.path.join(project_root, 'templates')
print(static_path)
template_path = os.path.join(project_root, './')
#app = Flask(__name__, template_folder=template_path, static_folder=static_path)
app = Flask(__name__)
import FlaskWebProject1.views
print(Admin.Admin.is_admin("1", "1"))
if __name__ == "__main__":
    app.run()