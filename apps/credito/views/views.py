from django.db.models import Q
from django.shortcuts import render
from django_filters import widgets, fields, filters, NumberFilter, CharFilter

from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_datatables import pagination as dt_pagination
from rest_framework_datatables.django_filters.filters import GlobalFilter
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.django_filters.backends import DatatablesFilterBackend

from apps.zona.models.localidad import Localidad
from apps.zona.api.v1.serializers.localidad import AlbumSerializer,LocalidadFilterSerializer


def index(request):
    return render(request, 'albums/albu.html')


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all().order_by('id')
    serializer_class = LocalidadFilterSerializer 



class AlbumPostListView(generics.ListAPIView):
    queryset = Localidad.objects.all().order_by('id')
    serializer_class = AlbumSerializer
    pagination_class = dt_pagination.DatatablesLimitOffsetPagination

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#---

class YADCFMultipleChoiceWidget(widgets.QueryArrayWidget):
    def value_from_datadict(self, data, files, name):
        if name not in data:
            return None
        vals = data[name].split("|")
        new_data = data.copy()
        new_data[name] = vals
        return super().value_from_datadict(new_data, files, name)


class YADCFModelMultipleChoiceField(fields.ModelMultipleChoiceField):
    widget = YADCFMultipleChoiceWidget


class YADCFModelMultipleChoiceFilter(filters.ModelMultipleChoiceFilter):
    field_class = YADCFModelMultipleChoiceField

    def global_q(self):
        """
        This method is necessary for the global filter
        - i.e. any string values entered into the search box.
        """
        if not self._global_search_value:
            return Q()
        kw = "{}__{}".format(self.field_name, self.lookup_expr)
        return Q(**{kw: self._global_search_value})


class GlobalCharFilter(GlobalFilter, filters.CharFilter):
    pass


class GlobalNumberFilter(GlobalFilter, filters.NumberFilter):
    pass


class AlbumFilter(DatatablesFilterSet):

    # the name of this attribute must match the declared 'data' attribute in
    # the DataTables column
    descripcion_desc= YADCFModelMultipleChoiceFilter(
        field_name="descripcion", queryset=Localidad.objects.all(), lookup_expr="contains"
    )

    # additional attributes need to be declared so that sorting works
    # the field names must match those declared in the DataTables columns.
    id = GlobalNumberFilter()
    descripcion = GlobalCharFilter()

    class Meta:
        model = Localidad
        fields = ('id',"descripcion", )


class AlbumFilterListView(generics.ListAPIView):
    # select_related() and prefetch_related provide more efficient DB queries
    queryset = Localidad.objects.all().order_by('id')
    serializer_class = AlbumSerializer
    filter_backends = (DatatablesFilterBackend,)
    filterset_class = AlbumFilter


class AlbumFilterArtistOptionsListView(APIView):
    """
    Return the list of options to appear in the Albums 'artist' column filter.
    """
    allowed_methods = ("GET",)
    pagination_class = None

    def get(self, request, *args, **kwargs):
        artists = list(
            Localidad.objects.filter()
            .values_list("id", "descripcion")
            .order_by("descripcion")
            .distinct()
        )
        options = list()
        for id_, name in artists:
            options.append({"value": str(id_), "label": name})
        return Response(data={"options": options}, status=status.HTTP_200_OK)
