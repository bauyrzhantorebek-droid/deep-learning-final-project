# Final Project Report
**Project Title:** Sentiment and Toxicity Classification of YouTube Comments
**Author:** Bauyrzhan Turebek

### 1. Project Title
Sentiment and Toxicity Classification of YouTube Comments

### 2. Problem Statement
The internet, particularly platforms like YouTube, struggles with managing toxic and abusive comments. Manual moderation is unscalable. This project aimed to build an automated Deep Learning system to classify raw text into six specific categories of toxicity to help maintain healthy online communities.

### 3. Dataset Description
- **Source:** Jigsaw Toxic Comment Classification Challenge (Kaggle).
- **Size:** Approximately 159,000 training examples.
- **Features:** Raw comment text (string).
- **Labels:** 6 binary labels (`toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, `identity_hate`).

### 4. Data Preprocessing
Data was cleaned by converting all text to lowercase and removing special characters and punctuation using regular expressions. For the baseline, text was vectorized using `TfidfVectorizer` (max 10,000 features). For the Deep Learning model, text was tokenized using Hugging Face's `DistilBertTokenizer` with dynamic padding up to 128 tokens.

### 5. Model Architecture
- **Baseline:** Logistic Regression trained separately for each label (Binary Relevance).
- **Deep Learning:** `DistilBertForSequenceClassification` fine-tuned for multi-label classification. DistilBERT was chosen as it retains 97% of BERT's language understanding capabilities while being 60% faster and lighter.

### 6. Training Setup
- **Hardware:** Google Colab T4 GPU.
- **Optimizer:** AdamW.
- **Learning Rate:** 2e-5.
- **Loss Function:** Binary Cross Entropy with Logits (`BCEWithLogitsLoss`), standard for multi-label tasks.
- **Batch Size:** 16.

### 7. Evaluation Metrics
The primary metric was the **F1-score** (macro average), as it properly accounts for the severe class imbalance in the dataset (toxic comments are a small minority). Accuracy and Precision/Recall were also monitored.

### 8. Results Table
| Model | Representation | F1-Score (Macro) | Notes |
| :--- | :--- | :--- | :--- |
| Logistic Regression | TF-IDF | ~0.65 | Fast, but struggles with context and sarcasm. |
| DistilBERT | Transformer Embeddings | ~0.78 | Captured deep semantic context significantly better. |

*Note: Metrics are based on a validation subset evaluated during the Colab training session.*

### 9. Error Analysis
The model occasionally struggled with implicit toxicity (sarcasm or passive-aggressive comments) that lacked explicit swear words. Additionally, due to class imbalance, rare classes like `threat` had slightly lower recall compared to the highly populated `toxic` class.

### 10. Limitations
- **Hardware constraints:** Fine-tuning the entire dataset locally was impossible without a GPU; Colab sessions were used but required aggressive subsampling to fit memory limits.
- **Language limitation:** The model is currently strictly limited to English comments.

### 11. Conclusion
The project successfully demonstrated that fine-tuning a pre-trained Transformer (DistilBERT) yields a significant performance boost over classic statistical methods (TF-IDF + LR) in natural language understanding tasks, specifically in identifying nuanced toxic behavior online.

### 12. References
- Jigsaw Toxic Comment Classification Dataset: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge
- Hugging Face Transformers Documentation: https://huggingface.co/docs/transformers/index
- PyTorch Documentation: https://pytorch.org/docs/stable/index.html
