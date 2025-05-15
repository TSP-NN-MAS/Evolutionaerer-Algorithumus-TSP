from os.path import split
from typing import Tuple
class filesandata:
    def __init__(self,filepath):
        self.filedir = filepath
        self.citys = self.extract_citys_as_lists_from_file(self.filedir)



    def create_data_tuple(self,line: str) -> tuple[int, int]:
        #line ist ein sting mit 3 verschiedenen Zahlen z.B. 1 102 123
        parts = line.split()
        #liune.split teilt es auf in 1, 102, 123
        x_koordinate = int(parts[1])
        y_koordinate = int(parts[2])
        return (x_koordinate, y_koordinate)

    def extract_citys_as_lists_from_file(self,filedir)->list[Tuple[int,int]]:
        dimension = 0
        citys =[]

        current_file_as_strings: list[tuple[int, str]] = []
        f=open(filedir,"r")


        #extrahiere die Menge an Datenpunkten
        #die menge an datenpunkten steht in der dritten Zeile von index 11 bis indey
        for index, line in enumerate(f):
            if index == 3:
                dimension=""
                for number in line:
                    try:
                        dimension+=str(int(number))# es wird nur ein buchstabe hinzugefügt der auch eine Zahl ist
                    except ValueError:
                        a =0 #macht nichts aber ich brauche das except damit das try funktioniert
                dimension = int(dimension) #buchstaben werden in die funktionale Zahl konvertiert
                break



        # f ist ein itterator und kann nur einmal durchgelaufen werden desswegen muss er nochmal befüllt werden
        f=open(filedir,"r")
        for index,line in enumerate(f):
            if index<6: continue
            # ab index 6 fangen die daten an
            if index>6+(dimension-1) :break
            else:
                #hier wird jede zeile konvertiert in ein tuple aus x und y achse
                citys.append(self.create_data_tuple(line))

        return citys



