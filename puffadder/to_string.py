def to_string(original_class):
    """
    Adds a __str__ function to return a formatted string of all instance attributes.

    e.g.:
    @to_string
    class Foo(object):
        _internal_attribute = "This will not be returned"
        name = "Lisa"
        age = 12

        def bar(self):
            pass

    print(Foo())
    >> {name=Lisa, age=12}
    """

    def __str__(self):
        attributes = [attr for attr in dir(self) if
                      not attr.startswith("_") and
                      not (
                          hasattr(original_class.__dict__[attr], "__call__")
                          if attr in original_class.__dict__
                          else hasattr(self.__dict__[attr], "__call__"))]

        formatted_vars = ["{}={}".format(attr,
                                         original_class.__dict__[attr]
                                         if attr in original_class.__dict__
                                         else self.__dict__[attr])
                          for attr in attributes]

        return "{{{}}}".format(', '.join(formatted_vars))

    original_class.__str__ = __str__
    return original_class