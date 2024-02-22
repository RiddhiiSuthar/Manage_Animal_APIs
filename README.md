## Animal Management API

### Description

This project implements an API for managing information about animals, focusing specifically on dogs and cats. Each animal is associated with a city and has certain attributes: dogs have bark decibels, while cats have a favorite fish. The API allows users to add, retrieve, update, and delete animals, as well as obtain statistics about the distribution of animals across cities.

### Solution

The solution comprises a RESTful API built using Python and FastAPI, a modern web framework. PostgreSQL is used as the database to store animal information. The API provides endpoints for CRUD operations on animals and a statistics endpoint for retrieving information about animal distribution across cities.

### Technical Choices

- **FastAPI**: FastAPI is chosen for its high performance, easy-to-use interface, and built-in support for asynchronous operations, making it ideal for building modern web APIs.
- **Python**: Python is used as the primary programming language due to its simplicity, readability, and extensive ecosystem of libraries.
- **PostgreSQL**: PostgreSQL is selected as the database management system for its reliability, robustness, and support for advanced features like JSONB data type, which can be useful for storing additional attributes of animals.
- **Pydantic**: Used for data validation and serialization/deserialization of request/response payloads, ensuring data integrity and consistency.
- **RESTful architecture**: Followed RESTful principles for designing the API endpoints, ensuring a logical and predictable interface for users.
- **Swagger/OpenAPI Specification**: FastAPI automatically generates interactive API documentation based on the OpenAPI Specification, providing users with a convenient way to explore and interact with the API.

### Trade-offs

- **Security**: Authentication and authorization mechanisms are not implemented in this version. Additional time would be needed to implement proper security measures such as JWT-based authentication and role-based access control.
- **Error Handling**: While basic error handling is implemented, more comprehensive error handling, including logging and handling of edge cases, could be added for improved robustness.
- **Testing**: Unit tests and integration tests are not included in this version. Test coverage could be improved to ensure the reliability and correctness of the codebase.

### Future Improvements

- **Authentication and Authorization**: Implement JWT-based authentication and role-based access control to secure the API endpoints.
- **Input Validation**: Enhance input validation to ensure data integrity and prevent malformed requests.
- **Testing**: Write comprehensive unit tests and integration tests to ensure the correctness and reliability of the API.
- **Logging**: Integrate logging to capture relevant information for debugging and monitoring purposes.
- **Pagination**: Implement pagination for endpoints that return a large number of results to improve performance.
- **Caching**: Utilize caching mechanisms to improve the performance of frequently accessed data.
- **Rate Limiting**: Implement rate limiting to prevent abuse or misuse of the API.
- **Containerization**: Dockerize the application for easier deployment and management in different environments.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Set up CI/CD pipelines to automate testing, building, and deployment processes.
- **Monitoring**: Implement monitoring and alerting to detect and respond to issues in real-time.
- **Documentation**: Improve documentation with examples, usage scenarios, and API best practices to facilitate understanding and adoption by users.

### Running the Application

## Prerequisites

### Python:

- Python 3.11.4: You can download and install Python 3.11.4 from the official Python website: [Python Downloads](https://www.python.org/downloads/)


## How to Run

To run the application locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/RiddhiiSuthar/Manage_Animal_APIs.git
```

2. Navigate to the project directory:

```
cd Manage_Animal_APIs
```

3. Create Virtual environment and Activate:

```
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
source venv/Scripts/activate

# On macOS/Linux
source venv/bin/activate

```

4. Install dependencies:

```
pip install -r requirements.txt
```

**Note:** Before proceeding, make sure to update the database name, username, and password in the `.env` file according to your database configuration.

5. Run the FastAPI server:

```
cd app
uvicorn main:app --reload
```

The APIs will be available at `http://localhost:8000/doc`.


### Base URL

The base URL for all endpoints is `http://localhost:8000/`.

## API Endpoints

### Cities

#### `GET /cities`

- **Description:** Retrieves a list of cities.
- **Operation:** Get
- **Response:** Returns a list of cities.

### Cats

#### `GET /cats`

- **Description:** Retrieves a list of cats.
- **Operation:** Get Cats
- **Response:** Returns a list of cats.

#### `POST /cats`

- **Description:** Creates a new cat.
- **Operation:** Create Cat
- **Request Body:** Data for creating the cat.
- **Response:** Returns the created cat.

#### `PUT /cats/{cat_id}`

- **Description:** Updates an existing cat.
- **Operation:** Update Cat
- **Path Parameters:** `cat_id` - ID of the cat to update.
- **Request Body:** Updated data for the cat.
- **Response:** Returns the updated cat.

#### `DELETE /cats/{cat_id}`

- **Description:** Deletes an existing cat.
- **Operation:** Delete Cat
- **Path Parameters:** `cat_id` - ID of the cat to delete.
- **Response:** Returns status indicating success or failure.

#### `GET /city/{city_name}/cats`

- **Description:** Retrieves a list of cats in a specific city.
- **Operation:** Get Cats In City
- **Path Parameters:** `city_name` - Name of the city.
- **Response:** Returns a list of cats in the specified city.

#### `POST /city/{city_name}/cats`

- **Description:** Creates new cats in a specific city.
- **Operation:** Create Cats In City
- **Path Parameters:** `city_name` - Name of the city.
- **Request Body:** Data for creating the cats.
- **Response:** Returns the created cats in the specified city.

#### `PUT /city/{city_name}/cats/{cat_id}`

- **Description:** Updates a cat in a specific city.
- **Operation:** Update Cat In City
- **Path Parameters:** `city_name` - Name of the city.
- `cat_id` - ID of the cat to update.
- **Request Body:** Updated data for the cat.
- **Response:** Returns the updated cat in the specified city.

#### `DELETE /city/{city_name}/cats/{cat_id}`

- **Description:** Deletes a cat in a specific city.
- **Operation:** Delete Cat In City
- **Path Parameters:** `city_name` - Name of the city.
- `cat_id` - ID of the cat to delete.
- **Response:** Returns status indicating success or failure.

### Dogs

#### `GET /dogs`

- **Description:** Retrieves a list of dogs.
- **Operation:** Get Dogs
- **Response:** Returns a list of dogs.

#### `POST /dogs`

- **Description:** Creates a new dog.
- **Operation:** Create Dog
- **Request Body:** Data for creating the dog.
- **Response:** Returns the created dog.

#### `PUT /dogs/{dog_id}`

- **Description:** Updates an existing dog.
- **Operation:** Update Dog
- **Path Parameters:** `dog_id` - ID of the dog to update.
- **Request Body:** Updated data for the dog.
- **Response:** Returns the updated dog.

#### `DELETE /dogs/{dog_id}`

- **Description:** Deletes an existing dog.
- **Operation:** Delete Dog
- **Path Parameters:** `dog_id` - ID of the dog to delete.
- **Response:** Returns status indicating success or failure.

#### `GET /city/{city_name}/dogs`

- **Description:** Retrieves a list of dogs in a specific city.
- **Operation:** Get Dogs In City
- **Path Parameters:** `city_name` - Name of the city.
- **Response:** Returns a list of dogs in the specified city.

#### `POST /city/{city_name}/dogs`

- **Description:** Creates new dogs in a specific city.
- **Operation:** Create Dogs In City
- **Path Parameters:** `city_name` - Name of the city.
- **Request Body:** Data for creating the dogs.
- **Response:** Returns the created dogs in the specified city.

#### `PUT /city/{city_name}/dogs/{dog_id}`

- **Description:** Updates a dog in a specific city.
- **Operation:** Update Dog In City
- **Path Parameters:** `city_name` - Name of the city.
- `dog_id` - ID of the dog to update.
- **Request Body:** Updated data for the dog.
- **Response:** Returns the updated dog in the specified city.

#### `DELETE /city/{city_name}/dogs/{dog_id}`

- **Description:** Deletes a dog in a specific city.
- **Operation:** Delete Dog In City
- **Path Parameters:** `city_name` - Name of the city.
- `dog_id` - ID of the dog to delete.
- **Response:** Returns status indicating success or failure.

### Statistics

#### `GET /stats/cats/`

- **Description:** Retrieves statistics related to cats.
- **Operation:** Cat Statistics
- **Response:** Returns statistics related to cats.

#### `GET /stats/dogs/`

- **Description:** Retrieves statistics related to dogs.
- **Operation:** Dog Statistics
- **Response:** Returns statistics related to dogs.