from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'date', 'article', 'tags')

    def create(self, validated_data):
        title = validated_data.get('title', None)
        article = validated_data.get('article', None)
        tags = validated_data.get('tags', None)
        date = validated_data.get('date', None)
        user = self.context.get("user")
        return Post.objects.create(title=title, author=user, tags=tags, article=article, date=date)
        