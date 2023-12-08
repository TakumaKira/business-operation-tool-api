def test_show_graphiql_page(client):
  response = client.get("/graphql", headers={"Accept": "text/html"})
  assert response.status_code == 200
