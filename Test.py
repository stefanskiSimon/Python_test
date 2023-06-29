import abc
class Employee(abc.ABC):
    cos = []
    def __init__(self,imie,nazwisko,stanowisko,pensja,adresmail) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.pensja = pensja
        self.adresmail = adresmail
        Employee.Workerslist = []
        Employee.Workerslist.append(self)
        Employee.cos.append(self.pensja)
    def __add__(self,other):
        wynagrodzenie = (self.pensja+other.pensja)/2
        if(other.stanowisko == self.stanowisko):
            print(self.imie,other.nazwisko,str(wynagrodzenie))
        else:
            return None
    
    def wyswietl(self):
        pass
    @property
    def pensja1(self):
        return self.pensja
    @pensja1.setter
    def pensja1(self,a):
        if(a > 3*(sum(Employee.cos)/len(Employee.cos)) or a < (min(Employee.cos))/2):
            raise ValueError("Cancer")
        self.pensja = a
class Manager(Employee):
    def __init__(self, imie, nazwisko, stanowisko, pensja, adresmail,liczba_projektow = 0) -> None:
        super().__init__(imie, nazwisko, stanowisko, pensja, adresmail)
        self.liczba_projektow = liczba_projektow
    def usun_projekt(self,usun):
        self.liczba_projektow -= usun
    def dodaj_projekt(self,liczba):
        self.liczba_projektow += liczba
    def wyswietl(self):
        print(" Imie: " + self.imie)
        print(" Nazwisko: " + self.nazwisko)
        print(" Pensja: " + str(self.pensja))
        print(" Stanowisko : " + self.stanowisko)
        print(" Adres e-mail : " + self.adresmail)
        print(" Liczba projektów: " + str(self.liczba_projektow))
        print("")
class Programmer(Employee):
    def __init__(self, imie, nazwisko, stanowisko, pensja, adresmail,language_list = 0) -> None:
        super().__init__(imie, nazwisko, stanowisko, pensja, adresmail)
        language_list = []
        self.language_list = language_list
    def add_language(self,language) -> None:
        self.language_list.append(language)
    def delete_language(self,language) -> None:
        self.language_list.remove(language)
    def __str__(self) -> str:
        return f'{self.language_list}'
    def wyswietl(self):
        print(" Imie: " + self.imie)
        print(" Nazwisko: " + self.nazwisko)
        print(" Pensja: " + str(self.pensja))
        print(" Stanowisko : " + self.stanowisko)
        print(" Adres e-mail : " + self.adresmail)
        print(" Lista języków: " + str(self.language_list))
        print("")   
class Tester(Employee):
    def __init__(self, imie, nazwisko, stanowisko, pensja, adresmail, liczba_testow=0) -> None:
        super().__init__(imie, nazwisko, stanowisko, pensja, adresmail)
        self.liczba_testow = liczba_testow
    def add_test(self,ilosc) -> None:
        self.liczba_testow += ilosc
    def delete_test(self,ilosc2) -> None:
        self.liczba_testow -= ilosc2
    def wyswietl(self):
        print(" Imie: " + self.imie)
        print(" Nazwisko: " + self.nazwisko)
        print(" Pensja: " + str(self.pensja))
        print(" Stanowisko : " + self.stanowisko)
        print(" Adres e-mail : " + self.adresmail)
        print(" Liczba testów: " + str(self.liczba_testow))
        print("")
postac = Programmer("Szymon","Stefanski","Programmer",3000,"adresemail@.com")
postac.add_language("Java")
postac.add_language("C#")
postac.wyswietl()
postac.pensja1 = postac.pensja

postac2 = Tester("Zbigniew","Szymański","Tester",5000,"Adresemail@com")
postac2.add_test(4)
postac2.delete_test(3)
postac2.wyswietl()
postac2.pensja1 = postac2.pensja

postac3 = Manager("Leon","Stańczyk","Manager",8000,"Adresemail@.com")
postac3.dodaj_projekt(12)
postac3.usun_projekt(3)
postac3.wyswietl()
postac3.pensja1 = postac3.pensja

postac4 = postac + postac2
