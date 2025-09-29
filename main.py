# working with strings
from pyscript import display, document


def sample_function(e):
    data1 = document.getElementById('input1').value
    data2 = document.getElementById('input2').value
    data3 = document.getElementById('input3').value

    display(f'Welcome {data1}, you are {data2} years old, and you study at {data3}')



