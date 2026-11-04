# Polymer Biomaterial Properties and Macrophage Immune Responses Through Comparative Gene Expression Analysis

**Author:** Rohan Mishra   
**Dataset:** NCBI GEO Series [GSE301422](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301422)  

---

## Project Overview
Implanted medical devices can trigger foreign body reactions and fibrosis, heavily mediated by macrophage responses to material properties (composition, stiffness, porosity, and surface texture) [1]. This project investigates human macrophage gene expression across 13 polymeric material conditions (39 total samples, 3 biological replicates per condition) from GEO dataset `GSE301422`.

The repository provides:
1. **Relational Database Schema & SQL Queries:** Modeled in SQLite to organize materials, material properties, biological samples, focused immune response gene panels, and normalized expression measurements.
2. **Data Processing Pipeline:** Python scripts (`pandas`, `numpy`) to clean sample labels, verify replicate assignments, and ingest GEO expression matrices.
3. **Comparative Analysis & Visualizations:** Statistical comparison of inflammatory and tissue-remodeling genes across material groups using `Matplotlib`.

---

## Repository Structure
```text
polymer_macrophage_project/
├── README.md
├── requirements.txt
├── database/
│   ├── schema.sql
│   └── queries.sql
├── data/
│   └── README_data.md
├── src/
│   ├── data_processing.py
│   └── analysis_and_plots.py
└── output/
    └── gene_expression_plots.png
```

---

## Getting Started

### Prerequisites
* Python 3.9+
* Required libraries: `pandas`, `numpy`, `matplotlib`, `sqlite3`

Install dependencies:
```bash
pip install -r requirements.txt
```

### Execution Steps
1. **Initialize Database:**
   ```bash
   sqlite3 data/biomaterials.db < database/schema.sql
   ```
2. **Run Data Processing & Ingestion:**
   ```bash
   python src/data_processing.py
   ```
3. **Run Comparative Analysis & Generate Visualizations:**
   ```bash
   python src/analysis_and_plots.py
   ```

---

## References
[1] J.M. Anderson, A. Rodriguez, and D.T. Chang, "Foreign body reaction to biomaterials," *Seminars in Immunology*, vol. 20, no. 2, pp. 86-100, 2008.  
[2] R. Sridharan et al., "Material stiffness influences the polarization state, function and migration mode of macrophages," *Acta Biomaterialia*, vol. 89, pp. 47-59, 2019.  
[3] NCBI GEO, Series GSE301422: "Transcriptomic analysis of the human macrophage response to 13 polymeric materials," 2026.

