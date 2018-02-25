# -*- coding: utf-8 -*-
import socket
import os


def get_response(request):

    greeting = "Hello mister! \n You are: "
    http = request.split('\n')
    directory = os.getcwd()[: -len('server')] + 'files/'

    get_path = http[0].split(' ')[1]
    user_data = http[2]

    if get_path == '/':
        return greeting + user_data[11:]

    elif get_path == '/test/':
        return request

    elif get_path == '/media/':
        files = ''
        for i in os.listdir(directory):
            files += i + ' '
        return files

    elif get_path[0:7] == '/media/':
        filename = directory + get_path[7:]
        content = ''
        try:
            with open(filename, 'r') as file:
                for line in file:
                    content += line + '\n'
            return content
        except IOError:
            return 'File not found'

    else:
        return "Page not found"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #Регистрация сокета на порте 8000
server_socket.listen(0)  #Переключает сокет в состояние прослушивания

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #Печать параметров клиента
        request_string = client_socket.recv(2048)  #Прочитать 2кб информации из сокета
        client_socket.send(get_response(request_string))  #Передаем результат выполнения get_response
        client_socket.close()
    except KeyboardInterrupt:  #Обработка ошибки KeyboardInterrupt
        print 'Stopped'
        server_socket.close()  #Закрываем сокет
        exit()
