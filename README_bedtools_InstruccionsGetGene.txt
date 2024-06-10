Instruccions Get Gene

Aquestes instruccions estan fetes per poder extreure la seqüència d'un gen X a partir del fitxer yps128.fasta

Per fer-ho:

1. Crear una carpeta i afegir el fitxer fasta i les bedtools de python d'en gerard.

2. Anar al nom de la carpeta (a dalt de tot un cop oberta) i escriure, substituint tot, "cmd"

3. CMD obrirà els comandaments de windows, i allà s'ha de posar seguit:
	python bedtools.py yps128.fasta ChrX STARTGENE STOPGENE
#posar 1000 bp extra upstream i downstream del gen d'interès
EXEMPLE:

C:\Users\selra\OneDrive\Escritorio\newprimers>python bedtools.py yps128.fasta Chr13 1 1000

CACACACACCCTAACACTATCTCAACCCTACCCTATTCTTACCCTGACCAACATGTCTCCCAGCTTACCCTCCATTACCCTACCTCTCCA...

Funciona!!! Enjoy:)

Remarcar que funciona pq hi ha un patch instal·lat de python a windows amb el paquet 'Bio'
Després, obrir l'arxiu amb la seqüència a l'ApE (a plasmid editor), i de la posició 750 a la 1200 (450 bp) es poden generar els primers utilitzant primers designing tool ncbi
