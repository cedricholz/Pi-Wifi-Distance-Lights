import json
import ftplib


def get_file_from_ftp_server(filename):
    try:
        with open("ftp_server_info.json") as server_file:
            info = json.load(server_file)
            server_file.close()

        session = ftplib.FTP(info['ip'], info['user'], info['pass'])

        localfile = open(filename, 'wb')
        session.retrbinary('RETR public_html/' + filename, localfile.write, 1024)

        session.quit()
        localfile.close()
    except:
        print("Error retrieving File")


def send_to_ftp_server(filename):
    try:
        with open("ftp_server_info.json") as server_file:
            info = json.load(server_file)
            server_file.close()

        session = ftplib.FTP(info['ip'], info['user'], info['pass'])
        file = open(filename, 'rb')
        session.storbinary('STOR public_html/' + filename, file)
        file.close()
        session.quit()
    except:
        print("No ftp info on file")



def file_to_json(filename):
    try:
        file = open(filename, 'r')
        contents = str(file.read())
        posts = json.loads(contents)
        file.close()
        return posts
    except FileNotFoundError:
        print("No such file: " + filename)
        exit(1)


def json_to_file(json_obj, filename):
    try:
        file = open(filename, 'w')
        json.dump(json_obj, file, sort_keys=True, indent=4, separators=(',', ': '))
        file.close()
    except FileNotFoundError:
        print("No such file: " + filename)
        exit(1)