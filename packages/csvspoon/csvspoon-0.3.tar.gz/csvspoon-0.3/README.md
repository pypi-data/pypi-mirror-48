# csvspoon: a tool to manipulate csv file with headers

Again, again, and again.

## Python module

All methods and functions are accessible in the python module.

## Cli example
### csvspoon cat: Concatenate CSV files
 - Change delimiter of a csv file:
```
csvspoon cat -d "\t" -u ";" file.csv > result.csv
```
 - Change delimiter of a csv file with specified output:
```
csvspoon cat -o result.csv -d "\t" -u ";" file.csv
```
 - Cat two csv files:
```
csvspoon cat file1.csv file2.csv
```
 - Reformat two columns of a csv files:
```
csvspoon cat -f a_colname:5.1f -f another_colname:04d file.csv
```
 - Cat one csv file, keeping only a column:
```
csvspoon cat file.csv:a_col
```
 - Cat two csv files, renaming a column on the second file:
```
csvspoon cat file1.csv file2.csv:new_col=old_col,another_col
```
### csvspoon apply: Apply functions to add columns
 - Combine text columns by a formula:
```
csvspoon apply -a name "lastname.upper()+' '+firstname.lower()" file.csv
```
 - Sum to integer columns:
```
csvspoon apply -t cola:int -t colb:int -a colsum "cola+colb" file.csv
```
 - Sum to integer columns and format the result:
```
csvspoon apply -t cola:int -t colb:int -a colsum:05d "cola+colb" file.csv
```
 - Compute complex expression between columns:
```
csvspoon apply \
        -b "import math" \
        -t x:float \
        -t y:float \
        -a norm "math.sqrt(x**2+y**2)" \
        file.csv
```
 - Multiple computation can be done reusing newly created columns:
```
csvspoon apply -t x:int -a x2p1 "x**2+1" -a x2p1m1 "x2p1-1" file.csv
```
### csvspoon sort: Sort CSV file
 - Sort csv file using column cola:
```
csvspoon sort -k cola file.csv
```
 - Sort csv file using columns cola and colb:
```
csvspoon sort -k cola -k colb file.csv
```
 - Sort csv file using numerical mode on column numcol:
```
csvspoon sort -n -k numcol file.csv
```
 - Shuffle csv file:
```
csvspoon sort -R file.csv
```
### csvspoon filter: Filter CSV from given conditions
 - Filter csv file using two columns:
```
csvspoon filter -a "lastname!=firstname" file.csv
```
 - Chain filters on csv file:
```
csvspoon filter \
        -a "lastname.startswith('Doe')" \
        -a "firstname.starswith('John')" \
        file.csv
```
 - Filter csv file with float column price:
```
csvspoon filter -t price:float -a "price>12.5" file.csv
```
 - Filter csv file with complex expression:
```
csvspoon filter \
        -b "import math" \
        -t x:float \
        -t y:float \
        -t z:float \
        -a "math.sqrt(x**2+y**2)>z" \
        file.csv
```
### csvspoon join: Join CSV files
 - Operate NATURAL JOIN on two csv files:
```
csvspoon join file1.csv file2.csv
```
 - Operate two NATURAL JOIN on three csv files:
```
csvspoon join file1.csv file2.csv file3.csv
```
 - Operate LEFT JOIN on two csv files
```
csvspoon join -l file1.csv file2.csv
```
### csvspoon aggregate: Compute aggregation on CSV file
 - Computing the total mean grade:
```
csvspoon aggregate \
        -b "import numpy as np" \
        -t grade:float \
        -a meangrade "np.mean(grade)" \
        file.csv
```
 - Computing the total mean grade specifing a format:
```
csvspoon aggregate \
        -b "import numpy as np" \
        -t grade:float \
        -a meangrade:.2f "np.mean(grade)" \
        file.csv
```
 - Computing the mean grade by group:
```
csvspoon aggregate \
        -b "import numpy as np" \
        -t grade:float \
        -a meangrade "np.mean(grade)" \
        -k group \
        file.csv
```
 - Computing the mean grade, median, standard deviation by group:
```
csvspoon aggregate \
        -b "import numpy as np" \
        -t grade:float \
        -a meangrade "np.mean(grade)" \
        -a mediangrade "np.median(grade)" \
        -a stdgrade "np.std(grade)" \
        -k group \
        file.csv
```
