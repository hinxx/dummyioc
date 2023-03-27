import sys


#file db/wfx.db {
#    pattern { ID, NELM,  FTVL,     SCAN }
#            {  1, 1, "DOUBLE", ".07 second" }
#...
#}

txt = 'file db/wfrec.db {\n'
txt += '    pattern { %35s, %5s, %10s, %15s }\n' % ('NAME', 'NELM', 'FTVL', 'SCAN')

nelm = int(sys.argv[2])
types = ['"DOUBLE"', '"LONG"', '"SHORT"', '"FLOAT"', '"CHAR"']
scans = ['".07 second"', '".05 second"', '".1 second"', '".5 second"', '"1 second"']

for i in range(int(sys.argv[1])):
	name = 'pvname-%d-%d-%s-%s' % (i, nelm, types[i%len(types)], scans[i%len(scans)])
	name = name.replace('"', '').replace('.', 'x').replace(' ', '_')
	name = '"' + name + '"'
	txt += '            { %35s, %5d, %10s, %15s }\n' % (name, nelm, types[i%len(types)], scans[i%len(scans)])

txt += '}\n'

print(txt)

