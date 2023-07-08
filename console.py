#!/usr/bin/python3
"""This module contains the console.py module"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import cmd
import os
import re


def tokenize(arg: str) -> list:
    """ Splits a string into tokens delimited by space

    Args:
        arg (string): strings to be splitted

    Returns:
        list: list of strings
    """
    token = re.split(r"[ .(),]", arg)
    return token


class HBNBCommand(cmd.Cmd):
    """The class HBNB that builds a console"""

    prompt = "(hbnb) "
    CLASSNAMES = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg: str) -> bool:
        """Quit command to exit the program"""

        return True

    def default(self, arg):
        """Default method"""

        func_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        tokens = tokenize(arg)
        for key in func_dict.keys():
            # checking for commands to call
            if key == tokens[1]:
                # for if args is parentheses eg("something")
                if tokens[2] != "" and len(tokens) < 6:
                    # print(tokens)
                    striped_arg = tokens[2].replace('"', '')
                    args = f"{tokens[0]} {striped_arg}"
                    return func_dict[tokens[1]](args)
                elif len(tokens) > 6:
                    # for update version 1
                    # print(tokens)
                    arg1 = tokens[2].replace('"', '')
                    arg2 = tokens[4].replace('"', '')
                    arg3 = tokens[6].replace('"', '')
                    args = f"{tokens[0]} {arg1} {arg2} {arg3}"
                    # print(args)
                    return func_dict[tokens[1]](args)

                else:
                    # print(tokens)
                    return func_dict[tokens[1]](tokens[0])

        # print(tokens)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg: str) -> None:
        """Creates a new instance"""

        tokens = tokenize(arg)
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        else:
            print(eval(tokens[0])().id)
            storage.save()

    def do_clear(self, args: str) -> None:
        """Clear the screen"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def do_show(self, arg: str) -> None:
        """prints the string representation of an instance"""

        tokens = tokenize(arg)
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tokens[0], tokens[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg: str) -> None:
        """Deletes an instance based on the class name and id"""

        tokens = tokenize(arg)
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tokens[0], tokens[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg: str) -> None:
        """Prints all string representation of all instances"""

        tokens = tokenize(arg)
        if arg == "":
            print([str(value) for value in storage.all().values()])
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        else:
            temp = [str(v) for k, v in storage.all().items()
                    if tokens[0] in k]
            print(temp)

    def do_update(self, arg: str) -> None:
        """ Updates the class"""
        tokens = tokenize(arg)
        object_json = storage.all()
        if arg == "":
            # print(tokens)
            print("** class name missing **")
            return False
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            # print(tokens)
            print("** class doesn't exist **")
            return False
        elif len(tokens) < 2:
            # print(tokens)
            print("** instance id missing **")
            return False

        elif f"{tokens[0]}.{tokens[1]}" not in object_json.keys():
            # print(tokens)
            print("** no instance found **")
            return False
        elif len(tokens) < 3:
            # print(tokens)
            print("** attribute name missing **")
            return False
        elif len(tokens) == 3:
            try:
                type(eval(tokens[2])) != dict
            except NameError:
                # print(tokens)
                print("** value missing **")
                return False

        if len(tokens) > 3:
            obj = object_json[f"{tokens[0]}.{tokens[1]}"]
            if tokens[2] in obj.__class__.__dict__.keys():
                # get the attribute value type for typecast
                val_type = type(obj.__class__.__dict__[tokens[2]])
                obj.__dict__[tokens[2]] = val_type(tokens[3])
            else:
                obj.__dict__[tokens[2]] = tokens[3]

        elif type(eval(tokens[2])) == dict:
            obj = object_json[f"{tokens[0]}.{tokens[1]}"]
            for k, v in eval(tokens[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in [str, int, float]):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v

        storage.save()

    def do_count(self, arg):
        """counts"""

        tokens = tokenize(arg)
        # set counter
        count = 0
        # get all object keys
        object_keys = storage.all().keys()
        for key in object_keys:
            if tokens[0] in key:
                count += 1
        print(count)

    def do_EOF(self, arg):
        """Handles EOF"""

        raise systemExit

    def emptyline(self):
        """This doesnt do anything when the no command is passed"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
