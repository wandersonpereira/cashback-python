# cashback-python

### Sctruture
This project use this archeteture
* Mongo
* Python 3

### Use docker-compose to start your project
```bash
  docker-compose up --build -d
```

### Test your Unit Test
With docker images is running, execute this command
```bash
  docker exec -it cashback-microservice python3 -m unittest discover -s tests/cashback/useCases -p "*_test.py"
```

### Logger
Yor loggers is genereted on va/log/***

