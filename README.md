**should add country.html file into templates folder in the project**

**Instructions for running the app via DOCKERfile**    
#build docker image  
docker build -t <name> .    

#example:  
docker build -t main .    

#run docker image  
docker run --name <name> -p 5000:5000 <tagname>    

#example:  
docker run --name main-docker 5000:5000 main    

#run the following url on brwoser to see the application running:
#http://localhost:5000/countryname/<country_name>
http://127.0.0.1:5000/countryname/<country_name>    

#example:

http://127.0.0.1:5000/countryname/aruba    


**Instructions for running the app via docker-compose**   
#start up the app  
docker-compose up    

#run the following url on brwoser to see the application running:   
http://localhost:8080/countryname/<country_name>  
http://127.0.0.1:8080/countryname/<country_name>    

#example  
http://127.0.0.1:8080/countryname/<aruba>        
![image](https://user-images.githubusercontent.com/82150368/115160313-4bb07880-a0a0-11eb-9820-d8347a75aaca.png)  
 **Enjoy running the app!**
