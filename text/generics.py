class CreateAPIView(mixins.CreateModelMixin,GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
    
class UpdateAPIView(mixins.UpdateModelMixin, GenericAPIView):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    
class ListAPIView(mixins.ListModelMixin,GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class RetrieveAPIView(mixins.RetrieveModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class GenericAPIView(views.APIView):
    queryset = None
    serializer_class = None