# DevOCGen
DevOCGen_IBD_workshop

## Workshop: Genomics of Identity-By-Descent (IBD) Segments

This repository contains a comprehensive Jupyter notebook for a practical workshop on the genomics of IBD segments. The workshop is designed to teach participants about IBD segment analysis through hands-on simulations and exercises.

### Workshop Content

The workshop is divided into three main parts:

1. **Identification of IBD Segments**
   - Introduction to IBD concepts
   - Simulation of genetic data
   - Detection and visualization of IBD segments
   - Understanding the relationship between IBD length and TMRCA

2. **Temporal Demographic Inference**
   - Using IBD segments to infer population history over time
   - Simulating demographic events (bottlenecks, expansions)
   - Estimating effective population size from IBD patterns

3. **Spatial Demographic Inference**
   - Analyzing population structure using IBD
   - Within- vs. between-population IBD sharing
   - Effects of migration on IBD patterns
   - Visualizing spatial genetic structure

### Tools and Technologies

The workshop uses the following simulation and analysis tools:

- **msprime**: Coalescent simulator for generating genetic variation data
- **tskit**: Library for working with tree sequences
- **pyslim**: Interface to SLiM forward-time population genetics simulator
- **Python scientific stack**: NumPy, Pandas, Matplotlib, Seaborn

### Getting Started

#### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab

#### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PA-GAGNAIRE/DevOCGen.git
   cd DevOCGen
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter:
   ```bash
   jupyter notebook IBD_genomics_workshop.ipynb
   ```

#### Quick Start (In the Notebook)

The notebook includes a setup cell that will install all required packages:
```python
!pip install msprime tskit pyslim numpy matplotlib pandas seaborn scipy
```

### Workshop Structure

Each section includes:
- **Theoretical background**: Introduction to key concepts
- **Hands-on exercises**: Simulation-based practical activities
- **Interactive questions**: Multiple-choice questions with immediate feedback
- **Visualizations**: Plots and figures to understand the data

### Learning Objectives

By the end of this workshop, participants will be able to:

1. Understand the biological basis of IBD segments
2. Simulate genetic data using coalescent and forward-time models
3. Identify and quantify IBD segments from tree sequences
4. Interpret IBD patterns to infer demographic history
5. Use IBD analysis to understand population structure
6. Apply these methods to real-world research questions

### References

Key papers and resources:
- Browning & Browning (2011). "A fast, powerful method for detecting identity by descent."
- Palamara et al. (2012). "Length distributions of identity by descent reveal fine-scale demographic history."
- Ralph & Coop (2013). "The geography of recent genetic ancestry across Europe."
- Kelleher et al. (2016). "Efficient coalescent simulation and genealogical analysis for large sample sizes."

### Documentation

- [msprime documentation](https://tskit.dev/msprime/)
- [tskit documentation](https://tskit.dev/tskit/)
- [SLiM documentation](https://messerlab.org/slim/)

### License

This workshop material is provided for educational purposes.

### Contact

For questions or issues, please open an issue on GitHub.
