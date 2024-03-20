# Client-Server-with-Sockets in Python

Client-server application to practice socket programming in Python.

## Project Description

This repository contains a client-server solution for the analysis of character strings. The client generates a file with character strings and sends them to the server for processing. The server receives the strings, calculates a weighting metric for each one, and returns the results to the client.

## Client Functionality

The client has the following responsibilities:

1. Generate a file containing character strings.
2. Send the strings contained in the generated file to the server using sockets.
3. Read the server's response from the analysis of each string and store this response in a file.

The strings are generated following these rules:

- The strings should only contain the characters: a-zA-Z0-9 and spaces.
- The strings should have a variable length between 50 and 100 characters.
- The strings should always randomly have between 3 and 5 non-consecutive spaces.
- The spaces can never be at the beginning or end of the string.

The generated file is stored with the name: `chains.txt`.

## Server Functionality

The server has the following responsibilities:

1. Receive the strings sent from the client.
2. Calculate the "string weighting" metric, which is defined as: $$\frac{(Number\ of\ letters * 1.5 + Number\ of\ numbers * 2)}{number\ of\ spaces}$$
3. Discard the strings that have two consecutive "a" (aa, AA, aA, Aa). For these cases, the value of the string metric will be 1000 and a log will be left indicating that a string with this rule has been detected.
4. Send the response to the client.

## Requirements

1. Python 3.10.4

## How to Run

First, you need to run the server. To do this, you need to run the Python script `server.py`, passing the port that the server will listen to as a parameter. For example:

```bash
python server.py -p 5050
```

The `-p` parameter refers to the port.

To run the client, it is necessary to specify the server's address to which it will connect, i.e., `ip:port`, and the number of strings to generate. For example:

```bash
python client.py -s 192.168.43.156:5050 -c 50
```

The `-s` argument refers to the server's address and the `-c` argument refers to the number of strings.
