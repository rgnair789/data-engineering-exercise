#! python3
from datetime import datetime, date, timedelta
from collections import Counter
import requests 
import csv
from os import path 

#######################################################
# used to open csv file
#######################################################
class CSVFileOpen:
  def __init__(self,file_name,mode):
    self.file_name=file_name
    self.mode=mode

  def __enter__(self):
    try:
      self.fobj=open(self.file_name,self.mode,newline='')
    except:
      print('Error: opening file '+self.file_name+' in mode='+self.mode+' failed...')
      raise
    else:
#      print('File '+self.file_name+' successful opened in mode='+self.mode)
      return(self.fobj)

  def __exit__(self,exc_type, exc_class, exc_tb):
    if self.fobj:
      self.fobj.close()


#######################################################
# Obtains feed using API 
#######################################################
def get_feed(url):
  try:
    response = requests.get(url)
    if response.status_code>299:
      print('Error: failed to get data from subjects API, status code =',response.status_code)
      raise
  except:

    raise
  else:
    print('Obtained feed from subjects API successfully')
    return(response)


#######################################################
# checks if the csv file is atleast of size 'min_size'
#######################################################
def check_csv_file_size(csv_file_name,min_size):

  if path.getsize(csv_file_name) < min_size:
    print('Warning: The size of csv file,',csv_file_name,' is below threshold of ',min_size)
 

#######################################################
# checks for duplicate names for the same key
#######################################################
def check_dup_keys(st,category):

  ctr=Counter(x for x,_ in st)

  if ctr.most_common(1)[0][1]>1:
    print('Error: ',category,'data has dup keys for',ctr.most_common(1)[0][0])
    raise


#######################################################
if __name__=='__main__':

  target_dir='d:/raghu_lite'
  csv_book_file_name=target_dir+'/csv_book.csv'
  csv_author_file_name=target_dir+'/csv_author.csv'
  csv_book_author_file_name=target_dir+'/csv_book_author.csv'

  response=get_feed("https://openlibrary.org/subjects/fantasy.json")
  response_json=response.json()

  st_books,st_authors,st_book_author=set(),set(),set()

  for work in response_json['works']:
    book_row=(work['key'],work['title'])
    authors_row=set((y['key'],y['name']) for y in work['authors'])
    st_books.add(book_row)
    st_authors.update(authors_row)
    book_key,book_name=book_row
    for author_key,author_name in authors_row:
      st_book_author.add((book_key,author_key,book_name,author_name))

  try:

    check_dup_keys(st_books,'Book')
    check_dup_keys(st_authors,'Author')

    with CSVFileOpen(csv_book_file_name,'w') as f: 
        csvwriter = csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) 
        csvwriter.writerow(["Book_key","Book_name"])
        csvwriter.writerows(st_books)

    with CSVFileOpen(csv_author_file_name,'w') as f: 
        csvwriter = csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) 
        csvwriter.writerow(["Author_key","Author_name"])
        csvwriter.writerows(st_authors)

    with CSVFileOpen(csv_book_author_file_name,'w') as f: 
        csvwriter = csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) 
        csvwriter.writerow(["Book_key","Author_key","Book_name","Author_name"])
        csvwriter.writerows(st_book_author)

    check_csv_file_size(csv_book_file_name,100)
    check_csv_file_size(csv_author_file_name,100)
    check_csv_file_size(csv_book_author_file_name,500)
    print('Files created:')
    print('1. ',csv_book_file_name)
    print('2. ',csv_author_file_name)
    print('3. ',csv_book_author_file_name)


  except:
    print('*** Error in processing ***')

  print('*** End of procesing ***')
