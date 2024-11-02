from flask import Flask, request,jsonify
import numpy as np
import pickle


@app.route('/prever', methods = ['GET'])

def prever():
    para1 float(request.args.get('comp_abd'))
    para2 float(request.args.get('comp_abd'))
    para3 float(request.args.get('comp_abd'))

    entrada = np.array([[para1,para2,para3]])
    resultado = modelo.predict(entrada)

    return jsonify({'previsao': resultado.tolist()})

if __name__ == '__main__':
    app.run(debug=True)