# RealmKeeper

RealmKeeper is a RESTful API for registering cloud compute instances with FreeIPA.

## Installation

### From Python Package Index (PyPI)
The easiest way to get started with RealmKeeper is install via pip.

```bash
$ pip install realmkeeper
```
## From source
```bash
$ git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/dsa-cloud-coe
$ cd RealmKeeper
$ python setup.py install
```

## With Docker
```bash
$ git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/dsa-cloud-coe
$ docker build -t realmkeeper:latest .
```

## Usage

```bash
$ export IPA_HOST=ipa.example.com
$ export PRINCIPAL=admin
$ export PASSWORD=secret
$ export AWS_REGION=us-east-1

$ realmkeeper
```


### Starting API Server with Docker
```bash
$ docker run \
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
$ sudo yum install freeipa-client -y

$ response=$(curl -k -X POST https://$RealmKeeperIP:5000/v1/aws/register)
$ hostname=$(echo $response | jq -r '.hostname')
$ otp=$(echo $response | jq -r '.password')

$ ipa-client-install -U hostname=$hostname -w $otp

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
