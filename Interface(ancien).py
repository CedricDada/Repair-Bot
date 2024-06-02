import sys
import json
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSignal, QObject, QThread

# Définition de l'adresse IP et du port du destinataire
HOST = '127.0.0.1'
PORT = 5039

# Création d'une socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion à l'adresse IP et au port du destinataire
sock.connect((HOST, PORT))

class Listener(QObject):
    message_received = pyqtSignal(str)

    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def listen(self):
        while True:
            received_data = self.socket.recv(1024).decode()
            if not received_data:
                break

            data = json.loads(received_data)
            if 'cause' in data:
                message = data['cause']
            elif 'potential_cause' in data:
                message = data['potential_cause']
            elif 'request' in data:
                message = data['request']
            elif 'refresh' in data:
                message = data['refresh']
            self.message_received.emit(message)

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter = 1
        self.setWindowTitle("Repair Bot")
        self.setFixedHeight(900)
        self.setFixedWidth(850)

        # Create a layout for the chat messages
        self.chat_layout = QVBoxLayout()

        # Create a widget to hold the chat messages
        self.chat_widget = QWidget()
        self.chat_widget.setLayout(self.chat_layout)

        # Create a scrollable area for the chat messages
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.chat_widget)

        # Create a text edit widget for user input
        self.input_box = QTextEdit()
        self.input_box.setFixedSize(834, 80)  # Set the minimum height to 50 pixels
        self.input_box.setPlaceholderText("Saisissez votre problème ici")

        # Create a button to send messages
        self.send_button = QPushButton("Envoyer")
        self.send_button.clicked.connect(self.send_message)
        self.refresh_button = QPushButton("Recommencer")
        self.refresh_button.clicked.connect(self.refresh)

        # Create a layout and add widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)
        layout.addWidget(self.refresh_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set the style sheet
        self.setStyleSheet("""
            QScrollArea {
                background-color: white;
            }
            QTextEdit#input_box {
                background-color: white;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
            }
        """)

        self.listener = Listener(sock)
        self.listener.message_received.connect(self.handle_message)
        self.thread = QThread()
        self.listener.moveToThread(self.thread)

        # Start the listening thread
        self.thread.started.connect(self.listener.listen)
        self.thread.start()

    def handle_message(self, message):
        if message == 'refresh':
            self.counter = 1
            self.input_box.clear()
            self.input_box.setPlaceholderText("Saisissez votre problème ici")
        else:
            # Create a new text edit widget for the message
            message_widget = QTextEdit(message)
            message_widget.setReadOnly(True)

            # Set the style sheet based on the sender
            message_widget.setStyleSheet("background-color: #f7f7f7;color: black; font-family: arial; padding:15px; font-size:15px")
            message_widget.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
            #message_widget.setSizeAdjustPolicy()

            # Add the message widget to the chat layout
            self.chat_layout.addWidget(message_widget)
            self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())
            # Start listening for messages in a separate thread
            #self.start_listening()



    def send_message(self):
        message = self.input_box.toPlainText()
        self.input_box.clear()
        self.input_box.setPlaceholderText("Saisissez votre réponse ici")

        # Create a new text edit widget for the message
        message_widget = QTextEdit(message)
        message_widget.setReadOnly(True)
        message_widget.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        #message_widget.setSize
        # Set the style sheet based on the sender
        message_widget.setStyleSheet("background-color: #005c96; color: white; text-align: right; font-family: arial; padding:15px; height:auto; font-size:15px")

        # Add the message widget to the chat layout
        self.chat_layout.addWidget(message_widget)
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

        # Send the message to the specified IP address
        if self.counter ==1 :
            data = {
                'pb': message,
            }
        else:
            data = {
                'response': message,
            }
        # Conversion de l'objet JSON en chaîne de caractères
        json_data = json.dumps(data)

        sock.sendall(json_data.encode())
        self.counter+=1

    def refresh(self):
        self.counter = 1
        self.input_box.clear()
        self.input_box.setPlaceholderText("Saisissez votre problème ici")
        # Supprimer tous les éléments du chat_layout
        while self.chat_layout.count():
            item = self.chat_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        data = {
                'response': 'refresh'
        }
        # Conversion de l'objet JSON en chaîne de caractères
        json_data = json.dumps(data)

        sock.sendall(json_data.encode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
    sock.close()