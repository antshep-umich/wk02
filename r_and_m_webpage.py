import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
    <style>
        table, th, td {
            border: 1px solid white;
            border-collapse: collapse;
        }
    </style>
</head>
<body>
"""



# Add character cards
for char in data["results"]:
    html_content += f"""
        <table>
            <tr>
                <td rowspan="5"><img src="{char['image']}" width = "100" alt="{char['name']}" alt="Portrait" style="float:left; margin-right:20px;"></td>
                <td colspan="2"><h2>{char['name']}</h2></td>
            </tr>
            <tr>
                <td>Species:</td>
                <td>{char['species']}</td>
            </tr>
            <tr>
                <td>Status:</td>
                <td>{char['status']}</td>
            </tr>
            <tr>
                <td>Location:</td>
                <td><a href="{char['location']['url']}">{char['location']['name']}</a></td>
            </tr>
            <tr>
                <td>Origin:</td>
                <td>{char['origin']['name']}</td>
            </tr>
        </table>
    """
    
# End character cards


html_content += """
</body>
</html>
"""
# End HTML structure

# Write to HTML file
with open("rick_and_morty.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_strong.html")

