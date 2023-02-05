"""
    module is nothing but a python file
    importing python file is nothing but using that file in current file

    https://docs.python.org/3.9/py-modindex.html
    Do check for different modules in python using above link
    you can check them and try them in your project

    We can use pip for installing python modules

    when you are installing python external modules. It will be stored in site-pkckages folder

    pip will come by inbuilt in 3.9
    to install any module in python we need to use -> pip install <module name>
    also we can uninstall any module by using -> pip uninstall <module name>
    


"""

from datetime import date

# print("min year " + str(date.MINYEAR))
# print("custom date " + str(datetime.date(2023,2,5)))
today = date.today()
print("today date ",today)

