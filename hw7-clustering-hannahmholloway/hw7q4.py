import clusters
account,words,data=clusters.readfile('userdata.txt')

print "For k=5"
kclust=clusters.kcluster(data, k=5)
for i in range(0,5):
	print "accounts in cluster"+' '+str(i+1)+'-------'
	for r in kclust[i]:
		print account[r]
	print '\n'
print "For k=10"
kclust=clusters.kcluster(data, k=10)
for i in range(0,10):
	print "accounts in cluster"+' '+str(i+1)+'-------'
	for r in kclust[i]:
		print account[r]
	print '\n'

print "For k=20"
kclust=clusters.kcluster(data, k=20)
for i in range(0,20):
	print "accounts in cluster"+' '+str(i+1)+'-------'
	for r in kclust[i]:
		print account[r]
	print '\n'
