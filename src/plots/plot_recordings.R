setwd("C:/UMoncton/Doctorat/dev/ecosongs")

recordings <- read.csv("recordings.csv")

recordings$plot <- factor(recordings$plot, levels = sort(levels(recordings$plot), decreasing =T))

opar <- par()
# par(mai = opar$mai + 1, oma = c(3,3,3,3))
plot(recordings$julian, recordings$plot, yaxt = "n", ylab="")
axis(side = 2, labels = levels(recordings$plot), las = 1, at = 1:22)
# par(opar)
