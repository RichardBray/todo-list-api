# Creating a basic REST api with Tornado

The title pretty much explains it.


## Install

`pip install -r requirements.txt`

`python app.py`

### List comprehension 

```py
# result = list(filter(lambda item: item['id'] == int(id), items))
result = [item for item in items if item['id'] == int(id)]
```
