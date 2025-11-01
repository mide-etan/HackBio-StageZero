**What single-cell data is teaching us about cancer evolution**

**1\. Introduction**

In the early years, cancer research depended on microscopy and pathology to correlate visible features of tumors with biomarkers. By the mid-20th century, molecular assays such as karyotyping and Sanger sequencing had identified key oncogenes and tumor suppressors. In the late 1990s, DNA microarrays enabled the first high-throughput analyses of gene expression, thus setting the stage for large-scale cancer genomics (Creighton, 2023).

These findings revolutionized the understanding of cancer. Cancer is now perceived not as a fixed disease but as a dynamic ecosystem of ever-evolving cells sculpted by natural selection. Tumor adaptation, survival, and resistance to therapy in mutation, selective pressure, and clonal competition (Mansur et al., 2023) are driven. The evolving nature of tumors thus allows mutations that disturb either cell-cycle regulation or immune evasion to confer a fitness advantage, enabling cells to colonize new tissues and create metastases (Thakur et al., 2024). The tumor microenvironment, therefore, serves both as an ecosystem and as a battleground.

A key outcome of this evolution is **tumor heterogeneity**-the coexistence of genetically and phenotypically distinct subpopulations within and across tumors (Fitzgerald et al., 2017). This diversity arises from accumulated mutations and epigenetic changes over time. Single-cell technologies have now made it possible to measure this heterogeneity directly. Studies in _Clinical Epigenetics_ (2023) show that tumors can contain thousands of distinct cell states with unique transcriptional and epigenetic signatures. Such complexity complicates treatment, as targeting one clone may leave others unaffected .

Heterogeneity also drives **therapy resistance**, one of cancer's most challenging clinical problems. Treatments like chemotherapy and targeted therapies eliminate sensitive cells but select for resistant ones that survive and repopulate the tumor (Thomas et al., 2022). Understanding therapy resistance as an evolutionary phenomenon allows for adaptive treatment strategies that anticipate tumor adaptation (Karagiannis & Rampias, 2022).

The advent of **next-generation sequencing (NGS)** in the mid-2000s enabled comprehensive mapping of cancer genomes. Bulk DNA sequencing identified recurrent mutations, and structural variants, confirming that cancer is driven by genetic alterations (Brosnan & Iacobuzio-Donahue, 2013). Likewise, bulk RNA profiling evolved from microarrays to RNA sequencing, revealing key molecular hallmarks of carcinogenesis and treatment response. However, bulk sequencing masks cellular heterogeneity by averaging signals across millions of cells. Rare mutations and minority subclones often fall below detection thresholds (Wu et al., 2021). Similarly, bulk RNA sequencing conceals differences among individual cell types, introducing bias and reducing reproducibility (Baslan & Hicks, 2017).

To overcome these limitations, **single-cell sequencing** now enables genome or transcriptome profiling at the cellular level, uncovering intratumoral heterogeneity and cell-to-cell communication networks (Wu et al., 2021). Bulk sequencing laid the groundwork for understanding the genetic basis of cancer, but single-cell technologies now expose the hidden clonal diversity that drives tumor evolution, metastasis, and therapeutic resistance.

**2\. Emergence of Single-Cell omics (scRNA-seq, scDNA-seq, scATAC-seq)**

Single-cell omics, including single-cell RNA sequencing (scRNA-seq), DNA sequencing (scDNA-seq), and chromatin accessibility sequencing (scATAC-seq), have revolutionized oncology by solved intratumoral heterogeneity and delineating cellular hierarchies previously obscured by bulk analyses. The introduction of single-cell DNA sequencing by Navin and colleagues (2011) revealed punctuated clonal evolution in breast tumors and established a framework for tracing tumor lineage dynamics. Ensuing studies (Tirosh et al., 2016) demonstrated remarkable transcriptional diversity within individual tumors, which recognized malignant, immune, and stromal subpopulations influencing disease progression and therapeutic response. As a whole, these findings reframed cancer as an ecosystem of heterogeneous cellular states rather than a uniform entity.

Puram et al. (2017) defined epithelial-mesenchymal transition states in head and neck cancers using scRNA-seq. Elyada et al. (2019) recognized antigen-presenting cancer-associated fibroblasts in pancreatic tumors, implicating the stroma in the modulation of immune responses. Moncada et al. (2020) integrated spatial transcriptomics with scRNA-seq, providing a strategy for restoring tissue architecture and hence for spatially resolved mapping of tumor-stroma interactions. Recently, Zhu et al. (2023) used single-cell multi-omics to look into how ecDNA drives intra-cell-line heterogeneity and gene amplification dynamics, pointing at epigenetic mechanisms underlying therapeutic resistance.

Single-cell omics has transitioned oncology from bulk molecular profiling to a cellularly resolved discipline. Foundational studies chart clonal dynamics (Navin et al., 2011), transcriptional heterogeneity (Tirosh et al., 2016), stromal-immune crosstalk (Elyada et al., 2019), and spatial architecture (Moncada et al., 2020). The recent pan-cancer single-cell chromatin atlases (Bairakdar et al., 2025) emphasize the possibility of predictive, clinically actionable frameworks that can be deciphered from single-cell data.

**2\. How single-cell RNA sequencing resolves clonal evolution architecture**

Single-cell RNA sequencing resolves clonal evolution architecture by providing high-resolution, cell-specific data, revealing genetic and transcriptional heterogeneity and allows for the reconstruction of phylogenetic trees. Unlike bulk sequencing which provides an average profile masking individual cell differences, scRNA-seq identifies specific characteristics of individual cells (Zhang et al, 2021).

Key mechanisms that scRNA-seq uses to resolve clonal evolution architecture includes, the identification of clonal heterogeneity done by finding distinct cell subpopulations within a tumour based on their unique expression profiles and somatic mutations (Zhou et al., 2019). By comparing unique mutational and gene expression profiles across single cells, evolutionary history and relationships among different clones can be reconstructed, revealing lineage of cancer cells (Liu et al., 2023). This technology is also useful in linking genotype to phenotype by analysing the genome and the transcriptome within the same cell, allowing for researchers to directly link specific mutations to resulting changes in the cell phenotype. Additionally, scRNA-seq can reveal dynamic changes over time. By performing scRNA-seq on samples collected at different stages of disease or treatment, researchers can determine how clonal architecture changes dynamically. Lastly, this technology enables detailed analysis of non-cancerous cells within the tumour microenvironment via ligand-receptor signalling, which is key in understanding tumour progression and immune evasion, as well as providing new targets for therapies (Chen et al., 2023).

**3\. Case Study: Single-Cell Omics in Glioblastoma and Breast Cancer**

To illustrate what single-cell data can reveal, we focus on glioblastoma and breast cancer, where these analyses have uncovered tumour diversity, cell plasticity, and therapy resistance.

**3.1 Glioblastoma**

Glioblastoma, the most aggressive primary brain tumor in adults, exhibits rapid proliferation, diffuse infiltration, and inevitable recurrence. Bulk sequencing has not explained why tumors with similar driver mutations behave unpredictably, but single-cell omics has revealed that glioblastoma comprises a dynamic ecosystem of malignant and non-malignant cells within a complex microenvironment (Soni et al., 2025).

Single-cell RNA sequencing shows that malignant cells occupy a few conserved transcriptional states-neural progenitor-like, oligodendrocyte progenitor-like, astrocyte-like, and mesenchymal-like-whose relative proportions create tumor-specific mosaics (Neftel et al., 2019). These states are plastic; cells transition between them in response to stress or therapy, providing a non-genetic mechanism of resistance. Integrative single-cell analyses reveal that genotype and phenotype are only partially coupled, as distinct clones can share cell states while single clones span multiple phenotypes (Soni et al., 2025).

Clinically, single-cell profiling enables functional stratification of tumors. Pre-treatment RNA or chromatin accessibility data can quantify stemness, DNA repair, and drug efflux programs linked to recurrence. Spatial mapping further localizes resistant states to hypoxic cores and invasive margins. Patients with higher fractions of stem-like or mesenchymal-like cells relapse earlier, suggesting that single-cell multi-omic profiling at diagnosis could refine risk prediction and guide therapy (Wang et al., 2022).

**3.2 Breast Cancer**

In breast cancer, particularly triple-negative and hormone receptor-positive subtypes, single-cell omics have elucidated the emergence and evolution of resistant clones under therapy (Ren et al., 2021). Whereas bulk sequencing suggested resistance arises from new mutations acquired during treatment, single-cell analyses reveal that resistant clones often pre-exist at low frequencies, defined by distinct transcriptional or epigenetic states conferring drug tolerance (Kim et al., 2018).

In triple-negative breast cancer (TNBC), Vishnubalaji et al. (2021) identified transcriptionally distinct cell clusters associated with non-response to neoadjuvant chemotherapy. These resistant populations frequently display epithelial-mesenchymal transition features and enhanced DNA damage repair capacity, which can be obscured in bulk analyses. Single-cell ATAC-seq further links endocrine therapy resistance to persistent chromatin accessibility at enhancer regions in tamoxifen-resistant clones, suggesting epigenetic priming for adaptation (Fang et al., 2024).

Integrative single-cell and spatial analyses indicate that resistant states often reside within immune-suppressed niches of the tumor microenvironment (Cheng et al., 2025). Collectively, these studies shift the paradigm from mutation-centric models of resistance toward functional state profiling at single-cell resolution.

**4\. Challenges and Limitations and Future Directions**

Despite its transformative potential, single-cell analysis faces major technical and conceptual barriers that limit clinical translation. Most protocols require fresh, viable tissue, constraining longitudinal studies and retrospective analyses. Sample preparation can also introduce artifacts: enzymatic or mechanical dissociation induces stress responses, such as heat shock signatures, that obscure true biological states and may mimic drug-tolerant "persister" cells.

Single-cell data are inherently sparse due to high dropout rates, complicating detection of low-abundance transcripts such as transcription factors that define cellular identity. Analysis further demands advanced bioinformatics expertise, yet a lack of standardized pipelines for normalization, batch correction, and clustering can yield inconsistent biological interpretations and hinder meta-analysis across datasets.

Conceptually, scRNA-seq remains largely descriptive. While it can identify cell populations expressing resistance-associated genes, establishing causality requires functional validation-isolating and testing these populations in model systems-a process that remains technically challenging and low throughput.

**Future directions** include the integration of multi-omic, spatial, and lineage-tracing approaches with standardized analytical frameworks to enable causal, clinically actionable insights from single-cell data.

**Reference**

Bairakdar, M. D., et al. (2025). _Learning the cellular origins across cancers using single-cell chromatin accessibility (SCOOP)._ _Nature Communications._

Barkley, D. (2022). _Recurrence of Cancer Cell States across Diverse Cancer Types and Their Interactions with the Tumor Microenvironment_ (Doctoral dissertation, New York University).

Baslan, T., & Hicks, J. (2017). Unravelling biology and shifting paradigms in cancer with single-cell sequencing. _Nature Reviews Cancer, 17_(9), 557-569. <https://doi.org/10.1038/nrc.2017.58>

Brosnan, J. A., & Iacobuzio-Donahue, C. A. (2012). A new branch on the tree: next-generation sequencing in the study of cancer evolution. _Seminars in cell & developmental biology_, _23_(2), 237-242. <https://doi.org/10.1016/j.semcdb.2011.12.008>

Cheng, X., Peng, T., Chu, T., Yang, Y., Liu, J., Gao, Q., Cao, C., & Wei, J. (2025). Application of single-cell and spatial omics in deciphering cellular hallmarks of cancer drug response and resistance. _Journal of Hematology & Oncology, 18_(1), 70. <https://doi.org/10.1186/s13045-025-01722-1>

Elyada, E., Bolisetty, M., Laise, P., et al. (2019). Cross-species single-cell analysis reveals antigen-presenting cancer-associated fibroblasts. _Cancer Discovery_, 9(8), 1102-1123.

Fang, K., Ohihoin, A. G., Liu, T., Choppavarapu, L., Nosirov, B., Wang, Q., Yu, X.-Z., Kamaraju, S., Leone, G., & Jin, V. X. (2024). Integrated single-cell analysis reveals distinct epigenetic-regulated cancer cell states and a heterogeneity-guided core signature in tamoxifen-resistant breast cancer. _Genome Medicine, 16_(1), 134. <https://doi.org/10.1186/s13073-024-01407-3>

Fitzgerald, D. M., Hastings, P. J., & Rosenberg, S. M. (2017). Stress-induced mutagenesis: implications in cancer and drug resistance. _Annual review of cancer biology_, _1_(1), 119-140.

Lim, B., et al. (2020). Advancing cancer research and medicine with single-cell technologies. _Cancer Cell_, 37(4), 514-528.

Kim, C., Gao, R., Sei, E., Brandt, R., Hartman, J., Hatschek, T., Crosetto, N., Foukakis, T., & Navin, N. E. (2018). Chemoresistance evolution in triple-negative breast cancer delineated by single-cell sequencing. _Cell, 173_(4), 879-893.e13. <https://doi.org/10.1016/j.cell.2018.03.041>

Lawson, A. R. J., Abascal, F., Nicola, P. A., Lensing, S. V., Roberts, A. L., Kalantzis, G., Baez‑Ortega, A., Brzozowska, N., El‑Sayed Moustafa, J. S., Vaitkute, D., Jakupovic, B., Nessa, A., Wadge, S., Österdahl, M. F., Paterson, A. L., Rassl, D. M., Alcantara, R. E., O'Neill, L., Widaa, S., Austin‑Guest, S., … Martincorena, I. (2025). _Somatic mutation and selection at population scale._ _Nature_. <https://doi.org/10.1038/s41586-025-09584-w>

Meyer, M., Reimand, J., Lan, X., Head, R., Zhu, X., Kushida, M., Bayani, J., Pressey, J. C., Lionel, A. C., Clarke, I. D., Cusimano, M., Squire, J. A., Scherer, S. W., Bernstein, M., Woodin, M. A., Bader, G. D., & Dirks, P. B. (2015). Single cell-derived clonal analysis of human glioblastoma links functional and genomic heterogeneity. _Proceedings of the National Academy of Sciences, 112_(3), 851-856. <https://doi.org/10.1073/pnas.1320611111>

Moncada, R., Barkley, D., Wagner, F., et al. (2020). Integrating spatial transcriptomics and single-cell RNA-seq reveals tissue architecture in pancreatic ductal adenocarcinomas. _Nature Biotechnology_, 38(3), 333-342.

Navin, N., Kendall, J., Troge, J., et al. (2011). Tumour evolution inferred by single-cell sequencing. _Nature_, 472(7341), 90-94.

Neftel, C., Laffy, J., Filbin, M. G., Hara, T., Shore, M. E., Rahme, G. J., Richman, A. R., Silverbush, D., Shaw, M. L., Hebert, C. M., Dewitt, J., Gritsch, S., Perez, E. M., Gonzalez Castro, L. N., Lan, X., Druck, N., Rodman, C., Dionne, D., Kaplan, A., … Suvà, M. L. (2019). An integrative model of cellular states, plasticity, and genetics for glioblastoma. _Cell, 178_(4), 835-849.e21. <https://doi.org/10.1016/j.cell.2019.06.024>

Pan, D., et al. (2021). Application of single-cell multi-omics in dissecting tumour heterogeneity. _Frontiers in Oncology_, 11, 675538.

Puram, S. V., Tirosh, I., Parikh, A. S., et al. (2017). Single-cell transcriptomic analysis of primary and metastatic tumour ecosystems in head and neck cancer. _Cell_, 171(7), 1611-1624.

Mansur, M. B., deSouza, N. M., Natrajan, R., Abegglen, L. M., Schiffman, J. D., & Greaves, M. (2023). Evolutionary determinants of curability in cancer. _Nature Ecology & Evolution_, _7_(11), 1761-1770.

Mansur, M. B., deSouza, N. M., Natrajan, R., Abegglen, L. M., Schiffman, J. D., & Greaves, M. (2023). Evolutionary determinants of curability in cancer. _Nature Ecology_

_& Evolution_, _7_(11), 1761-1770.

Nunes, S. C. (2020). Tumor microenvironment-selective pressures boosting cancer progression. _Tumor Microenvironment: The Main Driver of Metabolic Adaptation_, 35-49.

Ren, L., Li, J., Wang, C., Lou, Z., Gao, S., Zhao, L., Wang, S., Chaulagain, A., Zhang, M., & Li, X. (2021). Single cell RNA sequencing for breast cancer: Present and future. _Cell Death Discovery, 7_(1), 104. <https://doi.org/10.1038/s41420-021-00485-1>

Somarelli, J. A., & Johnson, N. A. (Eds.). (2024). _Cancer through the Lens of Evolution and Ecology_. CRC Press

Soni, N., Rawat, K., Chen, Z., DiMauro, A., Giotti, B., Hambardzumyan, D., & Tsankov, A. M. (2025). Single-cell dissection of the genotype-immunophenotype relationship in glioblastoma. _Brain, 148_(9), 3153-3169. <https://doi.org/10.1093/brain/awaf129>

Thomas, D. S., Cisneros, L. H., Anderson, A. R., & Maley, C. C. (2022). In silico investigations of multi-drug adaptive therapy protocols. _Cancers_, _14_(11), 2699.

Tirosh, I., Izar, B., Prakadan, S. M., et al. (2016). Dissecting the multicellular ecosystem of metastatic melanoma by single-cell RNA-seq. _Science_, 352(6282), 189-196.

Venkatesan, S., Swanton, C., Taylor, B. S., & Costello, J. F. (2017). Treatment-induced mutagenesis and selective pressures sculpt cancer evolution. _Cold Spring Harbor perspectives in medicine_, _7_(8), a026617.

Vishnubalaji, R., & Alajez, N. M. (2021). Transcriptional landscape associated with TNBC resistance to neoadjuvant chemotherapy revealed by single-cell RNA-seq. _Molecular Therapy - Oncolytics, 23_, 151-162. <https://doi.org/10.1016/j.omto.2021.09.002>

Wang, L., Jung, J., Babikir, H., Shamardani, K., Jain, S., Feng, X., Gupta, N., Rosi, S., Chang, S., Raleigh, D., Solomon, D., Phillips, J. J., & Diaz, A. A. (2022). A single-cell atlas of glioblastoma evolution under therapy reveals cell-intrinsic and cell-extrinsic therapeutic targets. _Nature Cancer, 3_(12), 1534-1552. <https://doi.org/10.1038/s43018-022-00475-x>

Wu, F., Fan, J., He, Y., Xiong, A., Yu, J., Zhao, W., Zhou, F., Li, W., Zhang, J., Zhang, X., Qiao, M., Gao, G., Chen, S., Chen, X., Li, X., Su, C., Ren, S., & Zhou, C. (2021). _Single-cell profiling of tumor heterogeneity and the microenvironment in advanced non-small cell lung cancer_. Nature Communications, 12, 2540. <https://doi.org/10.1038/s41467-021-22801-0>

Zhu, Q., Shah, S., Dries, R., Cai, L., & Yuan, G.-C. (2023). Single-cell multi-omics reveal intra-cell-line heterogeneity and extrachromosomal DNA effects in cancer cell lines. _Nature Communications_, 14, 43991.

Zhang, Y., Wang, D., Peng, M. _et al._ Single‐cell RNA sequencing in cancer research. _J Exp Clin Cancer Res_ **40**, 81 (2021). <https://doi.org/10.1186/s13046-021-01874-1>

Mossner, M., Baker, A. C., & Graham, T. A. (2021). The role of single-cell sequencing in studying tumour evolution. _Faculty reviews_, _10_, 49. <https://doi.org/10.12703/r/10-49>

Chen, S., Zhou, Z., Li, Y., Du, Y., & Chen, G. (2023). Application of single-cell sequencing to the research of tumor microenvironment. _Frontiers in Immunology_, _14_, 1285540. <https://doi.org/10.3389/fimmu.2023.1285540>

Liu, X., Griffiths, J.I., Bishara, I. _et al._ Phylogenetic inference from single-cell RNA-seq data. _Sci Rep_ **13**, 12854 (2023). <https://doi.org/10.1038/s41598-023-39995-6>

Zhou, Z., Xu, B., Minn, A., & Zhang, N. R. (2018). Genetic heterogeneity profiling by single cell RNA sequencing. In _bioRxiv_. <https://doi.org/10.1101/457622>
