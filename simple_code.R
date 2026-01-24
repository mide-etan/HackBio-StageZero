# This stores my personal details, a favorite gene, and its organism in a simple list,
# then prints them as a single, readable sentence.
names <- 'Olamide Aworetan'
affiliation <- 'Ekiti State University'
favorite_gene <- 'lacZ'
organism <- 'Escherichia coli'

paste0(
  "Hi, my name is ", names,
  ", a researcher at ", affiliation,
  ". My favorite gene is ", favorite_gene,
  " in ", organism
)
