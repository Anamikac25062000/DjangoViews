class CreateAPIView(mixins.CreateModelMixin,GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
    
class ListAPIView(mixins.ListModelMixin, GenericAPIView):
    