fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
lines = []
mails = []

for line in fh:
    if line.startswith('From '):
        lines = line.split()
        mails.append(lines[1])

for mail in mails:
    counts[mail] = counts.get(mail, 0) + 1

commiter = None
cont = None

for mail,count in counts.items():
    if cont is None or count > cont:
        commiter = mail
        cont = count

print(commiter, cont)
