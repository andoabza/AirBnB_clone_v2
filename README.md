# HBNB Console and Web Infrastucture

This repo contains a command interpreter for the Holberton Airbnb project, as well as applications for web deployment. The console can be run from the command line and to create, manipulate, and store class objects in a JSON format or using a MySQL database. You'll also find a series of Flask web applications used for deployment of dynamic web content. In a further [repository[(https://github.com/mmoscovics/AirBnB_clone_v3), I collaborated on building out an API for the site side of the project.

## Console
### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands
* delete - delete and object from database

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name> [param]`
Ex:
`create BaseModel name="john"`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`
### Delete
`delete` or `delete <obj>`
Ex:
`delete` or `delete user`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

