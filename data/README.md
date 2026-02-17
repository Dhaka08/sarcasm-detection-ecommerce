**# Data Directory**



**## Structure**



**data/**

**├── raw/                          # Original downloaded datasets**

**│   ├── train-balanced-sarcasm.csv        (1M Reddit - not tracked)**

**│   └── Sarcasm\_Headlines\_Dataset.json    (28k headlines - not tracked)**

**│**

**├── processed/                    # Preprocessed datasets**

**│   ├── preprocessed\_data.csv             (1M samples - not tracked)**

**│   └── preprocessed\_data\_sample\_50k.csv  (50k sample - not tracked)**

**│**

**└── indian\_reviews/               # Novel Indian dataset (tracked)**

&nbsp;   \*\*├── indian\\\_reviews\\\_dataset.csv         (150 annotated reviews)\*\*

    \*\*└── annotation\\\_guidelines.md           (labeling instructions)\*\*






**## Note on Large Files**

**Large CSV files are excluded from Git via .gitignore**

**to keep repository size manageable.**



**## Download Datasets**

**1. Reddit Sarcasm:**

**https://www.kaggle.com/datasets/danofer/sarcasm**

**2. News Headlines:**

**https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection**

**```**

