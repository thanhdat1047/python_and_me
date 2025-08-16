## Library
fastapi: Thư viện chính để xây dựng API.
uvicorn: Server để chạy ứng dụng FastAPI.
pydantic: Thư viện dùng để xác thực dữ liệu, đã được tích hợp sẵn trong FastAPI.

## Path parameters
- Path Parameters are variables embedded directly into the URL path.
- They are used to identify a spectify resource
- Using curly braces {} in the path string
- FastAPI automatically captures the value from the URL and passes it to your function as an argument

## Query parameters
- A set of key-value pairs appended to the URL after a question marks ?
- Used to filter, sort, paginate resources
- They are optional and can be defined as func arguments that are not part of the URL path

## Request Body
- Is the data sent from the client to your API typically in a POST, PUT or PATCH request.
- Is the content of the request itself, not part of the URL
- FastAPI uses Pydantic models to define the stucture and data types of the request body

## Class - In the context of Fast API
- A class is most often a Pydantic model
- Inherits from pydantic.BaseModel