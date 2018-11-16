library(feather)
library(lme4)
library(lmerTest)
setwd("/home/vin/Doctorat/dev/ecosongs/src/plots")

data <- read_feather("data_glm.feather")

str(data)
data$site <- as.factor(data$site)

model <- lmer(ACI_mean~julian + lat_mean+lon_mean+(1|site), data)
summary(model)
anova(model)