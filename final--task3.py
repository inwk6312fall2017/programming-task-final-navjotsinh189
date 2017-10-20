file=open('running-config.cfg')
file1=open('newconfigfile','w')


def replace_ip():
 for line in file:
   file1.write(line.replace('172','192'))
 file1.close() 
 file.close()
replace_ip()
