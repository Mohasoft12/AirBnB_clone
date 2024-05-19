#!/usr/bin/python3
"""Defines the console class which is the entry point of the Airbnb Project"""

from cmd import Cmd
from models import storage
import shlex

# Import all model classes
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Dictionary of valid classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}

class HBNBCommand(Cmd):
    """Implements the command interpreter for the HBNB project"""
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Exits the program in non-interactive mode"""
        return True

    def do_quit(self, args):
        """Quits the command interpreter"""
        return True

    def emptyline(self):
        """Overrides the default behavior to do nothing on an empty input line"""
        pass

    def do_create(self, args):
        """Creates a new instance of a model and prints its id"""
        args = shlex.split(args)
        if not args:
            self.print_error("class name missing")
        elif args[0] not in classes:
            self.print_error("class doesn't exist")
        else:
            instance = classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """Shows an instance of a model based on its model name and id"""
        args = shlex.split(args)
        if len(args) < 1:
            self.print_error("class name missing")
        elif len(args) < 2:
            self.print_error("instance id missing")
        else:
            try:
                instance = storage.find_by_id(*args)
                print(instance)
            except ModelNotFoundError:
                self.print_error("class doesn't exist")
            except InstanceNotFoundError:
                self.print_error("no instance found")

    def do_destroy(self, args):
        """Deletes an instance of a model based on its model name and id"""
        args = shlex.split(args)
        if len(args) < 1:
            self.print_error("class name missing")
        elif len(args) < 2:
            self.print_error("instance id missing")
        else:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                self.print_error("class doesn't exist")
            except InstanceNotFoundError:
                self.print_error("no instance found")

    def do_all(self, args):
        """Displays string representations of all instances of a given class or all instantiated objects"""
        args = shlex.split(args)
        if len(args) > 1:
            self.print_error("too many arguments for all")
        else:
            try:
                instances = storage.find_all(*args)
                print(instances)
            except ModelNotFoundError:
                self.print_error("class doesn't exist")

    def do_update(self, args):
        """Updates an instance based on its model name and id"""
        args = shlex.split(args)
        if len(args) < 1:
            self.print_error("class name missing")
        elif len(args) < 2:
            self.print_error("instance id missing")
        elif len(args) < 3:
            self.print_error("attribute name missing")
        elif len(args) < 4:
            self.print_error("value missing")
        else:
            try:
                storage.update_one(*args[:4])
            except ModelNotFoundError:
                self.print_error("class doesn't exist")
            except InstanceNotFoundError:
                self.print_error("no instance found")

    def default(self, args):
        """Handles class methods such as <class>.all(), <class>.show(), etc."""
        parts = args.split('.')
        if len(parts) > 1 and parts[1].endswith(')'):
            class_name, method_call = parts[0], parts[1]
            if class_name not in classes:
                self.print_error("class doesn't exist")
            else:
                self.handle_class_methods(class_name, method_call)
        else:
            Cmd.default(self, args)

    def do_models(self, args):
        """Prints all registered models"""
        print(" ".join(classes))

    def handle_class_methods(self, class_name, method_call):
        """Handles class methods like <class>.all(), <class>.show(), etc."""
        try:
            result = eval(f"{class_name}.{method_call}")
            if any(method in method_call for method in ["all()", "show(", "count()", "create()"]):
                print(result)
        except AttributeError:
            self.print_error("invalid method")
        except InstanceNotFoundError:
            self.print_error("no instance found")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ").strip("'")
            self.print_error(f"{field} missing")
        except Exception:
            self.print_error("invalid syntax")

    def print_error(self, message):
        """Prints an error message in the required format"""
        print(f"** {message} **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

