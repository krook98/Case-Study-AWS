from file_uploader import upload_file
from notifier import check_file, send_email


if __name__ == "__main__":
    upload_file()
    if check_file():
        send_email()