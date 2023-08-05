#!/usr/bin/env python3

import importlib.resources as pkg_resources
from tuichat import tuichat_utils
from select import select
from socket import socket
from urllib import request
from json import loads, dumps, JSONDecodeError
from uuid import uuid4


class Server:
    def __init__(self,):
        self.connections = []
        self.uuid = str(uuid4())
        self.nodes = [self.accept_new_clients]

    def main(self,):
        self.get_settings()

        logo_obj = tuichat_utils.ui.Logo('server')
        logo = logo_obj.logo if self.enable_ui else logo_obj.raw_logo
        print(logo)

        license_obj = tuichat_utils.ui.License()
        copyright = license_obj.license if self.enable_ui else license_obj.raw_license
        print(copyright)

        external_ip, start_time = self.run_server()

        server_infotable_obj = tuichat_utils.ui.ServerInfotable(start_time, self.port, self.max_connections, external_ip, self.enable_log, self.enable_ui)
        raw_infotable = server_infotable_obj.raw_infotable
        infotable = server_infotable_obj.infotable if self.enable_ui else raw_infotable
        if self.enable_log:
            self.save_log(raw_infotable, 'a')
        print(infotable)

        try:
            while self.connections:
                conns, _exc, _exc2 = select(self.connections, [], [])
                self.accept_new_clients(conns)
        except (KeyboardInterrupt, SystemExit):
            self.stop_server()
        except Exception as ex:
            print(ex)
            self.stop_server()

    def get_settings(self,):
        try:
            config = pkg_resources.read_text(__package__, 'config.json')
            config = loads(config)
            self.max_connections = config[0]['max_connections']
            if self.max_connections <= 0:
                raise ValueError
            self.port = config[1]['port']
            enable_log_input = config[2]['enable_log']
            self.enable_log = True if enable_log_input.lower() == 'true' else False
            enable_ui_input = config[3]['enable_ui']
            self.enable_ui = True if enable_ui_input.lower() == 'true' else False
        except FileNotFoundError:
            print('[ERROR] Configuration file not found!')
            self.max_connections, self.port, self.enable_log, self.enable_ui = self.configure()
        except JSONDecodeError:
            print('[ERROR] JSON decoding error!')
            self.max_connections, self.port, self.enable_log, self.enable_ui = self.configure()
        except (ValueError, KeyError):
            print('[ERROR] Error in config file! Check variables')
            self.max_connections, self.port, self.enable_log, self.enable_ui = self.configure()

    def save_log(self, data, open_type,):
        log_file = open('log.txt', open_type)
        log_file.write(data)
        log_file.close()

    def save_config(self, max_connections, port, enable_log, enable_ui,):
        parameters_list = [{'max_connections': max_connections}, {'port': port}, {'enable_log': enable_log}, {'enable_ui': enable_ui}]
        config = open('config.json', 'w')
        parametersJSON = dumps(parameters_list)
        config.write(parametersJSON)

    def configure(self,):
        while True:
            print('Would you like to configure server now? [Y/n]')
            answer = input('> ').lower().strip()
            if answer == 'y':
                try:
                    tuichat_utils.data_handler.clear_screen()
                    max_connections_input = tuichat_utils.data_handler.Server.configuration_input('max_connections')
                    port_input = tuichat_utils.data_handler.Server.configuration_input('port')

                    enable_log_input = tuichat_utils.data_handler.Server.configuration_input('enable_log')
                    enable_ui_input = tuichat_utils.data_handler.Server.configuration_input('enable_ui')

                    save_config_input = input('Save current settings to new configuration file? (Y/n) > ').lower().strip()
                    if save_config_input == 'y':
                        self.save_config(max_connections_input, port_input, enable_log_input, enable_ui_input)
                    else:
                        pass
                    tuichat_utils.data_handler.clear_screen()
                except ValueError:
                    tuichat_utils.data_handler.clear_screen()
                    print('[ERROR] Error in data entry!')
                else:
                    return max_connections_input, port_input, enable_log_input, enable_ui_input
            elif answer == 'n':
                tuichat_utils.data_handler.clear_screen()
                print('Using standart variables...')
                return 5, 8000, False, False
            else:
                tuichat_utils.data_handler.clear_screen()
                print('[ERROR] Unknown command!')

    def disconnect_clients(self,):
        server_closed_msg = {'message': 'closed!'}
        self.send_messages(server_closed_msg, 'Server', 'server_closed')
        for client in self.connections:
            client.close()
            self.connections.remove(client)

    def accept_new_clients(self, conns=0, exit=False,):
        if exit:
            try:
                self.disconnect_clients()
            except Exception as ex:
                return ex
            else:
                return True
        else:
            for resource in conns:
                if resource is self.sock:
                    if len(self.connections) < self.max_connections:
                        connection, address = self.sock.accept()
                        connection.setblocking(0)
                        self.connections.append(connection)
                        connection.send(bytes(dumps({'uuid': self.uuid}), encoding='utf-8'))
                        print(f'{tuichat_utils.data_handler.get_time()} {address[0]} connected!')
                        new_user_msg = {'message': 'connected!'}
                        self.send_messages(new_user_msg, address[0], 'message')
                    else:
                        temp_connection, _temp_address = self.sock.accept()
                        temp_connection.close()
                else:
                    self.get_data(resource, resource.getsockname()[0])

    def get_data(self, conn, address,):
        try:
            data = conn.recv(376).decode('utf-8')
            data = data.split(self.uuid)
            data = data[:-1]
            for element in data:
                data_dict = loads(element)
                data = f'{tuichat_utils.data_handler.get_time()} {address} - {data_dict["message"]}'
                print(data)
                if data_dict['type'] == 'disconnect':
                    raise ConnectionResetError
                else:
                    self.send_messages(data_dict, address, 'message')
        except (ConnectionResetError, ConnectionAbortedError):
            conn.close()
            self.connections.remove(conn)
            print(f'{tuichat_utils.data_handler.get_time()} {address} disconnected!')
            connection_aborted_msg = {'message': 'disconnected!'}
            self.send_messages(connection_aborted_msg, address, 'message')

    def send_messages(self, data_dict, address, type,):
        if self.enable_log:
            message = f'{tuichat_utils.data_handler.get_time()} {address} {data_dict["message"]}\n'
            self.save_log(message, 'a')

        message = tuichat_utils.data_handler.Server.serialize_server_data(data_dict['message'], address, self.uuid, type)
        message_to_sender = tuichat_utils.data_handler.Server.serialize_server_data(data_dict['message'], '[You]', self.uuid, type)
        for client in self.connections:
            if client is self.sock:
                continue
            elif client.getsockname()[0] != address:
                client.sendall(bytes(message, encoding='utf-8'))
            else:
                client.sendall(bytes(message_to_sender, encoding='utf-8'))

    def run_server(self,):
        self.sock = socket()
        self.sock.setblocking(0)
        self.connections.append(self.sock)
        self.sock.bind(("", self.port))
        self.sock.listen(self.max_connections)
        external_ip = request.urlopen('http://ifconfig.me/ip').read().decode('utf-8')
        start_time = tuichat_utils.data_handler.get_time()
        return external_ip, start_time

    def stop_server(self,):
        print('\nShutting down PYChat server ...')
        for node in self.nodes:
            response = node(exit=True)
            if response is not True:
                print(response)
            else:
                print(f'[{node.__name__}] node disabled! [OK]')
        print('PYChat server is down!')
        input('Press any key to exit ...')
        exit()


if __name__ == '__main__':
    server = Server()
    server.main()
