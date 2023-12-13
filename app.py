import pandas as pd
import json
import rpy2.robjects as ro
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return { "message": "Welcome to meta analysis service!"}

@app.route("/effect-size", methods=['GET'])
def effect_size():
   nt = int(request.args.get('nt'))
   mt = float(request.args.get('mt'))
   tdc = float(request.args.get('tdc'))
   tdt = float(request.args.get('tdt'))
   nc = int(request.args.get('nc'))
   mc = float(request.args.get('mc'))

   effect_size_params  =  pd.DataFrame([[nt, mt, tdt, nc, mc, tdc]])
   with localconverter(ro.default_converter + pandas2ri.converter):
    r_from_pd_df = ro.conversion.py2rpy(effect_size_params)
    ro.r.source("./effectSize.R")
    effect_size = ro.r.calculateEffectSize(r_from_pd_df)

    response = {
        "effect_size": effect_size["Effect_size"][0],
        "lower": effect_size["Lower"][0],
        "upper": effect_size["Upper"][0],
        "pval": effect_size["Pval"][0],
        "standard_err": effect_size["Standard_Err"][0],
        "weight": effect_size["Weight"][0],

    }
    return response
    


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=False)