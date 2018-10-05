# How to build a REST api in python with tornado (part 2)

This is a continuation of a tutorial that was started over here. I highly recommend you go through that tutorial before coming here or none of it will make sense. With that out of the way let's continue creating our REST API.


## A slightly better server

By default whenever we make a change we have to close and restart our server which isn't great for development so we'll change that now.

1. Our code thus far should look like this.

[code]

2. Ammnd the code on line 10 to look like this:
```py
return Application(urls, debug=True)
```

3. Now close and start the server, if all went well you shouldn't need stop and start as often.


## Changing Hello to Todo

Our todo list will be a list(array in JS), populated with an dicts. Let's start off by creating that main array.

1. Below all the imports add.
```py
items = []
```

2. Change the class name `HelloHandler` to `TodoItems` and inside the make_app() function.

3. Now ammend the dict in self.write to this
```py
self.write({'items': items})
```

4. Check the reponse in Postman and you should get this.

[image_1]


## Adding a Todo item

1. Let's add a new class below `TodoItems` but above `make_app` called `TodoItem` that inherits `RequestHandler`.

2. Inside `TodoItem` create a post method and add this line inside it:
```py
self.write({'message': self.request.body})
```

3. Now lest add a endpoint url to our server. Expand the urls list in `make_app` and add a new line to it:
```py
("/api/item/", TodoItem)
```

4. Your code should now look like this.

```py
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

items = []

class TodoItems(RequestHandler):
  def get(self):
    self.write({'items': items})


class TodoItem(RequestHandler):
  def post(self):
    items.append(self.request.body)
    self.write({'message': self.request.body})

def make_app():
  urls = [
    ("/", TodoItems),
    ("/api/item/", TodoItem)
  ]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3000)
  IOLoop.instance().start()
```

5. Go into Postman, click on the plus to create a new tab, change the `GET` dropdown to `POST` and add this url
```
http://localhost:3000/api/item/
```

If we had a frontend we will send some json data form it to the endpoint, but as we don't we can use Postman to simulate that.

6. Click on the Body tab beneath the url. Click on the raw radop button and change the dropdown on the right to `JSON(application/json)`.

7. Add this code to the body:
```json
{
	"id":1,
	"name": "test44"
}
```
and press Send.

8. You should get this response:

[image_2]

9. You'll notice the message looks a bit funky, that's because Python by default doesn't automatically convert a string to a dict, so let's import a library to do so.

10. Add this below the two imports:
```py
import json
```

11. Now change the `post` method to this
```py
self.write({'message': json.loads(self.request.body)})
```
And click Send in Postman again.

[image_3]

Nice.

12. Don't forget to save your request in postman as `/item`.

13. Now let's tweak the code to actually add the dict to items. Ammend the post method to look like this.
```py
  def post(self):
    items.append(json.loads(self.request.body))
    self.write({'message': 'new item added'})
```

14. Now add an item with postman, then go back to the items request and see you're newly added item.


## Deleting a todo

The way delete method will work is to create a new_items list form the one which will exclude the one that was deleted. We will pass the item id in the URL this time instead of the Body like with did with the post request.

1. First let's change the item url in `make_app` so that it can read id's using regex:

```py
(r"/api/item/([^/]+)?", TodoItem)
```

2. Create a new method in `TodoItem` called `delete` with a self and id attribute, and add code like this:
```py
  def delete(self, id):
    self.write({'message': id})
```

3. Jump to Postman and create a DELETE request with this url `http://localhost:3000/api/item/342`, the usual headers and press send.

[image_5]

I'm guessing you can figure out what's going here. By default the first argument of a method is `self` and the second argument is anything that will be after the `/` in the url. Currently were just showing a message for any id we place in the url, let's change the method so it can actually delete an item.

4. Make this the first line in the delete method:
```py
new_items = [item for item in items if item['id'] is not int(id)]
```

This is an example of list comprehension in Python. In Javascript the above line wrould be written with an array filter method like so:
```js
const new_items = items.filter(item => item.id !== +id)
```

And the same thing can be done in python using Lamdba a function: 
```py
new_items = filter(lambda item: item['id'] != int(id), items)
```

Which you're welcome to put in your actual code, but the first line of code is more readable and more Pythonic(the python way of coding), so that's why I would recommend doing it that way. You're welcome to put some prints in the code to see how it works before moving on.

5. Now lets assign new items to items, and give a message telling developers what item has been deleted. Add these two pines to the bottom of the new_item variable.

```py
    items = new_items
    self.write({'message': 'Item with id %s was deleted' % id})
```

6. Unlike Javascript in python if you want to change a global variable inside a function/method we need to use the keyword `global` and then the variable name we want to use in the method/function or it will give you an error. Place this code above the new_items variable since it references `items`.

```py
global items
```

7. One more tweak is required. Because our /api/item/ url has been rewritten to expect another argument the post method will no longer work since we're just passing in self and nothing else, to fix that you can ammend it like so:

```py
def post(self, _):
```

And with that done you've created your first API with Python and Tornado. This is what your finished code should look like:

```py
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json

items = []

class TodoItems(RequestHandler):
  def get(self):
    self.write({'items': items})


class TodoItem(RequestHandler):
  def post(self, _):
    items.append(json.loads(self.request.body))
    self.write({'message': 'new item added'})

  def delete(self, id):
    global items
    new_items = [item for item in items if item['id'] is not int(id)]
    items = new_items
    self.write({'message': 'Item with id %s was deleted' % id})


def make_app():
  urls = [
    ("/", TodoItems),
    (r"/api/item/([^/]+)?", TodoItem)
  ]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3000)
  IOLoop.instance().start()
```

Nice work! From here on out there are a few things you can do on your own:
- Add a `put` method to edit a Todo item
- Prevent multiple items with the same id to be added
- Create a `get` mthod to show the details of a single item
- Or if you're a front end dev you could create a little todo list that makes calls to your API

If you get a bit stuck I have the finished code here on Github (apart form the frontend). 

As you've noticed if you restart the server you loose all the todo items in your list which is not ideal. The way to fix that is to save your todo items in a database of some sort which is something I'm looking to write at some point in the future time permitting. But until then, I hope this has been a helpful intorduction to Tornado and REST API's in general.







