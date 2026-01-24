# This stores my personal details, a favorite gene, and its organism in a simple list,
# then prints them as a single, readable sentence.
info <- list(
  name = "Olamide Aworetan",
  affiliation = "Ekiti State University",
  gene = "lacZ",
  organism = "Escherichia coli"
)

cat("Hi, my name is", info$name,
    ", a researcher at", info$affiliation,
    ". My favorite gene is", info$gene,
    "in", info$organism, ".")
