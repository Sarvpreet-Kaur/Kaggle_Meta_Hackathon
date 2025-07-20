# 🌍 Kaggle Meta Hackathon – Interactive Data Insights

An interactive data exploration project built for the **Kaggle Meta Hackathon**, combining in-depth notebook analysis with a polished Streamlit frontend. This tool highlights global AI talent on Kaggle through medal efficiency, user trends, and modeling behavior.

---

## 📁 Project Overview

This repository contains:

- 📓 A **Jupyter Notebook** for data preprocessing and exploratory analysis.<br>
- 🌐 A **Streamlit app** to visualize and interact with key insights.<br>
- 📦 A `requirements.txt` to reproduce the environment.<br>
- 
---

## ⚙️ Setup Instructions

Follow these steps to run the project locally.  

### 1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git<br>  
cd your-repo-name  

### 2. Prepare the Dataset
Create a data/ folder inside the project directory and add the required Kaggle dataset files:<br>  

/data/
├── users.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-users-cleaned-dataset<br>
├── teams.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-dataset-teams-cleaned<br>
├── team-members.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-dataset-team-members-cleaned<br>
├── scripts.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-scripts-cleaned-dataset<br>
├── user-achievements.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-dataset-user-achievements-cleaned<br>
├── competitions.csv - https://www.kaggle.com/datasets/sarvpreetkaur22/meta-kaggle-competitions-cleaned-dataset<br>

💡 Ensure the filenames match exactly or adjust app.py and the notebook accordingly.

### 3. Set Up a Virtual Environment<br>
python -m venv venv

** Activate the environment **
 * On Windows:<br>
venv\Scripts\activate

 * On macOS/Linux:<br>
source venv/bin/activate

### 4. Install Dependencies<br>
pip install -r requirements.txt

### 5. Run the Jupyter Notebook 
Open the notebook in Jupyter or VS Code to explore the data and preprocessing steps:<br>
ai-without-borders-meta-hackathon.ipynb

### 6. Launch the Streamlit Dashboard
streamlit run app.py<br>
This will open the interactive dashboard in your browser, where you can:
* Filter countries by region and medal efficiency
* View top countries by Kaggle user base
* Analyze modeling keyword and tool trends
* Export filtered results as Excel or PDF
--- 

## 📊 Features:

✅ Region-based filtering<br>
✅ Top countries by efficiency and user count<br>
✅ Keyword and tool usage visualizations<br>
✅ Exportable reports<br>
✅ Fully interactive frontend<br>

## 🧪 Tech Stack
* Python 3.13
* Pandas, Seaborn, Matplotlib
* Streamlit
* Pycountry / pycountry-convert
* nltk
