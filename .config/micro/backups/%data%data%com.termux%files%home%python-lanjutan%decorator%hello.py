# without @decorator
def hello(name: str) -> str:
    return f"Hello, {name}"

def hello_css(func):
    def wrapper(param):
        result = func(param)
        return f"🌟 {result} 🌟"
    return wrapper

hello1 = hello_css(hello)
print(hello1("Ervan"))

# use @decorator
@hello_css
def welcome(username: str) -> str:
    return f"Welcome, {username}!"

print(welcome("karvanidx"))
