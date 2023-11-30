# business-operation-tool-api

- [business-operation-tool-api](#business-operation-tool-api)
  - [What is this?](#what-is-this)
  - [Steps](#steps)
    - [Make it work!](#make-it-work)
    - [Quality matters](#quality-matters)
  - [How to run](#how-to-run)
  - [Acknowledgments](#acknowledgments)

## What is this?

This self-coding challenge, crafted with the assistance of ChatGPT-4, aims to replicate the core system design of business operation tools. These tools typically interact with external service APIs to collect necessary data, enabling the visualization of comprehensive insights from user data across various services. This pattern is commonly observed in services like e-commerce platforms and booking sites. For a practical and realistic coding challenge, I have chosen specific core specifications to address and selected tech stacks to explore in this scenario.

## Steps

### Make it work!

1. API Server and GraphQL Setup:
   - Develop a GraphQL API server in Python using Graphene.
   - Integrate `graphene-mongo` for MongoDB interactions.

2. External API Integration:
   - Integrate with three external mock APIs: [Fake Store API](https://fakestoreapi.com/), [JSON Placeholder](https://jsonplaceholder.typicode.com/), and [DummyJSON](https://dummyjson.com/).
   - Understand and utilize different endpoints from these APIs for various data needs (e.g., products, user data, posts).

3. MongoDB Database:
   - Set up MongoDB as your database for caching data from these external APIs.
   - Design an appropriate schema in MongoDB to store the retrieved data.

4. Caching Mechanism:
   - Implement logic to cache data from external APIs in MongoDB.
   - Decide on the caching strategy, including how often to refresh the cache.

5. GraphQL Schema and Resolvers:
   - Define a GraphQL schema that includes types and fields relevant to the data you're working with.
   - Write resolvers in Graphene that interact with MongoDB to fetch and serve data, and make real-time API calls when necessary.

### Quality matters

6. Error Handling and Data Validation:
   - Implement comprehensive error handling, particularly for external API interactions and database operations.
   - Validate data before caching it in MongoDB to ensure integrity.

7. Security and Rate Limiting:
   - Implement necessary security measures to protect your API.
   - Handle rate limits of external APIs to avoid service interruptions.

8. Testing:
   - Write tests for your GraphQL resolvers and database interactions.
   - Test the integration with external APIs to ensure reliable data fetching and caching.

9. Documentation:
   - Document your API endpoints, detailing how to interact with your GraphQL API.
   - Include instructions on setting up and running your project.

10. Performance Considerations:
    - Optimize your MongoDB queries and GraphQL resolvers for performance.
    - Consider implementing strategies like batching and caching for efficiency.

## How to run

To run this API server, run:

```bash
poetry install
...
poetry shell
...
flask --app flaskr run
```

## Acknowledgments

I followed the following resources for faster learning.

- [Example Flask+MongoEngine Project](https://github.com/graphql-python/graphene-mongo/tree/master/examples/flask_mongoengine)
