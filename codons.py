def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split('\t')
            codon = row[0]
            amino_acid = row[2]
            codon_dict[codon] = amino_acid
    return codon_dict

