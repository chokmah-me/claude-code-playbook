---
paths:
  - "src/api/**/*.ts"
  - "src/routes/**/*.ts"
---
# API Layer Rules — loads only when touching src/api/ or src/routes/

All endpoints must validate input before processing (Zod or equivalent).
Response errors must use the shared ApiError class — never raw exceptions.
Never return raw database errors (Prisma, SQLAlchemy, etc.) to the client.
All protected routes must check authentication before authorization.
Rate limiting must be applied to any endpoint accepting user input.
