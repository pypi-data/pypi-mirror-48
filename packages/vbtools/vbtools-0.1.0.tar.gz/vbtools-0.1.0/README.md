# vbtools: a variant benchmark tool to compare VCFs with a consensus set
## Install
Before installation, make sure [conda](https://docs.conda.io/en/latest/miniconda.html) is under your `PATH`. Conda installation [here](https://docs.conda.io/en/latest/miniconda.html).

```sh
# clone this repo
git clone git@github.com:broadinstitute/vbtools.git

# setup conda environment
cd vbtools

conda env create -f env.yml # this will take a few minutes
conda list  # verify new environment was installed correctly

# activate environment
conda activate vbtools

# deactivate the environment when done
conda deactivate

# completely remove the virtual environment
conda remove -name vbtools --all
```

## Usage
You can use following command to benchmark a VCF against a reference/consensus VCF.
```sh
vcfbench.py -v <input.vcf> -b <reference.vcf>
```
`--prefix` is an option to define prefix to the output files.

Currently, only haploid VCF is supported in the analysis. Diploid VCF will be standardized into haploid before comparison. Input VCF should follow [VCF spec v4.2](https://samtools.github.io/hts-specs/VCFv4.2.pdf).

Following pre-processing steps are performed on the input VCF before the analysis:
1) remove unused alleles
2) remove monomorphic sites
3) remove sites with heterozygous genotypes
4) remove non-SNP sites
5) remove sites with asterisk marks
6) change diploid to haploid VCF

The script will output:
1) Site level comparison:
    - a tsv file including number of unique and shared sites.
2) Sample level comparision:
    - The sample level comparison functionality will be added to the script soon.
