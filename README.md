This is a team work in this projects called "AirBnB_clone". AUTHORS JUDE OTIM and .... The repo was created by JUDE OTIM with a github name JUDEOTIM.

About the Projects Be pycodestyle compliant! mandatory Write beautiful code that passes the pycodestyle checks All your files, classes, functions must be tested with unit tests Write a class BaseModel that defines all common attributes/methods for other classes:

models/base_model.py Public instance attributes: id: string - assign with an uuid when an instance is created: you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string the goal is to have unique id for each BaseModel created_at: datetime - assign with the current datetime when an instance is created updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object str: should print: [] (<self.id>) <self.dict> Public instance methods: save(self): updates the public instance attribute updated_at with the current datetime to_dict(self): returns a dictionary containing all keys/values of dict of the instance: by using self.dict, only instance attributes set will be returned a key class must be added to this dictionary with the class name of the object created_at and updated_at must be converted to string object in ISO format: format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259) you can use isoformat() of datetime object This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseMode

0x00. AirBnB clone - The console Background Context Welcome to the AirBnB clone project! First step: Write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel create the first abstracted storage engine of the project: File storage. create all unittests to validate all our classes and storage engine What’s a command interpreter? Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place) - Retrieve an object from a file, a database etc… - Do operations on objects (count, compute stats, etc…) - Update attributes of an object - Destroy an object

Execution Your shell should work like this in interactive mode:

$ ./console.py (hbnb) help

Documented commands (type help ):
EOF help quit

(hbnb) (hbnb) (hbnb) quit $ But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py (hbnb)

Documented commands (type help ):
EOF help quit (hbnb) $ $ cat test_help help $ $ cat test_help | ./console.py (hbnb)

Documented commands (type help ):
EOF help quit (hbnb) $ All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
