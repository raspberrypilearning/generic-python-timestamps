Sometimes you might want to get the current date and time as a string, for instance to give unique names to files or data. The `datetime` module is incredibly useful for creating such timestamps.

- First you'll need to import the `datetime` module, and specifically its `datetime` class.

	```python
	from datetime import datetime
	```
	
- If you go to a terminal window and type `print(datetime.now())`, you should see an output similar to `2017-04-25 15:16:00.122396`.

- You can't use the this `datetime` object as a timestamp, as it is not a string. Instead, you need to use a **formatter** to extract the object's data into a string.

*[string]: A sequence of characters

- There are lots of ways to format the `datetime` object to extract different types of data. Try the following lines of code and compare the output strings.

	```python
	now = datetime.now()
	print("{0:%Y}".format(now))
	print("{0:%a}".format(now))
	```

	- The `{ }` is used as a placeholder within the string to be printed.
	- The `0` tells the `print` command to use the 0th object that is passed to it. In this case that object is `now`.
	- The `:%Y` code tells the `print` command to take the full year from the `datetime.now()` object.
  - Can you tell what the `:%a` code stands for?

- You can chain these codes together, for example like this:

	```python
	now = datetime.now()
	print("Today is the {0:%W} of {0:%A} of {0:%Y}".format(now))
	``` 

- If you want to use the timestamp to name a file, you might want to use a shorter form. For instance:

	```python
	now = datetime.now()
	filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
	```
- [Have a look here](http://strftime.org/) for other codes you can use with the `datetime` module.
