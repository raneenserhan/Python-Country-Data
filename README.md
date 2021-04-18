#Instructions for running the DOCKERfile  
#build docker image  
docker build -t <name> .    

#example:  
docker build -t main .    

#run docker image  
docker run --name <name> -p 5000:5000 <tagname>    

#example:  
docker run --name main-docker 5000:5000 main    

#run the url on brwoser:  
http://127.0.0.1:5000/countryname/<country name>    

#example:  
http://127.0.0.1:5000/countryname/aruba    


Instructions for running the docker-compose  
docker-compose up



