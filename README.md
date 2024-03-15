```
@app.get("/home/{name}")
def print_name(name: str, q: Union[str,None] = None):
    return {"message": f"Hello, {name}, q: {q}"}
```

```
http://localhost:8000/home/Chandler?q=hello
```
