[![colab](https://img.shields.io/badge/colab-launch-blue.svg)](https://colab.research.google.com/drive/1BGLalP4rr5FdtXsEzb5oG4sHL5qmgbAS#scrollTo=YuW47K8E4IBZ)

# boo
Python client for Rosstat open data corporate reports. Creates a local CSV file with column names, importable as pandas dataframe.

## Goal

Access balance sheet, profit and loss and cash flow statements of Russian firms in less time and fewer boilerplate.


## Install

```
pip install git+https://github.com/ru-corporate/boo.git@master
```

## Usage

```python
from boo import prepare, read_dataframe

prepare(2012)
df = read_dataframe(2012)
print(df.head())
```

## Data model
 
CSV files are  located at `~/.boo` folder.

File name     | Description  | Column count |  Created by 
--------------|--------------|:------------:|:------------:
`raw_<year>.csv`     | Original CSV file from Rosstat website. No header row.    | 266 |`download(year)`
`trimmed_<year>.csv` | CSV file with column names in header row, unnamed columns. | 58\* | `cut(year)`
`canonic_<year>.csv` | CSV file with additional column transformations (eg. `region`) and error filters. Reference dataset for analysis. | 58\* | `put(year)`

(\*) equal by coincidence, some columns are added and some removed

## Hints

#### User

- CSV files are quite big, start with year 2012 to experiment.
- Use link above for Google Colab to run package remotely.
- Use `read_dataframe(year)` to read canonic CSV file. 
- `wipe(year)` if you do not want to keep intermediate CSV files.
- `wipe_all()` if you want to clean up everything.

#### Developper

- `boo.path.default_data_folder` shows where the CSV files on a computer.
- `boo.columns` controls CSV column selection and naming.
- `boo.year.TIMESTAMPS` is in change of finding proper URLs, which change with website updates. 
- New annual dataset released around September-October.

#### Script

Rosstat publishes CSV files without column headers. 
When preparing a readable CSV file we cut many unnecessary columns and 
give a name to remaining columns. This way we can handle information from CSV 
file meaningfully and also the size of the files is smaller.

For illustration, batch script below creates trimmed `p2012.csv` file with column names.

```bat
set url=http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20190329t000000-structure-20121231t000000.csv
set index=1,2,3,4,5,6,7,8,17,18,27,28,37,38,41,42,43,44,57,58,59,60,67,68,69,70,79,80,81,82,83,84,93,94,99,100,105,106,117,118,204,205,209,210,211,212,213,214,215,216,222,223,228,229,235,240,241,266 
set colnames=name,okpo,okopf,okfs,okved,inn,unit,report_type,of,of_lag,ta_fix,ta_fix_lag,cash,cash_lag,ta_nonfix,ta_nonfix_lag,ta,ta_lag,tp_capital,tp_capital_lag,debt_long,debt_long_lag,tp_long,tp_long_lag,debt_short,debt_short_lag,tp_short,tp_short_lag,tp,tp_lag,sales,sales_lag,profit_oper,profit_oper_lag,exp_interest,exp_interest_lag,profit_before_tax,profit_before_tax_lag,profit_after_tax,profit_after_tax_lag,cf_oper_in,cf_oper_in_sales,cf_oper_out,paid_to_supplier,paid_to_worker,paid_interest,paid_profit_tax,paid_other_costs,cf_oper,cf_inv_in,cf_inv_out,paid_fa_investment,cf_inv,cf_fin_in,cf_fin_out,cf_fin,cf,date_published

curl %url% > 2012.csv

echo %colnames% > p2012.csv
cat 2012.csv | csvcut -d; -e ansi -c%index%  | iconv -f cp1251 -t utf-8 >> p2012.csv

csvclean p2012.csv
```

This result is similar to running: 

```python 
from boo import download, cut
download(2012)
cut(2012)
```

## Limitations

- No timeseries: we can access all data for each year, but not several years for each firm,
  even though the data is available. 
- No database: we store files as CSV, not in a database.
