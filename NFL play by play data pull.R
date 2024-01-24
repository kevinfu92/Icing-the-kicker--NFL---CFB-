library(nflfastR)
# Pull NFL play by play data from https://www.nflfastr.com/
for (year in 2010:2023){
  data <- load_pbp(year)
  file_name = paste('C:\\Users\\kevin\\Desktop\\Python Projects\\Icing-the-kicker--NFL---CFB-\\NFL data\\',toString(year), '_nfl.csv', sep='')
  write.csv(data, file_name, row.names=FALSE)
  print(year)
}
