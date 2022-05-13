tmp <- read.csv("following_count_without_me.csv")
following_count <- tmp[,2]
> write(mean(following_count),stdout())
2953.198
> write(median(following_count),stdout())
369
> write(sd(following_count),stdout())
14123.16
