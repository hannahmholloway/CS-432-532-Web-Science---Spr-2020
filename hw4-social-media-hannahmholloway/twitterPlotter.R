pdf("twitterplotter.pdf")
mydata=read.table("twitter.data",sep="\t",header = FALSE)
num<-nrow(mydata)
nmean<-mean(mydata$V1)
nsd<-sd(mydata$V1)
nmedian<-median(mydata$V1)
mlnIdx<-which(mydata$V2 == "Hannah")
plot(sequence(num),mydata$V1, main = "Plot of number of followers on twitter", 
     xlab = "friends name", ylab = "number of friends one have",xaxt='n',pch=16,cex=0.5)
abline(v=mlnIdx,col="red",lwd=2,lty=2)
meanpos<-approx( x = mydata$V1,y = sequence(num), xout = nmean)
medianpos<-approx( x = mydata$V1,y = sequence(num), xout = nmedian)
sdpos<-approx( x = mydata$V1,y = sequence(num), xout = nsd)
axis(1, at=c(1,num),
     lab=c("F1",paste("F",num)))
legend(x=.1,y=max(mydata$V1),c("Hannah"),
       col = c("red"),lty=c(2),
       cex=0.5)
dev.off()
