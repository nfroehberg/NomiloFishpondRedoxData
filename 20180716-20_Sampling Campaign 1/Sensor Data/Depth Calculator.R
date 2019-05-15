library(readr)
NomiluStationData <- read_delim("NomiluStationData.csv", ";", escape_double = FALSE, trim_ws = TRUE)

#fro seawater absolute salinity and density:
library(gsw)
#for trapezoidal integration:
library(pracma)

out=data.frame()
for (i in c(1:max(NomiluStationData$station))){
  #extracting every station individually:
  station <- NomiluStationData[which(NomiluStationData$station==i),]
  station <- station[order(station$pW),]
  #insert dummy row with zero water pressure as integration represents the depth between first and last data point
  station <- rbind(station[1,], station)
  station$pW[1] <- 0
  #converting practical to absolute salinity using coordinates
  station$SA <- gsw_SA_from_SP(station$Salinity, station$pW*0.1, -159.526981, 21.887073)
  #calculating water density from absolute salinity, temperature [°C], and pressure [dbar]
  station$rho <- gsw_rho_t_exact(SA=station$SA, t=station$Tec, p=station$pW*0.1)
  #using trapezoidal integration to calculate depth from density and pressure
  station$Z <- cumtrapz(station$pW*1000, 1/(station$rho*9.81))
  #remove dummy row
  station <- station[c(-1),]
  out <- rbind(out, station)
}
write.csv(out, file="NomiluStationDataZ.csv")

                     