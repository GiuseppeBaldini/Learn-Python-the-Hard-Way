print "Ehi, benvenuto A Gotham City. Gradisce un costume da Batman?"
print "P.S. Batmobile non inclusa."

batman = raw_input("> ")

if batman == "Si":
    print "A Bruce Wayne non piace avere un concorrente."
    print "1. Affronti Bruce Wayne a mani nude. Scelta ammirevole."
    print "2. Te la svigni e torni a Barletta. Scelta pugliese."
    print "3. Chiedi l' aiuto da casa. Scelta Jerry Scotti."

    bruce = raw_input("> ")

    if bruce == "1":
        print "E' stato un piacere conoscerla. Porteremo fiori alla signora."
    elif bruce == "2":
        print "La capisco, bella regione la Puglia. Alfred ci va spesso."
    elif bruce == "3":
        print "Le risponde la suocera. Batman terrorizzato scappa in Uzbekisthan."
    else:
        "Essere alternative paga. Joker la arruola come portaborse."

elif batman == "No":
    print "E allora cosa ci fa a Gotham City? Torni a Bisceglie."

else:
    print "Dire si o no era troppo difficile eh? Eccole un costume da Enigmista"
