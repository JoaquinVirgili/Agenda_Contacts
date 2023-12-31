from os import system
from Controllers.ContactController import ContactController
from Model.DTO.ContactForDelete import ContactForDelete
from Model.DTO.ContactForUpdate import ContactForUpdate
from Model.DTO.UserForView import UserForView
from datetime import datetime

class ContactView:    
    def __init__(self, user):
        self.user_logged = user
    
    def Menu(self):
        while True:
            system("cls")
            print(" Menu de contactos ".center(50, "#"))
            print("1 - Lista de contactos")
            print("2 - Listar contactos que cumplan este mes")
            print("3 - Agregar contacto")
            print("4 - Editar contacto")
            print("5 - Eliminar contacto")
            print("6 - Cerrar sesion de usuario")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                self.listContacts()
            elif option == "2":
                self.listContacts_Birthday()
            elif option == "3":
                self.addContact()
            elif option == "4":
                self.editContact()
            elif option == "5":
                self.deleteContact()
            elif option == "6":
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))

    def listContacts(self):
        system("cls")
        print(" Lista de contactos ".center(50, "#"))
        contactC = ContactController()
        contacts = contactC.get_contacts_by_user(self.user_logged.username)
        for contact in contacts:
            print(contact)
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

    def listContacts_Birthday(self):
        system("cls")
        print(" Contactos que cumplen años este mes ".center(50, "#"))
        contactC = ContactController()
        contacts = contactC.get_contacts_birthday(self.user_logged.username)
        for contact in contacts:
            print(contact)
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

    def addContact(self):
        system("cls")
        print(" Alta de contacto ".center(50, "!"))
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        while True:
            fechaNacimiento = input("Ingrese fecha de nacimiento (deje vacío para finalizar): ").replace("/", "-")
            print("-"*50)

            if fechaNacimiento == "":
                break

            try:
                fechaNacimiento_date = datetime.strptime(fechaNacimiento, "%d-%m-%Y")
                break
            except ValueError:
                print("La fecha de cumpleaños es inválida. Ingrese una fecha válida o deje vacío para finalizar.")

        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        contactC = ContactController()
        contactC.add_contact(ContactForUpdate(0, name, surname, fechaNacimiento, email, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))

    def editContact(self):
        system("cls")
        print(" Editar contacto ".center(50, "#"))
        print("-"*50)
        id = input("Ingrese el id del contacto a editar: ")
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        while True:
            fechaNacimiento = input("Ingrese fecha de nacimiento (deje vacío para finalizar): ").replace("/", "-")
            print("-"*50)

            if fechaNacimiento == "":
                break

            try:
                fechaNacimiento_date = datetime.strptime(fechaNacimiento, "%d-%m-%Y")
                break
            except ValueError:
                print("La fecha de cumpleaños es inválida. Ingrese una fecha válida o deje vacío para finalizar.")

        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        contactC = ContactController()
        contactC.update_contact(ContactForUpdate(id, name, surname, fechaNacimiento, email, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))

    def deleteContact(self):
        system("cls")
        print(" Eliminar contacto ".center(50, "!"))
        print("-"*50)
        id = input("Ingrese el id del contacto a eliminar: ")
        print("-"*50)
        contactC = ContactController()
        contactC.delete_contact(ContactForDelete(id, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))
