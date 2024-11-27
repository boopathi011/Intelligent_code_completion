# Flask-Based Python Code Comment and Documentation Generator 🐍📜

Welcome to the **Flask-Based Python Code Comment and Documentation Generator**! 🚀  
This web application helps you generate meaningful comments and detailed documentation for your Python code, making it easier to understand and share.  

---

## ✨ Features  
- **📋 Code Commenting**: Automatically annotate your Python code with explanatory comments.  
- **📝 Documentation Creation**: Generates a Markdown file with a detailed breakdown of your code structure.  
- **🌐 Web Interface**: Provides a simple and intuitive interface for submitting your code.  
- **📂 Downloadable Files**: Easily download both the commented code and the documentation.  
- **🤖 AI-Powered**: Uses the CodeT5 machine learning model to enhance code processing and commenting.  

---

## 🚀 Getting Started  

### 🧑‍💻 Prerequisites  
- Python 3.7 or higher  
- Pip (Python package manager)  

### 📦 Installation  
1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```  
2. Install the required Python packages:  
   ```bash
   pip install -r requirements.txt
   ```  

---

## 🏃‍♂️ Usage  

### 🔧 Running the Application  
1. Start the Flask app:  
   ```bash
   python app.py
   ```  
2. Open your web browser and navigate to:  
   ```
   http://127.0.0.1:5000/
   ```  

### 🌟 Submitting Code  
- Paste your Python code into the web interface.  
- Click the **Generate Comments** button to process the code.  
- Download the outputs:  
  - **Commented Code**: Adds insightful comments to your Python file.  
  - **Documentation**: Provides a Markdown file explaining the code structure.  

---

## 📁 Project Structure  

```
project/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Web interface
├── commented_code.py      # Example output file (generated dynamically)
├── documentation.md       # Example documentation (generated dynamically)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🤖 How It Works  
1. **User Input**: Submit your Python code via the web interface.  
2. **AST Parsing**: The application uses Python’s Abstract Syntax Tree (AST) to analyze the code structure.  
3. **CodeT5 Model**: Enhances the understanding of the code to generate meaningful comments.  
4. **File Generation**: Outputs are saved as files that you can download.  

---

## 🛡️ Dependencies  
- **Flask**: For the web interface.  
- **Transformers**: To load and use the CodeT5 model.  
- **AST (Abstract Syntax Tree)**: For analyzing Python code structure.  

Install all dependencies using:  
```bash
pip install -r requirements.txt
```

---

## 💡 Example Outputs  

### Input Code:  
```python
def add_numbers(a, b):
    return a + b
```

### Commented Code:  
```python
# This is a function named 'add_numbers' which takes arguments (a, b) and performs specific logic.
def add_numbers(a, b):
    return a + b
```

### Documentation:  
```markdown
#### Function: add_numbers  
This function takes the following arguments: `a`, `b`.  
It performs a specific task of adding two numbers and returning the result.  
```

---

## 🛠️ Future Improvements  
- Add support for more programming languages.  
- Include advanced AI models for deeper code analysis.  
- Provide real-time syntax error detection.  

---

## 📝 License  
This project is open-source and available under the [MIT License](LICENSE).  

---

## 📬 Contact  
For questions, suggestions, or contributions, feel free to reach out!  
💻 **Developer**: Boopathi R, Abipriya R, Kabilan A 
📧 **Email**: boopathir.23aim@kongu.edu 

Happy coding! 🎉
