## Python timestamps

Sometimes it is useful to be able to get the current data and time as a string. This might be useful for uniquely naming files or labelling data, for instance.

1. The `datetime` module is incredibly useful for creating timestamps. First you'll need to import the datetime module, and specifically the `datetime` class.

	~~~python
	from datetime import datetime
	~~~
	
1. If you switch into the shell and type `print(datetime.now())`, you should see something like `2017-04-25 15:16:00.122396` output to the shell.

1. You can't use the this datetime object as a timestamp, as it is not a string. Instead, you need to use a `formatter` to extract the data into a string.

*[string]: A sequence of characters.

1. There are lots of ways of formating the datetime object, and extracting different types of data in different formats.

	~~~python
	print('{:%Y-%m-%d-%H-%M-%S}'.format(datetime.now()))
	print('{:%Y-%b-%d-%H-%M-%S}'.format(datetime.now()))
	print('{:%H-%M-%S}'.format(datetime.now()))
	~~~
