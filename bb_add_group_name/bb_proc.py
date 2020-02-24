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
			print rawline
			username=line.split(',')[0].strip('"').split('@')[0]#strip remove leading and trailing, without argument it removes white pspaces
			groupname='N/A'
			if len(rawline)==5:
				groupname=rawline[4].strip('\n')
			print groupname
			if not len(rawline[1])==2:
				#print ("Line{}:{}".format(cnt,username))#print username
				existing[str(username.strip('"'))]=groupname
			else:
				ungroup[str(username.strip('"'))]=1
			if len(rawline)==5:
				groupname=rawline[4]
				#if 
		line=fcr.readline()
		cnt+=1	
for key in existing:
	print "existing ",str(type(key)),len(key),key
new={}
bb_dict={}
with open('/home/chen/Downloads/CSE421/out_bb_user_co.csv','w')as out:
	with open('/home/chen/Downloads/CSE421/bb_user_co.csv', 'r') as fbb:
		line =fbb.readline()
		cnt=1
		while line:
			if cnt>1:	
				rawline=line.split(',')
				print rawline
				username_bb=line.split(',')[2].strip('"')
				print username_bb,len(username_bb)
				if username_bb in existing:
					out.write(line.rstrip('\n')+existing[username_bb]+",\n")	
				else:
					out.write(line)	
				#print str(type(username_bb)),len(username_bb),username_bb
				#if existing.get(username_bb)!=None:
				#	print username_bb+" exist!"
				#else:
				#	new[username_bb]=1 
			line=fbb.readline()
			print line
			cnt+=1	


#for key in new:
#	print key+"@buffalo.edu"

#print len(existing)
#print len(ungroup)
#print len(bb_dict)
#print len(new)






