# Heart Disease Prediction
This project aims to predict the presence of heart disease in patients using machine learning techniques. It utilizes the Cleveland Heart Disease dataset from the UCI Machine Learning Repository.

## Dataset
Source: [UCI Machine Learning Repository - Heart Disease](https://archive.ics.uci.edu/ml/datasets/heart+Disease)

Description: The dataset contains 303 instances with 14 attributes, including age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, ST depression induced by exercise, the slope of the peak exercise ST segment, number of major vessels colored by fluoroscopy, thalassemia, and the target variable indicating the presence of heart disease.

## Project Structure
Heart-Disease/
├── data/                 # Contains the dataset files
├── deployment/           # Scripts and files related to model deployment
├── models/               # Saved machine learning models
├── notebooks/            # Jupyter notebooks for data analysis and model training
├── results/              # Output results, such as evaluation metrics and plots
├── ui/                   # User interface components (if any)
├── .gitignore            # Specifies files to ignore in version control
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies

## Usage
### 1. Data Preparation:

Ensure that the dataset is placed in the data/ directory. If not already present, download the Cleveland Heart Disease dataset from the UCI Repository and place it in the data/ folder.

### 2. Exploratory Data Analysis (EDA):

Navigate to the notebooks/ directory and open the EDA notebook to explore the dataset, understand feature distributions, and identify any data preprocessing needs.

### 3. Model Training:

Use the training notebook in the notebooks/ directory to train machine learning models. This notebook includes data preprocessing steps, model selection, training, and evaluation

### 4. Model Evaluation:

After training, evaluate the model's performance using appropriate metrics such as accuracy, precision, recall, F1-score, and ROC-AUC. Visualizations like confusion matrices and ROC curves can be found in the results/ directory.

### 5. Deployment:

The deployment/ directory contains scripts and configurations to deploy the trained model. Follow the instructions in the deployment README or scripts to set up the deployment environment


## Results
Key findings and model performance metrics are documented in the results/ directory. This includes:

Confusion matrices

ROC curves

Precision-Recall curves

Model comparison tables

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
