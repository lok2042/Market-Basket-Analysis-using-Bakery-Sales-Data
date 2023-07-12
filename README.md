# Market Basket Analysis usibg Bakery Sales Data

![Bakery](https://upload.wikimedia.org/wikipedia/commons/6/66/Typical_French_bakery_pastries.jpg)

This repository contains a Python command line program that performs Market Basket Analysis using the Apriori and FP-Growth algorithms. The purpose of this application is to help retailers identify strong relationships between products based on customer purchase patterns. By analyzing frequent itemsets, retailers can make strategic decisions regarding product placement, cross-selling, up-selling, and store shelf arrangement.

## Objectives

1. Develop a Python command line program that allows users to upload or enter records, implement the Apriori and FP-Growth algorithms, and perform association rules on frequent itemsets.
2. Provide a comprehensive report detailing the design and development of the association analysis program.
3. Assist retailers in making informed decisions on strategic product placement, offering special deals, and creating attractive product bundles to boost sales.

## Folder Structure

The repository is organized as follows:

- **Application**: Contains the main program and supporting files.
  - **Bakery**: Contains the dataset and preprocessing script.
    - OriginalBakery.csv: Raw bakery sales dataset in CSV format obtained from Kaggle.
    - ModifiedBakery.csv: Preprocessed data.
    - preprocessing.py: Python script to transform OriginalBakery.csv into ModifiedBakery.csv.
  - main.py: Python command line program for Market Basket Analysis.
  - requirements.txt: List of required Python libraries for running the program.
- Report.pdf: Comprehensive report detailing the design and development of the association analysis program.
- Slides.pdf: Presentation slides summarizing the project.

## Usage

To use the Market Basket Analysis application, follow these steps:

1. Install the required Python libraries listed in the `requirements.txt` file.
2. Clone the repository and navigate to the `Application` directory.
3. Run the `main.py` program.
4. Choose the option to upload or enter records.
5. Select the algorithm (Apriori or FP-Growth) for association analysis.
6. View the generated frequent itemsets and association rules.
7. Make informed decisions on product placement, special deals, and product bundles based on the insights obtained.

## Credits

This project was developed with the support and guidance of [Ts. Dr Anbuselvan Sangodiah](https://scholar.google.com/citations?user=KmTXLTIAAAAJ&hl=en).
