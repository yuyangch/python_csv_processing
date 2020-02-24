#!/usr/bin/env python
#note it appears that list from blackboard gives weird string

existing={}
ungroup={}
group_dict={}


with open('/home/chen/Downloads/CSE421/grouping/classroom_roster.csv', 'r') as fcr:
	line =fcr.readline()
	cnt=1
	while line:
		#print line.split(',')
		if cnt>1:
			rawline=line.split(',')
			username=line.split(',')[0].strip('"').split('@')[0]#strip remove leading and trailing, without argument it removes white pspaces
			if len(rawline)==5:
				groupname=line.split(',')[4]
				if len(groupname)==2:
					continue
				elif groupname not in group_dict:
					#print "new group name",groupname
					group_dict[groupname]=list()
					#print "username",type(username)
					#print "[].append([username])",[username]
					group_dict[groupname]=[username]
					#print "group_dict[groupname]",group_dict[groupname]
				elif groupname in group_dict:
					templist=group_dict[groupname]
					#print "found a match",type(templist),templist,type(list),groupname
					if type(templist) == type(['123']):
						#print "append!"
						templist1=templist.append(username)
						#print templist
						#print group_dict[groupname]
						#group_dict[groupname]=templist.append(username)
						#print group_dict[groupname]
				else:
					continue


		line=fcr.readline()
		cnt+=1	

acc=0
for key in group_dict:
	acc+=len(group_dict[key])
	print key,group_dict[key]
	print "-------------------"

print acc

print "======================================================"


for key in group_dict:
	#acc+=len(group_dict[key])
	if len(group_dict[key])<=2:
		for name in group_dict[key]:
			print name+"@buffalo.edu"
		#print key,group_dict[key]
		#print "-------------------"

	
