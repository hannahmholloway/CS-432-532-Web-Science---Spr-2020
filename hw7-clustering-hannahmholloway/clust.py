import clusters
account,words,data=clusters.readfile('userdata.txt')
variable = clusters.hcluster(data)

# print ASCII dendrogram
clusters.printclust(variable, labels=blog)

# save JPEG dendrogram
clusters.drawdendrogram(variable, account, jpeg='dendrogram.jpg')
