## DEMO 1

### Disclaimer
This code is vulnerable and should not be used in any production deployments. It's meant to be used for demonstration purposes only.


### How to run
1. Backend service uses Equinix Playground API. In order to obtain API token register free account at https://developer.equinix.com/playground/registration
2. Saved generated environment variable into environment variable EQUINIX_BEARER 
3. Clone repository and navigate to demo1 directory
4. Run the following commands
```
docker-compose build
docker-compose up
```
5. Frontend application will start on port 3000/tcp on your localhost. 
