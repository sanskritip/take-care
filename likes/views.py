from django.shortcuts import render
# Create your views here.
'''
likelist=[]
def likeSet(request, slug):
     global likelist
     object_liked =ContentType.objects.all().filter(slug=slug).first()
     object_liker = User.objects.all().filter(username=request.user).first()
     like_set = Like.objects.all().filter(liked_by = object_liker).filter(slug=slug)
     l = Like(liked_by = object_liker, content_object=object_liked)
     if list(like_set)==[]:
        l.save()
     else:
         my_obj = Like.objects.get(liker = object_liker, content_type=object_liked)
         my_obj.delete()
     return redirect('/blogs/'+slug)'''
