from django.shortcuts import render_to_response
from blog.models import Blog,Tag
from django.http import Http404

def index(request,page_num = 1):
    try:
        page_num = int(page_num)
    except ValueError:
        raise Http404()
    blog_list = Blog.objects.all().order_by('-publish_time')[5*(page_num-1):5*page_num]
    tag_list = Tag.objects.all()
    all_page_num = (len(Blog.objects.all())+4)/5
    if page_num > all_page_num:
        raise Http404()
    if page_num < all_page_num or page_num < 1:
        next_page = page_num + 1
    else:
        next_page = None

    if page_num == 1:
        last_page = None
    else:
        last_page = page_num - 1
    return render_to_response('mainpage.html',{'blog_list':blog_list,'tag_list':tag_list,'page_num': page_num,'all_page_num':all_page_num,'next_page':next_page,'last_page':last_page})


def blog(request,id=1):
    ID = int(id)
    blog = Blog.objects.get(id=ID)
    return render_to_response('blogpage.html',{'blog':blog})

def tag(request,id=1,page_num = 1):
    ID = int(id)
    page_num = int(page_num)
    tag = Tag.objects.get(id = ID)
    blog_list = tag.blog_set.all()
    blog = blog_list[5*(page_num - 1):5*page_num]
    tag_list = Tag.objects.all()
    
    all_page_num = (len(blog_list)+4)/5
    if page_num < 1 or page_num > all_page_num:
        raise Http404()
    
    if page_num == 1:
        last_page = None
    else:
        last_page = page_num - 1 
    if page_num == all_page_num:
        next_page = None
    else:
        next_page = page_num + 1 
    return render_to_response('tagpage.html',{'blog_list':blog,'tag_list':tag_list,'next_page':next_page,'page_num':page_num,'all_page_num':all_page_num,'last_page':last_page,'tag_id':ID})
    

