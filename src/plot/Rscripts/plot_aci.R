library(ggplot2)

# setwd("C:/UMoncton/Doctorat/dev/ecosongs")
setwd("~/Doctorat/dev/ecosongs")

sval_aci <- read.csv("results/sval1_aci_summary.csv")
sval_aci$site <- "Svalbard"
burn_aci <- read.csv("results/burn1_aci_summary.csv")
burn_aci$site <- "Burnpoint Creek"
eaba_aci <- read.csv("results/eaba1_aci_summary.csv")
eaba_aci$site <- "East Bay"

aci <- rbind(sval_aci, burn_aci, eaba_aci)

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
