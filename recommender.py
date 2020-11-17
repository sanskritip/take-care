from feed.models import Like,Tag
from blogs.models import Post
from posts.models import Picture
from workout.models import Workout
from itertools import chain

def title_score(obj1, obj2):
    title1 = obj1.title
    title2 = obj2.title

    l1 = title1.split()
    l2 = title2.split()

    weight = 50
    return weight*jaccard_score(l1,l2)

def likeCount_score(obj1,obj2):
    count2 = obj2.likes.count()
    weight = 10
    return weight*count2

def author_score(obj1,obj2):
    f = 0
    if obj1.author == obj2.author:
        f = 1
    weight = 20
    return weight*f

def tag_score(obj1,obj2):
    l1 = []
    l2 = []
    t  = Tag.objects.all()
    for i in t:
        if i.content_object.slug == obj1.slug:
            l1.append(i.name)
        elif i.content_object.slug == obj2.slug:
            l2.append(i.name)

    weight = 1000
    return weight*jaccard_score(l1,l2)

def jaccard_score(l1,l2):
    intersection, union = 0,0
    for i in l1:
        if i in l2:
            intersection+= 1
    union = len(l1)+len(l2) - intersection
    if union==0 and intersection == 0:
        union =1

    jscore = float(intersection)/union
    return jscore

def get_recommendation(user):
    # need to generate an array with similarity of every post with each other.
    # check if user has liked that object. then scale first 10 similar posts related to the liked post by a value
    # return top 10 array of objects for recommendations.
    post_list = Picture.objects.all()
    blog_list = Post.objects.all()
    work_list = Workout.objects.all()

    combined_list = list(chain(post_list,blog_list,work_list))
    combined_list = sorted(combined_list, key = lambda x: x.likes.count())

    l = []
    likeset = Like.objects.all()
    for i in combined_list:
        for j in likeset:
            if j.liked_by == user and j.content_object == i:
                l.append(i)

    if l==[]:
        return combined_list[:10]

    else:
        score = list()
        for i in l:
            for j in combined_list:
                risk = tag_score(i,j) + author_score(i,j) + likeCount_score(i,j) + title_score(i,j)
                score.append([i,j,risk])

    score = sorted(score, key = lambda x: x[2], reverse = True)

    res = []
    for i in score:
        res.append(i[1])
    res += combined_list

    return res[:10]
