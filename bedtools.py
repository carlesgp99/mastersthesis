import argparse
import datetime

from Bio import SeqIO


def process_input(filename, chromosome, startGene, finGene):
    fasta_sequences = SeqIO.parse(open(filename), 'fasta')
    i = 1
    gene = ""
    for fasta in fasta_sequences:
        j = 0
        name, sequence = fasta.id, str(fasta.seq)
        if chromosome == name:
            while j < len(sequence) and i < startGene:
                j += 1
                i += 1
            if i == startGene:
                while j < len(sequence):
                    gene = gene + sequence[j]
                    if i == finGene:
                        return gene
                    j += 1
                    i += 1
            else:
                continue
        else:
            continue


if __name__ == "__main__":
    # Extraiem contingut del fitxer
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="FASTA file")
    parser.add_argument("chromosome", type=str, help="Chromosome selected")
    parser.add_argument("startGene", type=int)
    parser.add_argument("endGene", type=int)
    args = parser.parse_args()

    gene = process_input(args.filename, args.chromosome, args.startGene, args.endGene)
    print("\n"+gene)
    ts = datetime.datetime.now().timestamp()
    outfile = "GeneSeq" + str(int(ts)) + ".txt"

    with open(outfile, 'w') as out:
        out.write(gene)

