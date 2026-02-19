import streamlit as st
import pandas as pd
import time
from model_loader import SarcasmDetector

# Page configuration
st.set_page_config(
    page_title="Sarcasm Detection | Indian E-commerce",
    page_icon="😏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-top: 0;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        color: #000 !important;
    }
    .result-box h3 {
        color: #000 !important;
        margin-top: 0;
    }
    .result-box p {
        color: #000 !important;
        font-size: 1.1rem;
        margin: 8px 0;
    }
    .result-box strong {
        color: #000 !important;
    }
    .sarcastic {
        background-color: #ffe6e6;
        border-left: 5px solid #e74c3c;
    }
    .not-sarcastic {
        background-color: #e6ffe6;
        border-left: 5px solid #2ecc71;
    }
</style>
""", unsafe_allow_html=True)

# Initialize model (cache it so it loads only once)
@st.cache_resource
def load_detector():
    detector = SarcasmDetector()
    success = detector.load_model()
    if success:
        return detector
    return None

# Title
st.markdown('<h1 class="main-header">😏 Sarcasm Detection</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Powered by BERT | Trained on Indian E-commerce Reviews</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📊 Model Information")
    st.write("""
    **Architecture:** BERT-base-uncased  
    **Training Data:** 50k Reddit + 150 Indian reviews  
    **Accuracy:** 83.33% on Indian data  
    **Supported Languages:** English + Hinglish
    """)
    
    st.header("🎯 Sarcasm Types Detected")
    st.write("""
    1. **Exaggerated Positivity**  
       Praising clearly bad products
    
    2. **Praise-Criticism**  
       Positive words, negative experience
    
    3. **Hinglish Sarcasm**  
       Hindi-English mixed sarcasm
    
    4. **Cultural Reference**  
       Indian cultural references
    
    5. **Rhetorical Question**  
       Sarcastic questions
    """)
    
    st.header("👨‍💻 About")
    st.write("""
    **Project:** Sarcasm Detection  
    **Student:** Himanshu Dhaka  
    **Course:** PBL - Semester 6  
    **Duration:** 1 month
    """)
    
    st.markdown("---")
    st.caption("🔗 [GitHub Repository](#)")

# Load model
detector = load_detector()

if detector is None:
    st.error("⚠️ Model failed to load. Please check installation.")
    st.stop()

st.success("✅ Model loaded successfully!")

# Main area
st.header("🔍 Test Sarcasm Detection")

# Text input
user_input = st.text_area(
    "Enter a product review:",
    placeholder="Example: Amazing quality! Broke in exactly 2 days.",
    height=120,
    help="Type or paste a product review to check for sarcasm"
)

# Predict button
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    predict_button = st.button("🔍 Detect Sarcasm", type="primary", use_container_width=True)

with col2:
    clear_button = st.button("🗑️ Clear", use_container_width=True)

if clear_button:
    st.rerun()

if predict_button:
    if user_input.strip():
        with st.spinner("🤖 Analyzing review..."):
            # Simulate processing time
            time.sleep(0.5)
            
            # Get prediction
            result = detector.predict(user_input)
            
            st.markdown("---")
            st.subheader("📊 Analysis Results")
            
            # Results display
            if result['is_sarcastic']:
                st.markdown(f"""
                <div class="result-box sarcastic">
                    <h3>🎭 SARCASM DETECTED</h3>
                    <p><strong>Confidence:</strong> {result['confidence']:.2f}%</p>
                    <p><strong>Type:</strong> {result['sarcasm_type']}</p>
                    <p><strong>Explanation:</strong> {result['explanation']}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-box not-sarcastic">
                    <h3>✅ GENUINE REVIEW</h3>
                    <p><strong>Confidence:</strong> {result['confidence']:.2f}%</p>
                    <p><strong>Explanation:</strong> {result['explanation']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Detailed metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    "Sarcasm", 
                    "Yes" if result['is_sarcastic'] else "No",
                    delta=None
                )
            
            with col2:
                st.metric(
                    "Confidence",
                    f"{result['confidence']:.1f}%"
                )
            
            with col3:
                st.metric(
                    "Type",
                    result['sarcasm_type'] if result['sarcasm_type'] else "N/A"
                )
            
            with col4:
                reliability = "High" if result['confidence'] > 80 else "Medium" if result['confidence'] > 60 else "Low"
                st.metric("Reliability", reliability)
                
    else:
        st.warning("⚠️ Please enter a review to analyze!")

# Examples section
st.markdown("---")
st.header("📝 Try Example Reviews")

examples_data = {
    "Sarcastic - Electronics": {
        "text": "Amazing phone! Battery lasts a whole 2 hours. Truly revolutionary technology!",
        "emoji": "📱"
    },
    "Sarcastic - Hinglish": {
        "text": "Ekdum first class product hai bhai! Sirf teen din mein toot gaya. Paisa vasool!",
        "emoji": "🇮🇳"
    },
    "Genuine - Positive": {
        "text": "Good product for the price. Camera quality is decent and battery lasts all day.",
        "emoji": "✅"
    },
    "Sarcastic - Clothing": {
        "text": "Perfect fit! I ordered XL and got what appears to be clothing for a 5 year old.",
        "emoji": "👕"
    },
    "Sarcastic - Delivery": {
        "text": "Superfast delivery! Ordered on Monday, received on following Saturday of next month.",
        "emoji": "📦"
    },
    "Genuine - Negative": {
        "text": "Product quality is poor. Color faded after first wash. Not worth the price.",
        "emoji": "❌"
    }
}

cols = st.columns(3)

for idx, (label, data) in enumerate(examples_data.items()):
    col = cols[idx % 3]
    with col:
        if st.button(f"{data['emoji']} {label}", use_container_width=True):
            st.text_area("Selected Review:", value=data['text'], height=100, disabled=True)
            
            # Auto-predict
            with st.spinner("Analyzing..."):
                time.sleep(0.3)
                result = detector.predict(data['text'])
                
                if result['is_sarcastic']:
                    st.error(f"🎭 SARCASTIC ({result['confidence']:.1f}%)")
                    st.caption(f"Type: {result['sarcasm_type']}")
                else:
                    st.success(f"✅ GENUINE ({result['confidence']:.1f}%)")

# Batch analysis section
st.markdown("---")
st.header("📊 Batch Analysis")

st.write("Upload a CSV file with reviews to analyze multiple at once.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=['csv'],
    help="CSV should have a column named 'review_text'"
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        st.write(f"**Uploaded:** {uploaded_file.name}")
        st.write(f"**Total reviews:** {len(df)}")
        
        # Check for review column
        review_column = None
        for col in ['review_text', 'review', 'text', 'comment', 'content']:
            if col in df.columns:
                review_column = col
                break
        
        if review_column:
            st.success(f"✅ Found review column: '{review_column}'")
            
            if st.button("🔍 Analyze All Reviews", type="primary"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                results = []
                
                for idx, review in enumerate(df[review_column][:100]):  # Limit to 100
                    if pd.notna(review):
                        result = detector.predict(str(review))
                        results.append(result)
                    else:
                        results.append({
                            'is_sarcastic': False,
                            'confidence': 0,
                            'sarcasm_type': None,
                            'explanation': 'Empty review'
                        })
                    
                    # Update progress
                    progress = (idx + 1) / min(len(df), 100)
                    progress_bar.progress(progress)
                    status_text.text(f"Analyzing... {idx + 1}/{min(len(df), 100)}")
                
                # Add results to dataframe
                df_results = df.head(100).copy()
                df_results['is_sarcastic'] = [r['is_sarcastic'] for r in results]
                df_results['confidence'] = [r['confidence'] for r in results]
                df_results['sarcasm_type'] = [r['sarcasm_type'] for r in results]
                
                st.success("✅ Analysis complete!")
                
                # Summary statistics
                col1, col2, col3 = st.columns(3)
                
                sarcastic_count = sum([r['is_sarcastic'] for r in results])
                avg_confidence = sum([r['confidence'] for r in results]) / len(results)
                
                with col1:
                    st.metric("Total Analyzed", len(results))
                
                with col2:
                    st.metric("Sarcastic Reviews", sarcastic_count)
                
                with col3:
                    st.metric("Avg Confidence", f"{avg_confidence:.1f}%")
                
                # Show results
                st.subheader("📋 Results")
                st.dataframe(df_results[[review_column, 'is_sarcastic', 'confidence', 'sarcasm_type']])
                
                # Download results
                csv = df_results.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results as CSV",
                    data=csv,
                    file_name="sarcasm_analysis_results.csv",
                    mime="text/csv"
                )
        else:
            st.error("❌ Could not find a review column. Please ensure your CSV has a column named 'review_text', 'review', or 'text'.")
            
    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")


# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎓 <strong>Research Project</strong> | Sarcasm Detection in Indian E-commerce Reviews</p>
    <p>Built with Streamlit 🎈 | Powered by BERT 🤖</p>
</div>
""", unsafe_allow_html=True)