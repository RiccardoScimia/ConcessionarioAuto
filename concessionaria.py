class parco_Auto:

        def __init__(self):
            self.lista_auto = {}

        def aggiungi_auto(self, id_veicolo, marca, modello, tipo, anno):
            auto = {
                    "id_veicolo": id_veicolo,
                    "marca": marca,
                    "modello": modello,
                    "tipo": tipo,
                    "anno": anno                    
            }
            self.lista_auto.append(auto)
            print(f"{marca} {modello} aggiunto/a al parco auto")
        
        def visualizza_veicoli_disponibili(self):
            for auto in self.lista_auto:
                print(f"{auto['marca']} {auto['modello']} disponibile")


class veicolo_Assegnato(parco_Auto):
    
    def __init__(self, id_veicolo, marca,modello, tipo, anno, id_dipendente):
        super().__init__(id_veicolo, marca, modello, tipo, anno)
        self.id_dipendente = id_dipendente

    def lista_auto_assegnate(self):
        self.lista_auto_assegnate = []

    def assegna_veicolo(self, id_veicolo, id_dipendente):
        veicolo = {
            "id_veicolo": id_veicolo,
            "id_dipendente": id_dipendente
        }
        self.lista_auto_assegnate.append(veicolo)
        print(f"Veicolo {id_veicolo} assegnato a dipendente {id_dipendente}")
    
    def visualizza_assegnazioni(self):
        for veicolo in self.lista_auto_assegnate:
            print(f"Veicolo {veicolo['id_veicolo']} assegnato a dipendente {veicolo['id_dipendente']}")




class dipendente:
    def __init__(self):
        self.dipendenti = []

    def aggiungi_dipendente(self, id_dipendente, nome, cognome, reparto):
        dipendente = {
            "id_dipendente": id_dipendente,
            "nome": nome,
            "cognome": cognome,
            "reparto": reparto
        }
        self.dipendenti.append(dipendente)
        print(f"{nome} {cognome} aggiunto/a al registro dei dipendenti")



