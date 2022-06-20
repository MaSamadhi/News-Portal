from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(pRating=Sum('postRating'))
        pRat = 0
        pRat += postRat.get('pRating')

        commentRat = self.authorUser.comment_set.aggregate(cRating=Sum('commentRating'))
        cRat = 0
        cRat += commentRat.get('cRating')



        self.authorRating = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return str(self.authorUser)


class Category(models.Model):
    categoryName = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.categoryName.title()


class Post(models.Model):
    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICE = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default=ARTICLE)
    creationDate = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    postTitle = models.CharField(max_length=128)
    postText = models.TextField()
    postRating = models.SmallIntegerField(default=0)

    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

    def preview(self):
        return f'{self.postText[0:123]}...'

    def __str__(self):
        return f'{self.postTitle}: {str(self.postText)[0:123]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.postThrough)[0:32]}...: {self.categoryThrough}'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    commentDate = models.DateTimeField(auto_now_add=True)
    commentRating = models.SmallIntegerField(default=0)

    def like(self):
        self.commentRating += 1
        self.save()

    def dislike(self):
        self.commentRating -= 1
        self.save()

    def __str__(self):
        return f'{self.commentUser} in {self.commentPost.postTitle}: {self.commentText}'