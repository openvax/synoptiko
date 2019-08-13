<a href="https://travis-ci.org/openvax/synoptiko">
    <img src="https://travis-ci.org/openvax/synoptiko.svg?branch=master" alt="Build Status" />
</a>
<a href="https://coveralls.io/github/openvax/synoptiko?branch=master">
    <img src="https://coveralls.io/repos/openvax/synoptiko/badge.svg?branch=master&service=github" alt="Coverage Status" />
</a>
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
