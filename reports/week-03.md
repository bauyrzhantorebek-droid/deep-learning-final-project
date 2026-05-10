Week 3 Progress Report

Tasks accomplished this week:

PyTorch Environment Setup: Configured the deep learning environment using PyTorch and Hugging Face transformers.

Data Pipeline: Implemented a custom PyTorch Dataset class (src/dataset.py) to handle text tokenization and dynamic padding using DistilBertTokenizer.

Deep Learning Architecture: Initialized DistilBertForSequenceClassification with a custom classification head for 6 target labels (framing it as a multi-label classification task).

Training Loop: Developed the PyTorch training loop (notebooks/02_distilbert_model.ipynb), computing BCEWithLogitsLoss implicitly through the Hugging Face model interface, and optimized using AdamW.

Important Commits:

feat: add custom PyTorch dataset class

feat: implement DistilBERT training loop

docs: add week 3 progress report

Experiments run:
Ran an initial fine-tuning epoch on a subset of the data to verify the backward pass, loss computation, and GPU memory limits.

Results so far:
The DL training pipeline is fully functional without memory leaks. The model successfully updates weights.

Plan for next week:

Evaluate the DistilBERT model on the test set.

Compare DistilBERT metrics (F1, Accuracy) against the Logistic Regression baseline.

Compile the final presentation and report.
