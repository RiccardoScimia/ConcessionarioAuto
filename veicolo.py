veicolo = [{"id_veicolo": 1, "marca": "Fiat", "modello": "Panda", "tipo": "auto", "anno": 2010},
           {"id_veicolo": 2, "marca": "Mazda", "modello": "Mx-5", "tipo": "auto", "anno": 1995},
           {"id_veicolo": 3, "marca": "Fiat", "modello": "500", "tipo": "auto", "anno": 2015},
           {"id_veicolo": 4, "marca": "Fiat", "modello": "Bravo", "tipo": "auto", "anno": 2017},
           {"id_veicolo": 5, "marca": "Fiat", "modello": "Tipo", "tipo": "auto", "anno": 2019}]

dipendente = [{"id_dipendente": 1, "nome": "Mario", "Cognome": "Rossi", "reparto": "Vendite"},
              {"id_dipendente": 2, "nome": "Luca", "Cognome": "Verdi", "reparto": "Vendite"},
              {"id_dipendente": 3, "nome": "Paolo", "Cognome": "Bianchi", "reparto": "Vendite"},
              {"id_dipendente": 4, "nome": "Giovanni", "Cognome": "Neri", "reparto": "Vendite"},
              {"id_dipendente": 5, "nome": "Giuseppe", "Cognome": "Gialli", "reparto": "Vendite"}]

assegnazione = [{"id_assegnazione": 1, "id_veicolo": 1, "id_dipendente": 2, "data": "23/02/2012"},
                {"id_assegnazione": 2, "id_veicolo": 2, "id_dipendente": 3, "data": "20/04/2020"},
                {"id_assegnazione": 3, "id_veicolo": 3, "id_dipendente": 4, "data": "14/12/2020"}]

def aggiungi_veicolo(id_veicolo, marca, modello, tipo, anno):
    id_veicolo = veicolo[-1]["id_veicolo"] + 1
    veicolo.append({"id_veicolo": id_veicolo, "marca": marca, "modello": modello, "tipo": tipo, "anno": anno})
    
    return veicolo

def aggiungi_dipendente(id_dipendente, nome, cognome, reparto):
    id_dipendente = dipendente[-1]["id_dipendente"] + 1
    dipendente.append({"id_dipendente": id_dipendente, "nome": nome, "cognome": cognome, "reparto": reparto})
    
    return dipendente

def assegna_veicolo(id_assegnazione, id_veicolo, id_dipendente, data):
    id_assegnazione = assegnazione[-1]["id_assegnazione"] + 1
    
    assegnazione.append({"id_assegnazione": id_assegnazione, "id_veicolo": id_veicolo, "id_dipendente": id_dipendente, "data": data})
    
    if veicolo["id_veicolo"] == id_veicolo and dipendente["id_dipendente"] == id_dipendente:
        print("Veicolo assegnato")
        return assegnazione

    return assegnazione

#def elimina_veicolo(id_veicolo):
#    for i in veicolo:
#        if i["id_veicolo"] == id_veicolo:
#            veicolo.remove(i)
#            
#    return veicolo

print("1. Aggiungi veicolo\n2. Aggiungi dipendente\n3. Assegna veicolo\n4. Elimina dipendente\n5. Visualizza veicoli\n6. Visualizza dipendenti\n7. Esci\n")
scelta = int(input("Scegli un'opzione: "))

match scelta:
    case 1:
        aggiungi_veicolo(veicolo, input("Marca: "), input("Modello: "), input("Tipo: "), input("Anno: "))
    case 2:
        aggiungi_dipendente(dipendente, input("Nome: "), input("Cognome: "), input("Reparto: "))
    case 3:
        assegna_veicolo(assegnazione, input("ID veicolo"), input("ID dipendente"), input("Data: "))
    case _:
        print("Nessun match")