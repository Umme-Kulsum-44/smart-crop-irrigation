# Smart Crop Recommendation & Irrigation (Week 1)

This repository is for my Edunet Foundation 4-week internship project.

## Week 1 (30% Progress)
- ✅ Collected dataset: `data/raw/smart-crop-irrigation.csv`
- ✅ Performed EDA & preprocessing in `notebooks/1_data_preprocessing.ipynb`
- ✅ Saved `data/processed/preprocessed.csv` and `label_encoder.joblib`
- ✅ Added basic visualizations (class balance, feature histograms)


## Week 2 Deliverables
- Model training using Random Forest Classifier
- Evaluation with accuracy and classification report
- Streamlit web app for real-time crop recommendation
- Saved model file (`rf_model.joblib`)
- Updated documentation and dependencies
  

## 🚀 How to Run This Project Locally
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Umme-Kulsum-44/smart-crop-irrigation.git
cd smart-crop-irrigation
```
### 2️⃣ Create and activate the virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run model training
```bash
Open Jupyter and run notebooks/2_model_training.ipynb.
```
### 5️⃣ Launch the Streamlit app
```bash
streamlit run app/app.py

