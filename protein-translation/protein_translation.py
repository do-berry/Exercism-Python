codons = {
    'Methionine' : ["AUG"],
    'Phenylalanine' : ["UUU", "UUC"],
    'Leucine' : ["UUA", "UUG"],
    'Serine' : ["UCU", "UCC", "UCA", "UCG"],
    'Tyrosine' : ["UAU", "UAC"],
    'Cysteine' : ["UGU", "UGC"],
    'Tryptophan' : ["UGG"],
    'STOP' : ["UAA", "UAG", "UGA"]
}

def reset():
    return ""

def findInCodons(var):
    for key in codons.keys():
        if var  in codons[key]:
            return key

def proteins(strand):
    codon = ""
    protein = []
    for i in range(len(strand)):
        if i % 3 == 0:
            codon = reset()
        codon += strand[i]
        if i % 3 == 2:
            if findInCodons(codon) == "STOP":
                break
            else:
                protein.append(findInCodons(codon))
    return protein
