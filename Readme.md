# Product Queue

This project consists of two services. One receives request via a Rest API and queues them in a RabbitMQ queue.
The other consumes the queue, fetches the product information and sends an email with it.

## Run the project!

There are two available ways to run the project. I'd recommend doing it with docker since it's easier.
First you'll have to set up 2 .env files in each folder, I left you a python script that creates them.

Run:
```shell
python3 .\createEnvFiles.py host=rabbitMQ port=5672 username=guest password=guest email={email} email_password=
{app_password}
```

Note: The email provided will be the one sending the email, and the password needed to run this app is an 
application password which you can get [here](https://support.google.com/mail/answer/185833?hl=es-419).

### Local:

I'll leave you steps to run the project manually:

1. Run rabbitMQ server locally
2. Go to `./product-receiver` and run `mvn clean package` and then `java -jar target/product-0.0.1-SNAPSHOT.jar`
3. Then in another terminal go to `./product-request` and then run the same commands as 2.

### With docker:
Inside the root folder run the command: `docker-compose up --build`

## Try the project!

The project only has one endpoint, to test it with curl:
```bash
curl -X POST http://localhost:8080/product/request -H "Content-Type: application/json" -d '{"email":"your_email", 
"product_id": product_id}'
```
If you want to test it with powershell run:
```powershell
$url = "http://localhost:8080/product/request"
$headers = @{
    "Content-Type" = "application/json"
}
$body = @{
    "email" = "email@email.com"
    "product_id" = product_id
}
$jsonBody = $body | ConvertTo-Json
$response = Invoke-WebRequest -Uri $url -Method POST -Headers $headers -Body $jsonBody -ErrorAction Stop
Write-Output $response.Content
```
Note: I recommend using an email address that you can monitor.
#### Technologies:

- Maven
- Java 17
- RabbitMQ Server 3.13.4