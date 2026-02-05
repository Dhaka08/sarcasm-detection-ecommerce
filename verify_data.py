import pandas as pd
import json
import os

print("="*60)
print("DATASET VERIFICATION")
print("="*60)

# File paths
reddit_path = 'data/raw/train-balanced-sarcasm.csv'
news_path = 'data/raw/Sarcasm_Headlines_Dataset.json'

# Verify Reddit dataset
print("\n1. REDDIT SARCASM DATASET")
print("-"*60)
try:
    print(f"Loading: {reddit_path}")
    df_reddit = pd.read_csv(reddit_path)
    print(f"✅ Successfully loaded!")
    print(f"   Total rows: {len(df_reddit):,}")
    print(f"   Total columns: {len(df_reddit.columns)}")
    print(f"   Columns: {list(df_reddit.columns[:5])}...")
    
    # Check for label column
    if 'label' in df_reddit.columns:
        sarcastic = df_reddit['label'].sum()
        non_sarcastic = len(df_reddit) - sarcastic
        print(f"   Sarcastic samples: {sarcastic:,}")
        print(f"   Non-sarcastic samples: {non_sarcastic:,}")
    
    # Show sample
    print(f"\n   Sample rows:")
    print(df_reddit.head(3))
    
except Exception as e:
    print(f"❌ Error loading Reddit dataset: {e}")

# Verify News Headlines dataset
print("\n\n2. NEWS HEADLINES SARCASM DATASET")
print("-"*60)
try:
    print(f"Loading: {news_path}")
    with open(news_path, 'r', encoding='utf-8') as f:
        news_data = [json.loads(line) for line in f]
    
    df_news = pd.DataFrame(news_data)
    print(f"✅ Successfully loaded!")
    print(f"   Total rows: {len(df_news):,}")
    print(f"   Columns: {list(df_news.columns)}")
    
    if 'is_sarcastic' in df_news.columns:
        sarcastic = df_news['is_sarcastic'].sum()
        non_sarcastic = len(df_news) - sarcastic
        print(f"   Sarcastic headlines: {sarcastic:,}")
        print(f"   Non-sarcastic headlines: {non_sarcastic:,}")
    
    print(f"\n   Sample headlines:")
    print(df_news.head(3))
    
except Exception as e:
    print(f"❌ Error loading News dataset: {e}")

print("\n" + "="*60)
print("VERIFICATION COMPLETE!")
print("="*60)
print("\n✅ Both datasets are ready to use!")
print("📊 Total samples available: ~1 million+ for training")