# AI-Based Network Intrusion Detection System (NIDS)

## 📌 Project Overview
This project is an AI-powered security tool designed to detect malicious network traffic in real-time. It uses a **Random Forest Classifier** to analyze packet data (such as flow duration and packet length)
and classifies it as either *Malicious (Attack)*.

## 🚀 Key Features
* Real-time Dashboard: Interactive UI built with Streamlit.
* Machine Learning: Random Forest model for high-accuracy anomaly detection.
* Traffic Simulation: Built-in simulator to generate test packets.
* Visualizations: Charts showing traffic distribution and classification results.

## 🛠️ Technology Stack
* Language: Python 3.8+
* GUI Framework: Streamlit
* ML Library: Scikit-Learn
* Data Processing: Pandas, NumPy

## 🔧 How to Run
1.  Install dependencies:
    ```bash
    pip install pandas numpy scikit-learn streamlit seaborn matplotlib
    ```
2.  Run the application:
    ```bash
    streamlit run nids_main.py
    ```

---
*Developed by Chinmay Patil for the VOIS AICTE Internship (Batch 2).*
