from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template
html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Python Website</title>
</head>
<body>
    <h1>Welcome to my Python website!</h1>
    <p>This site was made using Flask.</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
