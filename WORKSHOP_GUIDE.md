# IBD Genomics Workshop - Instructor Guide

## Overview

This workshop provides a comprehensive introduction to Identity-By-Descent (IBD) segment analysis through hands-on simulations and interactive exercises. The workshop is designed for a 2-3 hour practical session.

## Workshop Structure

### Part 1: Identification of IBD Segments (45 minutes)
- **Introduction** (10 min): Theory of IBD segments, TMRCA, and recombination
- **Exercise 1.1** (10 min): Simulating populations and exploring tree sequences
- **Exercise 1.2** (15 min): Computing and visualizing IBD segments
- **Exercise 1.3** (10 min): Effect of recombination rate on IBD patterns

### Part 2: Temporal Demographic Inference (45 minutes)
- **Introduction** (10 min): Using IBD for demographic inference
- **Exercise 2.1** (10 min): Simulating demographic scenarios (bottleneck, expansion)
- **Exercise 2.2** (15 min): Comparing IBD patterns across scenarios
- **Exercise 2.3** (10 min): Inferring population size from IBD

### Part 3: Spatial Demographic Inference (45 minutes)
- **Introduction** (10 min): IBD and population structure
- **Exercise 3.1** (10 min): Simulating structured populations
- **Exercise 3.2** (15 min): Within vs. between-population IBD
- **Exercise 3.3** (5 min): Effect of migration on IBD
- **Exercise 3.4** (5 min): Creating IBD sharing matrices

### Wrap-up (15 minutes)
- Summary and discussion
- Optional exercises
- Q&A

## Prerequisites

### For Participants
- Basic knowledge of population genetics
- Familiarity with Python (beginner level)
- Understanding of coalescent theory (helpful but not required)

### Technical Requirements
- Python 3.7 or higher
- Jupyter Notebook or JupyterLab
- ~2GB free disk space for packages
- Internet connection for initial setup

## Setup Instructions

### Before the Workshop

1. **Test the environment** (recommended 1 week before):
   ```bash
   git clone https://github.com/PA-GAGNAIRE/DevOCGen.git
   cd DevOCGen
   pip install -r requirements.txt
   python3 test_notebook.py
   ```

2. **Have a backup plan**: Consider using cloud platforms (Google Colab, Binder) if local installations fail

3. **Prepare sample output**: Run through the notebook once to know expected outputs

### During Setup (First 15 minutes)

1. Participants clone the repository
2. Install packages using `pip install -r requirements.txt`
3. Launch Jupyter: `jupyter notebook IBD_genomics_workshop.ipynb`
4. Run the setup cell to verify installations

## Teaching Tips

### General Approach
- **Interactive**: Encourage participants to modify parameters and observe results
- **Visual**: Use the plots to explain concepts
- **Practical**: Relate simulations to real-world research questions
- **Flexible**: Adjust pace based on participant experience

### Common Questions and Answers

**Q: Why are IBD segments useful?**
A: They provide information about recent demographic history (~50-500 generations) that other methods can't capture.

**Q: What's the difference between IBD and IBS?**
A: IBD (Identity By Descent) means segments are inherited from a common ancestor. IBS (Identity By State) just means sequences are identical, which could be by chance.

**Q: How does recombination affect IBD?**
A: Higher recombination breaks up ancestral segments faster, resulting in shorter IBD segments for the same TMRCA.

**Q: Why do bottlenecks increase IBD sharing?**
A: Bottlenecks reduce diversity and force more recent common ancestry, creating more and longer IBD segments.

**Q: What time periods can IBD analysis inform?**
A: Primarily recent history (last ~200 generations), as older segments are broken up by recombination and recent segments are rare.

### Troubleshooting

**Installation Issues:**
- If msprime fails to install: Check Python version (needs 3.7+)
- If matplotlib doesn't display plots: Ensure Jupyter is using the correct kernel
- If memory errors occur: Reduce sample sizes in simulations

**Notebook Issues:**
- If cells don't run: Restart kernel and run all cells from the beginning
- If imports fail: Re-run the installation cell
- If plots are blank: Check if matplotlib backend is configured correctly

**Performance Issues:**
- Simulations taking too long: Reduce sequence length or sample size
- Large datasets: Use fewer IBD segment pairs for analysis

## Extended Activities

For advanced participants or longer workshops:

1. **Real data analysis**: Bring in empirical IBD data for comparison
2. **Method comparison**: Implement different IBD detection algorithms
3. **Parameter inference**: Use IBD patterns to estimate demographic parameters
4. **Custom scenarios**: Let participants design their own demographic models

## Assessment Ideas

### During Workshop
- Interactive questions in the notebook (immediate feedback)
- Ask participants to predict results before running cells
- Group discussions about interpretation

### Post-Workshop
- Small project: Analyze a provided dataset
- Report: Interpret IBD patterns from a specific demographic scenario
- Presentation: Explain how IBD relates to their research

## Resources for Further Learning

### Documentation
- [msprime](https://tskit.dev/msprime/): Coalescent simulation
- [tskit](https://tskit.dev/tskit/): Tree sequence analysis
- [SLiM](https://messerlab.org/slim/): Forward-time simulation

### Key Papers
1. Browning & Browning (2011) - IBD detection methods
2. Palamara et al. (2012) - Demographic inference from IBD
3. Ralph & Coop (2013) - Geographic patterns of IBD
4. Kelleher et al. (2016) - Efficient tree sequence methods

### Online Courses
- [PopGen Notes](https://github.com/cooplab/popgen-notes) by Graham Coop
- [EMBL Population Genetics Course](https://www.ebi.ac.uk/training/)

## Feedback and Improvements

After running the workshop, consider collecting:
- Participant feedback on difficulty level
- Technical issues encountered
- Suggestions for additional content
- Time spent on each section

Use this to refine the workshop for future sessions.

## Contact

For questions or issues with the workshop materials, please:
- Open an issue on GitHub: https://github.com/PA-GAGNAIRE/DevOCGen/issues
- Contact the maintainers

---

**Last Updated**: November 2025
**Version**: 1.0
