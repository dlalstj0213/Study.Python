def load_module_func(module_name, class_name):
    pass


mod = __import__("package_sample.something", fromlist=["submod"])
print(mod)
print(mod.__name__)
# cls = getattr(mod, "TestClass")()

# print(cls)

val = "hello_world"
print(val[0].upper() + val.split("_")[1][1:])
