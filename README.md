# Fibonacci API

This API calculates the n-th Fibonacci number for a given input number n.

## Usage

Send a GET request with a single integer 'n' as a parameter to get the Fibonacci number F(n) corresponding to that integer.

Example:

```bash
$ curl http://127.0.0.1:5000/1
1


1. Build the Docker Image:

Open a terminal window and navigate to the fibonacci-api directory. Run the following command to build the Docker image:

```
docker build -t fibonacci-api .
```
This command tells Docker to build an image with the tag fibonacci-api based on the current directory (.).

2. Run the Docker Container:

After building the Docker image, you can run a container based on that image:

```
docker run -p 5000:5000 fibonacci-api
```

3. Test

**Testing via Browser**

To navigate to the welcome page, open the following link in your browser: 

http://127.0.0.1:5000/

To fetch any nth Fibonacci number, change the link in your browser 

http://127.0.0.1:5000/{n}

such that n is the Fibonnaci number you want to fetch. 

Examples:

http://127.0.0.1:5000/1

http://127.0.0.1:5000/3

http://127.0.0.1:5000/7

**Testing via Curl**

Open another terminal and run a curl command with your desired value for n:

curl http://127.0.0.1:5000/{n}

Examples:

curl http://127.0.0.1:5000/1

curl http://127.0.0.1:5000/3

curl http://127.0.0.1:5000/7

Port:

If the port 5000 is already in use, you can replace 5000 to 5001 in the code base.

Changes to the API: 

If you make changes to the Python script, for example added a new route, you will have build the Docker image again.

