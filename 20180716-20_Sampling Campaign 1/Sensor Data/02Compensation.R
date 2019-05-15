library(readr)
dat <- read_csv("NomiluStationDataZ.csv")

#defining coefficients:
B0 <- -6.24097e-3
B1 <- -6.93498e-3
B2 <- -6.90358e-3
B3 <- -4.29155e-3
C0 <- -3.11680e-7

#scaled temperature:
Tsc <- log((298.15-dat$Toptode)/(273.15+dat$Toptode))
#salinity compensation:
dat$O2Comp <- dat$O2Concentration*exp(dat$Salinity * (B0+ B1*Tsc + B2*Tsc^2 + B3*Tsc^3) + C0*dat$Salinity)
#depth compensation:
dat$O2Comp <- dat$O2Comp*(1+((0.032*dat$pW*0.1)/1000))

Stations <- read_csv("C:/Users/Nico/OneDrive/Hawaii/Data/Sampling Campaign 1/cast/data/Combined/Nomilu Stations.csv")

Stations <- Stations[,c("Lat2","Long2","StationNum")]
for (i in c(1:nrow(dat))){
  station <- dat$station[i]
  dat$lat[i] <- Stations$Lat2[which(Stations$StationNum==station)]
  dat$lon[i] <- Stations$Long2[which(Stations$StationNum==station)]
}
dat <- dat[ , -which(names(dat) %in% c("X1", "X1_2", "X1_1"))]

#splitting date and time into components for ODV:
library(lubridate)
dat$ts <- as.POSIXct(dat$ts, format="%d.%m.%Y %H:%M")
dat$Year <- year(dat$ts)
dat$Month <- month(dat$ts)
dat$Day <- mday(dat$ts)
dat$Hour <- hour(dat$ts)
dat$Minute <- minute(dat$ts)
dat$Second <- second(dat$ts)

#writing output for ODV of mapping campaign and time profile
write.csv(dat, file="NomiluStationDataZ.csv")
write.csv(subset(dat, station >=1 & station <= 20), file="NomiluStationDataProfiles.csv")
write.csv(subset(dat, station >=22 & station <= 26), file="NomiluStationDataTimeSeries.csv")

