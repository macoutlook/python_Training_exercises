
TASK
-----------

Write program which will generate two kinds of reports for the text
in the file `sherlock.txt`:

1. For the --count flag, implement a `print_count` function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word. Store all the words as lowercase,
so 'The' and 'the' count as the same word.


2. For the --top flag, implement a `print_top` function which is similar
to `print_count`, but which prints just the top 20 most common words sorted,
so the most common word is first, then the next most common, and so on.

There is already some code in `wordcount.py` file, you just need to add missing
implementation of mentioned functions.


TIPS
------------

1. In order to get list of words use `.split` method on the text line to split on all whitespace.
2. Define a helper function for parsing file to avoid code duplication inside `print_count` and `print_top`.


So example session might look as follows:

# no arguments
$ python wordcount.py
Usage: ./wordcount.py {--count | --top} <file name>


# print word counts
$ python wordcount.py --count sherlock.txt
"'a 1
"'about 1
...

# print top word counts
$ python wordcount.py --top sherlock.txt
the 5704
and 2882
...


