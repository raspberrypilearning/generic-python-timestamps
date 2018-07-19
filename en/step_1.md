Sometimes you might want to get the current date and time as a string, for instance to give unique names to files or data. The `datetime` module is incredibly useful for creating such timestamps.

- First you'll need to import the `datetime` module, and specifically its `datetime` class.

	```python
	from datetime import datetime
	```
  
- If you want to use the timestamp to name a file, you might want to use this for instance:

	```python
	filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
  ``` 
	- The `{ }` is used as a placeholder within the string.
	- The `0` tells the `print` command to use the 0th object that is passed to it. In this case that object is `now`.
	- The `:%Y` code tells the `print` command to take the full year from the `datetime.now()` object.
  - Can you tell what the `:%m` and  `:%d` codes stand for?

- [Have a look here](http://strftime.org/) for other codes you can use with the `datetime` module.
