from graphene.test import Client

from flaskr.schema import schema


def test_resolve_dummy_json_todos_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonTodos { id } }''')
    arr = executed.get('data').get('dummyJsonTodos')
    assert any(item['id'] is not None for item in arr)

def test_resolve_dummy_json_todos_user_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonTodos { userId } }''')
    arr = executed.get('data').get('dummyJsonTodos')
    assert any(item['userId'] is not None for item in arr)

def test_resolve_dummy_json_todos_todo():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonTodos { todo } }''')
    arr = executed.get('data').get('dummyJsonTodos')
    assert any(item['todo'] is not None for item in arr)

def test_resolve_dummy_json_todos_completed():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonTodos { completed } }''')
    arr = executed.get('data').get('dummyJsonTodos')
    assert any(item['completed'] is not None for item in arr)

def test_resolve_dummy_json_todo_by_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonTodoById(id:1) { id } }''')
    assert executed == { 'data': { 'dummyJsonTodoById': { 'id': '1' } } }
