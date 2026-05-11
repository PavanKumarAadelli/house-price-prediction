# 🏠 Real Estate Price Prediction System (Bengaluru)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📝 Overview

This project is a comprehensive **End-to-End Data Science Solution** designed to solve the problem of subjective manual property valuation. By leveraging historical real estate data from Bengaluru, India, this project builds a machine learning model to predict house prices based on key features such as location, square footage, number of bedrooms, and amenities.

The final model is deployed as an interactive **Web Application** using **Streamlit**, allowing users to input property details and receive an instant estimated price.

---

## 🌐 Business Problem

**Scenario:**
Real estate pricing is often subjective and prone to human error when estimated manually by agents. Inconsistent pricing leads to lost revenue (underpricing) or lost customers (overpricing).

**Objective:**
To develop an automated, data-driven prediction system that estimates the fair market value of a property, thereby reducing subjectivity and improving business efficiency.

---

## 🛠 Tech Stack

*   **Language:** Python
*   **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
*   **Machine Learning:** Scikit-Learn (Linear Regression, Ridge, Lasso, Random Forest)
*   **Deployment:** Streamlit, Streamlit Cloud
*   **Version Control:** Git & GitHub

---

## 🚀 Key Features & Methodology

The project demonstrates the complete Data Science lifecycle:

1.  **Data Cleaning & Preprocessing:**
    *   Handled missing values using Median/Mode imputation.
    *   Feature Engineering: Extracted integers from text (e.g., "2 BHK" -> 2) and converted range values (e.g., "2100-2850" -> 2475).
    *   Data Transformation: Applied Log Transformation to `price` and `total_sqft` to handle skewness.

2.  **Exploratory Data Analysis (EDA):**
    *   Visualized distributions (Histograms, Box plots).
    *   Analyzed correlations (Heatmap).
    *   Detected and handled outliers using the IQR method.

3.  **Feature Engineering:**
    *   **Encoding:** Applied One-Hot Encoding (Area Type) and Label Encoding (Location).
    *   **Scaling:** Used Standard Scaler for numerical features.
    *   **Selection:** Identified key predictors using Recursive Feature Elimination (RFE) and Decision Tree Importance.

4.  **Model Building & Validation:**
    *   Trained multiple algorithms: Linear Regression, Ridge, Lasso, Decision Tree, and Random Forest.
    *   **Hyperparameter Tuning:** Used GridSearchCV to optimize Random Forest parameters (max_depth, n_estimators).
    *   **Validation:** Used K-Fold Cross Validation to ensure the model generalizes well.

---

## 📊 Model Performance

The models were evaluated based on **R2 Score** (Coefficient of Determination) and **RMSE** (Root Mean Squared Error) on the log-transformed target variable.

The **Random Forest Regressor** demonstrated superior performance, capturing complex non-linear relationships in the data (e.g., location premiums) better than the Linear baseline.

| Model | R2 Score | RMSE | Status |
| :--- | :---: | :---: | :---: |
| Linear Regression | 0.6516 | 0.4245 | Baseline Model |
| Random Forest (Tuned) | **0.7407** | **0.3661** | **Best Model** |

**Observations:**
*   **R2 Score:** The Random Forest model explains **74.07%** of the variance in house prices, a significant improvement over the Linear model's 65%.
*   **RMSE:** The lower RMSE (0.3661) indicates that the Random Forest's predictions are, on average, closer to the actual prices.

---

## 📦 Installation & Usage

To run this project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/PavanKumarAadelli/house-price-prediction.git
cd house-price-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501`.

---

## 📁 Project Structure

```bash
house-price-prediction/
├── app.py                  # Main Streamlit application file
├── house_price_model.pkl   # Serialized trained model (Joblib)
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── Data/                   # (Optional) Raw dataset
    └── Bengaluru_House_Data.csv
```

---

## 🌟 Live Demo

Check out the live application here: **[https://house-price-prediction-99.streamlit.app/]**

<img width="1876" height="752" alt="Screenshot 2026-05-11 055042" src="https://github.com/user-attachments/assets/adcf2bbb-2d5b-48b8-8ac6-a85f7b57a7be" />

---

## 📄 Dataset

The dataset used for this project is the **Bengaluru House Price Data** available on Kaggle.
*   Source: [Kaggle - Bengaluru House Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
*   Size: ~13,000 records.

---

## 🔮 Future Scope

*   **Spatial Analysis:** Integrate Latitude/Longitude data to calculate distances from key amenities (schools, malls, metro).
*   **Sentiment Analysis:** Analyze description text for keywords that boost value.
*   **Deep Learning:** Explore Neural Networks for potentially higher accuracy on larger datasets.

---

## 👨‍💻 Author

**PavanKumarAadelli**
*   GitHub: [https://github.com/PavanKumarAadelli]
*   LinkedIn: [https://www.linkedin.com/in/pavan-kumar-aadelli-1998043a0/]
