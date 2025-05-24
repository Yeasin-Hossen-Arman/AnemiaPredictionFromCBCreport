from flask import Flask, render_template, request
import fitz  # PyMuPDF
import pandas as pd
import re
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load your dataset and train the model (you can also use a saved model instead)
df = pd.read_csv('anemia.csv')
X = df.drop("Result", axis=1)
y = df['Result']
model = LogisticRegression()
model.fit(X, y)

def extract_cbc_data(text):
    patterns = {
        "Hemoglobin": r"(?:Hemoglobin|Hb)\s*[:\-]?\s*([\d\.]+)",
        "MCV": r"(?:MCV)\s*[:\-]?\s*([\d\.]+)",
        "MCH": r"(?:MCH)\s*[:\-]?\s*([\d\.]+)",
        "MCHC": r"(?:MCHC)\s*[:\-]?\s*([\d\.]+)"
    }
    results = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        results[key] = float(match.group(1)) if match else None
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        gender = int(request.form.get("gender"))
        hemoglobin = mch = mchc = mcv = None

        # Handle PDF file input
        if "pdf_file" in request.files and request.files["pdf_file"].filename != "":
            pdf_file = request.files["pdf_file"]
            pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")
            text = "".join([page.get_text() for page in pdf])
            cbc = extract_cbc_data(text)
            hemoglobin = cbc["Hemoglobin"]
            mch = cbc["MCH"]
            mchc = cbc["MCHC"]
            mcv = cbc["MCV"]
        else:
            # Handle manual input form
            hemoglobin = request.form.get("hemoglobin", type=float)
            mch = request.form.get("mch", type=float)
            mchc = request.form.get("mchc", type=float)
            mcv = request.form.get("mcv", type=float)

        if None not in [gender, hemoglobin, mch, mchc, mcv]:
            prediction = model.predict([[gender, hemoglobin, mch, mchc, mcv]])[0]
            result = "✅ Anemia Detected" if prediction == 1 else "❌ No Anemia Detected"
        else:
            result = "⚠️ Incomplete or invalid data"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
