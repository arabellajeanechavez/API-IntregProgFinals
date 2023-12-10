NOTE, THIS IS AN UNFINISHED API, Recommendations mentioned by the prof were not integrated on the code.



# groupF

**Barangay Disaster Web Service API**

**Overview**

The Barangay Disaster Web Service API is designed to facilitate efficient management of barangay and institutional data. Developed by GROUP F, this API provides endpoints for NGOs and institutions to retrieve, update, and contribute essential information. It supports user authentication, enabling secure access to the system.


**Team Members**
- Echavez, Arabella Jean A.

**Base URL**
The base URL for the API is http://localhost:5000.

**JWT Token**
Type: API Key
Name: Authorization
Location: Header


**Features**

- GET Barangay Records (`/ngos/barangay-records`):
- Retrieve barangay information with JWT authentication.
  
- GET Evacuation Centers (`/ngos/evacuation-centers`):
- Access evacuation center details with JWT authentication.
  
- GET Barangay Records (`/barangay`):
- Retrieve barangay information with JWT authentication.
  
- PUT Update Barangay Records (`/barangay/update-records`):
- Update specific barangay details securely with JWT authentication.
  
- PUT Update Barangay Situation (`/barangay/update-situation`):
- Update barangay situation details securely with JWT authentication.
  
- PUT Update Disaster Status for Institutions (`/institutions/update-disaster-status`):
- Update disaster status for institutions with JWT authentication.
  
- POST Feedback and Reporting for Institutions (`/institutions/feedback-and-reporting`):
-  Submit feedback and reports securely with JWT authentication.
  
- DELETE Delete Barangay Information (`/barangay/delete-information`):
- Delete barangay information securely with JWT authentication.
  
- POST User Registration (`/register`):
- Register new users securely.
  
- POST User Login (`/login`):
- Log in users securely.
  
- POST Add Barangay (`/ngos/add-barangay`):
- Add new barangay information securely.



**Getting Started**
1. Clone the repository.
2. Install required dependencies.
3. Run the API locally.


**## Endpoints**

**Get Barangay Records for NGOs**

Endpoint: /ngos/barangay-records
Method: GET
Purpose: Obtain detailed barangay information for authorized NGOs.
Security: Requires a valid JWT token for authentication.
Get Evacuation Centers for NGOs
Success (200 OK): Returns detailed barangay information for NGOs.
Unauthorized (401 Unauthorized): Invalid or missing JWT token.

Endpoint: /ngos/evacuation-centers
Method: GET
Purpose: Retrieve information about evacuation centers for authorized NGOs.
Security: Requires a valid JWT token for authentication.
Success (200 OK): Returns information about evacuation centers for NGOs.
Unauthorized (401 Unauthorized): Invalid or missing JWT token.

**Get Barangay Records**

Endpoint: /barangay
Method: GET
Purpose: Retrieve detailed barangay information.
Security: Requires a valid JWT token for authentication.
Success (200 OK): Returns detailed barangay information.
Unauthorized (401 Unauthorized): Invalid or missing JWT token.

**Update Barangay Records**

Endpoint: /barangay/update-records
Method: PUT
Purpose: Update specific barangay information.
Security: Requires a valid JWT token for authentication.
Request Body: {"BarangayID": "string", "UpdatedField": "string", "NewValue": "string"}
Success (200 OK): Indicates successful update of barangay information.
Not Found (404 Not Found): No matching record found.
Bad Request (400 Bad Request): Missing required fields.

**Update Barangay Situation**

Endpoint: /barangay/update-situation
Method: PUT
Purpose: Update barangay situation details.
Security: Requires a valid JWT token for authentication.
Request Body: {"BarangayID": "string", "UpdatedField": "string", "NewValue": "string"}
Success (200 OK): Indicates successful update of barangay situation.
Not Found (404 Not Found): No matching record found.
Bad Request (400 Bad Request): Missing required fields.

**Update Disaster Status for Institutions**

Endpoint: /institutions/update-disaster-status
Method: PUT
Purpose: Update the disaster status for institutions.
Security: Requires a valid JWT token for authentication.
Request Body: {"disasterID": "string", "status": "string"}
Success (200 OK): Indicates successful update of disaster status.
Not Found (404 Not Found): Disaster not found.
Not Modified (304 Not Modified): No changes applied.
Bad Request (400 Bad Request): Missing required fields.

**Feedback and Reporting for Institutions**

Endpoint: /institutions/feedback-and-reporting
Method: POST
Purpose: Allow institutions to submit feedback and reports.
Security: Requires a valid JWT token for authentication.
Request Body: Contains relevant feedback/report data.
Created (201 Created): Feedback/report submitted successfully.
Internal Server Error (500 Internal Server Error): Failed to submit feedback/report.

Delete Barangay Information

Endpoint: /barangay/delete-information
Method: DELETE
Purpose: Delete barangay information.
Security: Requires a valid JWT token for authentication.
Request Body: {"BarangayID": "string"}
Success (200 OK): Barangay information deleted successfully.
Not Found (404 Not Found): Barangay not found.
Bad Request (400 Bad Request): Missing required fields.

**Add Barangay for NGOs**

Endpoint: /ngos/add-barangay
Method: POST
Purpose: Allow NGOs to add new barangay information.
Security: Requires a valid JWT token for authentication.
Request Body: Contains new barangay data.
Created (201 Created): Barangay added successfully.
Conflict (409 Conflict): BarangayID already exists.
Internal Server Error (500 Internal Server Error): Failed to add barangay.
Bad Request (400 Bad Request): Missing required fields.

**User Registration **

Endpoint: /register
Method: POST
Purpose: Allow users to register for access to the system.
Request Body: {"username": "string", "password": "string"}
User Login
Created (201 Created): User registered successfully.
Internal Server Error (500 Internal Server Error): Failed to register user.
Bad Request (400 Bad Request): Missing required fields.

**Endpoint: /login**
Method: POST
Purpose: Authenticate users and provide a JWT token for subsequent requests.
Request Body: {"username": "string", "password": "string"}
OK (200 OK): Authentication successful, returns JWT token.
Unauthorized (401 Unauthorized): Invalid username or password.
Bad Request (400 Bad Request): Missing required fields.

