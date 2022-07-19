# Demonstration
The objective is to take a csv containing data, and print it to the console in neatly formatted columns, with a bar graph depicting the data contained in the final column.

Example Output:
```
2021-10-08	  219.77	||||||||||||||||||||||||||||||||||||||||||||
2021-10-15	  175.54	||||||||||||||||||||||||||||||||||||
2021-10-22	  195.74	||||||||||||||||||||||||||||||||||||||||
2021-10-29	  241.30	|||||||||||||||||||||||||||||||||||||||||||||||||
2021-11-05	  208.06	||||||||||||||||||||||||||||||||||||||||||
2021-11-12	  111.32	|||||||||||||||||||||||
2021-11-19	  172.78	|||||||||||||||||||||||||||||||||||
2021-11-26	  208.62	||||||||||||||||||||||||||||||||||||||||||
2021-12-03	  264.07	|||||||||||||||||||||||||||||||||||||||||||||||||||||
2021-12-10	  233.21	|||||||||||||||||||||||||||||||||||||||||||||||
2021-12-17	  219.43	||||||||||||||||||||||||||||||||||||||||||||
2021-12-24	  226.22	||||||||||||||||||||||||||||||||||||||||||||||
2021-12-31	   57.81	||||||||||||
```

Current Limitations:
<ul>
    <li>Columns won't line up if the values in a given column vary more than 8 characters in length.</li>
    <li>Script will fail if the final column contains anything other than numerical data.</li>
    <li>Cannot graph negative values.</li>
</ul>
