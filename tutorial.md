# How to build a REST api in python with tornado

I'm been a front-end developer for a pretty long time now and I've worked a lot with REST api endpoints before but never knew how to create one. At ocotpus labs we use Python and Tornado to create enpoints, and for my 10% projec ttime I decided to open this black box, and it's not as difficult as I though it would be. I decided to create a little tutorial for other forntenders who want to have a go at doing the same, or just people who want to learn how to use Tornado.

This tutorial assumes you either have a basic knowledge of python or some modern javascript experience.

## Main setup
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

2. Copy and paste this piece of code (this code will be explained later):

```py
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

class HelloHandler(RequestHandler):
  def get(self):
    self.write({'message': 'hello world'})

def make_app():
  urls = [("/", HelloHandler)]
  return Application(urls)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
```

3. Then in your terminal run `python app.py`. Nothing should happen which is good.

4. Now navigate to (http://localhost:3000/)[http://localhost:3000/] in your browser and if all goes well you should see:

[image_3]

Congratulations, you've created an endpoint.

Now let's explain what these 15 lines of code are doing, much of it is self explanitory.

---

Lines one and two are importing:

```py
from tornado.web import Application, RequestHandler # application creats app, requesthandler, deals with HTTP requests
from tornado.ioloop import IOLoop # input output loop used to run async server
```

The class HelloHandler which inherits RequestHandler had a function called get and that writes a dict (object in JS) to the page as JSON.
```py
class HelloHandler(RequestHandler):
  def get(self):
    self.write({'message': 'hello world'})
```
`self` in python is similar to `this` in JS.

The make_app function (lines 8-10) is what deals with the urls and server settings as well as creating the applicaiton.

And the last section runs the server.
```py
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
```
The `if __name__ == '__main__'` code here is a condition to make sure this code is runs only when `app.py` is executed. So if you created another python file `app2.py`, imported this file into it and ran `python app2.py` in the terminal, the code below `if __name__ == '__main__':` since __name__ will equal `app`.

To be honest this is included only for convention, in this case you could take it out and the endpoint will still work fine, but we'll leave it in.


## Postman setup

As we're not going to be checking endpoints in the browser the whole time let's setup postman to do it.

1. Click on the new collection icon and give it a name of `Tornado todo list`.

[image_4]

2. In `New Tab` if the dropdown next to the address bar doesn't say `GET` change it so it does.

3. Put this in the address bar `http://localhost:3000/`.

4. Then below that click on the headers tab, add a key of `Content-Type` and value of `application/json`.

5. Clicking the blue `SEND` button should show the relevant response.

[image_6]

6. Last but not least, save this new endpoint in the folder you've just created with the request name `/items` (this will make sense later on).

One endpoint down, 4 more to go :)

---

At the risk of making this post too long I will top here and release the rest as a part 2. The main setup is pretty much complete, from here on we will add a few more endpoints for a little todo list we will create (if you haven't figured that out already). I hope you've learn't something from this and I hope you click on to the next part to learn a bit more.
