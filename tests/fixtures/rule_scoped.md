---
paths:
  - "src/api/**/*.ts"
  - "src/routes/**/*.ts"
---
# API Layer Rules — loads only when touching src/api/ or src/routes/

All endpoints must validate input before processing.
Response errors must use the shared ApiError class.
Never return raw database errors to the client.
