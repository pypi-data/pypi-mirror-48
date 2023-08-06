# JSON Table

A little package to convert from a JSON to a table! This project was born out of a need to transform many JSONs mined from APIs to something that Pandas or a relational database could understand.

## Warning

Above all, I want to mention that whilst I inted to expand the functionality of this package, at the moment it can only take a simple sequence of keys to navigate a path. This is, the full functionality proposed by Stefan Gossner in his [jsonpath](https://goessner.net/articles/JsonPath/) is not yet implemented.

If you are looking for a package that simply extracts a single value from a JSON by using more complex paths (and its functions), I recommend you look at [jsonpath-rw](https://github.com/kennknowles/python-jsonpath-rw) by Kenn Knowles [jsonpath-ng](https://pypi.org/project/jsonpath-ng/) by Tomas Aparicio or [jsonpath2](https://pypi.org/project/jsonpath2/) by Mark Borkum. 

However, if you are looking for a simple configurable extractor that can help you abstract the interpretation of JSONs then you are at the right place.

## How to install

The package is available through pypi. So simply go to your command line and:

```bash
pip install jsontable
```
You're also welcome to download the code from github and modify to suit your needs. And if you have time let me know what cool functionality you added and we can improve the project!

## How it works

It works in a similar manner to JSON parsers
1. Create a converter object
2. Add your path mapped to your columns to the converter
3. Give the converter a __decoded__ JSON object you want to read, and it returns a table

## Usage

Here is a super quick example to get you going

```python
import jsontable

paths = [{"$.id":"id"},	{"$.name":"name"}, {"$.address.city":"city"}]
sample = {"id":"1","name":"Ernesto","address":{"city":"London"}}

converter = jsontable.converter()
converter.set_paths(paths)
converter.convert_json(sample)
```

## How paths work

The converter will navigate your JSON from the root looking for your path. I want to mention two important cases

#### Lists
When the converter encounters a list, it will expand it into rows. Similar to how you would expect an SQL JOIN to work. For example:

```python
paths = [{"$.name":"Name"},{"$.telephones.type":"Telephone Type"},{"$.telephones.number":"Telephone Number"}]
sample = {
			"id":"1",
			"name":"Ernesto",
			"telephones":[
				{"type":"mobile", "number":"01234567"},
				{"type":"home", "number":"76543210"}
			]
		}
converter = jsontable.converter()
converter.set_paths(paths)
converter.convert_json(sample)
```
Will result in

```
[['Name', 'Telephone Number', 'Telephone Type'], ['Ernesto', '01234567', 'mobile'], ['Ernesto', '76543210', 'home']]
```

#### Concatenation
Since sometimes you want to stop the path before you get to the last element of your JSON (like the case above where I could want to have the street concatenated in a single row), I have added the following condition:
 - If the last element of your path results in a leaf (i.e. a value), it will save it to the table cell as a string
 - If the last element of your path is not a leaf (i.e. there is more JSON)

So for example, the following code:
```python
paths = [{"$.address":"address_column"}]
sample = {
			"id":"1",
			"name":"Ernesto",
			"address":{
				"city":"London",
				"street":[
					"Appartment 123",
					"Sample Street"
				]
			}
		}
converter = jsontable.converter()
converter.set_paths(paths)
converter.convert_json(sample)
```
Results in:
```
[['address_column'], ["{'city': 'London', 'street': ['Appartment 123', 'Sample Street']}"]]
```

## Final disclaimer

I will continue to look for improvements in the package and hopefully add some useful functionality. If you have issues let me know and I will try my best to help.

You can use this package as you wish, but unfortunatelly, I cannot take responsibility of how this code is used, or the results it provides. It is up to you to test this does what you want it to!