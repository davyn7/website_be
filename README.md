# website_be

### Make empty repo on git
### Requirements.txt
### Setup conda env
### Setup project and docker (https://fastapi.tiangolo.com/deployment/docker/)
### Setup routes
### Test docker deploy
### Start creating sql models (https://sqlmodel.tiangolo.com/)
### Start creating CRUD APIs
### Start with Journey CRUD, test as you go
### Setup folders for every other CRUD feature

sudo docker build -t myimage .
sudo docker run -d --name mycontainer -p 80:80 myimage
sudo docker stop mycontainer
sudo docker rm mycontainer
docker ps to check

localhost:80/docs