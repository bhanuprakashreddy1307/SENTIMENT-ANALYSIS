import nltk
import string
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Download stopwords
nltk.download('stopwords')

# Sample dataset with simple textual data
text_data = [
    "I love this product! It's amazing.",
    "This is the worst experience I have ever had.",
    "Absolutely fantastic service, highly recommend!",
    "I hate this so much, it's terrible.",
    "Not bad, but could be better.",
    "Very disappointing experience, I expected more.",
    "This is the best thing ever!",
    "Horrible! Never buying again.",
    "Just okay, nothing special.",
    "Excellent quality and great value."
]

# Corresponding labels (1 for positive, 0 for negative)
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Preprocess text data
processed_texts = [preprocess_text(text) for text in text_data]

# Convert text data into numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_texts)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict sentiment for test data
y_pred = model.predict(X_test)

# Display results
for i, text in enumerate(text_data[-2:]):  # Checking last two examples
    prediction = "Positive" if y_pred[i] == 1 else "Negative"
    print(f"Text: {text}\nPredicted Sentiment: {prediction}\n")
