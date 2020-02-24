#!/usr/bin/env python
#note it appears that list from blackboard gives weird string

existing={}
ungroup={}


with open('/home/chen/Downloads/CSE421/classroom_roster.csv', 'r') as fcr:
	line =fcr.readline()
	cnt=1
	while line:
		#print line.split(',')
		if cnt>1:
			rawline=line.split(',')
			username=line.split(',')[0].strip('"').split('@')[0]#strip remove leading and trailing, without argument it removes white pspaces
			if not len(rawline[1])==2:
				#print ("Line{}:{}".format(cnt,username))#print username
				existing[str(username.strip('"'))]=1
			else:
				ungroup[str(username.strip('"'))]=1	
		line=fcr.readline()
		cnt+=1	
for key in existing:
	print "existing ",str(type(key)),len(key),key
new={}
bb_dict={}
with open('/home/chen/Downloads/CSE421/classroom_roster.csv', 'r') as fbb:
	line =fbb.readline()
	cnt=1
	while line:
		if cnt>1:	
			rawline=line.split(',')
			username_bb=line.split(',')[0].strip('"').split('@')[0]
			print str(type(username_bb)),len(username_bb),username_bb
			if existing.get(username_bb)!=None:
				print username_bb+" exist!"
			else:
				new[username_bb]=1 
		line=fbb.readline()
		cnt+=1	


for key in new:
	print key+"@buffalo.edu"

print len(existing)
print len(ungroup)
#print len(bb_dict)
print len(new)






