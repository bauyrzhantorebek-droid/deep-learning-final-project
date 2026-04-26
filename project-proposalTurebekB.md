1. Project Title

Sentiment and Toxicity Classification of YouTube Comments

2. Problem Statement

1. What problem are you trying to solve?
The project aims to automatically classify text comments into categories such as positive, neutral, negative, or toxic.
2. Why is this problem useful or interesting?
Content creators often manage communities across various spheres and face thousands of daily comments. Manually filtering toxic behavior or analyzing audience sentiment is time-consuming and practically impossible at scale. An automated system helps maintain a healthy community environment.
3. What will the model predict or generate?
The model will predict the probability of a comment belonging to a specific class (e.g., toxic vs. non-toxic, or sentiment polarity) based on the raw text input.

3. Dataset

Dataset name: Jigsaw Toxic Comment Classification Challenge (or similar YouTube Sentiment Dataset).

Dataset source link: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data 

Number of examples: ~159,000 training examples.

Input features: Raw text data (string).

Target labels: Binary labels for multiple classes (toxic, severe_toxic, obscene, threat, insult, identity_hate).

Data format: CSV.

License: CC0 (Public Domain) / Kaggle Terms of Use.

4. Planned Method

Baseline: Logistic Regression with TF-IDF vectorization. This is a fast and interpretable model for text classification.

Deep learning model: A transformer-based model, specifically DistilBERT (fine-tuned for sequence classification). It is lightweight enough to train quickly but powerful enough to capture deep contextual meaning in text.

Loss function: Binary Cross-Entropy with Logits (BCEWithLogitsLoss) since this can be framed as a multi-label classification problem.

Evaluation metrics: F1-score (macro/micro), Precision, Recall, and Accuracy. F1-score is heavily prioritized due to expected class imbalance.

Train/validation/test split plan: 80% Training, 10% Validation, 10% Testing.

5. Expected Challenges

Dataset imbalance: Toxic comments represent a very small minority of the overall dataset, which might cause the model to blindly predict the majority class.

Informal language: Internet comments contain heavy use of slang, emojis, typos, and sarcasm, making tokenization and context extraction difficult.

Computational limits: Fine-tuning a transformer model like DistilBERT requires significant GPU memory and can lead to long training times.

Overfitting: The deep learning model might memorize the training data rather than generalizing well to unseen, novel internet slang.

6. Weekly Plan
   
Week,Planned Work,Expected Output
Week 1,"Dataset selection, GitHub repository setup, Exploratory Data Analysis (EDA) to check class balance and text lengths.","Proposal, README.md, dataset summary, and EDA notebook."
Week 2,"Text preprocessing (tokenization, lowercasing, cleaning), dataset splitting, and implementation of the Logistic Regression baseline.","Baseline metrics (Accuracy, F1), preprocessing scripts, and Week 2 report."
Week 3,"Implementation of the PyTorch training loop, fine-tuning the DistilBERT model, and running evaluation experiments.","DistilBERT model weights, training loss plots, initial DL metrics, and Week 3 report."
Week 4,"Error analysis, hyperparameter tuning, final metric comparison between baseline and DL model, writing the final report.","Final code pushed to GitHub, final report, and presentation slides."
