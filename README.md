
# 📧 Spam Detector

A simple and interactive spam detection web app built using **Streamlit**. This project uses a **TF-IDF Vectorizer** and a **Multinomial Naive Bayes model** trained on a public spam dataset to classify SMS messages as *spam* or *not spam*.

---

## 🔍 Features

- ✅ Classifies messages in real-time as **Spam** or **Not Spam**
- 🔠 Preprocessing using **TF-IDF Vectorization**
- 🧠 Model trained using **Multinomial Naive Bayes**
- 🖥️ Lightweight UI built with **Streamlit**

---

## 📁 Project Structure

```
spam-detector/
│
├── app.py                  # Streamlit web app
├── model_training.ipynb    # Jupyter notebook used to train the model
├── spam.csv                # Dataset used for training
├── spam_model.pkl          # Trained spam classification model
├── tfidf_vectorizer.pkl    # TF-IDF vectorizer used for preprocessing
├── requirements.txt        # Project dependencies
```

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/spam-detector.git
cd spam-detector
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the App

```bash
streamlit run app.py
```

Once started, the app will open in your default browser. Enter a message in the text area, and the model will predict whether it is spam or not.

---

## 🧠 Model Training Summary

- **Dataset**: `spam.csv` (SMS Spam Collection Dataset)
- **Text preprocessing**: TF-IDF vectorization (`max_features=5000`)
- **Model**: Multinomial Naive Bayes (`MultinomialNB`)
- **Test Accuracy**: Displayed in the training notebook

---

## 📦 Requirements

All required libraries are listed in `requirements.txt`.  
Main packages include:

- `streamlit==1.28.0`
- `flask==2.3.2`
- `scikit-learn==1.3.0`
- `pandas==2.0.3`
- `joblib==1.3.2`

---

## ✍️ Author

Created by [Your Name Here] – feel free to contribute or share feedback!
