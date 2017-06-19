Sometimes it is useful to be able to get the current data and time as a string. This might be useful for uniquely naming files or labelling data, for instance.

- The `datetime` module is incredibly useful for creating timestamps. First you'll need to import the datetime module, and specifically the `datetime` class.

	```python
	from datetime import datetime
	```
	
- If you switch into the shell and type `print(datetime.now())`, you should see something like `2017-04-25 15:16:00.122396` output to the shell.

- You can't use the this datetime object as a timestamp, as it is not a string. Instead, you need to use a `formatter` to extract the data into a string.

*[string]: A sequence of characters.

- There are lots of ways of formating the datetime object, and extracting different types of data in different formats. Try the following three lines to see the strings that are output.

	```python
	now = datetime.now()
	print("{0:%Y}".format(now))
	print("{0:%a}".format(now))
	```

	- The `{ }` is used as a place holder within the string to be printed.
	- The `0` is telling the print statement to use the zeroth object that is passed to it. In this case that is `now`.
	- The `:%Y` for instance, then tells the print statement to take the full year from the `datetime.now()` object

- You can chain these place holders together. So you coudl write something like:

	```python
	now = datetime.now()
	print("Today is the {0:%W} of {0:%A} of {0:%Y}".format(now))
	``` 

- If you wanted to use the timestamp to name a file, then you might want to use a shorter form. For instance:

	```python
	now = datetime.now()
	filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
	```
- [Have a look here](http://strftime.org/) for the other codes you can use with the `datetime` module.
