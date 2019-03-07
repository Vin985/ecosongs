library(ggplot2)
library(feather)
library(data.table)

setwd("C:/UMoncton/Doctorat/dev/ecosongs/src/plots")
# setwd("~/Doctorat/dev/ecosongs/src/plots")

aci <- read_feather("ACI.feather")

aci <- data.table(aci)

aci$date <- as.POSIXlt(aci$date)
aci$julian <- aci$date$yday


aci <- aci[aci$julian > 150,]

plot(burn_aci$julian, burn_aci$ACI, type = "l")
lines(sval_aci$julian, sval_aci$ACI, col = "blue")

ggplot(data = aci, aes(
  x = julian,
  y = ACI,
  colour = site
)) + facet_grid(rows = vars(site)) + geom_line()



# recordings$plot <- factor(recordings$plot, levels = sort(levels(recordings$plot), decreasing =T))
#
# opar <- par()
# par(mai = opar$mai + 1, oma = c(3,3,3,3))
# plot(recordings$julian, recordings$plot, yaxt = "n", ylab="")
# axis(side = 2, labels = levels(recordings$plot), las = 1, at = 1:22)
# par(opar)
