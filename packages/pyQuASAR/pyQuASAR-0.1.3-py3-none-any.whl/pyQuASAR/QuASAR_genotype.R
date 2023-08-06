#!/usr/bin/Rscript
#===============================================================================
# quasar_genotype.R
#===============================================================================

# Apply QuASAR to a prepared input file and generate genotype calls




# Libraries --------------------------------------------------------------------

library(QuASAR)




# Parse arguments --------------------------------------------------------------

input_file_names <- commandArgs(trailingOnly=T)




# Execute ----------------------------------------------------------------------

sink("/dev/null")
ase.dat <- UnionExtractFields(input_file_names, combine=TRUE)
ase.dat.gt <- PrepForGenotyping(ase.dat, min.coverage=5)
sample.names <- colnames(ase.dat.gt$ref)
if (length(input_file_names) > 1) {
    ase.joint <- fitAseNullMulti(ase.dat.gt$ref, ase.dat.gt$alt, log.gmat=log(ase.dat.gt$gmat))
} else if (length(input_file_names) == 1) {
    ase.joint <- fitAseNull(ase.dat.gt$ref, ase.dat.gt$alt, log.gmat=log(ase.dat.gt$gmat))
}
out_dat <- data.frame(ase.dat.gt$annotations[, -5], map=ase.joint$gt)
sink()
write.table(out_dat, row.names=FALSE, col.names=FALSE, quote=FALSE, sep="\t")
