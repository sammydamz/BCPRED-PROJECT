# BCPRED - Breast Tumor Classification Tool

This repository contains a web application developed for breast tumor classification using machine learning techniques. The application employs the powerful XGBoost algorithm to predict whether a breast tumor is malignant or benign based on Fine Needle Aspiration (FNA) cell feature parameters.

## Features

Accurate breast tumor classification using the XGBoost algorithm
User-friendly web interface built with the Streamlit framework
Comprehensive model evaluation and selection process
Utilization of popular Python libraries for data manipulation, visualization, and machine learning

## Dataset

The project utilizes the Wisconsin Breast Cancer Database (WBCD) dataset, which includes 569 samples with 30 features describing characteristics of cell nuclei present in digitized images of FNA samples. The dataset is preprocessed, and relevant features are selected for model training and evaluation.

## Tools Used

- Python: The primary programming language used for the project.
- Machine Learning Libraries: NumPy, Pandas, Scikit-learn, XGBoost.
- Data Visualization Libraries: Matplotlib, Seaborn.
- Web Development: Streamlit framework.

## Getting Started

1. Clone the repository: git clone https://github.com/your-username/breast-tumor-classification.git
2. Install the required dependencies: pip install -r requirements.txt
3. Run the web application: streamlit run app.py
4. Access the application in your web browser at the provided local URL.
