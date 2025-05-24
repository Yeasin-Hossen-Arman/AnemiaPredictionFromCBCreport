# AnemiaPredictionFromCBCreport
# 🩸 Anemia Prediction from CBC Reports

This project is a web-based application that predicts the likelihood of anemia based on Complete Blood Count (CBC) values. Users can either **manually enter blood test data** or **upload a clinical report (PDF/Image)** to extract values using Optical Character Recognition (OCR).

## 🔍 Features

- 📄 Upload CBC report in image or PDF format (OCR-based extraction)
- 🧾 Manual form for entering lab values (Gender, Hemoglobin, MCH, MCHC, MCV)
- 🤖 Machine Learning model (Logistic Regression) trained on medical data
- 📊 Real-time prediction with user-friendly result display
- 🌐 Responsive and modern web interface using HTML & CSS

## 💡 Technologies Used

- **Flask** (Backend Web Framework)
- **Scikit-learn** (Machine Learning Model)
- **Pandas** (Data Processing)
- **Tesseract OCR** (Text Extraction from Images)
- **HTML5 & CSS3** (Frontend UI)

## 📥 Inputs Accepted

- **Gender** (0 = Female, 1 = Male)
- **Hemoglobin**
- **MCH**
- **MCHC**
- **MCV**

## 🚀 How to Run the App

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/anemia-prediction.git
   cd anemia-prediction
