# Developing-API-with-Python
API development, management, testing with python

<b>REST Architecture:</b> REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.
#### REST defines the following architectural constraints:
<li><b>Stateless:</b> The server won’t maintain any state between requests from the client.</li>
<li><b>Client-server:</b>  The client and server must be decoupled from each other, allowing each to develop independently.</li>
<li><b>Cacheable:</b>  The data retrieved from the server should be cacheable either by the client or by the server.</li>
<li><b>Uniform interface:</b> The server will provide a uniform interface for accessing resources without defining their representation.</li>
<li><b>Layered system:</b>  The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.</li>
<li><b>Code on demand (optional):</b>  The server may transfer code to the client that it can run, such as JavaScript for a single-page application.</li>

#### A REST web service is any web service that adheres to REST architecture constraints. These web services expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs.

#### A resource is any data available in the web service that can be accessed and manipulated with HTTP requests to the REST API. 
#### The HTTP method tells the API which action to perform on the resource.


| HTTP  | method	Description                     |
|-------|--------------------------------------   |
| GET   |	Retrieve an existing resource.          |
| POST  |  Create a new resource.                 |
| PUT	  |  Update an existing resource.           |
| PATCH |	Partially update an existing resource.  |
|DELETE | Delete a resource.                      |
|CONNECT| Starts two-way comms(open a tunnel)     |
| HEAD  | Requests the headers                    |
|OPTIONS| Requests permitted comms options        |
| TRACE | Performs a message loop-back test(debug)|

#### Status Codes: Once a REST API receives and processes an HTTP request, it will return an HTTP response. Included in this response is an HTTP status code. This code provides information about the results of the request.

|Code	|Meaning	              |  Description                                                                            |
|-----|-----------------------|---------------------------------------------------------------------------------------- |
|200	|  OK	                  |  The requested action was successful.                                                   |
|201	|  Created	            |   A new resource was created.                                                           |
|202	|  Accepted	            | The request was received, but no modification has been made yet.                        |
|204	|  No Content	          | The request was successful, but the response has no content.                            |
|400	|  Bad Request	        |   The request was malformed.                                                            |
|401	|  Unauthorized	        | The client is not authorized to perform the requested action.                           |
|404	|  Not Found	          |   The requested resource was not found.                                                 |
|415	|  Unsupported          |   Media Type	The request data format is not supported by the server.                   |
|422	|  Unprocessable        |   Entity	The request data was properly formatted but contained invalid or missing data.|
|500	|  Internal Server Error|	The server threw an error when processing the request.                                  |

### Project Overview: Library Management API

#### Aim
The aim of this project was to build a robust and efficient Library Management API using FastAPI. The API provides functionalities for managing books, authors, and borrowers, allowing easy integration with various client applications. By deploying it on Heroku, the API is accessible online, ensuring high availability and scalability.

#### Technology Used
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Heroku**: A cloud platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- **PostgreSQL**: An open-source relational database management system used for storing library data.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for interacting with the PostgreSQL database.
- **Pydantic**: Used for data validation and settings management using Python type annotations.
- **Postman**: A collaboration platform for API development, used for testing and documenting the API endpoints.
- **GitHub**: Used for version control and collaboration.

#### Workflow of the Project

1. **Project Setup**
   - **FastAPI Installation**: Started by setting up a virtual environment and installing FastAPI along with other necessary dependencies using `pip`.
   - **Database Setup**: Configured PostgreSQL and SQLAlchemy to handle data persistence. Defined database models for books, authors, and borrowers.

2. **API Development**
   - **Defining Models**: Created Pydantic models for request and response schemas.
   - **Building Endpoints**: Developed CRUD (Create, Read, Update, Delete) endpoints for managing books, authors, and borrowers.
     - **Books**: Endpoints to add, retrieve, update, and delete book records.
     - **Authors**: Endpoints to manage author information.
     - **Borrowers**: Endpoints to track borrower details and book loans.
   - **Routing**: Organized the endpoints using FastAPI's routing capabilities to ensure a clean and maintainable code structure.

3. **Testing with Postman**
   - **Endpoint Testing**: Used Postman to test each API endpoint for expected functionality and performance.
   - **Collection Documentation**: Created a Postman collection to document the API endpoints, including request formats, parameters, and expected responses.

4. **Deployment on Heroku**
   - **Procfile Creation**: Defined a `Procfile` to specify the commands that are executed by the Heroku app.
   - **Heroku Configuration**: Set up environment variables and configured the Heroku app to connect with the PostgreSQL database.
   - **Deployment**: Pushed the code to a GitHub repository and deployed the app to Heroku using Heroku CLI.

5. **Maintenance and Monitoring**
   - **Error Handling**: Implemented comprehensive error handling to manage exceptions and provide meaningful error messages to the clients.
   - **Performance Optimization**: Monitored the API performance on Heroku and optimized database queries and endpoint logic where necessary.
   - **Continuous Integration**: Set up CI/CD pipelines with GitHub Actions to automate testing and deployment processes.

### Conclusion
The Library Management API project was a comprehensive endeavor to create a scalable and efficient API using modern technologies. FastAPI's high performance and ease of use, combined with Heroku's seamless deployment capabilities, resulted in a robust solution for managing library data. Postman played a crucial role in ensuring the reliability and correctness of the API through thorough testing and documentation. This project showcases the effective use of contemporary tools and frameworks to build and deploy a functional and user-friendly API.
