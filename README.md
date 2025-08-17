# Carbon-Footprint-Calculator
A simple Streamlit app for calculating the Carbon Footprint. 
# 🌍 Carbon Footprint Calculator using Advanced Machine Learning (CNN)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

A sophisticated **machine learning–driven web application** that estimates and visualizes individual CO₂ emissions using **Convolutional Neural Networks (CNN)**. Built with a focus on **scalability, usability, and environmental sustainability**.


## ✨ Key Features

- **CNN-Based Prediction** – Accurately estimates carbon footprint from user lifestyle inputs.  
- **Interactive Web Interface** – Built with **Streamlit** for real-time input & visualization.  
- **Data Pipelines** – Efficient preprocessing with **Pandas** and **NumPy**.  
- **Visual Insights** – Category breakdowns and global comparisons via **Matplotlib** and **Seaborn**.  
- **Cloud-Ready Architecture** – API-first design for easy deployment and scaling.  



## 🛠️ Tech Stack

| Category               | Tools & Libraries                                  |
|------------------------|----------------------------------------------------|
| **Programming**        | Python                                             |
| **Machine Learning**   | TensorFlow, Keras (CNN)                            |
| **Data Handling**      | Pandas, NumPy                                      |
| **Visualization**      | Matplotlib, Seaborn                                |
| **Frontend**           | Streamlit                                          |
| **Deployment**         | Cloud-ready, API-based integration                 |



## 📂 Project Workflow

```mermaid
flowchart TD
    A[User Input: Transport, Energy, Diet, Waste] --> B[Data Preprocessing - Pandas, NumPy]
    B --> C[CNN Model - TensorFlow/Keras]
    C --> D[Emission Prediction - CO2 tonnes per year]
    D --> E[Visualization - Matplotlib, Seaborn]
    E --> F[Streamlit Dashboard - Real Time Insights]
    F --> G[Country Comparison and Sustainability Analytics]

git clone https://github.com/ViivianREINE/Carbon-Footprint-Calculator-using-Advanced-Machine-Learning-CNN.git
cd Carbon-Footprint-Calculator-using-Advanced-Machine-Learning-CNN

pip install -r requirements.txt


streamlit run app.py


http://localhost:8501

Screenshots / Demo
🔹 Dashboard Home

🔹 Emission Breakdown (Category-wise)

🔹 Global Comparison Heatmap

🔹 Demo GIF (User Interaction)

Usage

1.Enter lifestyle inputs (transport, electricity, diet, waste).

2.Submit for CNN-powered carbon footprint prediction.

3.Explore interactive dashboards with category-wise breakdowns.

4.Compare results against global and national averages.

Future Enhancements

1.Add more lifestyle factors (shopping, travel, water usage).

2.Integration with live sustainability APIs.

3.Mobile-friendly dashboard version.

4.Personalized sustainability recommendations.


Author

Priyam Parashar
Biotechnology Engineering Student | AI & Sustainability Enthusiast
📍 VR Academy, Bengaluru
🎓 Mentor: Mr. Vijayanand


