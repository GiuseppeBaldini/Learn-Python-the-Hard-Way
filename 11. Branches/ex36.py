from sys import exit

def pd():
    print """Benvenuto nel PD. Come sa, abbiamo leggeri conflitti interni
al momento. Lei con chi si schiera: Renzi o Speranza?"""

    choice = raw_input("Scriva pure qui: ")
    if choice == "Renzi" or choice == "renzi":
        print """Ti piace vincere facile, eh? Buone notizie, piaci a Renzi.
Quante migliaia di voti credi di poter prendere a livello nazionale?"""

        voti = int(raw_input("Numero di voti in migliaia: "))
        if voti >= 50:
            print "Congratulazioni! Sei eletto alla Camera. Ottimo lavoro!"
            exit(0)
        elif voti < 50 and voti >= 30:
            print """Congratulazioni! Sei eletto al Senato
(che esiste ancora, grazie Referendum.)"""
        elif voti < 30:
            not_elected("Non hai raccolto abbastanza voti.")
        else:
            not_elected("Mi sembrava di aver chiesto un numero.")
    elif choice == "Speranza" or choice == "speranza":
        print "Certo che hai proprio la faccia come il culo!"
        not_elected("E poi, non puoi mica pretendere di essere eletto con Speranza")
    else:
        print "Impari a leggere, avevo chiesto Renzi o Speranza."
        not_elected("Spiacente, ma di analfabeti in politica ne abbiamo abbastanza.")

def m5s():
    print "Benvenuto al tuo primo meetup M5S. Hai mai fatto parte di partiti politici?"
    choice = raw_input("Si o no? ")
    if choice == "si":
        not_elected("Vergogna uomo della casta, torna nel tuo partito!")
    elif choice == "no":
        print "Sembri un tipo apposto. Benvenuto nel Movimento!"
        exit(0)
    else:
        not_elected("Le avevo chiesto si o no, non mi sembrava di aver chiesto molto.")

def fi():
    print "Benvenuto in Forza Italia. Silvio ti sta aspettando."
    print "Ma prima, una domanda: sei mai stato indagato?"
    choice = raw_input("Si o no? ")
    if choice == "si":
        print """Ottimo! Ti troverai molto bene qui. Fai come fossi a casa tua.
        Consigli:
        1) Parla lentamente con Gasparri, a volte non capisce se parli troppo
        veloce.
        2) Attento a non calpestare Brunetta"""
        exit(0)
    elif choice == "no":
        not_elected("Ma ci ha preso per gente onesta?!")
    else:
        not_elected("Le avevo chiesto si o no, non mi sembrava di aver chiesto molto.")

def new():
    print "Lei ha indubbiamente del fegato! Come si chiama questo nuovo partito?"
    choice = raw_input("Scriva qui >> ")
    print "%s, dice? Guardi, con un nome cosi prende meno voti di Casini." %choice
    exit(0)

def not_elected(why):
    print why, "E ora fuori di qui, vada a fare il portaborse!"

def start():
    print """Benvenuto nel mondo della politica italiana. Si sieda comodo e
stia attento a non calpestare Brunetta.
Come sa, le elezioni si avvicinano, con chi si candida?
PD, Movimento 5 Stelle (M5S), Forza Italia o nuovo partito?"""

    choice = raw_input("Prego, scriva qui il nome del partito >> ")

    if choice == "pd" or choice == "PD" or choice == "partito democratico":
        pd()
    elif choice == "Movimento 5 Stelle " or choice == "m5s" or choice == "M5S":
        m5s()
    elif choice == "Forza Italia" or choice == "fi" or choice == "forza italia":
        fi()
    elif choice == "nuovo partito" or choice == "nuovo":
        new()
    else:
        not_elected("Iniziamo bene, non sa neanche scegliere.")

start()
