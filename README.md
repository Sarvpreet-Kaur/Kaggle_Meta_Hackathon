# 🌍 Kaggle Meta Hackathon – Interactive Data Insights

An interactive data exploration project built for the **Kaggle Meta Hackathon**, combining in-depth notebook analysis with a polished Streamlit frontend. This tool highlights global AI talent on Kaggle through medal efficiency, user trends, and modeling behavior.

---

## 📁 Project Overview

This repository contains:

- 📓 A **Jupyter Notebook** for data preprocessing and exploratory analysis.
- 🌐 A **Streamlit app** to visualize and interact with key insights.
- 📦 A `requirements.txt` to reproduce the environment.
- 
---

## ⚙️ Setup Instructions

Follow these steps to run the project locally.

### 1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Prepare the Dataset
Create a data/ folder inside the project directory and add the required Kaggle dataset files:

/data/
├── users.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-users-cleaned-dataset
├── teams.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-dataset-teams-cleaned
├── team-members.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-dataset-team-members-cleaned
├── scripts.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-scripts-cleaned-dataset
├── user-achievements.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-dataset-user-achievements-cleaned
├── competitions.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-competitions-cleaned-dataset

💡 Ensure the filenames match exactly or adjust app.py and the notebook accordingly.

### 3. Set Up a Virtual Environment
python -m venv venv
# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

### 4. Install Dependencies
pip install -r requirements.txt

### 5. Run the Jupyter Notebook 
Open the notebook in Jupyter or VS Code to explore the data and preprocessing steps:
ai-without-borders-meta-hackathon.ipynb

### 6. Launch the Streamlit Dashboard
streamlit run app.py
This will open the interactive dashboard in your browser, where you can:
* Filter countries by region and medal efficiency
* View top countries by Kaggle user base
* Analyze modeling keyword and tool trends
* Export filtered results as Excel or PDF

📊 Features
✅ Region-based filtering
✅ Top countries by efficiency and user count
✅ Keyword and tool usage visualizations
✅ Exportable reports
✅ Fully interactive frontend

🧪 Tech Stack
Python 3.13
Pandas, Seaborn, Matplotlib
Streamlit
Pycountry / pycountry-convert
nltk
