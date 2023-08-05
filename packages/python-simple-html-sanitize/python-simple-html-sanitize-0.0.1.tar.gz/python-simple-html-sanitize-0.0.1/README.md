# python-simple-html-sanitizer
##### v0.0.1

Will only keep the text and 'u', 'b', 'i' & 'br' tags into an html string.

### Installation :
`pip install python-simple-html-sanitizer`  

### Requirements :
`python >= 3.4`  
`beautifulsoup4 >= 4.6`  

### Usage / Example :

```python
from simple_html_sanitizer import sanitize_html

html_str = """
<h3><u>Hello</u> World</h3>
"""

print(sanitize_html(html_str))
# <u>Hello</u> World
```  

###### Support / Contact : remaudcorentin.dev@gmail.com

