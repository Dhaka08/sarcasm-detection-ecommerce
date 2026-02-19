**# Project Architecture**



**## System Overview**

**```**

**┌─────────────────────────────────────────────────────────────┐**

**│                    SARCASM DETECTION SYSTEM                  │**

**└─────────────────────────────────────────────────────────────┘**



**┌─────────────────┐**

**│   DATA LAYER    │**

**└────────┬────────┘**

         **│**

         **├─► Reddit Dataset (1M samples)**

         **├─► News Headlines (28k samples)**  

         **└─► Indian Reviews (150 samples - Novel)**

         **│**

         **▼**

**┌─────────────────┐**

**│ PREPROCESSING   │**

**└────────┬────────┘**

         **│**

         **├─► Text Cleaning**

         **├─► Tokenization**

         **├─► Feature Extraction**

         **└─► Data Augmentation**

         **│**

         **▼**

**┌─────────────────────────────────────────────────────────────┐**

**│                     MODEL LAYER                              │**

**├─────────────────────────────────────────────────────────────┤**

**│                                                              │**

**│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │**

**│  │   Baseline   │  │     LSTM     │  │     BERT     │     │**

**│  │  Logistic    │  │ Bidirectional│  │  Fine-tuned  │     │**

**│  │  Regression  │  │   + GloVe    │  │ Transformer  │     │**

**│  │              │  │              │  │              │     │**

**│  │   66.41%     │  │   ~75%       │  │   83.33%     │     │**

**│  └──────────────┘  └──────────────┘  └──────────────┘     │**

**│                                                              │**

**└──────────────────────────┬───────────────────────────────────┘**

                          **│**

                          **▼**

**┌─────────────────────────────────────────────────────────────┐**

**│                    APPLICATION LAYER                         │**

**├─────────────────────────────────────────────────────────────┤**

**│                                                              │**

**│  ┌────────────────────────────────────────────────────┐    │**

**│  │           STREAMLIT WEB APPLICATION                 │    │**

**│  │                                                      │    │**

**│  │  • Single Review Analysis                           │    │**

**│  │  • Batch CSV Processing                             │    │**

**│  │  • Confidence Scoring                               │    │**

**│  │  • Sarcasm Type Classification                      │    │**

**│  │  • Hinglish Support                                 │    │**

**│  │  • Results Download                                 │    │**

**│  └────────────────────────────────────────────────────┘    │**

**│                                                              │**

**└─────────────────────────────────────────────────────────────┘**

**```**



**## Data Flow**

**```**

**User Input**

    **│**

    **▼**

**┌─────────────┐**

**│ Text Input  │**

**└──────┬──────┘**

       **│**

       **▼**

**┌─────────────┐      ┌──────────────┐**

**│ Tokenizer   │─────►│ BERT Model   │**

**└─────────────┘      └──────┬───────┘**

                             **│**

                             **▼**

                      **┌──────────────┐**

                      **│ Prediction   │**

                      **│ • Label      │**

                      **│ • Confidence │**

                      **│ • Type       │**

                      **└──────┬───────┘**

                             **│**

                             **▼**

                      **┌──────────────┐**

                      **│ UI Display   │**

                      **└──────────────┘**

**```**



**## Technology Stack**

**```**

**┌─────────────────────────────────────────────────────┐**

**│                  FRONTEND / UI                       │**

**│  • Streamlit (Web Framework)                        │**

**│  • Custom CSS (Styling)                             │**

**│  • HTML/Markdown (Content)                          │**

**└─────────────────────────────────────────────────────┘**

                          **▲**

                          **│**

**┌─────────────────────────────────────────────────────┐**

**│              ML / BACKEND PROCESSING                 │**

**│  • PyTorch / TensorFlow (Deep Learning)             │**

**│  • Hugging Face Transformers (BERT)                 │**

**│  • Scikit-learn (Classical ML)                      │**

**│  • NLTK (Text Processing)                           │**

**└─────────────────────────────────────────────────────┘**

                          **▲**

                          **│**

**┌─────────────────────────────────────────────────────┐**

**│               DATA PROCESSING                        │**

**│  • Pandas (Data Manipulation)                       │**

**│  • NumPy (Numerical Computing)                      │**

**│  • Matplotlib/Seaborn (Visualization)               │**

**└─────────────────────────────────────────────────────┘**

**```**



**## Model Progression**

**```**

**Baseline → LSTM → BERT → Production**

**66.41%     ~75%    83.33%   Demo App**



**Improvement: +16.92% absolute**

**```**



**## File Structure**

**```**

**sarcasm-detection-ecommerce/**

**├── app/                    # Streamlit application**

**├── data/                   # Datasets**

**│   ├── raw/               # Original data**

**│   ├── processed/         # Cleaned data**

**│   └── indian\_reviews/    # Novel dataset**

**├── notebooks/              # Jupyter notebooks (6 total)**

**├── results/               # Visualizations \& findings**

**├── models/                # Trained models**

**└── docs/                  # Documentation**

**```**



**## Deployment Options**

**```**

**Local Deployment:**

   **streamlit run app.py**



**Cloud Deployment (Future):**

   **• Streamlit Cloud (Free)**

   **• Heroku (Containerized)**

   **• AWS EC2 (Production)**

   **• Docker (Portable)**

**```**

