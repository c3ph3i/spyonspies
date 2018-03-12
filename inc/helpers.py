def take_photo():
    # initialize the camera
    cam = VideoCapture(0)  # 0 -> index of camera
    s, img = cam.read()

    image_name = today + '.jpg'

    image_path_name = os.path.join(PHOTOS_PATH, image_name)

    if s:  # frame captured without any errors
        imwrite(image_path_name, img)  # save image


def write_in_log():
    log_path = DATA_PATH + '/log.txt'

    log = open(log_path, 'a')
    log.write("IP: " + str(ip) + " \t DATE: " + today + '\n')


def send_email():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    # Prepare actual message

    # If photo saving is disabled - get photo for email and remove after
    if not SAVE_PHOTO:
        take_photo()

    img = os.path.join(PHOTOS_PATH, today + '.jpg')
    img_data = open(img, 'rb').read()
    text = """Someone got into your system \n
    IP: """ + str(ip) + """\n
    Date: """ + today + """\n 
    """

    msg = MIMEMultipart()
    msg['Subject'] = 'Someone got into your system'
    msg['From'] = EMAIL_RECIPIENT
    msg['To'] = EMAIL_RECIPIENT

    text = MIMEText(text)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(img))
    msg.attach(image)

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(SMTP_USER, SMTP_PASSWORD)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    if not SAVE_PHOTO:
        os.remove(img)
