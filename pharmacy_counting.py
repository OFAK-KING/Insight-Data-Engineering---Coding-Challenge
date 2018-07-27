import csv
def read_rawdata(filename):
    results={}
    with open (filename, newline = '') as csvfile:
        data = csv.DictReader(csvfile,delimiter = ',')

        for row in  data:
            drug_name=row['drug_name']
            drug_stats = results.get(drug_name,None)
            if not drug_stats:
                results[drug_name]=(1,int(row['drug_cost']))
            else:
                (counter, amt)  = drug_stats
                results[drug_name] = (counter+1,amt + int(row['drug_cost']))
        print("{name}\t{prescriptions}\t{total}".format(
               name="drug_name",
               prescriptions="num_prescriber",
               total="total_cost"
            ))
        for (drug,(cnt,amt)) in results.items():
            print("{name}\t{prescriptions}\t{total}".format(
               name=drug,
               prescriptions=cnt,
               total=amt
            ))


read_rawdata("Data.txt")
