💼 College Placement Salary Prediction App



An end-to-end Machine Learning project that predicts a candidate’s expected salary based on academic, cognitive, and personal features.

The project covers data preprocessing, feature engineering, model training, and deployment using Streamlit.



📌 Project Overview



This project demonstrates how a real-world ML system is built and deployed:



Handles missing values gracefully



Uses a single ML pipeline for training and inference



Allows optional user inputs (no forced fields)



Provides a clean and interactive Streamlit UI



Deployed-ready and version-controlled using GitHub



🎯 Problem Statement



Predict the monthly salary (INR) of a candidate based on:



Academic performance



Cognitive ability



Work experience



Personal and financial attributes



📊 Dataset Features

Feature	Description

CGPA	Academic performance (0–10)

IQ	Cognitive ability score

Year\_of\_Experience	Total years of work experience

Dependents	Number of dependents

Expenses	Monthly expenses (INR)

Gender	Male / Female

Marital\_Status	Single / Married

Target	Salary (INR per month)



⚠️ The dataset intentionally contains missing values to simulate real-world scenarios.



🧠 Machine Learning Approach

🔹 Model Used



Multiple Linear Regression



🔹 Preprocessing \& Feature Engineering



All preprocessing is handled inside a single pipeline:



Numeric features



Median imputation (SimpleImputer)



Standard scaling (StandardScaler)



Categorical features



Mode imputation



One-Hot Encoding (OneHotEncoder)



Handles unseen categories safely



Pipeline



Ensures no data leakage



Same preprocessing during training \& prediction



⚠️ Handling Missing \& Invalid Inputs



Users may leave any input field empty



Empty or invalid values are converted to None



Missing values are handled by the trained pipeline



Out-of-range values are safely ignored and imputed



Business rule applied to avoid unrealistic salary predictions



🖥️ Streamlit Web Application

Features



Clean \& user-friendly UI



Two-column input layout



Optional inputs (no forced restrictions)



Real-time salary prediction



Visual feedback \& messages



ℹ️ Linear Regression is unconstrained; therefore, a minimum realistic salary floor is applied to avoid negative predictions.



📁 Project Structure

College\_Placement/

│

├── app.py                  # Streamlit application

├── model\_training.ipynb    # Data cleaning \& model training

├── salary\_model.pkl        # Trained ML pipeline

├── data.csv                # Dataset

├── requirements.txt        # Dependencies

├── README.md               # Project documentation

└── .gitignore



🚀 How to Run Locally

1️⃣ Clone the repository

git clone https://github.com/sadafkhan0509/College\_Placement.git

cd College\_Placement



2️⃣ Create \& activate virtual environment

python -m venv venv

venv\\Scripts\\activate



3️⃣ Install dependencies

pip install -r requirements.txt



4️⃣ Run Streamlit app

python -m streamlit run app.py





Open browser at:



http://localhost:8501



🌐 Deployment



The application can be deployed using Streamlit Cloud:



Connect GitHub repository



Select app.py as entry file



Deploy



🔗 (Add live link here once deployed)



📈 Future Enhancements



Use log-transformed target for better predictions



Try tree-based models (Random Forest, XGBoost)



Add confidence intervals



Improve dataset realism



Add authentication \& logging



🧑‍💻 Author



Sadaf Khan

📘 B.Sc. Applied Component (Statistics)

📊 Aspiring Data Scientist



⭐ Key Learnings



End-to-end ML pipeline design



Handling missing \& real-world data



Model deployment using Streamlit



Debugging environment \& dependency issues



Version control with Git \& GitHub

