import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION & TITLE ---
st.set_page_config(page_title="AI-NIDS Dashboard", layout="wide")
st.title("🛡️ AI-Based Network Intrusion Detection System")
st.markdown("### Real-time anomaly detection using Random Forest")

# --- 2. DATA LOADING (SIMULATION MODE) ---
@st.cache_data
def load_data():
    # Simulating a network traffic dataset since external CSV might not be available
    # Features: Destination Port, Flow Duration, Total Fwd Packets, Total Backward Packets, Packet Length
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'Destination Port': np.random.randint(0, 65535, n_samples),
        'Flow Duration': np.random.randint(0, 100000, n_samples),
        'Total Fwd Packets': np.random.randint(1, 100, n_samples),
        'Total Backward Packets': np.random.randint(1, 100, n_samples),
        'Total Length of Fwd Packets': np.random.randint(0, 5000, n_samples),
        'Label': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]) # 0=Benign, 1=Malicious
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

# --- 3. SIDEBAR: MODEL TRAINING ---
st.sidebar.header("🔧 Control Panel")
st.sidebar.subheader("Model Configuration")

if st.sidebar.button("Train Model Now"):
    with st.spinner("Training Random Forest Classifier..."):
        # Features and Target
        X = df.drop('Label', axis=1)
        y = df['Label']
        
        # Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # Train Model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        st.session_state['model'] = model
        st.session_state['accuracy'] = acc
        st.sidebar.success(f"Model Trained! Accuracy: {acc:.2f}")

# --- 4. MAIN DASHBOARD ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Network Traffic Data (Preview)")
    st.dataframe(df.head(30))
    
    st.subheader("📈 Traffic Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='Label', data=df, ax=ax, palette="viridis")
    plt.xticks([0, 1], ['Benign (Safe)', 'Malicious (Attack)'])
    st.pyplot(fig)

# --- 5. LIVE SIMULATION SECTION ---
with col2:
    st.subheader("🚨 Live Traffic Simulator")
    st.info("Input packet details to test the model.")
    
    p1 = st.number_input("Destination Port", 0, 65535, 80)
    p2 = st.number_input("Flow Duration", 0, 1000000, 500)
    p3 = st.number_input("Total Fwd Packets", 0, 1000, 10)
    p4 = st.number_input("Total Backward Packets", 0, 1000, 8)
    p5 = st.number_input("Total Length Fwd Packets", 0, 10000, 500)
    
    if st.button("Analyze Packet"):
        if 'model' in st.session_state:
            input_data = np.array([[p1, p2, p3, p4, p5]])
            prediction = st.session_state['model'].predict(input_data)
            
            if prediction[0] == 1:
                st.error("⚠️ ALERT: Malicious Traffic Detected!")
            else:
                st.success("✅ Traffic is Benign (Safe).")
        else:
            st.warning("Please train the model from the Sidebar first!")

# --- 6. FOOTER ---
st.markdown("---")

st.caption("AI-Based NIDS Project | VOIS Internship | Developed by Chinmay Patil")
