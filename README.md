A Flask Based Web Application that serves a ML model. 
The model is trained on the MNIST dataset and is used to predict the handwritten digits.

## Cloing the repository
```bash
git clone https://github.com/Aryan-Deshpande/HandWritten.git
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage
### Running the application locally

```sh
flask run --host 0.0.0.0 --port 5000
```
![image](hhttps://cdn.discordapp.com/attachments/835750351621718030/1032880918777573406/unknown.png)

### Running the application on a Docker container

- Make sure to be in the same directory as the Dockerfile or specify " /path " instead of " . "
```sh
docker build -t handwritten . \ 
&& docker run --rm -p 5000:5000 handwritten
```

### Running the application for production purpose
- Make sure that a python server for windows / unix is used instead of flasks developement server. Here you can install gunicorn, which is a python server for UNIX.
```sh
pip install gunicorn \
&& gunicorn --bind 0.0.0.0:5000 server:app --timeout 600 --workers 2
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
