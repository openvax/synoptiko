[![Tests](https://github.com/openvax/synoptiko/actions/workflows/tests.yml/badge.svg)](https://github.com/openvax/synoptiko/actions/workflows/tests.yml)
<a href="https://pypi.python.org/pypi/synoptiko/">
    <img src="https://img.shields.io/pypi/v/synoptiko.svg?maxAge=1000" alt="PyPI" />
</a>

# synoptiko

Summary report of somatic mutations from cancer DNA sequencing data

## Usage

```
synoptiko --vcf mutect.vcf --vcf mutect2.vcf
                total variants:   680
                        # SNVs:   630
                      # indels:    50
coding non-synonymous variants:   150
===

Coding variants in known cancer genes:
-- LATS2 p.R352L (chr13 g.21562864C>A)
-- FLT3 p.R387L (chr13 g.28622457C>A)
-- TP53 p.C141Y (chr17 g.7578508C>T)
-- DNMT3A p.R484W (chr2 g.25468913G>A)
-- NFE2L2 p.LWRQDIDLGVSREVFDFSQ22del (chr2 g.178098921_178098977delGCTGACTGAAGTCAAATACTTCTCGACTTACTCCAAGATCTATATCTTGCCTCCAAA)
-- ZNF133 p.Q533K (chr20 g.18297095C>A)

Coding variants in MHC-I presentation genes:
-- HLA-C p.R155G (chr6 g.31239006G>C)

Coding variants in interferon response genes:
    none
```

## Installation and annotation semantics

Requires Python 3.11+ and Varcode 11.1+ (below 12). Install with
`pip install --upgrade synoptiko`, and install the matching reference annotation
with PyEnsembl before annotating a VCF. Varcode and pandas are declared runtime
dependencies.

The coding count includes a variant when any concrete candidate changes its
protein. The primary annotation can still be intronic or synonymous. Each gene
panel retains the primary description and lists candidate consequences,
including unresolved alternatives. Priority and producer ordering do not give
probabilities; none of these annotations establish RNA expression or peptide
presentation. Gene panels are the bundled historical CSVs, not a current CTA
curation or target-admission policy.

For development, install `.[test]`, then run `./lint.sh` and `./test.sh`.
The annotated integration test requires human Ensembl release 75; other tests
run with `./test.sh -m 'not ensembl'`.
