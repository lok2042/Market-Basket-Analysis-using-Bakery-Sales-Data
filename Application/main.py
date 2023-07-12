import csv
import string
import random
import os.path
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

def get_csv():
    while True:
        print("\n------ Records ------")
        print("1 - Terminal Keyboard 💻")
        print("2 - Input File 📄")
        print("0 - Quit 🛑 ")

        try:
            choice = int(input("Choice : "))
            print()

            if choice == 1:
                try:
                    print("Rule #1: Enter your records line by line or paste them.")
                    print("Rule #2: Separate each item using ','.")
                    print("Rule #3: Enter '-1' to stop.\n")

                    lines = []
                    while True:
                        line = input()
                        if line == '-1':
                            break
                        elif line:
                            lines.append(line)
                        else:
                            break
                    
                    # Create a random file name
                    letters = string.ascii_letters
                    filename = ''.join(random.choice(letters) for i in range(5))

                    # Create a new CSV file
                    with open(f'{filename}.csv', 'w', newline='') as f:
                        w = csv.writer(f)
                        for row in lines:
                            items = row.split(',')
                            items = [x.upper() for x in items]
                            w.writerow(items)
                        
                    return f'{filename}.csv' 
                except:
                    print("❗Please enter correct records❗\n")

            elif choice == 2:
                try:
                    path = input("Enter the path to your .csv file: ")
                    print()

                    if (os.path.exists(path) and path.endswith('.csv')):
                        return path
                    else:
                        raise Exception("❗ File not found / invalid path / not a .csv file❗")
                except:
                    print("❗Please provide a valid file path❗\n")

            elif choice == 0:
                return 'quit'

            else:
                print("Invalid Choice! Please try again.")
        except:
            print("\nPlease enter an integer!")


def select_method():
    while True:
        print("\n------ Method ------")
        print("1 - Apriori 💡")
        print("2 - FP-Growth 🌱")

        try:
            choice = int(input("Choice : "))
            if choice in [1, 2]:
                return choice
            else:
                print("\nInvalid Choice! Please try again.") 
        except:
            print("\nPlease enter an integer!")


def get_minsup_count():
    while True:
        try:
            print("\n------ Threshold ------")
            minsup = float(input("Enter minimum support count (0 - 100): "))

            if minsup >= 0 and minsup <= 100:
                return minsup
            else:
                print("Please enter a value between 0 and 100. Decimal or integer.")
        except:
            print("\nPlease enter a valid floating point value!")


def run_association_rules(frq_items):
    rules = association_rules(frq_items, metric='support', min_threshold=0.0)
    # print(rules)
    
    maxSupport = max(rules['support'])
    maxConfidence = max(rules['confidence'])
    maxLift = max(rules['lift'])

    while True:
        print("\n------ Association Rules ------")
        print("1 - Support 💪")
        print("2 - Confidence 😎")
        print("3 - Lift 🏋️")
        print("4 - Support, Confidence, and Lift 💪😎🏋️")
        print("0 - Finish 🏁")

        try:
            choice = int(input("Choice : "))
            print()
            if choice in [1, 2, 3, 4]:
                values = ''
                if choice == 1:
                    print('🚧 Highest support: %.4f' %maxSupport)
                    minsup = float(input("Enter Minimum Support (0.0 - 1.0)   : "))
                    if minsup < 0 or minsup > 1:
                        print('❗Enter a value between 0 and 1❗')
                    else:
                        results = rules[(rules['support'] >= minsup)]
                        if (len(results) > 0):
                            values = 'support'
                            print('\nAssociation Rules based on Support:')
                            print(results.sort_values('support', ascending=False))
                        else:
                            print('\nNo association rules can be generated. Your support value may be too high. Please try again.')

                elif choice == 2:
                    print('🚧  Highest confidence: %.4f' %maxConfidence)
                    minconf = float(input("Enter Minimum Confidence (0.0 - 1.0) : "))
                    if minconf < 0 or minconf > 1:
                        print('❗Enter a value between 0 and 1❗')
                    else:
                        results = rules[(rules['confidence'] >= minconf)]
                        if (len(results) > 0):
                            values = 'confidence'
                            print('\nAssociation Rules based on Confidence:')
                            print(results.sort_values('confidence', ascending=False))
                        else:
                            print('\nNo association rules can be generated. Your confidence value may be too high. Please try again.')
                        
                elif choice == 3:
                    print('🚧 Highest lift: %.4f' %maxLift) 
                    lift = float(input("Enter Lift value: "))
                    if lift < 0 or lift > maxLift:
                        print('❗Enter a value between 0 and {maxLift}❗')
                    else:
                        results = rules[(rules['lift'] >= lift)]
                        if (len(results) > 0):
                            values = 'lift'
                            print('\nAssociation Rules based on Lift:')
                            print(results.sort_values('lift', ascending=False))
                        else:
                            print('\nNo association rules can be generated. Your lift value may be too high. Please try again.')
   
                elif choice == 4:
                    print('🚧 Highest support: %.4f' %maxSupport)
                    minsup = float(input("Enter Minimum Support (0.0 - 1.0)   : "))

                    print('🚧  Highest confidence: %.4f' %maxConfidence)
                    minconf = float(input("Enter Minimum Confidence (0.0 - 1.0) : "))

                    print('🚧 Highest lift: %.4f' %maxLift) 
                    lift = float(input("Enter Lift value: "))

                    if minsup < 0 or minsup > 1 or minconf < 0 or minconf > 1 or lift < 0 or lift > maxLift:
                        print('❗Ensure all fields are between 0 and their respective highest value❗')
                    else:
                        results = rules[(rules['support'] >= minsup) & (rules['confidence'] >= minconf) & (rules['lift'] > lift)]
                        if (len(results) > 0):
                            values = 'lift'
                            print('\nAssociation Rules based on Support, Confidence, and Lift:')
                            print(results.sort_values(['lift', 'confidence', 'support'], ascending=[False, False, False]))
                        else:
                            print('\nNo association rules can be generated. Your values may be too high. Please try again.')

                if values != '':
                    # Convert antecedents and consequents into strings
                    results['antecedents'] = results['antecedents'].apply(lambda a: ','.join(list(a)))
                    results['consequents'] = results['consequents'].apply(lambda a: ','.join(list(a)))

                    # Transform antecedent, consequent, and (support, confidence, or lift) into matrix
                    support_table = results.pivot(index='consequents', columns='antecedents', values=values)
                    
                    # Display heatmap
                    plt.figure(figsize=(10,8))
                    sns.heatmap(support_table, annot=True, cbar=False)
                    b, t = plt.ylim() 
                    b += 0.5 
                    t -= 0.5 
                    plt.ylim(b, t) 
                    plt.yticks(rotation=0)
                    plt.xticks(rotation=90)
                    plt.subplots_adjust(top=0.99)
                    plt.show()
                else:
                    print('Please try again...')
            elif choice == 0:
                break
            else:
                print("\nInvalid Choice! Please try again.") 
        except:
            print("\nSomething went wrong 😔")


def terminate():
    # Terminate Program
    print("\n👋 👋 END OF PROGRAM 👋 👋 \n")
    exit()


def main():
    print("\n=== 📊 Association Analysis 📈 ===")

    # Set display dimensions
    desired_width = 1000
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None)

    # Suppress any warnings
    warnings.filterwarnings('ignore')

    while True: 
        # Get Records in .csv file
        csv = get_csv()

        if (csv == 'quit'):
            terminate()
        
        largest_column_count = 0
        with open(csv, 'r') as temp_f:
            lines = temp_f.readlines()
            for l in lines:
                # Count the column count for the current line
                column_count = len(l.split(',')) + 1
                # Set the new most column count
                largest_column_count = column_count if largest_column_count < column_count else largest_column_count

        # Generate column names (will be 0, 1, 2, ..., largest_column_count - 1)
        column_names = [i for i in range(0, largest_column_count)]

        # Read csv
        dataset = pd.read_csv(csv, header=None, delimiter=',', names=column_names)
        # dataset.info()

        # Transform data into dataframe
        df_out = dataset.apply(lambda x: list(x.dropna().values), axis=1).to_list()
        te = TransactionEncoder()
        te_ary = te.fit(df_out).transform(df_out)
        dataframe = pd.DataFrame(te_ary, columns=te.columns_)

        while True:
            print("\n------ Analysis ------")
            print("1 - Generate frequent itemsets and perform association analysis 📈 🔗")
            print("2 - Display frequency of n-th most purchased items 👍 📊")
            print("3 - Display frequency of n-th least purchased items 👎 📊")
            print("0 - Quit 🛑 ")

            try:
                choice = int(input("Choice : "))
                print()

                if choice == 1:
                    # Get Method
                    method = select_method()
                    # Get Threshold
                    minsup = get_minsup_count()

                    if (len(dataframe) > 0):
                        # Generate frequent itemsets
                        print("\n------ Frequent Itemsets ------")
                        print(f'Minimum Support Count: {minsup}%')
                        if (method == 1):
                            frq_items = apriori(dataframe, min_support=minsup / 100, use_colnames=True)
                        else:
                            frq_items = fpgrowth(dataframe, min_support=minsup / 100, use_colnames=True)

                        if (len(frq_items) > 0):
                            print(frq_items)
                            run_association_rules(frq_items)
                        else:
                            print("No frequent itemsets generated. You may need to reduce your munimum support count")
                    else:
                        print("\n❌ Empty Dataset!")

                elif choice == 2 or choice == 3:
                    n = int(input("Enter value of n: "))
                    max = len(dataset)
                    if n > 1 and n < max:
                        color = plt.cm.rainbow(np.linspace(0, 1, n))
                        if (choice == 2):
                            dataset[0].value_counts().head(n).plot.bar(color = color, figsize=(13,8))
                            plt.title(f'Frequency of {n} Most Purchased Items', fontsize = 14)
                        else:
                            dataset[0].value_counts().tail(n).plot.bar(color = color, figsize=(13,8))
                            plt.title(f'Frequency of {n} Least Purchased Items', fontsize = 14)
                        plt.xticks(rotation = 90)
                        plt.grid()
                        plt.show()
                    else:
                        print(f"Value of n must be more than 0 and less than {max}!")

                elif choice == 0:
                    break
                
                else:
                    print("Invalid Choice! Please try again.")
            
            except:
                print("Something went wrong 😔")
    
        terminate()
    

if __name__ == '__main__':
    main()
