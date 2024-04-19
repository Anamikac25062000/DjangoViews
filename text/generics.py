class CreateAPIView(mixins.CreateModelMixin,GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
    
class UpdateAPIView(mixins.UpdateModelMixin, GenericAPIView):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    