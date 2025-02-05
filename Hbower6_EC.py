#!/usr/bin/env python3
import sys

blastfile = open(sys.argv[1])
bedfile = open(sys.argv[2])
outfile = sys.argv[3]

blastcontent = blastfile.read()
bedcontent = bedfile.read()

# blast file editing
temp = blastcontent.replace("\n", "\t")
# bed file editing
bed_lines = bedcontent.split("\n")

bed_data = []
for l in bed_lines:
    tempsplit = l.split("\t")
    bed_data.append(tempsplit)

blasthits = []
genehit = []

temp = blastcontent.replace("\n", "\t")
for p in blastcontent.split("\n"):
    splitblast = p.split("\t")
    if len(splitblast) > 12:
        blastpercentid = float(splitblast[2])
        blastalignlen = float(splitblast[3])
        blastqlen = float(splitblast[12])

    # >30% pid and >.9len
    if blastpercentid > 30 and blastalignlen > (0.9 * blastqlen):
        blasthits.append(splitblast)

bed_data = []
for line in bed_lines:
    columns = line.split("\t")
    bed_data.append(columns)

for i in blasthits:
    blastsequenceid = i[1]
    blaststart = int(i[8])
    blaststop = int(i[9])
    if blaststart < blaststop:
        blast_orentation = "+"
    else:
        blast_orentation = "-"

    for j in bed_data:
        if len(j) > 4:
            bedseqid = j[0]
            genename = j[3]
            bedstart = int(j[1])
            bedstop = int(j[2])
            bed_orientation = str(j[5])

            if blastsequenceid != bedseqid:
                continue
            if blaststart > bedstop:
                continue
            if blaststart < bedstart:
                break

            if (blaststart >= bedstart) and (blaststart <= bedstop) and (blaststop >= bedstart) and (
                    blaststop <= bedstop):

                if blast_orentation != bed_orientation:
                    continue

                genehit.append(genename)

# removing duplicates:
genehits_FINAL = []
for k in genehit:
    if k not in genehits_FINAL:
        genehits_FINAL.append(k)
        print("Matches: " + k)

# outfile time
with open(outfile, "w") as file:
    for o in genehits_FINAL:
        file.write("Match: " + o + "\n")
total_matches = len(genehits_FINAL)
print("Total matches: " + str(total_matches))
