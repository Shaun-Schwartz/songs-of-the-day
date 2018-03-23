def send_email(user, pwd, recipient, subject, body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, pwd)

    COMMASPACE = ', '
    fromaddr = user
    toaddr = recipient if type(recipient) is list else [recipient]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = COMMASPACE.join(toaddr)
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, pwd)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("Successfully sent mail")
    except Exception as e:
        print(f"Failed to send mail. Error: {e}")
