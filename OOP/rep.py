def dna_to_rna(dna):
    rna = dna.replace('T', 'U')
    print(rna)

dna_to_rna('TREGTHRNYT')

def powers_of_two(n):
    result = []
    for i in range(n + 1):   
        result.append(2 ** i)
    return result

print(powers_of_two(5))

msg = "HELLO WORLD"
for i, c in enumerate(msg):
    print(" " * i + c)



