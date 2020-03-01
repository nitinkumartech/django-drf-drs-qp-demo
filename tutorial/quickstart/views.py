from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from tutorial.quickstart.models import Songs
from tutorial.quickstart.serializers import SongsSerializer
from django_filters import rest_framework as filters
import django_filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ListSongsFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Songs
        fields = ['artist']

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class ListSongsViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fclass = ListSongsFilter

    def get_songs(self):
        try:
            return Songs.objects.get(artist=self.kwargs['artist'])
        except Songs.DoesNotExist:
            return None

#    def get_queryset(self):
#            """
#            Optionally restricts the returned purchases to a given user,
###            by filtering against a `username` query parameter in the URL.
#            """
#            queryset = Songs.objects.all()
#            artist = self.request.query_params.get('artist', None)
#            if artist is not None:
#                queryset = queryset.filter(songs__artist=artist)
#            return queryset
    # def get_queryset(self):
    #         song = self.get_songs()
    #         if song is None:
    #             return self.queryset.none()

    #         return self.queryset.filter(song=song).filter(artist=self.request.artist)

    @swagger_auto_schema(operation_description="partial_update description override", responses={404: 'slug not found'})
    def partial_update(self, request, *args, **kwargs):
        return None

    artist_param = openapi.Parameter('artist', in_=openapi.IN_QUERY, description='Artist',
                                    type=openapi.TYPE_STRING)
    @swagger_auto_schema(operation_description="get description override", responses={404: 'slug not found'}, manual_parameters=[artist_param])
    def list(self, request, *args, **kwargs):
        return None