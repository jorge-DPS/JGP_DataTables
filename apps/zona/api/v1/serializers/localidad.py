from rest_framework import serializers
from apps.zona.models import Localidad

class LocalidadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = (
            'id',
            'descripcion', 
            'codigo_departamento',
            'codigo_localidad',
            'usuario_actualizacion',
            'sucursal_creacion',
            'creado_en',
            'actualizado_en',
            'eliminado_en',
        )

class LocalidadFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = (
            'id',
            'descripcion', 
            'codigo_departamento',
            'codigo_localidad',
            'creado_en',
            
        )

class AlbumSerializer22222(serializers.ModelSerializer):
    
    class Meta:
        model = Localidad
        fields = (
            'id',
            'descripcion', 
            'codigo_departamento',
            'codigo_localidad',
            'creado_en'
            
        )


#---------------------------------------ALBUMENS

from apps.albums.models.models import Album, Artist


class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Artist
        fields = (
            'id', 'name',
        )
        # Specifying fields in datatables_always_serialize
        # will also force them to always be serialized.
        datatables_always_serialize = ('id',)


class AlbumSerializer(serializers.ModelSerializer):
    #artist_name = serializers.ReadOnlyField(source='artist.name')
    # DRF-Datatables can deal with nested serializers as well.
    #artist = ArtistSerializer()
    

    # If you want, you can add special fields understood by Datatables,
    # the fields starting with DT_Row will always be serialized.
    # See: https://datatables.net/manual/server-side#Returned-data
    DT_RowId = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()

    def get_DT_RowId(self, album):
        return 'row_%d' % album.pk

    def get_DT_RowAttr(self, album):
        return {'data-pk': album.pk}

    class Meta:
        model = Localidad
        fields = (
            'DT_RowId', 'DT_RowAttr', 'id','descripcion','codigo_localidad',
        )


