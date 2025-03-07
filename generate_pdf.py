import markdown
import pdfkit

with open("cv_gautier_thomas.md", "r") as md_file:
    md_str = md_file.read()

html_str = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Document</title>
</head>
<body>
    {markdown.markdown(md_str)}
</body>
<style>
    table {{
        width: 100%;
        border-collapse: collapse;
        page-break-inside: avoid;
    }}
    table, th, td {{
        border: 1px solid black;
    }}
    th, td {{
        padding: 8px;
        text-align: left;
    }}
</style>
</html>
"""

pdfkit.from_string(html_str, "cv_gautier_thomas.pdf")