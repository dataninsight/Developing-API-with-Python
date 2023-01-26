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
