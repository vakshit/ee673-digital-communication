import base64
import socket
import ssl


class EmailClient:
    def __init__(
        self, smtp_server: str, smtp_port: int, username: str, email: str, password: str
    ) -> None:
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.email = email
        self.password = password

        self.login()

    def log_message(self, type: str, message: Exception) -> None:
        print("-----------------------------")
        print(f"{type}: {message}\n")

    def setup_ssl(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.smtp_server, self.smtp_port))
        self.ssl_context = ssl.create_default_context()
        self.ssl_socket = self.ssl_context.wrap_socket(
            self.socket, server_hostname=self.smtp_server
        )

    def exchange(self, message) -> str:
        print("[RUNNING]: ", message if message != "" else "Greeting")
        print("----------------------")
        if str != "":
            self.ssl_socket.send((message + "\r\n").encode())
        try:
            response = self.ssl_socket.recv(4096).decode()
        except Exception as e:
            self.log_message("ERROR", e)
            exit(1)
        print(response)
        print()
        return response

    def login(self) -> None:
        self.setup_ssl()
        self.exchange("")
        self.exchange(f"EHLO {self.username}")
        self.exchange("STARTTLS")
        self.exchange("AUTH LOGIN")
        self.exchange(base64.b64encode(self.email.encode()).decode())
        response = self.exchange(base64.b64encode(self.password.encode()).decode())
        # if "235" not in response:
        #     self.log_message("ERROR", "Authentication failed")
        #     exit(1)
        # set the sender after login
        self.exchange(f"MAIL FROM:<{self.username}>")

    def _add_receipients(self, to_addr: list, cc_addrs: list, bcc_addrs: list) -> None:
        for recipient in to_addr + cc_addrs + bcc_addrs:
            self.exchange(f"RCPT TO:<{recipient}>")

    def _compose_email(
        self,
        subject: str,
        message: str,
        to_addrs: list,
        cc_addrs: list = [],
        bcc_addrs: list = [],
        attachment_paths: list = [],
    ) -> str:
        email_message = ""
        email_message += f"Subject: {subject}\r\n"
        email_message += "MIME-Version: 1.0\r\n"
        email_message += f"From: {self.email}\r\n"
        email_message += f"To: {','.join(to_addrs)}\r\n"
        email_message += f"Cc: {','.join(cc_addrs)}\r\n"
        email_message += f"Bcc: {','.join(bcc_addrs)}\r\n"
        email_message += "Content-type: multipart/mixed; boundary=boundary123\r\n\r\n"
        email_message += "--boundary123\r\n"
        email_message += "Content-type: text/plain; charset=utf-8\r\n\r\n"
        email_message += message.replace("\n", "\r\n")
        # Add attachments
        for attachment_path in attachment_paths:
            email_message += "\r\n--boundary123\r\n"
            attachment_name = attachment_path.split("/")[-1]
            email_message += (
                f"Content-Disposition: attachment; filename={attachment_name}\r\n"
            )
            email_message += "Content-Type: application/octet-stream\r\n"
            email_message += "Content-Transfer-Encoding: base64\r\n\r\n"

            with open(attachment_path, "rb") as file:
                attachment_data = base64.b64encode(file.read()).decode()
                email_message += attachment_data
        email_message += "\r\n--boundary123--\r\n"
        email_message += "."
        return email_message

    def send_email(
        self,
        subject: str,
        message: str,
        to_addrs: list,
        cc_addrs: list = [],
        bcc_addrs: list = [],
        attachment_paths: list = [],
    ):
        try:
            self._add_receipients(to_addrs, cc_addrs, bcc_addrs)

            self.exchange("DATA")
            self.exchange(
                self._compose_email(
                    subject, message, to_addrs, cc_addrs, bcc_addrs, attachment_paths
                )
            )
            self.exchange("QUIT")
        except Exception as e:
            print("An error occurred:", e.with_traceback())
        self.ssl_socket.close()


def main():
    email_client = EmailClient(
        smtp_server="mmtp.iitk.ac.in",
        smtp_port=465,
        username="Akshit Verma",
        email="akshitv20@iitk.ac.in",
        password="",
    )
    email_client.send_email(
        subject="Trial Subject",
        message="Trial Message",
        to_addrs=["mail1@example.com"],
        cc_addrs=["mail2@example.com"],
        bcc_addrs=["mail3@example.com"],
        attachment_paths=["./attachment1.txt", "./attachment2.txt"],
    )


# Usage
if __name__ == "__main__":
    main()
