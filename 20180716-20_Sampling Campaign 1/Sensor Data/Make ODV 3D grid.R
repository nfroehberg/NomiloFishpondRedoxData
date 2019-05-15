library(readr)
ODV_grid <- read_csv("ODV_grid.csv")
res <- 0.2

out <- data.frame()
for (i in c(1 : nrow(ODV_grid))){
  levels <- ODV_grid[i,3]%/%res
  for (j in c(1:levels[1,1])){
    depth <- 0 + (j-1)*res
    line <- data.frame(paste (ODV_grid$X[i],ODV_grid$Y[i], depth))
    out <- rbind(out, line)
  }
}
write.table(out, file="ODV_grid.txt", row.names=FALSE, col.names=FALSE, quote=FALSE)
