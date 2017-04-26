## Python timestamps

Sometimes it is useful to be able to get the current data and time as a string. This might be useful for uniquely naming files or labelling data, for instance.

1. The `datetime` module is incredibly useful for creating timestamps. First you'll need to import the datetime module, and specifically the `datetime` class.

	~~~python
	from datetime import datetime
	~~~
	
1. If you switch into the shell and type `print(datetime.now())`, you should see something like `2017-04-25 15:16:00.122396` output to the shell.

1. You can't use the this datetime object as a timestamp, as it is not a string. Instead, you need to use a `formatter` to extract the data into a string.

*[string]: A sequence of characters.

1. There are lots of ways of formating the datetime object, and extracting different types of data in different formats. Try the following three lines to see the strings that are output.

	~~~python
	now = datetime.now()
	print("{0:%Y}".format(now))
	print("{0:%a}".format(now))
	~~~

	1. The `{ }` is used as a place holder within the string to be printed.
	1. The `0` is telling the print statement to use the zeroth object that is passed to it. In this case that is `now`.
	1. The `:%Y` for instance, then tells the print statement to take the full year from the `datetime.now()` object

1. You can chain these place holders together. So you coudl write something like:

	~~~python
	now = datetime.now()
	print("Today is the {0:%W} of {0:%A} of {0:%Y}".format(now))
	~~~ 

1. If you wanted to use the timestamp to name a file, then you might want to use a shorter form. For instance:

	~~~python
	now = datetime.now()
	filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
	~~~

1. Here's a list of a few of the various placeholders you can use with a `datetime` object.

| Code  | Meaning                                                                          | Example                    |
|-------|----------------------------------------------------------------------------------|----------------------------|
| `%a`  | Weekday as locale's abbreviated name.                                            | `Mon`                      |
| `%A`  | Weekday as locale's full name.                                                   | `Monday`                   |
| `%w`  | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.                | `1`                        |
| `%d`  | Day of the month as a zero-padded decimal number.                                | `30`                       |
| `%-d` | Day of the month as a decimal number. (Platform specific)                        | `30`                       |
| `%b`  | Month as locale's abbreviated name.                                              | `Sep`                      |
| `%B`  | Month as locale's full name.                                                     | `September`                |
| `%m`  | Month as a zero-padded decimal number.                                           | `09`                       |
| `%-m` | Month as a decimal number. (Platform specific)                                   | `9`                        |
| `%y`  | Year without century as a zero-padded decimal number.                            | `13`                       |
| `%Y`  | Year with century as a decimal number.                                           | `2013`                     |
| `%H`  | Hour (24-hour clock) as a zero-padded decimal number.                            | `07`                       |
| `%-H` | Hour (24-hour clock) as a decimal number. (Platform specific)                    | `7`                        |
| `%I`  | Hour (12-hour clock) as a zero-padded decimal number.                            | `07`                       |
| `%-I` | Hour (12-hour clock) as a decimal number. (Platform specific)                    | `7`                        |
| `%p`  | Locale's equivalent of either AM or PM.                                          | `AM`                       |
| `%M`  | Minute as a zero-padded decimal number.                                          | `06`                       |
| `%-M` | Minute as a decimal number. (Platform specific)                                  | `6`                        |
| `%S`  | Second as a zero-padded decimal number.                                          | `05`                       |
| `%-S` | Second as a decimal number. (Platform specific)                                  | `5`                        |
| `%f`  | Microsecond as a decimal number, zero-padded on the left.                        | `000000`                   |
| `%j`  | Day of the year as a zero-padded decimal number.                                 | `273`                      |
| `%-j` | Day of the year as a decimal number. (Platform specific)                         | `273`                      |
| `%U`  | Week number of the year  the first Sunday are considered to be in week 0.        | `39`                       |
| `%W`  | Week number of the year (Monday as the first day of the week)                    | `39`                       |
| `%c`  | Locale's appropriate date and time representation.                               | `Mon Sep 30 07:06:05 2013` |
| `%x`  | Locale's appropriate date representation.                                        | `09/30/13`                 |
| `%X`  | Locale's appropriate time representation.                                        | `07:06:05`                 |
| `%%`  | A literal '%' character.                                                         | `%`                        |
