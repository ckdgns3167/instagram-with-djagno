from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from instagram.forms import PostForm


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())  # pk가 필요하기 때문에 save를 하고 다대다 관계 사이의 값을 저장시켜주자...
            messages.success(request, "성공적으로 포스팅되었습니다.")
            return redirect('/')  # TODO: use get_absolute_url
    else:
        form = PostForm()

    return render(request, 'instagram/post_form.html', {
        'form': form
    })
