# telegramSend


Small python script for sending messages to telegram both message and to include a image.
Simple to add file and then use in yor own python apps to integrate with telegram


# Buld and run
In the fins folder (ORe what you called it)



Build
```
docker-compose build
```

Run
```
docker-compose up
```

When you devlope you can set so the docker only trace fstab and you can exec into the contaner and start the service from inside the docker. 
This is good when you develope.

1. Set docker-comopse to use fstab

```
command: tail -f /etc/fstab
```
2. Start up with docker compose

```
docker-compose up
```

3. Exec into the continer

find the container
```
docker ps
```
Exec into
```
docker exec -it "ID OF CONTANER" sh 
```

4. Start the service

```
python3 start.py
```


