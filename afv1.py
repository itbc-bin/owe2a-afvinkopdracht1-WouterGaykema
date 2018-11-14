# Naam:
# Datum:
# Versie:


# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje 
# van het bestand, met 5 tot 10 fasta's. Ga je runnen met het echte bestand,
# geef je programma dan even de tijd.

def main():
    bestand = "alpaca_test.fa"
    headers, seqs = lees_inhoud(bestand)
    
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:", headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA.  Er is iets fout gegaan.")
    

def lees_inhoud(
        bestands_naam):
        # deze functie zet een bestand om in een lijst
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
                headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs

    
def is_dna(
        seq):
        # Deze functie test of een string DNA is
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        dna = True
    return dna


def knipt(
        alpaca_seq):
        # deze functie geeft een lijst van alle enzymen die in de sequentie knippen
    bestand = open("enzymen.txt")
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^", "")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")
        try:
            is_dna(seq) 
        except:
            print("eiwitbestand is niet goed gesplitst")

try:
    bestandsnaam.endswith(".fasta")
except:
    print("Verkeerd bestandstype; fastabestand verwacht.")
    
    
try:
    type(check_is_dna) is bool
except: print("is_dna geeft geen boolean")
            
try:
    main()
except IOError:
    print("Bestand niet gevonden.)
