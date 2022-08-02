from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author_fk = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        # fields = ('title',)
        fields = '__all__'
