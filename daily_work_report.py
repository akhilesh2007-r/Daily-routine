class WorkReportEmailSender:
    def __init__(self, smtp_server, email, password):
        self.smtp_server = smtp_server
        self.email = email
        self.password = password

    def send_email(self, recipient_email, subject, body):
        import smtplib
        from email.mime.text import MIMEText

        # Create the email
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = recipient_email

        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server) as server:
                server.starttls()  # Secure the connection
                server.login(self.email, self.password)
                server.sendmail(self.email, recipient_email, msg.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print(f'Failed to send email: {e}')