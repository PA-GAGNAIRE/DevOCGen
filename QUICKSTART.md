# Quick Start Guide

Get started with the IBD Genomics Workshop in just a few minutes!

## 🚀 Quick Setup (5 minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/PA-GAGNAIRE/DevOCGen.git
cd DevOCGen
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Launch the Notebook
```bash
jupyter notebook IBD_genomics_workshop.ipynb
```

## ✅ Verify Installation

Run this command to test everything is working:
```bash
python3 test_notebook.py
```

You should see:
```
✓ Notebook format is valid
✓ All tests passed!
```

## 🎯 What You'll Learn

### Part 1: IBD Identification (45 min)
- What are IBD segments?
- How to detect them in genetic data
- Relationship between IBD length and ancestry

### Part 2: Temporal Inference (45 min)
- Using IBD to infer population history
- Detecting bottlenecks and expansions
- Estimating effective population size

### Part 3: Spatial Inference (45 min)
- IBD and population structure
- Within vs. between-population patterns
- Effect of migration on IBD sharing

## 💡 Key Features

- **Interactive**: Modify parameters and see results
- **Visual**: Rich plots and figures
- **Hands-on**: Real simulations, not toy examples
- **Self-paced**: Questions with immediate feedback

## 🔧 Troubleshooting

### Installation fails?
- Check Python version: `python3 --version` (need 3.7+)
- Try installing packages one by one:
  ```bash
  pip install msprime tskit numpy pandas matplotlib
  ```

### Notebook won't open?
- Make sure Jupyter is installed: `pip install jupyter`
- Try JupyterLab: `jupyter lab IBD_genomics_workshop.ipynb`

### Need help?
- Check the full [README.md](README.md)
- See [WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md) for instructor notes
- Open an issue on GitHub

## 🌐 Alternative: Run in the Cloud

Can't install locally? Use Google Colab:

1. Go to [Google Colab](https://colab.research.google.com/)
2. Click "File" → "Open notebook" → "GitHub"
3. Enter: `PA-GAGNAIRE/DevOCGen`
4. Open `IBD_genomics_workshop.ipynb`
5. Run the first cell to install packages

## 📚 Prerequisites

- Basic Python knowledge
- Understanding of population genetics concepts
- Familiarity with Jupyter notebooks (helpful)

## ⏱️ Time Commitment

- Full workshop: 2-3 hours
- Quick walkthrough: 1 hour
- Just experimenting: 30 minutes

## 🎓 After the Workshop

Continue learning:
- Try the optional exercises at the end
- Modify simulations with your own parameters
- Apply to your own research questions
- Explore the documentation links

## 📊 What's Inside

The notebook includes:
- 49 cells (22 code, 27 markdown)
- 8 interactive exercises
- 6 interactive questions with feedback
- Multiple visualization types
- Real population genetics simulations

## 🔬 Tools Used

- **msprime**: Fast coalescent simulations
- **tskit**: Tree sequence toolkit
- **pyslim**: SLiM interface
- **numpy/pandas**: Data analysis
- **matplotlib/seaborn**: Visualization

## ✨ Tips for Success

1. **Read the theory**: Don't skip the markdown cells
2. **Run in order**: Cells depend on previous ones
3. **Experiment**: Change parameters and re-run
4. **Save often**: Use "File" → "Save and Checkpoint"
5. **Ask questions**: Use the discussion forum

## 🎉 Ready to Start?

Open the notebook and begin your journey into IBD genomics:

```bash
jupyter notebook IBD_genomics_workshop.ipynb
```

Enjoy the workshop! 🧬
