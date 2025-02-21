from django.db import models

# Create your models here.

class BksAuthor(models.Model):
    birth_year = models.IntegerField(blank=False, null=False)
    death_year =  models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=128, blank=False, null=False)
    class Meta:
        db_table = "books_author"

    def __str__(self):
        return self.name
    
class BksBook(models.Model):
    author = models.ManyToManyField("BksBkAuthors", related_name="books") 
    language = models.ManyToManyField("BksBkLanguages", related_name="books") 
    subject = models.ManyToManyField("BksBkSubjects", related_name="books") 
    shelves = models.ManyToManyField("BksBkBookshelves", related_name="books")
    download_count = models.IntegerField()
    gutenberg_id = models.IntegerField(blank=False, null=False)
    media_type= models.CharField(max_length=16, blank=False, null=False)
    title = models.TextField()
    
    class Meta:
        db_table = "books_book"

    def __str__(self):
        return self.title

class BksBkAuthors(models.Model):
    book= models.ForeignKey(BksBook, on_delete=models.CASCADE, related_name="book_authors")
    author =models.ForeignKey(BksAuthor, on_delete=models.CASCADE)
    class Meta:
        db_table = "books_book_authors"

    def __str__(self):
        return f"{self.book.title} - {self.author.name}"
     

class BksBookshelf(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    class Meta:
        db_table = "books_bookshelf"

    def __str__(self):
        return self.name 
    
#
class BksBkBookshelves(models.Model):
    book= models.ForeignKey(BksBook, on_delete=models.CASCADE, related_name="shelve")
    bookshelf= models.ForeignKey(BksBookshelf, on_delete=models.CASCADE)
    class Meta:
        db_table = "books_book_bookshelves"
     
    def __str__(self):
        return f"{self.book}-{self.bookshelf}"


class BksLanguage(models.Model):
    code = models.CharField(max_length=4, blank=False, null=False)
    class Meta:
        db_table = "books_language"

    def __str__(self):
        return self.code
    
#
class BksBkLanguages(models.Model):
    book= models.ForeignKey(BksBook, on_delete=models.CASCADE, related_name="language_book")
    language = models.ForeignKey(BksLanguage, on_delete=models.CASCADE)
    class Meta:
        db_table = "books_book_languages"

    def __str__(self):
        return f"{self.book}-{self.language}"


class BksSubject(models.Model):
    name = models.TextField(blank=False, null=False)
    class Meta:
        db_table = "books_subject"

    def __str__(self):
        return self.name  

#
class BksBkSubjects(models.Model):
    book= models.ForeignKey(BksBook, on_delete=models.CASCADE, related_name="subjects")
    subject = models.ForeignKey(BksSubject, on_delete=models.CASCADE)
    class Meta:
        db_table = "books_book_subjects"

    def __str__(self):
        return f"{self.book}-{self.subject}"

#
class BksFormat(models.Model):
    mime_type = models.CharField(max_length=32, blank=False, null=False)
    url = models.TextField(blank=False, null=False)
    book = models.ForeignKey(BksBook, on_delete=models.CASCADE)
    class Meta:
        db_table = "books_format"

    def __str__(self):
        return f"{self.book}-{self.url}"  


    
