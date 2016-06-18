from django.shortcuts import render
from . import models as fbask_models

from django.views.generic import ListView, TemplateView


class InternalView(ListView):
    def render_to_response(self, context, **response_kwargs):
        return context, response_kwargs


class ArticleList(InternalView):
    model = fbask_models.Article


class AuthorList(InternalView):
    model = fbask_models.Author


class MultiView(TemplateView):
    template_name = 'fbask/multiview.html'

    def get_context_data(self, **kwargs):
        context = super(MultiView, self).get_context_data(**kwargs)

        context.update(self.article_context)
        context.update(self.author_context)
        return context

    def dispatch(self, request, *args, **kwargs):
        self.article_context, article_kwargs = \
            ArticleList.as_view()(request, *args, **kwargs)
        self.author_context, authoe_kwargs = \
            AuthorList.as_view()(request, *args, **kwargs)

        return super(MultiView, self).dispatch(request, *args, **kwargs)
