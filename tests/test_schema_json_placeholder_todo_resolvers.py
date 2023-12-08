from graphene.test import Client

from flaskr.schema import schema


def test_resolve_json_placeholder_todos_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderTodos { id } }''')
    arr = executed.get('data').get('jsonPlaceholderTodos')
    assert any(item['id'] is not None for item in arr)

def test_resolve_json_placeholder_todos_user_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderTodos { userId } }''')
    arr = executed.get('data').get('jsonPlaceholderTodos')
    assert any(item['userId'] is not None for item in arr)

def test_resolve_json_placeholder_todos_title():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderTodos { title } }''')
    arr = executed.get('data').get('jsonPlaceholderTodos')
    assert any(item['title'] is not None for item in arr)

def test_resolve_json_placeholder_todos_completed():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderTodos { completed } }''')
    arr = executed.get('data').get('jsonPlaceholderTodos')
    assert any(item['completed'] is not None for item in arr)

def test_resolve_json_placeholder_todo_by_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderTodoById(id:1) { id } }''')
    assert executed == { 'data': { 'jsonPlaceholderTodoById': { 'id': '1' } } }
