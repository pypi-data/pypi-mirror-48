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
