from flask import Flask
import os
import yaml
import joblib
import numpy as np
import requests
from flask import render_template, request

params_parh="params.yaml"
webapp_root="webapp"

static_dir=os.path.join(webapp_root, "static")
template_dir=os.path.join(webapp_root,"templates")


app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        pass
    else:
        return render_template("index.html")


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)