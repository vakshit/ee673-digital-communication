# Assignment 1

The assignment is divided into 3 questions. The first question has 2 subparts, TCP/UDP client and server. The second question has 1 part. The third question has 1 part. The bonus question is a separate question. The folder structure is as follows:

```bash
  ├── Assignment 1.pdf
  ├── Bonus Question
  │   ├── client.py
  │   └── server.py
  ├── Question 1
  │   ├── TCP_Client.py
  │   ├── TCP_Server.py
  │   ├── UDP_Client.py
  │   └── UDP_Server.py
  ├── Question 2
  │   └── server.py
  ├── Question 3
  │   └── mail_client.py
  ├── README.md
  └── requirements.txt
```

## Installation

`NOTE`: The code has been tested on `Python 3.8.10` on `Ubuntu 20.04.6 LTS`. Use `pip` to install the dependencies incase they are not found.

```bash
pip install -r requirements.txt
# for opencv on ubuntu based systems use
sudo apt install python3-opencv
```

## Usage

### Question 1

```bash
cd Question\ 1
```

#### TCP Server/Client

```bash
python3 TCP_Server.py
# then run
python3 TCP_Client.py
```

#### UDP Server/Client

```bash
python3 UDP_Server.py
# then run
python3 UDP_Client.py
```

### Question 2

`NOTE:`The mobile phone should be connected to the same network as the machine.
If using Ethernet, pass the name of your interface as an argument to the constructor in this line, for example, if your interface is `enp0s3` then the line would be:

```py
chatapp = ChatServer(client=(client_ip, client_port), interface="enp0s3", port=12000)
```

Interface name can be found by running `ifconfig` in the terminal for `ubuntu` based systems.

```bash
cd Question\ 2
python3 server.py
```

`NOTE:` In order to receive messages, make sure to allow the port number for connection by the firewall. For `ubuntu` based systems, run the following command:

```bash
sudo ufw allow $port
sudo ufw enable
```

Sudo access required.

### Question 3

Add your credentials in the main function of `mail_client.py`. An app password (not the regular google password) is required in case of gmail ID. Refer [this](https://support.google.com/accounts/answer/185833?hl=en) for more on app password and its creation.

`NOTE:` Make sure to refer `path/to/attachment` in the same directory as `./file` and not just `file`.

Here `cc_addrs`, `bcc_addrs`, `attachment_paths` are optional arguments and `to_addrs`, `cc_addrs`, `bcc_addrs`, `attachment_paths` are all lists and not string to allow multiple entries.

```bash
cd Question\ 3
python3 mail_client.py
```

## Bonus Question

This one uses TCP for connection. In order to use UDP, packts are needed to be manually created and buffered on the receiver side.

The webcam or default video device is used for streaming. The server can handle multiple clients at the same time as it spawns separate thread for each client. The client can be run on multiple machines on the same network.

```bash
cd Bonus\ Question
python3 server.py
# then run
python3 client.py
```
