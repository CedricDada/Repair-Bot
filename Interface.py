import sys
import json
import socket
from PyQt5.QtWidgets import QScrollBar, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QAction, QFileDialog, QScrollArea, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QFile, pyqtSignal,QObject, QThread

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

class ChatBotWindow(QMainWindow):
    
    typing_speed = 50  # Caractères par minute

    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.counter = 1
        current_text = ""
        current_index = 0
        
        self.listener = Listener(sock)
        self.listener.message_received.connect(self.handle_message)
        self.thread = QThread()
        self.listener.moveToThread(self.thread)

        # Start the listening thread
        self.thread.started.connect(self.listener.listen)
        self.thread.start()
        
    def initUI(self):
        self.setWindowTitle("The Maintainer App")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(300, 350, 500, 500)

        # Charger les styles CSS à partir du fichier styles.css
        style_file = QFile("styles.css")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            style_sheet = style_file.readAll().data().decode("utf-8")
            style_file.close()

        # Création de la zone de texte pour l'entrée de l'utilisateur
        self.input_edit = QTextEdit()
        self.input_edit.setMaximumHeight(120)
        self.input_edit.setStyleSheet(style_sheet)
        self.input_edit.setPlaceholderText("Decrivez votre probleme")

        # Création du bouton d'envoi
        self.send_button = QPushButton("Envoyer")
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setObjectName("send_button")
        self.send_button.setShortcut("Ctrl+Return")
        self.send_button.setStyleSheet(style_sheet)

        # Création du bouton pour effacer la conversation
        self.clear_button = QPushButton("Effacer")
        self.clear_button.clicked.connect(self.refresh)
        self.clear_button.setObjectName("clear_button")
        self.clear_button.setShortcut("Ctrl+x")
        self.clear_button.setStyleSheet(style_sheet)

        # Création de l'action "Ouvrir" dans la barre de menu
        open_action = QAction(QIcon("open.png"), "Ouvrir", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)

        # Création de l'action "Sauvegarder" dans la barre de menu
        save_action = QAction(QIcon(""), "Sauvegarder", self)
        save_action.setShortcut("Ctrl+s")
        save_action.triggered.connect(self.save_conversation)

        # Création des actions pour le thème jour et nuit
        day_theme_action = QAction(QIcon(), "Thème Jour", self)
        day_theme_action.triggered.connect(self.set_day_theme)

        night_theme_action = QAction(QIcon(), "Thème Nuit", self)
        night_theme_action.triggered.connect(self.set_night_theme)

        # Création de la barre de menu
        menubar = self.menuBar()
        menubar.setObjectName("menu")
        file_menu = menubar.addMenu("Options")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(day_theme_action)
        file_menu.addAction(night_theme_action)
        file_menu =menubar.addMenu("Retour")
        

        # Création du layout vertical pour organiser les widgets
        vbox = QVBoxLayout()

        # Création d'un widget pour afficher les messages dans une zone déroulante
        self.message_widget = QWidget()
        self.message_layout = QVBoxLayout()
        self.message_widget.setLayout(self.message_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.message_widget)

        vbox.addWidget(scroll_area)
        vbox.addWidget(self.input_edit)

        hbox = QHBoxLayout()
        hbox.addWidget(self.send_button)
        hbox.addWidget(self.clear_button)

        vbox.addLayout(hbox)

        # Création du widget principal et assignation du layout
        main_widget = QWidget()
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)

    def handle_message(self, message):
        if message == 'refresh':
            self.counter = 1
            self.input_edit.clear()
            self.input_edit.setPlaceholderText("Saisissez votre problème ici")
        else:
            self.display_message(message, "white", "black")
            self.bot_message_label = QLabel()
            
            self.bot_message_label.setWordWrap(True)
            # Ajouter le widget QLabel du message du bot à la layout
            self.message_layout.addWidget(self.bot_message_label)
        

    def send_message(self):

        user_input = self.input_edit.toPlainText()

        # Charger les styles CSS à partir du fichier styles.css
        style_file = QFile("styles.css")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            style_sheet = style_file.readAll().data().decode("utf-8")
            style_file.close()

        self.display_message(user_input, "#8A9Bea", "white")
        self.input_edit.clear()
        self.bot_message_label = QLabel()
        self.bot_message_label.setWordWrap(True)

        # Ajouter le widget QLabel du message du bot à la layout
        self.message_layout.addWidget(self.bot_message_label)

        # Send the message to the specified IP address
        if self.counter ==1 :
            data = {
                'pb': user_input,
            }
        else:
            data = {
                'response': user_input,
            }
        # Conversion de l'objet JSON en chaîne de caractères
        json_data = json.dumps(data)

        sock.sendall(json_data.encode())
        self.counter+=1

    def display_message(self, message, color_label, color_text):
        # Création d'un widget QLabel pour afficher le message dans une bulle
        message_label = QLabel(message)        
        message_label.setWordWrap(True)
        message_label.setStyleSheet(f"""
            QLabel {{
                background-color: {color_label};
                color : {color_text};
                border-radius: 10px;
                padding: 15px;
                margin : 10px;
                font-size: 9px;
                font-size : 17px;
                font-family : Helvetica;
                color : {color_text};
            }}
        """)
        message_label.adjustSize()

        # Ajout du widget QLabel au layout
        self.message_layout.addWidget(message_label)

        # Défilement vers le bas pour afficher le dernier message
        scroll_area = self.message_widget.parentWidget()

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Ouvrir un fichier", "", "Fichiers texte (*.txt)")
        if file_path:
            with open(file_path, "r") as file:
                file_content = file.read()
                self.input_edit.setPlainText(file_content)

    def save_conversation(self):
        # Ouvrir une boîte de dialogue pour sélectionner l'emplacement de sauvegarde du fichier
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Sauvegarder la conversation", "", "Fichiers texte (*.txt)")

        if file_path:
            # Récupérer le contenu de tous les messages affichés
            conversation = ""
            for i in range(self.message_layout.count()):
                message_widget = self.message_layout.itemAt(i).widget()
                if isinstance(message_widget, QLabel):
                    message_text = message_widget.text()
                    conversation += message_text + "\n"

            # Sauvegarder la conversation dans le fichier
            with open(file_path, "w") as file:
                file.write(conversation)
        return("conversation saved")

    def refresh(self):
        self.counter = 1
        self.input_edit.clear()
        self.input_edit.setPlaceholderText("Saisissez votre problème ici")
        # Supprimer tous les éléments du chat_layout
        while self.message_layout.count():
            item = self.message_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        data = {
                'response': 'refresh'
        }
        # Conversion de l'objet JSON en chaîne de caractères
        json_data = json.dumps(data)

        sock.sendall(json_data.encode())

    def set_day_theme(self):
        # Changer le thème de l'application pour le thème jour
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
            QLabel {
                background-color: #075E54;
                color: white;
                border-radius: 10px;
                padding: 8px;
                font-size: 12px;
            }
            QPushButton {
                background-color: #25D366;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 8px 16px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #128C7E;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 8px;
                font-size: 12px;
            }
        """)

    def set_night_theme(self):
        # Changer le thème de l'application pour le thème nuit
        self.setStyleSheet("""
            QMainWindow {
                background-color: #222222;
            }
            QLabel {
                background-color: #DCF8C6;
                color: black;
                border-radius: 10px;
                padding: 8px;
                font-size: 12px;
            }
            QPushButton {
                background-color: #25D366;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 8px 16px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #128C7E;
            }
            QTextEdit {
                background-color: #333333;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 8px;
                font-size: 12px;
            }
        """)


    def type_message(self):
        if self.current_index < len(self.current_text):
            self.message_widget.setText(self.current_text[:self.current_index])
            self.current_index += 1
        else:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatBotWindow()
    window.show()    
    sys.exit(app.exec_())
    sock.close()