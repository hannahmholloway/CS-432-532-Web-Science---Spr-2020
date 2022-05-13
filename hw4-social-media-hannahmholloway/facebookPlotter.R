> data=read.csv("HW4-friend-count.csv", header=T, sep=',')
> FRIENDCOUNT=data[-nrow(data),]
> print(mean(FRIENDCOUNT[,"FRIENDCOUNT"]))
[1] 538.8247
> print(sd(FRIENDCOUNT[,"FRIENDCOUNT"]))
[1] 540.8818
> print(median(FRIENDCOUNT[,"FRIENDCOUNT"]))
[1] 395
> data=data[order(data[,"FRIENDCOUNT"],decreasing=TRUE),]
> Mc=which(data[,"USER"]=='Mc')
> plot(log(data[,"FRIENDCOUNT"],base=2),main="Friend# of My Friends", xlab="My Friends",ylab="log2(Number of Friends)")
> text(Mc, log(data[Mc,"FRIENDCOUNT"],base=2)+0.5,"Mc", col="Red")
