from menu import menu
import creecompte


if __name__ == '__main__':
    choix = menu()
    match choix:
        case 0:
            print("Notre service client n'est pas disponible pour l'intant merci de reassayer plus tards")
        case 1:
            creecompte.newcompte()