# pydbsnp

Interface with dbSNP VCF data

## Installation

First install the python package via `pip3`

```sh
pip3 install pydbsnp
```
or
```sh
pip3 install --user pydbsnp
```

Once the python package is installed, download and index the dbSBP VCF data:

```sh
pydbsnp-download
pydbsnp-index
```

For hg19/GRCh37 coordinates:

```sh
pydbsnp-download --reference-build GRCh37
pydbsnp-index
```

## Command line usage

```sh
pydbsnp-query -h
```

```sh
pydbsnp-query rs689
pydbsnp-query --reference-build GRCh37 rs689
```

## API

Two classes are provided: `Variant` and `GeneralizedVariant`.

```python
from pydbsnp import Variant
v = Variant('rs8056814')
print(v.chrom, v.pos, v.id, v.ref, v.alt)
print(v.info)
help(Variant)
```

```python
gv = GeneralizedVariant('rs8056814')
print(v.chrom, v.pos, v.id, v.ref, v.alt)
```