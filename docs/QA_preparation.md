# Q&A Preparation Guide

## Technical Questions

### Q1: Why did you choose BERT over other models?
**Answer:** BERT was chosen for three main reasons: (1) Pre-trained on massive text corpus for better context understanding, (2) Bidirectional attention mechanism, and (3) State-of-the-art performance on NLP tasks. I compared it with Logistic Regression (66.41%) and LSTM (~75%) to demonstrate progressive improvement. BERT achieved 83.33% on Indian data.

### Q2: How did you handle Hinglish text?
**Answer:** BERT-base was pre-trained on multilingual data including Hindi. For Hinglish, I: (1) Preserved Hindi words during preprocessing, (2) Leveraged BERT's subword tokenization, (3) Included 20+ Hinglish examples in training, achieving 80% accuracy on Hinglish sarcasm.

### Q3: How did you collect the Indian dataset?
**Answer:** Manually collected 150 reviews from Amazon India and Flipkart. Process: identified products with controversial reviews, annotated with 5 sarcasm categories, created annotation guidelines, ensured balanced distribution. This is a novel contribution as no Indian e-commerce sarcasm dataset existed.

### Q4: Why higher accuracy on Indian data vs Reddit?
**Answer:** Indian e-commerce reviews have clearer sarcasm markers: (1) Star-rating contradictions, (2) Excessive punctuation, (3) Explicit temporal irony, (4) More obvious patterns. Reddit sarcasm is subtle and context-dependent.

### Q5: What preprocessing steps did you use?
**Answer:** Multi-step pipeline: (1) Text cleaning - removed URLs/mentions, normalized whitespace, kept punctuation, (2) Tokenization using BERT tokenizer with max length 64, (3) Feature engineering - TF-IDF for baseline, contextual embeddings for BERT.

### Q6: Training time for each model?
**Answer:** Baseline: 2-3 minutes (CPU), LSTM: 45-60 minutes (CPU), BERT: 15-20 minutes (GPU on Google Colab T4).

### Q7: BERT hyperparameters?
**Answer:** Learning rate: 2e-5, Optimizer: AdamW, Batch size: 32, Epochs: 3, Max sequence length: 64. Based on BERT paper recommendations.

### Q8: Production deployment strategy?
**Answer:** Immediate: Streamlit Cloud. Scalable: FastAPI REST API. Enterprise: AWS/Azure with load balancing. Optimize with model distillation. Monitor accuracy drift.

### Q9: Limitations of your approach?
**Answer:** (1) Small Indian dataset (150 reviews), (2) English/Hinglish only, (3) Subtle sarcasm still challenging, (4) Slower BERT inference, (5) No emoji analysis. These are future work opportunities.

### Q10: How does this compare to existing research?
**Answer:** Novel contributions: (1) First Indian e-commerce sarcasm dataset, (2) Hinglish code-mixing analysis, (3) Cultural context capture. Existing work focused on Western datasets, English-only, no e-commerce focus.

---

## Project Management Questions

### Q11: Main challenges faced?
**Answer:** (1) Manual annotation time-consuming - solved with clear guidelines, (2) Limited GPU access - optimized with 50k samples, (3) Hinglish handling - leveraged BERT multilingual capability.

### Q12: Project timeline?
**Answer:** Completed in 9 days: Days 1-2 (data), Days 3-5 (models), Day 6 (Indian dataset), Day 7 (demo), Days 8-9 (documentation). Total 40-45 hours over 1 month.

### Q13: What would you do differently?
**Answer:** (1) Start with smaller dataset for iteration, (2) Use pre-trained Hinglish models, (3) Collect Indian data earlier, (4) Plan GPU usage better, (5) Document continuously.

---

## Future Work Questions

### Q14: Future improvements?
**Answer:** Priority: (1) Expand to 1000+ reviews, (2) Add Tamil/Telugu support, (3) Multi-modal analysis (emoji/images). Technical: model distillation, active learning, ensemble methods.

### Q15: Production readiness?
**Answer:** Demo-ready with 83% accuracy, batch processing, Hinglish support. For production needs: larger dataset, API endpoint, performance optimization, monitoring, A/B testing. Provides strong foundation.

---

## Quick Stats to Remember

- **Accuracy Progression:** 66.41% → ~75% → 83.33%
- **Dataset Sizes:** 1M (Reddit) + 150 (Indian novel)
- **Model Parameters:** 50K (LR) → 1.5M (LSTM) → 110M (BERT)
- **Training Time:** 2min → 60min → 20min (GPU)
- **Improvement:** +16.92% absolute from baseline
- **Novel Contribution:** First Indian e-commerce sarcasm study

---

## Confidence Boosters

**When nervous, remember:**
- ✅ You built 3 working models
- ✅ You created a novel dataset
- ✅ You achieved 83% accuracy
- ✅ You have a working demo
- ✅ You completed in 9 days
- ✅ You documented everything

**You know this project inside-out!**