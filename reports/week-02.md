Week 2 Progress Report

Tasks accomplished this week:

Data Acquisition: Downloaded the Jigsaw Toxic Comment dataset and set up local data/ directory (added to .gitignore to prevent pushing large files).

Text Preprocessing: Implemented basic text cleaning (lowercasing, removing non-alphabetic characters) in src/data_preprocessing.py.

Baseline Implementation: Created a Jupyter notebook (notebooks/01_baseline_model.ipynb) to train a baseline model.

Baseline Model Details: - Feature extraction: TfidfVectorizer (max 10,000 features).

Algorithm: LogisticRegression (with balanced class weights to handle severe class imbalance).

Handled as a multi-label classification problem by training separate models for each toxicity category (toxic, severe_toxic, obscene, threat, insult, identity_hate).

Important Commits:

feat: add initial EDA and baseline model notebook

feat: create text preprocessing script

docs: add week 2 progress report

Results so far:
The baseline model is running successfully and providing initial F1-scores for all 6 target classes. This establishes a solid benchmark to evaluate our upcoming Deep Learning model.

Plan for next week:

Set up the PyTorch environment.

Start working on the Deep Learning implementation (DistilBERT).

Write the training loop and begin fine-tuning.
