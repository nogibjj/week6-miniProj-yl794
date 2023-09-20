
# Student Grades Visualization Tool

This project offers a convenient tool to visualize the distribution of student grades using histograms. Built on the `polars` dataframe library and `matplotlib`, it provides insight into grade distributions and basic statistics, such as mean and standard deviation.

## Files:

1. **main.py** 
   - Contains the main functions:
     - `plot_polar(data)`: Plots a histogram visualization of the grades distribution.
     - Main execution block:
       - Reads the dataset `test.csv`.
       - Computes the mean and standard deviation of the grades.
       - Calls `plot_polar(data)` to generate a histogram and save it as `RESULT.png`.

2. **test.csv**
   - A dataset containing student names and their final grades.

## Setup and Usage:

### Prerequisites:
- Ensure you have Python 3 installed.
- Required libraries: `polars`, `matplotlib`. Install them using pip:
  ```
  pip install polars matplotlib
  ```

### Running the Visualization:

1. Clone the repository.
2. Navigate to the project directory.
3. Run `main.py`:
   ```
   python main.py
   ```
4. Check the output histogram image `RESULT.png` in the project directory.

## Contributing:

If you have suggestions, improvements, or find any discrepancies, please submit a pull request or open an issue.

