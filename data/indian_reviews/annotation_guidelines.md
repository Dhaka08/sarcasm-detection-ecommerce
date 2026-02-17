**# Annotation Guidelines: Indian Sarcasm Detection**



**## What is Sarcasm?**

**Sarcasm is when someone says the opposite of what they mean,**

**usually to criticize or mock something.**



**## Sarcasm Types in Dataset:**



**### Type 1: Exaggerated Positivity**

**Praises something that is clearly bad.**

**Example: "Amazing! Battery lasts a whole 2 hours. Revolutionary!"**



**### Type 2: Praise-Criticism**

**Positive words used for clearly negative experience.**

**Example: "Perfect timing! Broke exactly 1 day after warranty!"**



**### Type 3: Hinglish Sarcasm**

**Mix of Hindi and English used sarcastically.**

**Example: "Ekdum first class! Sirf teen din mein toot gaya!"**



**### Type 4: Cultural Reference**

**Uses Indian cultural references sarcastically.**

**Example: "Warm as a tandoor in summer - perfect all-season jacket!"**



**### Type 5: Rhetorical Question**

**Sarcastic questions implying the opposite.**

**Example: "Who needs both earphones working anyway right?"**



**## Label Values:**

**- is\_sarcastic: 1 = Sarcastic**

**- is\_sarcastic: 0 = Not Sarcastic**



**## Columns Explained:**

**- id: Unique review number**

**- product\_category: Electronics/Clothing/Home Appliances/Food**

**- review\_text: The actual review**

**- star\_rating: 1-5 stars given by reviewer**

**- platform: Amazon India or Flipkart**

**- is\_sarcastic: 0 or 1**

**- sarcasm\_type: Type of sarcasm if applicable**

**- annotator\_notes: Extra observations**

