def decorator(function):
    def envelop():
        print("I'm was executed before")
        function()
        print("I'll be executed after")

    return envelop

@decorator
def hello_world():
    print("Hello world")


# hello_world = decorator(hello_world)
hello_world()