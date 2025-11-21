#!/usr/bin/env python3
"""
Test script to validate the IBD genomics workshop notebook.
This script checks that the notebook is valid and tests the core functions.
"""

import sys

def test_notebook_format():
    """Test that the notebook file is valid JSON and properly formatted."""
    try:
        import nbformat
        nb = nbformat.read('IBD_genomics_workshop.ipynb', as_version=4)
        print(f"✓ Notebook format is valid")
        print(f"  - Number of cells: {len(nb.cells)}")
        
        # Count different cell types
        code_cells = sum(1 for cell in nb.cells if cell.cell_type == 'code')
        markdown_cells = sum(1 for cell in nb.cells if cell.cell_type == 'markdown')
        print(f"  - Code cells: {code_cells}")
        print(f"  - Markdown cells: {markdown_cells}")
        return True
    except Exception as e:
        print(f"✗ Notebook format validation failed: {e}")
        return False

def test_imports():
    """Test that required packages can be imported."""
    print("\nTesting package imports:")
    required_packages = ['msprime', 'tskit', 'numpy', 'pandas']
    all_imported = True
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} (not installed)")
            all_imported = False
    
    return all_imported

def test_simulations():
    """Test the core simulation functions."""
    print("\nTesting simulation functions:")
    try:
        import msprime
        import tskit
        
        # Test simple simulation
        ts = msprime.sim_ancestry(
            samples=10,
            population_size=10000,
            sequence_length=1e6,
            recombination_rate=1e-8,
            random_seed=42
        )
        print(f"  ✓ Basic simulation works ({ts.num_trees} trees, {ts.num_samples} samples)")
        
        # Test demographic model
        demography = msprime.Demography()
        demography.add_population(name="A", initial_size=10000)
        demography.add_population_parameters_change(time=200, population="A", initial_size=1000)
        
        ts_demo = msprime.sim_ancestry(
            samples={"A": 10},
            demography=demography,
            sequence_length=1e6,
            recombination_rate=1e-8,
            random_seed=42
        )
        print(f"  ✓ Demographic simulation works ({ts_demo.num_trees} trees)")
        
        # Test two-population model
        demography2 = msprime.Demography()
        demography2.add_population(name="Pop1", initial_size=10000)
        demography2.add_population(name="Pop2", initial_size=10000)
        demography2.add_population(name="Ancestral", initial_size=10000)
        demography2.set_migration_rate(source="Pop1", dest="Pop2", rate=1e-4)
        demography2.set_migration_rate(source="Pop2", dest="Pop1", rate=1e-4)
        demography2.add_population_split(time=1000, derived=["Pop1", "Pop2"], ancestral="Ancestral")
        
        ts_struct = msprime.sim_ancestry(
            samples={"Pop1": 10, "Pop2": 10},
            demography=demography2,
            sequence_length=1e6,
            recombination_rate=1e-8,
            random_seed=42
        )
        print(f"  ✓ Structured population works ({ts_struct.num_trees} trees, {ts_struct.num_samples} samples)")
        
        return True
    except Exception as e:
        print(f"  ✗ Simulation test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("Testing IBD Genomics Workshop Notebook")
    print("=" * 60)
    
    results = []
    
    # Test 1: Notebook format
    results.append(test_notebook_format())
    
    # Test 2: Package imports
    results.append(test_imports())
    
    # Test 3: Simulations
    results.append(test_simulations())
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    if all(results):
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
