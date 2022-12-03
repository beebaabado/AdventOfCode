elf_totals = []
elf_max = 0
total = 0

lines = open('day1_input.txt')

for line in lines:
    print("Line: ", line)
    if line.strip():
        total = total + int(line)
        print(total)
    else:
        print("ELF total: ", total)
        elf_totals.append(total)
        if total > elf_max:
           elf_max = total
        total = 0

elf_totals.sort(reverse=True)
print(elf_totals[:3])
print(elf_totals[0] + elf_totals[1] + elf_totals[2])
print(elf_max, elf_totals[0])	
