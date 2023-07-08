#!/usr/bin/env python3
"""Defines a command line interpreter."""

import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models import storage
from json.decoder import JSONDecodeError
RG1 = r'\s*?[\"\']?(.*?)[\"\'],\s+?\"?\'?(\w+)\"?\'?,\s+?\"?\'?(\w+)\"?\'?'
RG2 = r'\s*?(\w+)\s+?(.*?)?\s[\'\"]?(\w+)[\'\"]?\s+?[\'\"]?(.*)[\'\"]?'


def get_sub_classes():
    """Gets the subclasses of BaseModel"""
    return [cl.__name__ for cl in BaseModel.__subclasses__()]


class HBNBCommand(cmd.Cmd):
    """HBNBCommand is a command line interpreter"""
    __classes = ["BaseModel", *get_sub_classes()]
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        print()
        return True

    def emptyline(self):
        """Does nothing."""
        pass

    def do_count(self, arg):
        """Counts instances of a class"""
        all_inst = storage.all()
        counts = 0
        if arg and arg != "()":
            for key in all_inst.keys():
                if arg.split()[0] in key:
                    counts += 1
            print(counts)
        else:
            print(len(all_inst))

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id."""
        if arg and arg != "()":
            if arg.split()[0] in HBNBCommand.__classes:
                base = eval(arg.split()[0])()
                base.save()
                print(base.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id."""
        self.check_args(arg, self.printing)

    def do_destroy(self, arg):
        """Delete a BaseModel instance"""
        self.check_args(arg, self.delete_arg)

    def do_all(self, arg):
        """Prints all the BaseModel instance created"""
        all_d = storage.all()
        if arg and arg != "()":
            if arg.split()[0] in HBNBCommand.__classes:
                for k, v in all_d.items():
                    if k.split(".")[0] == arg.split()[0]:
                        print(v)
            else:
                print("** class doesn't exist **")
        else:
            [print(v) for k, v in all_d.items()]

    def do_update(self, arg):
        """Updates a BaseModel instance object, adds new or update attribute
        e.g update <class_name> <class_id> <key> <value>"""
        if type(arg) != tuple:
            obj = self.check_args(arg, self.get_object)
            if obj:
                # update the value of object
                self.run_update(obj, arg)
                return
        elif type(arg) == tuple:
            ar = f"{arg[0]} {arg[1]}"
            obj = self.check_args(ar, self.get_object)
            if obj:
                # update the value of object
                self.run_update(obj, arg)
                return

    @staticmethod
    def run_update(obj, args):
        """Updates the value of a given object using the regex to get
        the values and keys"""
        # parse simple words, "complex", "more complex", number, float
        not_allowed = ["created_at", "updated_at", "id"]
        if (type(args) == tuple and not args[2] and type(args[2]) == int):
            pattern = r'\s*?[\"\']?(.*)?[\"\'],\s+?\"?\'?(\w+)\"?\'?'
            match_atr = re.match(pattern, args[1])
            if match_atr:
                ar = list(match_atr.groups())[1:]
                if ar:
                    match_val = re.match(RG1, args[1])
                    if match_val:
                        id, key, value = match_val.groups()
                        try:
                            val = HBNBCommand.valtype(value)(value)
                        except SyntaxError:
                            pass
                        if key not in not_allowed:
                            setattr(obj, key, val)
                        return
                    else:
                        print("** value missing **")
                        return
                else:
                    print("** attribute name missing **")
                    return
            print("** attribute name missing **")
            return

        if (type(args) == tuple and args[3]):
            new_dict = ''
            for c in args[2]:
                if c == "'":
                    new_dict += '"'
                    continue
                new_dict += c
            try:
                _dict = json.loads(new_dict)
                if _dict:
                    [
                        setattr(obj, k, _dict[k]) for k in _dict.keys()
                        if k not in not_allowed
                    ]
                    obj.save()
                else:
                    print("** attribute name missing **")
            except JSONDecodeError:
                print("** value missing **")
        else:
            arg = re.match(r"\s*?(\w+)\s+?(.*?)?\s[\'\"]?(\w+)[\'\"]?",
                           args)
            if arg:
                arg2 = re.match(RG2, args)
                if arg2:
                    cls, id, key, values = arg2.groups()
                    # test if it's a double quoted string
                    val = values.split('"')[0]
                    try:
                        val = HBNBCommand.valtype(val)(val)
                    except SyntaxError:
                        pass
                    if key not in not_allowed:
                        setattr(obj, key, val)
                        obj.save()
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")

    @staticmethod
    def valtype(arg):
        """Get and return the type of a value to update"""
        try:
            return type(eval(arg))
        except (NameError, TypeError):
            return str

    @staticmethod
    def get_object(arg):
        """retrieves the object to update"""
        id = re.match(r'[\"\']?([^\"\']+)[\'\"]?', arg[1])
        if id:
            return (storage.all()[f"{arg[0]}.{id.groups()[0]}"])
        raise KeyError

    @staticmethod
    def printing(arg):
        """prints a given object"""
        id = re.match(r'[\"\']?([^\"\']+)[\'\"]?', arg[1])
        if id:
            print(storage.all()[f"{arg[0]}.{id.groups()[0]}"])
            return
        raise KeyError

    @staticmethod
    def delete_arg(arg):
        """deletes an object and update storage"""
        id = re.match(r'[\"\']?([^\"\']+)[\'\"]?', arg[1])
        if id:
            del storage.all()[f"{arg[0]}.{id.groups()[0]}"]
            storage.save()
            return
        raise KeyError

    @staticmethod
    def check_args(arg, func):
        """parses and checks the needed argument to a function"""
        func_fail = [HBNBCommand.delete_arg, HBNBCommand.printing]

        if arg == "()" and func in func_fail:
            print("** class name missing **")
            return
        arg = arg.split()
        arg_len = len(arg)

        if arg_len < 1:
            print("** class name missing **")
            return
        if arg[0].split()[0] in HBNBCommand.__classes:
            if arg_len < 2:
                print("** instance id missing **")
                return
            try:
                return (func(arg))
            except KeyError:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """Runs as default to functions not parsed by onecmd"""
        func_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "update": self.do_update,
            "count": self.do_count,
            "create": self.do_create,
            "destroy": self.do_destroy,
            "quit": self.do_quit,
        }
        match_dict = re.match(
            r'\s*?(\w+)\.(\w+)\([\"\'](.*)[\"\'],\s+?({(.*?)})\)', arg)
        if match_dict is None:
            match_no_args = re.match(r"\s*?(\w+)\.(\w+)\(\)", arg)
            if match_no_args:
                cls, func = match_no_args.groups()
                if func in func_dict:
                    func_dict[func](cls)
                    return False
                else:
                    print(f"** Invalid syntax ** {arg}")
                    return False
            matchid = re.match(r"\s*?(\w+)\.(\w+)\([\"\']([^\"\']*)[\'\"]\)",
                               arg)
            if matchid:
                cls, func, id = matchid.groups()
                ar = f"{cls} {id}"
                if func in func_dict and func != "update":
                    func_dict[func](ar)
                    return False
                elif func == "update":
                    ar = cls, id, 0
                    func_dict[func](ar)
                    return False
                else:
                    print(f"** Invalid syntax ** {arg}")
                    return False

            match_update = re.match(r"\s*?(\w+)\.(\w+)\([\"\'](.*?)[\"\']\)",
                                    arg)
            if match_update:
                ma = match_update.groups()
                ma = list(ma)
                first = ma[2].split(", ")[0]
                if first[len(first) - 1] == "'":
                    ma[2] = "'" + ma[2][:]
                else:
                    ma[2] = '"' + ma[2][:]
                cls, func, args = ma
                ar = f"{cls} {args}"
                if func in func_dict and func != "update":
                    func_dict[func](ar)
                    return False
                elif func == "update":
                    ar = cls, args, 0
                    func_dict[func](ar)
                    return False
                else:
                    print(f"** Invalid syntax ** {arg}")
                    return False
            else:
                print(f"** Invalid syntax ** {arg}")
                return False
        else:
            cls, func, id, _dict, k = match_dict.groups()
            if func in func_dict and func == "update":
                ar = f"{id} {_dict}"
                ar = cls, id, _dict, 1
                func_dict[func](ar)
                return False

            print(f"** Invalid syntax ** {arg}")
            return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
