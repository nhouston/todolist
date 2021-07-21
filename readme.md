# Todo list

To run the frontend, navigate to the frontend directory, you may need to install npm dependencies. To do this run:
```
npm install
```

after this has completed bring up the frontend by running:

```
npm run serve
```

To start the flask backend service, you will need to have python 3 installed with flask and flask-cors.

I recommend running it in an virtual enviroment

You will need to tell flask what file to use, you can do this by entering this in the command line:

```
export FLASK_APP=main.py  
```


# Design

For the todo list, I decided to go with a simple design, making sure that it doesn't destract from the users need to get stuff done. Keeping it simple and allowing to show what items have been completed and those that haven't.

To provide some feedback for the user, alert messages are displayed at the top of the page to indicate any changes that have been made, e.g. adding a item to the todo list

Currently if the todo list backend is killed, the users list will not be saved. This would require a deeper integration and make use of a database, potentially an SQL database.