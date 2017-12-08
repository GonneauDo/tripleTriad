import asyncore, socket

class Handler(asyncore.dispatcher):
    def __init__(self, serveur, sock=None, map=None):
        asyncore.dispatcher.__init__(self, sock, map)
        self.out_buffer = ''
        self.serveur = serveur

    def handle_read(self):
        data = self.recv(8192)
        if data:
            print(data.decode('utf-8'))
            self.send(data)

    def handle_close(self):
        print('Disconnected')
        self.serveur.deconnexion()
        self.close()

class Serveur(asyncore.dispatcher):
    nbJoueur = 0
    @classmethod
    def connexion(classe):
        classe.nbJoueur += 1
        print("Nombre de clients : ", Serveur.nbJoueur)

    @classmethod
    def deconnexion(classe):
        classe.nbJoueur -= 1
        print("Nombre de clients : ", Serveur.nbJoueur)

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_connect(self):
        pass

    def handle_close(self):
        print("Server Disconnected")
        self.close()

    def handle_read(self):
        print(self.recv(8192))

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            if Serveur.nbJoueur < 2:
                print('Incoming connection from %s' % repr(addr))
                Serveur.connexion()
                handler = Handler(self, sock)
            else:
                sock.close()

serv = Serveur('localhost', 8080)
asyncore.loop()
