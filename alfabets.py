alfabets=["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","R","S","Š","T","U","Ū","V","Z","Ž"]

vardi={burt: None for burt in alfabets}

def valid_input(word):

    return word[0].isupper() and word.isalpha()

def pievienot_vardu(word):
    if not valid_input(word):
        print("Nederīga ievade!")
        return
    
    pirmais_burts= word[0].upper()


    if pirmais_burts in vardi:

        if vardi[pirmais_burts] is None:
            vardi[pirmais_burts]=word
            print(f"Pievienoju vārdu {word} vietā {pirmais_burts}, apmainu vardu {vardi[pirmais_burts]} ar {word}")

        else:
            print(f"Vārda vietā {pirmais_burts} jau")
            vardi[pirmais_burts]=word
    else:
        print("Nepareizs pirmais burts! Ludzu ievadi kko norm")

def izvada_vardus():
    print("\nAlfabēta vārdi:")
    for burt, vards, in vardi.items():
        if vards:
            print(f"{burt}: {vards}")
        else:
            print(f"{burt}: Nav vārda")
def viss_aizpildīts():
    return (vards is not None for vards in vardi.values())
    
    
    

def galvena_programma():
    vārdi=["Ainaži", "Saulkrasti", "Dobele", "Sigulda", "Ventspils", "Vecumnieki", "Zilupe", "Engure", "Jūrmala", "Rīga","Ogre"]
    

    for vards in vārdi:
        pievienot_vardu(vards)
        izvada_vardus()
    else:
        print("\n Alfabēt aizpildīts")
        #if viss_aizpildīts():
            #print("\n Alfabets aizpildits")
           # break
        

galvena_programma()