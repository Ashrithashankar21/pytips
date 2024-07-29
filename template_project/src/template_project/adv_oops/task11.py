import weakref


class DynamicAttribute:
    def __init__(self):
        self._data = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._data.get(instance, None)

    def __set__(self, instance, value):
        if instance is None:
            raise AttributeError("Cannot set attribute on class")
        self._data[instance] = value

    def __delete__(self, instance):
        if instance is None:
            raise AttributeError("Cannot delete attribute on class")
        if instance in self._data:
            del self._data[instance]


class RequestMetaclass(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if isinstance(value, dict):
                dct[key] = DynamicAttribute()
        return super().__new__(cls, name, bases, dct)


class Request(metaclass=RequestMetaclass):
    headers = {}
    query_params = {}
    body = {}

    def __init__(self):
        pass


class PostRequest(Request):
    def __init__(self):
        super().__init__()


req1 = Request()
req2 = Request()

req1.headers = {"Content-Type": "application/json"}
req2.headers = {"Content-Type": "text/html"}

print(f"Request 1 headers: {req1.headers}")
print(f"Request 2 headers: {req2.headers}")

post_req1 = PostRequest()
post_req2 = PostRequest()

post_req1.body = {"key": "value"}
post_req2.body = {"another_key": "another_value"}

print(f"PostRequest 1 body: {post_req1.body}")
print(f"PostRequest 2 body: {post_req2.body}")
