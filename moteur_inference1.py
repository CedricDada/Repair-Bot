from experta import *
import json
import socket
import time
import re

# Définition de l'adresse IP et du port du destinataire
HOST = '127.0.0.1'
PORT = 5039

# Ouvrir le fichier .txt
with open('./Knowledge_engine.txt', 'r') as file:
    content = file.read()

# Suppression des caractères de fin de ligne et de la balise 'end'
content = re.sub(r'(\n|end)', '', content)

# Conversion du contenu en une liste de dictionnaires
list_causes_effets = eval(content)

class Cause(Fact):
    pass

class Effet(Fact):
    pass

class Potential_cause(Fact):
    pass

class Launch_find_causes(Fact):
    pass

class liste_Effets(Fact):
    pass
#ici, effets implique causes, causes implique solutions
class Launch(Fact):
    pass

class base_connaissances(KnowledgeEngine):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
    @DefFacts()
    def _initial_action(self):
       yield Fact(action="greet")
    

    def send_and_receive(self, message):
        data = {
            'request': message,
        }
        json_data_request = json.dumps(data)

        try:
            self.conn.sendall(json_data_request.encode())
        except BrokenPipeError:
            print("La connexion a été fermée.")

        # Attente de la réponse
        response = None
        while response is None:
            # Réception de la réponse
            received_data = self.conn.recv(1024).decode()
            print("received_data",received_data)
            # Conversion de la chaîne de caractères en objet JSON
            json_response = json.loads(received_data)

            # Vérification si la réponse est présente dans les données reçues
            if 'response' in json_response:
                response = json_response['response']
                print(response)
            if 'pb' in json_response:
                response = json_response['pb']
                print(response)

        return response
    @Rule(Fact(action="greet"))
    def greetings(self):
        problem=self.send_and_receive("Donner une description de votre problème")
        print("problem", problem)
        if(problem!="refresh"):
            self.declare(Launch(action="launch", pb=problem))

    @Rule(Launch(action="launch", pb=MATCH.pb))
    def ask_effect(self, pb):
        #pb=input("Décrivez votre problème: ")
        pb1 = pb.lower()
        effets=""#effets doit contenir tous les effets recupérés dans list_causes_effets associés aux mots clés présents dans la variable pb
        for elt_list_causes_effets in list_causes_effets:
            for effet,mots_cles_effet in elt_list_causes_effets["mots_cles"].items():
                for mot_cle in mots_cles_effet:
                    if mot_cle in pb1:
                        effets+=effet+","
                        break
        effets = effets.split(",")
        effets = effets[:-1]
        if(len(effets)!=0):
            self.declare(liste_Effets(effets=effets))
        else:
            data = {
                'potential_cause': "Nous sommes désolé mais nous ne pouvons résoudre votre problème",
            }
            # Conversion de l'objet JSON en chaîne de caractères
            json_data = json.dumps(data)
            try:
                self.conn.sendall(json_data.encode())
            except BrokenPipeError:
                print("La connexion a été fermée.")
        print("self.conn",self.conn)
    
    @Rule(liste_Effets(effets=MATCH.effets))
    def  generation_Effets(self,effets):
        for i in range(len(effets)):
            self.declare(Effet(effet=effets[i]))
        self.declare(Launch_find_causes(action="go"))
    
    @Rule(Potential_cause(position_cause_in_list_causes_effets=MATCH.position_cause_in_list_causes_effets, list_effets=MATCH.list_effets))
    #pour lancer le potentiel cause, il faudrait que j'ai également reçu un fait de type MessagePotential qui sera envoyé à partir de l'interface
    #es ce que le premier potential cause va attendre le premier MessagePotential avant de lancer la règle ci
    #et de façon générale de i eme potential cause?
    def verification(self,position_cause_in_list_causes_effets, list_effets):
        list_effets_str=""
        for i in range(len(list_effets)):
            if i==0:
                list_effets_str+="\t -\t"+list_effets[i]
            else:
                list_effets_str+=",\n \t -\t"+list_effets[i]
        msg_request = "Potentielle cause de votre problème: \n"+list_causes_effets[position_cause_in_list_causes_effets]['cause']+"\n Cette cause produit généralement d'autres effets. Pour nous rassurer que la cause potentielle détectée est effectivement l'une des causes de votre problème, nous avons besoin de savoir si vous notez simultanément les effets suivants (repondez par oui ou non si c'est le cas)?:\n "+ list_effets_str
        val = self.send_and_receive(msg_request)

        if (val=='oui'):
            cause="Votre réponse nous permet conclure que la cause suivante est effectivement une cause de votre problème: \n"+list_causes_effets[position_cause_in_list_causes_effets]['cause']+" \n Les solutions à envisager sont les suivantes: \n"+list_causes_effets[position_cause_in_list_causes_effets]["solution"]+". \n Comme, méthodes préventives: "+list_causes_effets[position_cause_in_list_causes_effets]['prevention']
            data = {
                'cause': cause,
            }
            # Conversion de l'objet JSON en chaîne de caractères
            json_data = json.dumps(data)
            try:
                self.conn.sendall(json_data.encode())
            except BrokenPipeError:
                print("La connexion a été fermée.")

            print("\n")
            print(cause)
            print("\n")
        elif (val=='refresh'):
            self.reset()
        else:
            print("\n")
            cause="Votre réponse nous fait penser que le problème est ailleurs"
            data = {
                'cause': cause,
            }
            # Conversion de l'objet JSON en chaîne de caractères
            json_data = json.dumps(data)
            try:
                self.conn.sendall(json_data.encode())
            except BrokenPipeError:
                print("La connexion a été fermée.")
            print("Votre réponse nous fait penser que le problème est ailleurs, Envisageons une autre possibilité")
            print("\n")

    #for i in range(len(list_causes_effets)):
     #   for j in range(len(list_causes_effets[i]["effets"])):
     #           @Rule(Effet(effet=(list_causes_effets[i]["effets"])[j]))
     #           def regle1(self):
     #               self.declare(Cause(cause=list_causes_effets[i]["cause"]))

     #           @Rule(Effet(cause=(list_causes_effets[i]["cause"])))
      #          def regle2(self):
       #             print(list_causes_effets[i]["solution"])

    #@Rule(Effet(effet='écran noir'))
    #def regle1(self):
    #    self.declare(Cause(cause="problème d'alimentation"))

    #@Rule(Cause(cause="problème d'alimentation"))
    #def regle2(self):
    #    print("Mettez votre machine en charge")
            
    @Rule(Launch_find_causes(action="go"))
    def find_causes(self):
        #nous allons utiliser le chaînage arrière
        #la liste des causes est notre liste de buts, il faut alors l'extraire est notre liste de buts, cherchons toutes les règles dans lesquelles, elles apparaissent comme conséquences
        #ici, vu qu'ils n'y a pas de règles effets implique effets, on ne fera alors qu'un seule itération dans le chaînage arrière
        list_effets_utilisateur = []
        for i in range(len(self.facts)):
            if isinstance(self.facts[i],Effet):
                list_effets_utilisateur.append(self.facts[i]["effet"])
        #list_effets_utilisateur est bien définie
                
        for i in range(len(list_causes_effets)):
            result_verify_cause=[]#on doit allr checker self.facts pour filtrer 
            position=i
            #récupérons tous les effets de list_effets_utilisateur qui sont dans list_causes_effets[i]
            list_elts_in_i=[]
            for elt in list_effets_utilisateur:
                if elt in list_causes_effets[i]["effets"]:
                    list_elts_in_i.append(elt)
            result_verify_cause = list(set(list_causes_effets[i]['effets'])-set(list_elts_in_i))

            if(list_elts_in_i!=[] and len(list_elts_in_i)!=len(list_causes_effets[i]["effets"])):
                self.declare(Potential_cause(position_cause_in_list_causes_effets=position, list_effets=result_verify_cause))
            elif len(list_elts_in_i)==len(list_causes_effets[i]["effets"]):
                #on a trouver la cause du problème
                # Send the message to the specified IP address$
                cause="Nous pouvons citer comme causes de votre problème: "+list_causes_effets[i]["cause"]+'('+list_causes_effets[i]['organe']+')'+" et les solutions que vous pouvez envisager sont: "+list_causes_effets[i]["solution"]+". Comme, méthodes préventives: "+list_causes_effets[i]['prevention']
                data = {
                    'cause': cause,
                }
                # Conversion de l'objet JSON en chaîne de caractères
                json_data = json.dumps(data)
                try:
                    self.conn.sendall(json_data.encode())
                except BrokenPipeError:
                    print("La connexion a été fermée.")

                print("\n")
                print(cause)
                print("\n")

# Création d'une socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison de la socket à l'adresse IP et au port d'écoute
sock.bind((HOST, PORT))
print("sock",sock)

# Mise en écoute de la socket
sock.listen(1)

# Attente d'une connexion entrante
print('En attente de connexion...')
conn, addr = sock.accept()
print('Connexion établie avec', addr)

engine = base_connaissances(conn)
engine.reset()
#on met un écouteur de messages ici et quand je reçois le premier message,
#je penses que je peux faire en sorte que lorsque je reçois le premier message, qui est la description du problème, qu'on ajoute un fait de type FACT(action="launch", pb=contenu_message)
while True:
    engine.run()#chercher à faire que lorsqu'il n'y a plus de règle activable, que le moteur d'inférence reste quand même en running
    #chercher comment déclarer un fait à partir d'un autre fichier
    engine.reset()
    data = {
        'refresh': 'refresh',
    }
    # Conversion de l'objet JSON en chaîne de caractères
    json_data = json.dumps(data)
    try:
        conn.sendall(json_data.encode())
    except BrokenPipeError:
        print("La connexion a été fermée.")
conn.close()