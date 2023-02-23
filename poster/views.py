from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Category, Customer
from .forms import PostForm, CustomerForm
from django.template.defaultfilters import slugify
import cloudinary


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).filter(
        approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category'] = Category.objects.order_by('-created_on')
        return context


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        # queryset = Post.objects
        post = get_object_or_404(Post, slug=slug)
        return render(
            request,
            "post/post_detail.html",
            {
                "post": post,
            },
        )


class MyPostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).filter(
        approved=True).order_by('-created_on')
    template_name = 'post/my_posts.html'
    paginate_by = 6

    def get_queryset(self):
        return self.model.objects.filter(seller=self.request.user)


class NewPost(View):
    def get(self, request):
        return render(
            request,
            "post/new_post.html",
            {
                "post_form": PostForm
            },
        )

    def post(self, request):
        post_form = PostForm(data=request.POST, files=request.FILES)

        if post_form.is_valid():
            post_form.instance.seller = request.user
            post = post_form.save(commit=False)
            post.slug = slugify(post_form.cleaned_data['title'])
            post.save()
            messages.success(request,
                             "New Addvertisement created successfully!")
            return render(
                request,
                "post/post_detail.html",
                {
                    "post": post,
                },
            )
        else:
            post_form = PostForm()
            messages.danger(request,
                            "Oops, something went wrong, please try again!")
            return render(
                request,
                "post/new_post.html",
                {
                    "post_form": PostForm
                },
            )


class EditPost(View):
    def get(self, request, slug, *args, **kwargs):
        # queryset = Post.objects
        post = get_object_or_404(Post, slug=slug)
        post_form = PostForm(instance=post)
        return render(
            request,
            "post/edit_post.html",
            {
                "post_form": post_form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        # queryset = Post.objects
        post = get_object_or_404(Post, slug=slug)
        post_form = PostForm(data=request.POST, files=request.FILES,
                             instance=post)

        if post_form.is_valid():
            epost = post_form.save(commit=False)
            epost.slug = slugify(post_form.cleaned_data['title'])
            epost.save()
            messages.success(request, "Advertisement updated successfully!")
            return render(
                request,
                "post/post_detail.html",
                {
                    "post": epost,
                },
            )
        else:
            post_form = PostForm()
            messages.danger(request,
                            "Oops, something went wrong, please try again!")
            return render(
                request,
                "post/new_post.html",
                {
                    "post_form": PostForm
                },
            )


class PostSold(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        post.status = not post.status
        post.save()
        messages.success(request, "Advertisement status changed successfully!")
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class BuyPost(View):
    def get(self, request, slug, *args, **kwargs):
        return render(
            request,
            "post/buy_post.html",
            {
                "customer_form": CustomerForm,
                "slug": slug
            },
        )

    def post(self, request, slug, *args, **kwargs):
        customer_form = CustomerForm(data=request.POST)
        post = get_object_or_404(Post, slug=slug)
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.post_id = post
            customer.save()
            messages.success(request,
                             "Information sent. Seller will contact you soon!")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            customer_form = CustomerForm()
            messages.danger(request,
                            "Oops, something went wrong, please try again!")
            return render(
                request,
                "post/buy_post.html",
                {
                    "customer_form": CustomerForm
                },
            )


class DeletePost(SuccessMessageMixin, generic.DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_message = "Advertisement deleted successfully!"
    success_url = "/posts/my-posts"


class Customers(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        customer_list = Customer.objects.filter(post_id=post).order_by(
                                                '-created_on')
        paginator = Paginator(customer_list, 4)
        page = request.GET.get('page')
        customer_list = paginator.get_page(page)
        return render(
            request,
            "post/customers.html",
            {
                "customer_list": customer_list,
            },
        )
