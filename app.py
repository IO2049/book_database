#[X] import models
#[X] main menu - add, search, analysis, exit, view
#[] add books to the database
#[] edit books
#[] search books
#[] data cleaning
#[] loop running program

from models import (Base, session,
                    Book, engine)
import datetime, csv
import pandas as pd
import numpy as np

def menu():
    while True:
        print(
            '''
            \nPROGRAMMING BOOKS
            \r1) Add
            \r2) View All
            \r3) Search
            \r4) Analyse
            \r5) Exit
            '''
        )
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input(
            '''
            \rPlease choose one of the options above
            \rA number from 1-5
            \rPress enter to try again '''
            )

def clean_date(date_str):
    months = [
        'January', 'February', 'March',
        'April', 'May', 'June',
        'July','August', 'September',
        'October', 'November', 'December'
        ]
    split_date = date_str.split(' ')
    #print(split_date)
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)

def clean_price(price_str):
    price_float = float(price_str)
    return int(price_float * 100)

def add_csv():
    with open('suggested_books.csv') as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            book_in_db = session.query(Book).filter(Book.title == row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title = title, author = author,
                            published_date = date, price = price)
                session.add(new_book)
        session.commit()

    # db_books = pd.read_csv('suggested_books.csv', header=None)
    # print(db_books.head())



def app():
    app_running = True
    while app_running:
        choice = menu()

        match choice:
            case "1":
                return "1"
            case "2'":
                return "2"
            case "3":
                return "3"
            case "4":
                return "4"
            case "5":
                return "5"


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #app()
    add_csv()

    for book in session.query(Book):
        print(book)