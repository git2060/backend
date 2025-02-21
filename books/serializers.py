from rest_framework import serializers
from .models import BksAuthor, BksBkAuthors,BksFormat,BksBkLanguages,BksBook,BksBookshelf,BksBkBookshelves,BksLanguage,BksSubject,BksBkSubjects


class BksAuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksAuthor
        fields=['id','birth_year','death_year','name']



class BksBkAuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksBkAuthors
        fields=['id','book_id','author_id']    
   

class BksBkBookshelvesSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksBkBookshelves
        fields=['id','book_id','bookshelf_id'] 


class BksBkLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksBkLanguages
        fields=['id','book_id','language_id']


class BksBkSubjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksBkSubjects
        fields=['id','book_id','subject_id']       


class BksBookshelfSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksBookshelf
        fields=['id','name']     


class BksFormatSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksFormat
        fields=['id','mime_type','url','book_id'] 


class BksLanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksLanguage
        fields=['id','code'] 


class BksSubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksSubject
        fields=['id','name']


class BksBookSerializers(serializers.ModelSerializer):
    class Meta:
        model=BksBook
        fields=['id','download_count','gutenberg_id','media_type','title']


class BookSerializersView(serializers.ModelSerializer):
    author=BksBkAuthorsSerializers(read_only=True, many=True)
    language= BksBkLanguagesSerializers(read_only=True, many=True)
    subject=BksBkSubjectsSerializers(read_only=True, many=True)
    shelves=BksBkBookshelvesSerializers(read_only=True, many=True)
    format=BksFormatSerializers(read_only=True, many=True)
  
    urls = serializers.SerializerMethodField()

    class Meta:
        model=BksBook
        fields=["id","title","author","language","subject","shelves","format","urls"]        


    def get_urls(self, obj):
        return [format.url for format in obj.bksformat_set.all()]    