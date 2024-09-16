import requests
import json
def get_something():
    request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print('get something ')
    print('status code response: ', request.status_code)
    print('content response: ', request.content)
    all_fields = json.loads(request.content)
    print('all fields', all_fields)


#print(get_something())

def delete_something():
    request = requests.delete("https://jsonplaceholder.typicode.com/todos/1")
    print("delete something: ")
    print("status code",request.status_code)

print(delete_something())

def post_something():
    json = {
        'title': 'xiaofang',
        'body': 'fangyilun',
        'userId': 1
    }
    request = requests.post("https://jsonplaceholder.typicode.com/todos", json)
    print("posting chinese actor: ")
    print("status code response: ", request.status_code)
    print("response content: ", request.content)

print(post_something())

def update_something():
    json = {'title': 'fangyilun',
            'body':'xiaofang',
            'userId':1
    }
    request = requests.put("https://jsonplaceholder.typicode.com/todos/1", json)
    print('update chinese actor: ')
    print("status code response:", request.status_code)
    print("content response", request.content)

print(update_something())


def path_something():
    json = {
        'title': 'FANG YILUN',
        'body': 'XIAO FANG',}
    request = requests.patch("https://jsonplaceholder.typicode.com/todos/1", json)
    print('patching chinese actor: ')
    print('status', request.status_code)
    print('content', request.content)
print(path_something())
    
