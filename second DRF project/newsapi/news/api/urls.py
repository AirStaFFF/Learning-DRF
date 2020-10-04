from django.urls import path

# from news.api.views import (article_list_create_view_api as article_list,
#                             article_detail_api_view as article_detail)

from news.api.views import (ArticleListCreateViewApi,
                            ArticleDetailApiView,
                            JournalistCreateApiView,
                            JournalistDetailsApiView)

urlpatterns = [
    # path('articles/', article_list, name="article-list"),
    # path('articles/<int:pk>', article_detail, name="article-detail")
    path('articles/', ArticleListCreateViewApi.as_view(), name="article-list"),
    path('articles/<int:pk>', ArticleDetailApiView.as_view(), name="article-detail"),
    path('journalists/', JournalistCreateApiView.as_view(), name="journalist-list"),
    path('journalists/<int:pk>', JournalistDetailsApiView.as_view(), name="journalist-detail")
]