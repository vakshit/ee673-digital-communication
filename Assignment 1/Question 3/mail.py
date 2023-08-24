import socket
import ssl
import base64


class EmailClient:
    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, to_addr, subject, message):
        try:
            # Establish a connection to the SMTP server
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.server, self.port))
            ssl_context = ssl.create_default_context()
            ssl_socket = ssl_context.wrap_socket(
                client_socket, server_hostname=self.server
            )

            # Receive the server's initial greeting
            self.receive_response(ssl_socket)

            # Send HELO/EHLO
            print("Sending HELO/EHLO")
            self.send_command(ssl_socket, f"EHLO Akshit")

            # Start TLS if supported
            print(type(self.receive_response(ssl_socket)))
            # if 220 in self.receive_response(ssl_socket):
            if True:
                self.send_command(ssl_socket, "STARTTLS")
                self.receive_response(ssl_socket)

                # Log in using base64-encoded username and password
                self.send_command(ssl_socket, "AUTH LOGIN")
                self.receive_response(ssl_socket)

                encoded_username = base64.b64encode(self.username.encode()).decode()
                self.send_command(ssl_socket, encoded_username)
                self.receive_response(ssl_socket)

                encoded_password = base64.b64encode(self.password.encode()).decode()
                self.send_command(ssl_socket, encoded_password)
                # if 235 not in self.receive_response(ssl_socket):
                #     raise Exception("Authentication failed")

                # Send the email
                self.send_command(ssl_socket, f"MAIL FROM:<{self.username}>")
                self.receive_response(ssl_socket)

                self.send_command(ssl_socket, f"RCPT TO:<{to_addr}>")
                self.receive_response(ssl_socket)

                self.send_command(ssl_socket, "DATA")
                self.receive_response(ssl_socket)

                # Construct and send the email content
                email_content = f"Subject: {subject}\r\n\r\n{message}\r\n."
                self.send_command(ssl_socket, email_content)
                self.receive_response(ssl_socket)

                # Quit and close the connection
                self.send_command(ssl_socket, "QUIT")
                self.receive_response(ssl_socket)

                ssl_socket.close()
        except Exception as e:
            print("An error occurred:", e)

    def send_command(self, socket, command):
        socket.send((command + "\r\n").encode())

    def receive_response(self, socket):
        response = socket.recv(4096).decode()
        response_code = int(response[:3])
        print(response)
        return response_code


# Usage
if __name__ == "__main__":
    email_client = EmailClient(
        "smtp.gmail.com",
        465,
        "email@example.com",
        "password",
    )
    email_client.send_email("mail@example.com", "Test Subject", "This is a test email.")
