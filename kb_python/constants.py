INFO_FILENAME = 'info.txt'

# Default filenames
CDNA_FILENAME = 'cdna.fa'
INTRON_FILENAME = 'introns.fa'
SORTED_FASTA_FILENAME = 'sorted.fa'
SORTED_GTF_FILENAME = 'sorted.gtf'
COMBINED_FILENAME = 'combined.fa'
INDEX_FILENAME = 'transcriptome.idx'
WHITELIST_FILENAME = 'whitelist.txt'
FILTER_WHITELIST_FILENAME = 'filter_barcodes.txt'
INSPECT_FILENAME = 'inspect.json'

BUS_FILENAME = 'output.bus'
BUS_S_FILENAME = 'output.s.bus'
BUS_SC_FILENAME = 'output.s.c.bus'
BUS_UNFILTERED_FILENAME = 'output.unfiltered.bus'
BUS_FILTERED_FILENAME = 'output.filtered.bus'
BUS_CDNA_PREFIX = 'spliced'
BUS_INTRON_PREFIX = 'unspliced'
ECMAP_FILENAME = 'matrix.ec'
TXNAMES_FILENAME = 'transcripts.txt'
COUNTS_PREFIX = 'cells_x_genes'
TCC_PREFIX = 'cells_x_tcc'
ADATA_PREFIX = 'adata'

UNFILTERED_COUNTS_DIR = 'counts_unfiltered'
FILTERED_COUNTS_DIR = 'counts_filtered'

BUS_UNFILTERED_SUFFIX = '.unfiltered.bus'
BUS_FILTERED_SUFFIX = '.filtered.bus'

# File codes.
# These are appended to the filename whenever it undergoes some kind of
# transformation.
SORT_CODE = 's'
CORRECT_CODE = 'c'
FILTERED_CODE = 'filtered'
UNFILTERED_CODE = 'unfiltered'
PROJECT_CODE = 'p'
