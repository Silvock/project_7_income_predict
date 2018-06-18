# Perou

PMQUANDL.GINI.V1=c( 99.91, 45.72, 44.02, 53.72, 56.14, 56.34, 50.77, 51.83, 54.04, 53.71, 51.2, 51.84, 51.67, 51.35, 48.55, 47.96, 46.21, 45.48, 45.11, 44.73)

Date=c( 1985, 1986, 1994, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013)

Noms = rep('PER',20)

indice_gini_perou =data.frame(Noms,Date,PMQUANDL.GINI.V1)

# Mexique

PMQUANDL.GINI.V1=c( 48.95, 54.34, 50.95, 51.7, 48.47, 48.97, 51.67, 49.54, 46.03, 51.11, 48.01, 48.23, 48.13, 48.07)

Date=c( 1984, 1989, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2005, 2006, 2008, 2010, 2012)

Noms = rep('MEX',14)

indice_gini_mexique=data.frame(Noms,Date,PMQUANDL.GINI.V1)

# Canada

PMQUANDL.GINI.V1=c( 32.6, 31.6, 31.15, 31.39, 31.77, 33.59, 33.65, 33.88, 33.9, 33.68)

Date=c( 1981, 1987, 1991, 1994, 1997, 1998, 2000, 2004, 2007, 2010)

Noms = rep('CAN',10)

indice_gini_canada=data.frame(Noms,Date,PMQUANDL.GINI.V1)

# Autriche

PMQUANDL.GINI.V1=c( 23.04, 31.52, 31.06, 30.28, 28.97, 29.87, 28.72, 29.59, 30.58, 30.45, 31.5, 30.25, 30.8, 30.48)

Date=c( 1987, 1994, 1995, 1997, 2000, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012)

Noms = rep('AUT',14)

indice_gini_autriche=data.frame(Noms,Date,PMQUANDL.GINI.V1)

#Allemagne

PMQUANDL.GINI.V1=c( 28.13, 28.46, 29.21, 28.61, 30.01, 29.44, 31.5, 32.78, NaN, 32.4, 31.29, 31.51, 31.14, 30.13)

Date=c( 1981, 1983, 1984, 1989, 1994, 2000, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011)

Noms = rep('DEU',14)

indice_gini_allemagne=data.frame(Noms,Date,PMQUANDL.GINI.V1)

indice_gini = rbind(indice_gini_allemagne,indice_gini_autriche,indice_gini_canada,indice_gini_mexique,indice_gini_perou)

write.csv(indice_gini,file='../../fichiers_csv/new_indice_gini.csv')

