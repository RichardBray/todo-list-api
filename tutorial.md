# How to build a REST api in python with tornado

I'm been a front-end developer for a pretty long time now...
..I've worked with json endpoints before but never knew how one was created...

This tutorial assumes you either have a basic knowledge of python or some modern javascript experience.

## The setup
1. Make sure you have a decent text editor, I recommend VScode because of the debugging support and it's free.

2. Download [postman](https://www.getpostman.com/) and install it on your machine, it's free too. This will be used check our api is working.

3. Make sure you have python installed, check py typing `python` into the terminal and you should be taken to the python console.

[image_1]

If not you can download it [here](https://www.python.org/). For this tutorial it doesn't matter if you have the 2x or 3x version of python.

Exit the console by typing `quit()`.

4. You will need to get [pipenv](https://github.com/pypa/pipenv) which is the python equivalent of [npm](https://www.npmjs.com/). To download it type this into the terminal `brew install pipenv`. Then typing `pipenv` should show:

[image_2]

5. Create a folder somewhere called `todo-list-api` and cd into it.

6. Type `pipenv install tornado` to install [tornado](http://www.tornadoweb.org/en/stable/). Once it's done you should see a `Pipfile` and `Pipfile.lock` equivalent to package.json and package-lock.json.


## A simple endpoint

1. Inside the todo-list-api folder create a file called `app.py`.

2. 