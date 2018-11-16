def readinputfile():
    filepath = 'full_database.xml'
    count=0;
    f=open(filepath,'r');
    line=f.readline();
    l=line.lstrip()
    l=l.rstrip()
    flag=1
    lc=0;
    while len(line)>0:
        if l[0:6]=='<drug ':
            count=count+1
            print "the "+str(count)+"th Drug is creating"
            nf=open("drugs/"+str(count)+".xml",'w')
            while (not (l[0:7]=='</drug>') or (flag==0)):
                nf.write(line)
                line=f.readline()
                l=line.lstrip()
                l=l.rstrip()
                if l[0:8]=='<pathway':
                    flag=0
                if l[0:9]=='</pathway' or l[0:11]=='<pathways/>':
                    flag=1
                if l[0:9]=="<ndc-id/>":
                    line=l[0:7]+l[8:len(l)]
                if l[len(l)-2:len(l)]=="/>":
                    line=l[0:len(l)-2]+">null</"+l[1:len(l)-2]+">\n"
                    if l[0:19]=="<ended-marketing-on":
                        line="<ended-marketing-on>2070-11-08</ended-marketing-on>"
                    if l[0:21]=="<started-marketing-on":
                        line="<started-marketing-on>2070-11-08</started-marketing-on>"
                    if l[0:14]=="<gene-sequence":
                        line="<gene-sequence> without sequence</gene-sequence>"
                    l=line.lstrip()
                    l=l.rstrip()
                if "'" in (line):
                    line=line.replace("'","")
            nf.write(line)
            nf.close()
            flag=1
        line=f.readline()
        l=line.lstrip()
        if len(l)==0:
            lc=lc+1
        if lc>100:
            break
    print 'The program reached to EOF'
    return;

readinputfile()
