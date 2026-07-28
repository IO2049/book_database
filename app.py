#import models
#main menu - add, search, analysis, exit, view
#add books to the database
#edit books
#search books
#data cleaning
#loop running program

from models import (Base, session,
                    Book, engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)