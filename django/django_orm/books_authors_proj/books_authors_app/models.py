from django.db import models
    
class BOOK(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        authorsList = ""
        for eachAuthor in self.Authors.all():
            authorsList = authorsList + ", " + eachAuthor.first_name + "(" + str(eachAuthor.id) + ")"
        
        return f"< ({self.id}) BOOK object: {self.title}, {self.description}, Authors: {authorsList[2:]}>"

class AUTHOR(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    Books = models.ManyToManyField(BOOK, related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __repr__(self):
        bookList = ""
        for eachBook in self.Books.all():
            bookList = bookList + ", " + eachBook.title + "(" + str(eachBook.id) + ")"
        
        return f"< (id{self.id}) AUTHOR object: {self.first_name}, {self.last_name}, {self.notes}, Books: {bookList[2:]}>"  