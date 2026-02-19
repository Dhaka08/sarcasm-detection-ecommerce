import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

class SarcasmDetector:
    def __init__(self):
        """Initialize the sarcasm detector with simple rule-based logic"""
        self.model_type = "Rule-Based + Pattern Matching"
        
        # Sarcasm indicators
        self.sarcasm_indicators = {
            'positive_words': ['amazing', 'excellent', 'perfect', 'outstanding', 
                              'fantastic', 'wonderful', 'great', 'superb', 'love'],
            'negative_context': ['broke', 'broken', 'failed', 'worst', 'terrible',
                                'useless', 'waste', 'horrible', 'disappointed', 'stopped'],
            'time_irony': ['2 days', '3 days', 'one day', 'minutes', 'hours',
                          'exactly', 'just', 'only', 'whole'],
            'hinglish': ['hai', 'bhai', 'ekdum', 'bahut', 'mast', 'sirf', 
                        'kharab', 'acha', 'bilkul', 'paisa vasool', 'toot gaya'],
            'exaggeration': ['revolutionary', 'groundbreaking', 'incredible',
                            'unbelievable', 'mind-blowing']
        }
        
        self.sarcasm_types = [
            "Exaggerated Positivity",
            "Praise-Criticism",
            "Hinglish Sarcasm",
            "Cultural Reference",
            "Rhetorical Question"
        ]
    
    def load_model(self):
        """Load model (for rule-based, just return True)"""
        print("✅ Rule-based detector ready!")
        return True
    
    def predict(self, text):
        """
        Predict sarcasm using rule-based approach
        
        Args:
            text (str): Review text to analyze
            
        Returns:
            dict: Prediction results
        """
        text_lower = text.lower()
        
        # Calculate sarcasm score
        score = 0
        reasons = []
        
        # Check for positive + negative contradiction
        has_positive = any(word in text_lower for word in self.sarcasm_indicators['positive_words'])
        has_negative = any(word in text_lower for word in self.sarcasm_indicators['negative_context'])
        
        if has_positive and has_negative:
            score += 40
            reasons.append("positive-negative contradiction")
        
        # Check for time irony
        if any(phrase in text_lower for phrase in self.sarcasm_indicators['time_irony']):
            score += 20
            reasons.append("time-based irony")
        
        # Check for exaggeration
        if any(word in text_lower for word in self.sarcasm_indicators['exaggeration']):
            score += 15
            reasons.append("exaggerated language")
        
        # Check for excessive punctuation
        if '!' in text and text.count('!') >= 2:
            score += 10
            reasons.append("excessive punctuation")
        
        # Check for rhetorical questions
        if '?' in text and any(word in text_lower for word in ['who', 'why', 'what', 'anyway', 'right']):
            score += 15
            reasons.append("rhetorical question")
        
        # Check for Hinglish
        is_hinglish = any(word in text_lower for word in self.sarcasm_indicators['hinglish'])
        if is_hinglish:
            score += 25
            reasons.append("Hinglish sarcasm patterns")
        
        # Determine if sarcastic (threshold: 40)
        is_sarcastic = score >= 40
        confidence = min(score, 100)
        
        # Identify sarcasm type
        sarcasm_type = self._identify_sarcasm_type(text_lower, is_hinglish, has_positive, has_negative)
        
        # Generate explanation
        explanation = self._generate_explanation(is_sarcastic, confidence, reasons)
        
        return {
            'is_sarcastic': is_sarcastic,
            'confidence': float(confidence),
            'sarcasm_type': sarcasm_type if is_sarcastic else None,
            'explanation': explanation
        }
    
    def _identify_sarcasm_type(self, text_lower, is_hinglish, has_positive, has_negative):
        """Identify type of sarcasm"""
        if is_hinglish:
            return "Hinglish Sarcasm"
        
        if has_positive and has_negative:
            return "Praise-Criticism"
        
        if any(word in text_lower for word in self.sarcasm_indicators['exaggeration']):
            return "Exaggerated Positivity"
        
        if '?' in text_lower:
            return "Rhetorical Question"
        
        return "Cultural Reference"
    
    def _generate_explanation(self, is_sarcastic, confidence, reasons):
        """Generate explanation"""
        if is_sarcastic:
            reason_text = ", ".join(reasons) if reasons else "sarcasm patterns"
            if confidence > 75:
                return f"Strong sarcasm detected based on: {reason_text}."
            elif confidence > 50:
                return f"Likely sarcastic due to: {reason_text}."
            else:
                return f"Possible sarcasm: {reason_text}."
        else:
            return "No clear sarcasm indicators detected. Text appears genuine."