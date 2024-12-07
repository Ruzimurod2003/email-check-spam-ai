# **Spam Email Detection Using Naive Bayes Classifier**

## **Overview**
This project is a spam email detection system built using Python. It uses the Naive Bayes classification algorithm with the `scikit-learn` library to classify email messages as **Spam** or **Ham (Not Spam)**. The dataset `spam.csv` is processed and evaluated using various machine learning metrics.

---

## **Table of Contents**
1. [Technologies Used](#technologies-used)
2. [Installation](#installation)
3. [How to Run](#how-to-run)
4. [Project Structure](#project-structure)
5. [Model Evaluation Metrics](#model-evaluation-metrics)
6. [Usage Example](#usage-example)
7. [Contributing](#contributing)
8. [License](#license)

---

## **Technologies Used**
- **Programming Language:** Python 3.x
- **Libraries:** 
  - `pandas` - Data handling
  - `scikit-learn` - Model creation, evaluation, and metrics
  - `warnings` - Ignore unnecessary warnings

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Ruzimurod2003/email-check-spam-ai.git
   cd email-check-spam-ai
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **How to Run**
1. Ensure the dataset `spam.csv` is in the project root directory.
2. Run the script:
   ```bash
   python main.py
   ```

---

## **Project Structure**
```
spam-email-detector/
│── spam.csv              # Dataset file
│── main.py               # Main code file
│── README.md             # Project documentation
│── requirements.txt      # Project dependencies
```

---

## **Model Evaluation Metrics**
The following evaluation metrics are used:
- **Precision**: Correctly identified spam messages out of all predicted spam messages.
- **Recall**: Correctly identified spam messages out of actual spam messages.
- **Accuracy**: Correct predictions over all messages.
- **F1-Score**: Harmonic mean of precision and recall.
- **ROC-AUC Score**: Model performance based on the probability threshold.

---

## **Usage Example**
### Sample Emails Tested:
```python
sample_email = "Congratulations! You have WON a $1000 Gift Card!"
result = detect_spam(sample_email)
print(result)  # Expected: This is a Spam Email!

sample_email = "My name is Tulganoy"
result = detect_spam(sample_email)
print(result)  # Expected: This is a Ham Email!
```

---

## **Contributing**
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Happy Coding! 🚀**
