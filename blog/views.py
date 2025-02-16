from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect


class PostListView(View):
    """
    Vue pour afficher la liste des articles du blog.
    """
    template_name = 'blog/post_list.html'

    def get(self, request):
        posts = Post.objects.all()  # Récupère tous les articles

        context = {
            'posts': posts,
            'page': 'lexique-blog'
        }

        return render(request, self.template_name, context)


class CreatePostView(LoginRequiredMixin, View):
    """
    Vue pour créer un nouvel article. Nécessite d'être connecté.
    """
    template_name = 'blog/post_form.html'

    def get(self, request):
        posts = PostForm()  # Initialise un formulaire vide
        return render(request, self.template_name, {'posts': posts})

    def post(self, request):
        posts = PostForm(request.POST)
        if posts.is_valid():
            posts = posts.save(commit=False)
            posts.author = request.user  # Associe l'article à l'utilisateur connecté
            posts.save()
            return redirect(reverse_lazy('blog:post_list'))

        return render(request, self.template_name,
                    {'posts': posts, 'page': 'create-post'})


class DetailPostView(View):
    """
    Vue pour afficher les détails d'un article spécifique.
    """
    template_name = 'blog/post_detail.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # Récupère les commentaires liés à l'article
        comments = Comment.objects.filter(post=post)

        return render(request, self.template_name,
                    {'post': post, 'comments': comments, 'page': 'detail-blog'})


class CreateCommentPostView(LoginRequiredMixin, View):
    """
    Vue pour ajouter un commentaire à un article.
    """
    template_name = 'blog/comment_form.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm()  # Formulaire de commentaire

        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associe le commentaire à l'article
            comment.author = request.user  # Associe le commentaire à l'utilisateur connecté
            comment.save()
            return redirect(reverse('blog:post_detail', kwargs={'pk': pk}))

        return render(request, self.template_name, {'form': form})


class UpdatePostView(LoginRequiredMixin, View):
    """
    Vue pour modifier un article. Seul l'auteur peut le modifier.
    """
    template_name = 'blog/post_update.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            # Redirection si l'utilisateur n'est pas l'auteur
            return redirect('blog:post_list')
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            return redirect('blog:post_list')
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
        return render(request, self.template_name, {'form': form, 'post': post})


class DeletePostView(LoginRequiredMixin, View):
    """
    Vue pour supprimer un article. Seul l'auteur peut le supprimer.
    """
    template_name = 'blog/post_confirm_delete.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            # Empêche la suppression si l'utilisateur n'est pas l'auteur
            return redirect('blog:post_list')
        return render(request, self.template_name, {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            return redirect('blog:post_list')
        post.delete()
        return redirect('blog:post_list')


class UpdateCommentView(LoginRequiredMixin, View):
    """
    Vue pour modifier un commentaire. Seul l'auteur peut le modifier.
    """
    template_name = 'blog/comment_update.html'

    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author != request.user:
            return redirect('blog:post_list')
        form = CommentForm(instance=comment)
        return render(request, self.template_name, {'form': form, 'comment': comment})

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author != request.user:
            return redirect('blog:post_list')
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
        return render(request, self.template_name, {'form': form, 'comment': comment})


class DeleteCommentView(LoginRequiredMixin, View):
    """
    Vue pour supprimer un commentaire. Seul l'auteur peut le supprimer.
    """
    template_name = 'blog/comment_confirm_delete.html'

    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author != request.user:
            return redirect('blog:post_list')
        return render(request, self.template_name, {'comment': comment})

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author != request.user:
            return redirect('blog:post_list')
        comment.delete()
        return redirect('blog:post_list')
