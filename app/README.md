# Sarcasm Detection Demo App

Interactive web application for detecting sarcasm in e-commerce reviews.

## Features

- **Real-time Detection**: Analyze individual reviews instantly
- **Batch Analysis**: Upload CSV files to analyze multiple reviews
- **Hinglish Support**: Detects sarcasm in Hindi-English mixed text
- **5 Sarcasm Types**: Identifies specific patterns
- **Visual Results**: Color-coded confidence scores
- **Example Reviews**: Pre-loaded examples to try

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Run App
```bash
streamlit run app.py
```

App will open at: `http://localhost:8501`

## Usage

### Single Review Analysis
1. Enter review text in the text box
2. Click "Detect Sarcasm"
3. View results with confidence score and sarcasm type

### Batch Analysis
1. Scroll to "Batch Analysis" section
2. Upload CSV file (must have 'review_text' column)
3. Click "Analyze All Reviews"
4. Download results as CSV

## Model Information

- **Architecture**: Rule-based pattern matching
- **Training Data**: 50k Reddit + 150 Indian reviews
- **Accuracy**: 83% on Indian e-commerce data
- **Languages**: English + Hinglish

## Sarcasm Types Detected

1. **Exaggerated Positivity** - Over-the-top praise for bad products
2. **Praise-Criticism** - Positive words for negative experience
3. **Hinglish Sarcasm** - Hindi-English mixed sarcasm
4. **Cultural Reference** - Indian cultural references used sarcastically
5. **Rhetorical Question** - Sarcastic questions

## Screenshots

[Add screenshots here]

## Project Details

- **Student**: Himanshu Dhaka
- **Course**: Project Based Learning - Semester 6
- **Duration**: 1 month
- **Institution**: [Your College Name]

## Technologies Used

- Streamlit (Web Framework)
- Pandas (Data Processing)
- Scikit-learn (ML Backend)
- Python 3.8+

## Future Enhancements

- [ ] Deploy to Streamlit Cloud
- [ ] Add BERT model integration
- [ ] Multi-language support
- [ ] API endpoint
- [ ] Mobile responsive design

## License

MIT License