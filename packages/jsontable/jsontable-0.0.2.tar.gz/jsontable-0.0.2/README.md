# JSON Table

A Relational Mapper for JSON objects in python. This class is based on the following simple steps:
1. Create a mapper object
2. Configure the mapper object to read a JSON structure of your choice
3. Give the mapper a JSON object you want to read, and it returns a table

The intention is to at some point be able to add database support here. But you can already use this class to start playing around.

## Warnings

Just before we go on, a couple of things I want to point out:
 - The JSON paths are read simply as a sequence of key:values, this means its not a full implementation of the jsonpath functionality
 - There is no database connectivity. At the moment, the class only takes in a JSON and outputs a List of rows.

I hope to have time to make this project more useful, but we got to start somewhere! Now moving on.

## Configuration File

The configuration file is meant to tell our class all that it needs to know about the JSON structure it will be reading and converting to a table. This file is itself a JSON with the following elements:
- Columns: These are one to one mappings of JSON Paths to Database Columns
- Table name: This indicates which table is the destination in the DB
- Keys: Tells the mapper which columns will be used as keys

Here is a sample configuration JSON

```
{
	"columns":[
	 	{"path":"$.id","mapped_column":"id"},
	 	{"path":"$.name","mapped_column":"name"},
	 	{"path":"$.address.city","mapped_column":"city"}
	],
	"table_name":"myTable",
	"key_columns":[
		"id"
	]
}
```