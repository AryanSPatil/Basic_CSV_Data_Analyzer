import csv
import sys

print("Welcome to the Basic CSV Analyzer")
print("=#"*40)


while True:


    File_name = input("Please input the EXACT file name(With the .csv extention): ").strip()

    try:
                
            with open(File_name, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                header_row = reader.fieldnames

            print(f"\nFile '{File_name}' opened successfully.")
            print(f"   Availabe Columns: {','.join(header_row)}")


            while True:

                column = input("\nInput the name of column you want to analyze: ").strip()

                if column not in header_row:
                    print(f"ERROR: Column '{column}' not found. Please check spelling.")
                    continue

                data_values = []

                with open(File_name,mode='r',newline='',encoding='utf-8') as f_inner:
                    reader_inner = csv.DictReader(f_inner)

                    for i, row in enumerate(reader_inner):
                        clm_values = row[column]

                        try:

                            number = float(clm_values)
                            data_values.append(number)

                        except ValueError:
                            print(f"\nSkipping non-numeric values: '{clm_values}' (Row{i+2})")

                        except KeyError:
                            print(f"\nWARING: Row '{i+2}' is missing data for column {column}")

                    if not data_values:
                        print(f"\nWARNING: Column '{column}'contains no numeric data for analysis.")

                    else:
                        sum_data = sum(data_values)

                        avg_data = sum_data/len(data_values)

                        max_data = max(data_values)

                        min_data = min(data_values)

                        lenght = len(data_values)

                        print("\n","+="*40)
                        print(f"\nThe Sum of all Data in column {column} is: {sum_data:.2f}",
                                f"\nThe Average of all Data in column {column} is: {avg_data:.2f}",
                                f"\nThe Max value in of all the Data in column {column} is: {max_data:.2f}",
                                f"\nThe Min value in of all the Data in column {column} is: {min_data:.2f}",
                                f"\nThe Length of Data in column {column} is: {lenght}",)     
                        print("\n","+="*40)

                    while True:
                        yes_col = input("\nDo you want to Analyze another column from this file?(Y/N): ").strip().upper()

                        if yes_col in ('Y','N'):
                            break
                        print("\nInvalid input. Please enter 'Y' or 'N'.")
                    
                    if yes_col == 'N':
                        break

            while True:
                yes_file = input("\nEnter a new file name for analysis? (Y/N): ").strip().upper()
                if yes_file in ('Y','N'):
                    break
                print("\nInvalid input. Please Enter 'Y' or 'N'")

            if yes_file == 'N':
                print("\n Thank You For Using The Analyzer!")
                sys.exit()


    except FileNotFoundError:
        print(f"ERROR : The file {File_name} does not exist. Please check file name")

    except Exception as e:
        print(f"\n An Unexpexcted ERROR ouccurred: {e}")    
                    
                