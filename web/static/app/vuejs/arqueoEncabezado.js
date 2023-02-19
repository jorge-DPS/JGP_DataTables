var csrf_token = { headers: { "X-CSRFToken": csrftoken } };
var app = new Vue({
    el:'#arqueo',
    data:{
        arqueoEncabezado:{
            caja_id:null,
            usuario_id:null,
            observaciones:null,
            detalle:[
                {
                    codigo_corte_moneda:null,
                    cantidad_corte_moneda:null,
                    valor_corte_moneda:null,
                }
            ]
        }

        lista
    },

    methods: {
        cargarArqueo: function () {
            console.log("entrando al metodo");
            var url = URLS.endpoints.crearListarArqueo();
            this.$http.get(url).then((response) => {
                this.lista_zonas = response.body;
                console.log(this.lista_zonas);
            });
        },
    }
})