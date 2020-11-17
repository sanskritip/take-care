from django.shortcuts import render,redirect
from django.views import generic
from .models import Picture, PComment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import  LoginRequiredMixin
from .forms import PictureForm, CommentForm
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from feed.views import set_like,set_save
def like_post(request,slug):
    set_like(request,slug,2)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def save_post(request,slug):
    set_save(request,slug,2)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def picture_detail(request, slug):
    template_name = 'picture_detail.html'
    picture = get_object_or_404(Picture, slug=slug)
    currentuser=request.user
    alllikescount=picture.likes.count()
    alllikes=picture.likes.all()
    likelist=[]
    for i in alllikes:
        likelist.append(i.liked_by)
    comments = PComment.objects.all().filter(picture = picture)
    #comments = post.comments;
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.workout = workout
            new_comment.author = currentuser
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'picture': picture,
                                           'piccomments': comments,
                                           'currentuser':currentuser,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'alllikescount':alllikescount,
                                           'likelist':likelist,
                                           })
def addpicture(request):
    template_name='addpicture.html'
    user=request.user
    '''user=get_object_or_404(User)
    posts=post.filter(status=1,author=user)'''
    new_picture=None
    if request.method=='POST':
        addpicture_form =PictureForm(request.POST,request.FILES)
        if addpicture_form.is_valid():
            new_picture=addpicture_form.save(commit=False)
            new_picture.author=user
            new_picture.save()
        return redirect('dashboard')
    else:
        addpicture_form=PictureForm()
    return render(request,template_name,{
                                    'user':user,
                                    'new_picture':new_picture,
                                    'addpicture_form':addpicture_form})

def picture_update(request,slug):
    obj = get_object_or_404(Picture,slug=slug)
    form = PictureForm(request.POST or None, request.FILES or None, instance= obj)
    context= {'form': form}
    if request.method=='POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            return redirect('dashboard')
        else:
            context= {'form': form,'error': 'The form was not updated successfully. Please enter in a title and content'}
    return render(request, 'picture_update.html', context)


def picture_delete(request, slug):
    picture = get_object_or_404(Picture, slug=slug)
    picture.delete()
    return redirect('dashboard')


def picture_comment(request, slug):
    #template_name = 'picture_comment.html'
    picture = get_object_or_404(Picture, slug=slug)
    user=request.user
    #comments = Comment.objects.filter(post = post)
    #comments = workout.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        new_comment=PComment(body=request.POST.get('messages'))
        #comment_form = CommentForm(data=request.POST)
        #if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            #new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
        #new_comment.body = body
        new_comment.picture = picture
        new_comment.author = user
        new_comment.active = True
            # Save the comment to the database
        new_comment.save()
        #else:
        #   comment_form = CommentForm()
    #return redirect('newsfeed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    '''
    return render(request, template_name, {'workout': workout,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
'''
