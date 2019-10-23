FROM python:3

RUN git clone https://github.com/valefaraz/sudoku.git

WORKDIR /sudoku

RUN pip freeze > requirements.txt

RUN pip3 install requests

RUN pip install -r requirements.txt

CMD ["python", "./ingreso.py"]