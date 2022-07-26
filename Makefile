# BUILD=Comando para buildar
setup:  
	docker build -t trabwebimage .

# RUN=Comando para rodar
run: 
	docker run -p 8080:8080 --name trabwebcontainer trabwebimage