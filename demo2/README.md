## DEMO 2

### Disclaimer
This code is vulnerable and should not be used in any production deployments. It's meant to be used for demonstration purposes only.


### How to run
1. Clone repository and navigate to demo2 directory
4. Run the following commands
```
docker-compose build
docker-compose up
```
5. API service will start on port 3001/tcp on your localhost. There are only 2 endpoints available:
- GET /health
- POST /api/v1/orders/generate_document