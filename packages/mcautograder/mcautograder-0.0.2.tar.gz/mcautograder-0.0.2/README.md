# Multiple Choice Autograder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/chrispyles/mcautograder/master?filepath=mcautograder-demo.ipynb)

This repository contains a small Python-based multiple-choice question autograder inteded for use in Jupyter Notebooks. It is meant to be packaged with each assignment so that they are easier for use on third-party servers, e.g. MyBinder.

## Usage

To use the autograder, just include the `mcautograder.py` file in the directory containing your notebook, along with your [tests file](#tests). When you load the notebook dependencies, import the file and initialize the grader by creating an instance of the `Notebook` class (the argument to pass is the path to your tests file):

```python
import mcautograder
grader = mcautograder.Notebook("tests.txt")
```

If you want the autograder to score the questions, make sure to set `scored=True` in your `Notebook` call. **The default behavior of the autograder is to allow students to submit answers until they get the correct one.** If you want to change this behavior, you must set the `max_retakes` argument to an integer, the maximum number of retakes allowed. If this is the case, when students hit that ceiling, the check cells will throw an `AssertionError` because they've hit the retake ceiling.

An example call for a scored notebook with a retake ceiling of 5 is given below.

```python
grader = Notebook("tests.txt", scored=True, max_retakes=5)
```

To use the autograder to check answers, have students assign their answers to variables in the notebook; these answers can strings of length 1 or single-digit integers. Then call the `Notebook.check()` function; the first argument should be the question identifier in your tests file and the second should be the variable the student created.

```python
my_answer = "A"
grader.check("q1", my_answer)
```

If the student's response matches the test file, then `Correct.` will be printed; otherwise, `Try again.` will be printed. If the student enters an invalid response (e.g. `float`, answer of > 1 character, hit retake ceiling), the grader will throw an `AssertionError` with a descriptive message.

To get the score on a scored autograder, simply call `Notebook.score()`:

```python
grader.score()
```

The output will contain the fraction of earned points out of possible points and the percentage.

For a more descriptive introduction to the autograder, launch our [Binder](https://mybinder.org/v2/gh/chrispyles/mcautograder/master?filepath=mcautograder-demo.ipynb).

<div id="tests"></div>

## Tests

The autograder relies on a tests file to get the answers for the questions. In this repo, the file is `tests.txt` and it is public; in practice, I usually distribute the answers as a hidden file, `.tests.txt`. It is unhidden here so that you can peruse its structure and contents.

The file has a specific format: each line represents a single question, with an identifier, an answer, and a score. The structure should be `identifier answer score` (note the space). Answers **must** be of length 1 (i.e. a single-character string or a single-digit integer). The score must be included because of how the autograder parses each line. If you don't want your notebook scored, just set each score to 0 and set the `scored` argument of `Notebook()` to `False`.

An example of a file is given below.

```
q1 1 0
q2_1 3 0
q2_2 2 3
q3 A 4
q4 E 0
q5 C 1
question6 7 0
```

The identifiers have no set format, other than that they cannot contain a space. This is because the identifier is passed to `Notebook.check()` when you call it in the notebook.