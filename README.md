# Boost_LP_EFM

Supplementary information related to publication ["Boosting the extraction of Elementary Flux Modes
in Genome-Scale Metabolic Networks using the Linear Programming approach"](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btaa280/5826992)
 in Bioinformatics.


./run.py --config models/e_coli_core/config_e_coli_core.json --scale 0.2 --loop 5000

When finish, some stats will be shown in the console. The set of solutions (EFMs) will be located in the folder "outputs".


## Bibtex


```
@article{10.1093/bioinformatics/btaa280,
    author = {Guil, Francisco and Hidalgo, José F and García, José M},
    title = "{Boosting the extraction of Elementary Flux Modes in Genome-Scale Metabolic Networks using the Linear Programming approach}",
    journal = {Bioinformatics},
    year = {2020},
    month = {04},
    abstract = "{Elementary flux modes (EFMs) are a key tool for analyzing genome-scale metabolic networks (GSMNs), and several methods have been proposed to compute them. Among them, those based on solving Linear Programming (LP) problems are known to be very efficient if the main interest lies in computing large enough sets of EFMs.Here, we propose a new method called EFM-Ta that boosts the efficiency rate by analyzing the information provided by the LP solver. We base our method on a further study of the final Tableau of the simplex method. By performing additional elementary steps and avoiding trivial solutions consisting of 2-cycles, we obtain many more EFMs for each LP problem posed, improving the efficiency rate of previously proposed methods by more than one order of magnitude.Software is freely available at https://https://github.com/biogacop/Boost\_LP\_EFM}",
    issn = {1367-4803},
    doi = {10.1093/bioinformatics/btaa280},
    url = {https://doi.org/10.1093/bioinformatics/btaa280},
    note = {btaa280},
    eprint = {https://academic.oup.com/bioinformatics/advance-article-pdf/doi/10.1093/bioinformatics/btaa280/33146167/btaa280.pdf},
}


```

