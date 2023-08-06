# RealmKeeper

RealmKeeper is a RESTful API for registering cloud compute instances with FreeIPA.

## Installation

The easiest way to get started with RealmKeeper is making use of it via Docker.

```bash
docker build -t realmkeeper:latest .
```

## Usage

### Starting API Server with Docker
```bash
docker run \
-d \
-p 5000:5000 \
-e IPA_HOST=ipa.example.com \
-e PRINCIPAL=admin \
-e PASSWORD=secret \
-e AWS_REGION=us-east-1 \
realmkeeper:lastest
```

### Client Example

```bash
sudo yum install freeipa-client -y

response=$(curl -k -X POST https://10.0.3.242:5000/v1/aws/register)
hostname=$(echo $response | jq -r '.hostname')
otp=$(echo $response | jq -r '.password')

ipa-client-install -U hostname=$hostname -w $otp

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
