#!/Users/pablogarcia/opt/anaconda3/envs/ibm_cloud/bin/python3.9
import machinetranslation
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    
    # Write your code here
    return machinetranslation.traslator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return machinetranslation.traslator.french_to_english(textToTranslate)


@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
