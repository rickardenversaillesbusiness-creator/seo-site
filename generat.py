keywords = []

base = [
"students",
"teachers",
"designers",
"developers",
"marketers",
"writers"
]

for b in base:
    keywords.append(f"ai tools for {b}")
    keywords.append(f"best ai tools for {b}")
    keywords.append(f"free ai tools for {b}")

links = ""

for keyword in keywords:

    filename = keyword.replace(" ","-") + ".html"

    links += f'<li><a href="{filename}">{keyword}</a></li>\n'

    html = f"""
<html>
<head>
<title>{keyword}</title>
</head>

<body>

<h1>{keyword}</h1>

<p>This page talks about {keyword}.</p>

<a href="index.html">Back to home</a>

</body>
</html>
"""

    with open(filename,"w") as f:
        f.write(html)

# créer la homepage automatiquement
index = f"""
<html>
<head>
<title>AI Tools Hub</title>
</head>

<body>

<h1>AI Tools Hub</h1>

<ul>
{links}
</ul>

</body>
</html>
"""

with open("index.html","w") as f:
    f.write(index)