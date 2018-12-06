"""
Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance
About singleton pattern: https://en.wikipedia.org/wiki/Singleton_pattern
In singleton
    * declare all constructors of the class to be private
    * providing a static method that returns a refernce to the instance
In python variables with __doubleUnderscore are not accessible outside the class.
"""

class Singleton:
    __instance1 = None
    __instance2 = None
    __count = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance1 == None or Singleton.__instance2 == None:
            Singleton()

        if Singleton.__count % 2 == 0:
            Singleton.__count = 1
            return Singleton.__instance1
        else:
            Singleton.__count = 0
            return Singleton.__instance2

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance1 != None or Singleton.__instance2 != None:
            raise Exception("This class is Singleton!")
        else:
            Singleton.__instance1 = "one"
            Singleton.__instance2 = "two"
            Singleton.__count = 0

def main():
    s = Singleton()
    print(s)

    s = Singleton.getInstance() # even instance
    print(s)

    s = Singleton.getInstance() # odd instance
    print(s)

if __name__ == '__main__':
    main()
