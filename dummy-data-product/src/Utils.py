import csv

def saving_to_csv(output_file, dataset_metadata):
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["Title", "Link"]
        Final = csv.DictWriter(csvfile, fieldnames=fieldnames)
        Final.writeheader()
        Final.writerows(dataset_metadata)
        print("Data saved to", output_file)