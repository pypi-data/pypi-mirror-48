
# `myfitness`: Tools to Analyze Apple Health Data

---

Build_Stamp [![Build Status](https://travis-ci.org/LevanniaLildhar/DATA533_lab4_Liza_Levannia.svg?branch=master)](https://travis-ci.org/LevanniaLildhar/DATA533_lab4_Liza_Levannia)

---

The Apple Health Fitness Tracker was a collaborative project by Liza Wood and Levannia Lildhar.

The `myfitness` package provides some basic tools to analyze the health data in a CSV file downloaded from Apple Health. These tools could be used to analyze and compare the data from multiple people.

`healthdata`
- contains two modules
    1. `data` - contains the name, age and gender of the person (the "superclass") and a method to read in the CSV health data file using pandas
    2. `chart` - uses pygal to provide an interactive bar chart to the user

`summary`
- contains two modules
    1. `table` - returns a summarized dataframe of average steps per month
    2. `maxmin`- contains functions to calculate the maximum and minimum number of steps

## Package Structure

`myfitness` --> package

  - `healthdata` --> sub-package

    - `data` --> module
    - `chart` -->module

  - `summary` --> sub-package

    - `table` --> module
    - `maxmin` --> module

## Package Details

The package functions of `myfitness` are described below. The use of the package is also demonstrated in the test file included in this repositry.

### `healthdata`

This subpackage provides users a method of importing data as well as viewing the data interactively.

Detailed descriptions of the `data` module in the `healthdata` subpackage is shown below:  

| Class/Function | Description                                                            | Parameters        | Return                  |
| -------------  |:------------------------------------------------------------------:   | :----------------:|:-----------------------:|
| `Person`     | Create an object of class Person() to be used in further analysis. The 'display' function displays the name, age and gender of a Person() object  | name, age, gender | An object of class Person with name, age and gender attributes |
| `healthdata`   | Create a object of class healthdata() this inherits from the superclass Person()| name, age, gender, file (downloaded from Apple Health, as CSV) | Display of healthdata object attributes name, age, gender and dataframe containing healthdata() object file |

Detailed descriptions of the  `chart` function in the `healthdata` subpackage is shown below:  

| Function       | Description                                                            | Parameters        | Return                  |
| -------------  |:------------------------------------------------------------------:   | :----------------:|:-----------------------:|
| `chart`     | Creates an interactive bar graph using pygal | columnX as list of strings, columnY as list of values, xlabel as string, ylabel as string, filename | .svg file with xlabel, ylabel, title, and filename |

### `summary`

This subpackage provides users with some basic statistical analysis tools to view their data extracted from Apple Health.

Detailed descriptions of the `table` function in the `summary` subpackage is shown below:  

|Function        | Description                                                            | Parameters        | Return                  |
| -------------  |:------------------------------------------------------------------:   | :----------------:|:-----------------------:|
| `table`     | Function to summarize the average number of steps taken per month using the pandas package | data: Apple Health .csv file imported as a Pandas DataFrame | A Pandas dataframe, summarizing the average number of steps taken by month, indicated by the last date of the month. |

Detailed descriptions  of the `maxMin` function in the `summary` subpackage is shown below:  

| Function        | Description                                                            | Parameters        | Return                  |
| -------------  |:------------------------------------------------------------------:   | :----------------:|:-----------------------:|
| `getMax`     | Find the maximum number of steps in the data and the date it was achieved. | data: Pandas DataFrame containing Apple Health data imported from a CSV file.|The row of values for when the maximum number of steps were achieved:Start date, Finish date,Distance(mi), Steps (count) |
| `getMin`      | Find the maximum number of steps in the data and the date it was achieved.| data: Pandas DataFrame containing Apple Health data imported from a CSV file. | The row of values for when the maximum number of steps were achieved:Start date, Finish date, Distance(mi), Steps (count) |

## Testing

`myfitness_tests` contains the necessary test suite and classes to verify that the package is working correctly. There are a total of four classes that conduct unit testing as well as the suite.

Test Suite Coverge Report ![Coverage Report](https://github.com/lizawood/Apple-Health-Fitness-Tracker/blob/master/Package/myfitness_tests/Test_Coverage_Report_Screenshot.png)

## Requirements

This package requires the following Python modules:

- numpy
- pandas
- pygal
- IPython
- CairoSVG
