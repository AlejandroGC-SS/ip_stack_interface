# IPStack Locator
This repository is a Python tool that allows you to retrieve the latitude and longitude information for a specific IP address using the IPStack API.

## Initial Setup

Before using this program, you will need to have the following things ready:
- have Docker already installed in your system
- request a IPStack API TOKEN from [this website](https://ipstack.com/), you will need to create a free account for that
- create a .env file at the root leve of the project and add the following content
  ```API_TOKEN=your_token```


Once you have that set up, you should be able to build the corresponding docker image
To build this project with docker, run the following command
```docker
docker build -t ipstack --rm .
```

### Usage

once this is done, you can make use of this utility by running the following command
```shell
docker run -it --rm ipstack python run.py --ip_address 'your_desired_ip'
```

If you're okay with running this script outside of docker, you can also run this with the following command, just be sure to have Python 3.11 installed in your system
```shell
python run.py --ip_address 'your_desired_ip'
```
### Output Example
```shell
latitude : -38.0673713684082
longitude: 145.14476013183594
```