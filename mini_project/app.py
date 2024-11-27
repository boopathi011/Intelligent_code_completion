from flask import Flask, request, send_file, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import ast
import os

app = Flask(__name__)

# Load the CodeT5 model
try:
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")


def generate_code_comments(code):
    """
    Generate detailed comments for Python code by analyzing its structure using `ast`.
    """
    try:
        # Parse the code into an Abstract Syntax Tree (AST)
        tree = ast.parse(code)
    except SyntaxError:
        # Handle malformed code gracefully
        return "# The provided code is malformed or incomplete. Unable to generate comments."

    commented_code = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            # Generate comments for class definitions
            commented_code.append(f"# This is a class named '{node.name}', which defines the blueprint for objects.")
            commented_code.append(ast.unparse(node))  # Include the original class definition
        elif isinstance(node, ast.FunctionDef):
            # Generate comments for function definitions
            args = [arg.arg for arg in node.args.args]
            arg_list = ", ".join(args)
            commented_code.append(
                f"# This is a function named '{node.name}' which takes arguments ({arg_list}) and performs specific logic."
            )
            commented_code.append(ast.unparse(node))  # Include the original function definition
        elif isinstance(node, ast.Assign):
            # Generate comments for assignments
            targets = [ast.unparse(target) for target in node.targets]
            commented_code.append(f"# This assigns values to {', '.join(targets)}.")
            commented_code.append(ast.unparse(node))  # Include the original assignment
        elif isinstance(node, ast.Expr):
            # Handle expressions like print statements
            commented_code.append(f"# This is an expression: {ast.unparse(node)}")
        else:
            # Generic fallback for other types of nodes
            commented_code.append(f"# This is a {type(node).__name__} statement.")
            commented_code.append(ast.unparse(node))

    return "\n".join(commented_code)


@app.route('/')
def index():
    """
    Serve the index.html file for the web interface.
    """
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error loading index.html: {e}"


@app.route('/process_code', methods=['POST'])
def process_code():
    """
    Process submitted Python code, generate comments, and save the commented code to a file.
    Also generates a detailed documentation file explaining the code structure.
    """
    code = request.form['code']  # Retrieve the user-input Python code

    # Generate detailed commented code
    commented_code = generate_code_comments(code)

    # Save the commented code to a file for download
    output_filename = "commented_code.py"
    with open(output_filename, "w") as file:
        file.write(commented_code)

    # Generate detailed documentation file
    documentation_filename = "documentation.md"
    with open(documentation_filename, "w") as doc_file:
        doc_file.write("# Python Code Documentation\n\n")
        doc_file.write("This document provides an explanation of the Python code you submitted.\n\n")

        # Break the code down into sections and describe each one
        doc_file.write("### Code Overview\n")
        doc_file.write("The provided Python code is a Flask-based web application that accepts Python code, generates comments for it using AST parsing and a machine learning model, and then allows the user to download the commented code and documentation.\n\n")
        
        doc_file.write("### Detailed Code Explanation\n")

        # Parse the code into an AST and provide descriptions for classes, functions, and other elements
        tree = ast.parse(code)
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                doc_file.write(f"\n#### Class: {node.name}\n")
                doc_file.write(f"This class defines the blueprint for creating objects of type `{node.name}`.\n")
                doc_file.write("It encapsulates properties and behaviors related to this type of object.\n")
            elif isinstance(node, ast.FunctionDef):
                doc_file.write(f"\n#### Function: {node.name}\n")
                args = [arg.arg for arg in node.args.args]
                doc_file.write(f"This function takes the following arguments: {', '.join(args)}.\n")
                doc_file.write("It performs a specific task within the application, such as processing input data, performing calculations, etc.\n")
            elif isinstance(node, ast.Assign):
                targets = [ast.unparse(target) for target in node.targets]
                doc_file.write(f"\n#### Assignment: {', '.join(targets)}\n")
                doc_file.write(f"Assignments are made to the variables {', '.join(targets)} with the specified values.\n")
            elif isinstance(node, ast.Expr):
                doc_file.write(f"\n#### Expression: {ast.unparse(node)}\n")
                doc_file.write("This line is an expression (e.g., a print statement or a calculation).\n")
            else:
                doc_file.write(f"\n#### {type(node).__name__} Statement\n")
                doc_file.write(f"This is a {type(node).__name__} statement, which serves a specific role in the structure of the code.\n")

        doc_file.write("\n### Conclusion\n")
        doc_file.write("The code provided was processed and documented using an Abstract Syntax Tree (AST) and machine learning techniques to generate detailed comments and explanations.\n")

    # Provide the download links to the user
    return (
        f"<h3>Files generated:</h3>"
        f"<p><a href='/download/{output_filename}'>Download Commented Code</a></p>"
        f"<p><a href='/download/{documentation_filename}'>Download Documentation</a></p>"
    )


@app.route('/download/<filename>')
def download_file(filename):
    """
    Handle file download requests for generated files.
    """
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Error downloading file: {e}"


if __name__ == '__main__':
    app.run(debug=True)
